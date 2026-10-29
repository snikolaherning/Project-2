"""Lab 17. Public CSV downloads; no API key. Streamlit run asof_app.py."""
from datetime import date
from io import StringIO
import re
from urllib.parse import urlencode
from urllib.request import Request, urlopen
import pandas as pd
import streamlit as st

NAMES = {'BAA': "Moody's Baa corporate bond yield", 'FEDFUNDS': 'Federal funds rate',
         'DGS10': '10-year Treasury yield', 'MORTGAGE30US': '30-year mortgage rate'}

def parse_csv(text):
    frame = pd.read_csv(StringIO(text), na_values=['.'])
    if len(frame.columns) != 2:
        raise ValueError('Expected a date column and one series column.')
    frame.columns = ['Date', 'Value']
    frame['Date'] = pd.to_datetime(frame['Date'], errors='raise')
    frame['Value'] = pd.to_numeric(frame['Value'], errors='raise')
    if frame['Date'].duplicated().any():
        raise ValueError('Duplicate observation dates in source.')
    return frame.dropna(subset=['Value']).sort_values('Date').set_index('Date')['Value']

def fetch(url):
    import subprocess
    response = subprocess.run(['curl', '-fLsS', '--max-time', '25', url], capture_output=True, timeout=30)
    if response.returncode:
        raise ValueError(response.stderr.decode('utf-8', errors='replace').strip())
    raw = response.stdout.decode('utf-8-sig')
    return parse_csv(raw), date.today().isoformat(), url

@st.cache_data(ttl=3600, show_spinner=False)
def download_today(series):
    return fetch('https://fred.stlouisfed.org/graph/fredgraph.csv?' + urlencode({'id': series}))

@st.cache_data(ttl=3600, show_spinner=False)
def download_vintage(series, vintage):
    return fetch('https://alfred.stlouisfed.org/graph/alfredgraph.csv?' + urlencode({'id': series, 'vintage_date': vintage}))

def compare(current, historical):
    if historical.empty:
        return {'Known measured date': None, 'Known value': None,
                'Latest measured date': None if current.empty else current.index[-1].date().isoformat(),
                'Latest value': None if current.empty else float(current.iloc[-1]),
                'Later observations': None, 'Revised common dates': 0}
    common = current.index.intersection(historical.index)
    revised = ((current.loc[common] - historical.loc[common]).abs() > 1e-9).sum()
    return {'Known measured date': historical.index[-1].date().isoformat(),
            'Known value': float(historical.iloc[-1]),
            'Latest measured date': None if current.empty else current.index[-1].date().isoformat(),
            'Latest value': None if current.empty else float(current.iloc[-1]),
            'Later observations': int((current.index > historical.index[-1]).sum()),
            'Revised common dates': int(revised)}

def main():
    st.set_page_config(page_title='Rates as known then', layout='wide')
    st.title('Rates as known then')
    st.caption(f'Data from FRED and ALFRED, Federal Reserve Bank of St. Louis, downloaded today ({date.today()}); built with AI help, a learning demonstration, not investment advice.')
    with st.sidebar:
        selected = st.multiselect('Series', list(NAMES), default=list(NAMES), format_func=lambda x: f'{x} — {NAMES[x]}')
        extra = st.text_input('Add a FRED series ID', help='For your Treasury-bill series, enter TB3MS. For the required probe, enter PAYEMS.').strip().upper()
        start = st.date_input('Chart start date', value=date(2020,1,1))
        vintage = st.date_input('As known on', value=date.today(), max_value=date.today())
    ids = list(dict.fromkeys(selected + ([extra] if extra else [])))
    st.caption('Chart start changes charts only. Counts use complete downloaded histories, excluding missing observations. Monthly dates label the measured month, not publication day. Values retain each source’s units; PAYEMS is thousands of jobs, not a rate.')
    records = []
    for series in ids:
        if not re.fullmatch(r'[A-Z0-9_]+',series):
            st.error(f'{series}: invalid series ID.'); continue
        st.subheader(f'{series} — {NAMES.get(series, "Additional series")}')
        try:
            current, downloaded, url = download_today(series)
            historical, vintage_downloaded, historical_url = download_vintage(series, vintage.isoformat())
            st.line_chart(current.loc[current.index >= pd.Timestamp(start)].rename(series))
            record = compare(current,historical)
            st.write(f'Last measured date known on {vintage}: {record["Known measured date"] or "No observations"}')
            st.markdown(f'[FRED source](https://fred.stlouisfed.org/series/{series}) · [Current CSV]({url}) · [Vintage CSV]({historical_url})')
            st.caption(f'Current CSV fetched {downloaded}; vintage CSV fetched {vintage_downloaded}. Cached for up to one hour.')
            records.append({'Series':f'https://fred.stlouisfed.org/series/{series}', **record})
            with st.expander('Inspect values on matching dates'):
                st.dataframe(pd.concat([historical.rename('As known then'), current.rename('Today')],axis=1).tail(36))
        except Exception as error:
            st.error(f'{series}: download or parsing failed: {error}')
    st.subheader('Point-in-time comparison')
    if records:
        st.dataframe(pd.DataFrame(records), hide_index=True,
                     column_config={'Series':st.column_config.LinkColumn('Series',display_text=r'https://fred\.stlouisfed\.org/series/(.*)')})
    st.caption('Later observations and revisions are different. Zero observed revisions does not guarantee a series will never be corrected. A vintage date establishes availability by that date, not necessarily the exact original publication timestamp.')

if __name__ == '__main__':
    main()
