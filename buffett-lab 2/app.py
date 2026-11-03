"""Run: python -m streamlit run app.py"""
import importlib.util
from pathlib import Path
import pandas as pd
import streamlit as st

ROOT = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('edgar', ROOT / '.agents/skills/buffett-edgar/scripts/edgar.py')
edgar = importlib.util.module_from_spec(spec)
spec.loader.exec_module(edgar)
st.set_page_config(page_title='Buffett business check', layout='wide')
st.title('Buffett business check')
st.caption('data from SEC EDGAR; built with AI help, a learning demonstration, not investment advice.')
ticker = st.text_input('Ticker', 'COST').strip().upper()
refresh = st.button('Refresh SEC data')
try:
    result = edgar.analyze(ticker, refresh)
except Exception as error:
    st.error(str(error))
    st.stop()
st.subheader(result['company'])
st.caption(result['method'])
chart = pd.DataFrame([{'Fiscal year': str(r['fiscal_year']),
    'Owner earnings': None if r['owner_earnings']['value'] is None else r['owner_earnings']['value'] / 1e6,
    'Net income': None if r['net_income']['value'] is None else r['net_income']['value'] / 1e6}
    for r in result['rows']]).set_index('Fiscal year')
st.line_chart(chart)
st.caption('USD millions. Missing values are gaps, never zeroes.')
st.dataframe(pd.DataFrame(edgar.table(result)), hide_index=True)
for label, outcome in result['checks'].items():
    st.write(f'**{label}: {outcome}**')
st.markdown(f'[SEC company facts]({result["source"]})')
memo_path = ROOT / 'memos' / (ticker + '.md')
saved = memo_path.read_text() if memo_path.exists() else 'Run the buffett-edgar skill in Codex to write this ticker’s memo.'
memo = st.text_area('Memo — edit here to test an unsupported number', saved, height=250, key='memo_' + ticker)
st.markdown(memo)
flags = edgar.unsupported_numbers(memo, result)
if flags:
    st.error('Numbers not printed by the script: ' + ', '.join(flags))
else:
    st.success('Every numerical value in this memo matches a printed value.')
st.caption('This checks numerical values, not whether a value supports its surrounding claim.')
if st.button('Save memo'):
    memo_path.parent.mkdir(exist_ok=True)
    memo_path.write_text(memo)
    st.success('Memo saved.')
st.download_button('Download memo', memo, file_name=ticker + '.md')
st.text_area('Your decision: do you trust this verdict, and why?', key='reflection_' + ticker)
