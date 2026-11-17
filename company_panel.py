"""Run from this folder: python -m streamlit run app.py"""
import json
from pathlib import Path
import sys
import pandas as pd
import streamlit as st

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / 'scripts'))
import panel

st.set_page_config(page_title='Legend panel — Lab 19', layout='wide')
st.title('Legend panel — Buffett · Cathie Wood · Burry')
st.caption('data from SEC EDGAR; built with AI help, a learning demonstration, not investment advice.')
st.caption('Cathie Wood uses the instructor-assigned defensive checks. These are classroom rules, not her actual investment method.')
ticker = st.text_input('Ticker', 'COST').strip().upper()
threshold = st.number_input('Cathie Wood current-ratio threshold — temporary app probe', min_value=0.1,
                            value=panel.wood_threshold(), step=0.1)
st.caption('The saved default comes from the Wood SKILL.md. Change its Current-ratio threshold line to retain a new default.')
refresh = st.button('Refresh SEC data')
try:
    result = panel.analyze_panel(ticker, refresh, threshold)
except Exception as error:
    st.error(str(error))
    st.stop()
st.subheader(result['company'])
st.caption(result['method'])
st.write('Printed thresholds:', result['thresholds'])
chart = pd.DataFrame([{'Fiscal year': str(r['fiscal_year']),
    'Owner earnings': None if r['owner_earnings']['value'] is None else r['owner_earnings']['value'] / 1e6,
    'Net income': None if r['net_income']['value'] is None else r['net_income']['value'] / 1e6}
    for r in result['rows']]).set_index('Fiscal year')
st.line_chart(chart)
st.caption('USD millions. Missing values remain gaps, not zeroes.')
st.subheader('Shared facts and source tags')
st.dataframe(pd.DataFrame(panel.edgar.table(result)), hide_index=True)
with st.expander('SEC filing provenance — dates, accessions and exact values'):
    st.json(result['rows'])
st.markdown(f'[SEC company facts]({result["source"]})')
st.subheader('Panel checks')
st.dataframe(pd.DataFrame(panel.panel_table(result)), hide_index=True)
st.download_button('Download panel data', json.dumps(result, indent=2), file_name=ticker + '-panel.json')
if threshold != panel.wood_threshold():
    st.warning('Probe setting active: the checks use your temporary threshold. Saved memos reflect the saved skill setting; rerun the skill to revise a verdict.')
columns = st.columns(3)
all_flags = {}
for investor, column in zip(panel.INVESTORS, columns):
    with column:
        st.subheader(investor)
        path = panel.memo_path(ticker, investor)
        saved = path.read_text() if path.exists() else 'Memo not written. Ask Codex to use this investor’s skill on the printed output.'
        memo = st.text_area('Memo — editable number probe', saved, height=320, key=ticker + '_' + panel.SLUGS[investor])
        st.write('**Verdict:**', panel.verdict(memo))
        st.markdown(memo)
        flags = panel.unsupported_numbers(memo, result)
        all_flags[investor] = flags
        if flags:
            st.error('Unprinted numbers: ' + ', '.join(flags))
        elif path.exists():
            st.success('No unprinted numbers detected.')
        if st.button('Save memo', key='save_' + investor):
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(memo)
            st.success('Saved.')
        st.download_button('Download memo', memo, file_name=ticker + '-' + panel.SLUGS[investor] + '.md', key='download_' + investor)
if any(all_flags.values()):
    st.error('Panel number check: ' + '; '.join(name + ': ' + ', '.join(flags) for name, flags in all_flags.items() if flags))
else:
    st.success('Panel number check: no unprinted numbers detected across the three memo editors.')
st.caption('Numeric matching does not prove the surrounding claim, financial judgment, or stock valuation.')
st.subheader('Your checkout notes')
notes_path = ROOT / 'checkout-notes.json'
notes = json.loads(notes_path.read_text()) if notes_path.exists() else {}
fields = [('threshold_reason', 'Threshold you keep and why'), ('bull', 'Your company — bull case, two sentences'),
          ('bear', 'Partner bear case, two sentences; record the role swap too'),
          ('decision', 'Would you let this panel screen Project 2 companies? Name the condition.'),
          ('reflection', 'Where the panel agrees/splits; what the threshold probe taught you')]
for key, label in fields:
    notes[key] = st.text_area(label, notes.get(key, ''), key='notes_' + key)
if st.button('Save checkout notes'):
    notes_path.write_text(json.dumps(notes, indent=2))
    st.success('Notes saved to checkout-notes.json.')
st.download_button('Download checkout notes', json.dumps(notes, indent=2), file_name='checkout-notes.json')
