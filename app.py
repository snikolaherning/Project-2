"""Interactive committee app. Launch: python -m streamlit run app.py"""
import json
import streamlit as st
import pandas as pd
from committee import run, decision_for, build_fingerprint
st.set_page_config(page_title='Club reserve | Investment committee',layout='wide')
st.title('University club reserve — committee workspace')
st.caption(f"Build fingerprint: {build_fingerprint()[:16]} — compare with the launcher and downloaded JSON.")
st.caption('Codex assisted with code, analysis checks and documentation. The analysis and decision belong to the student; education, not investment advice.')
st.warning('Research prototype: PILOT in simulation only. Live allocation: 0% pending protected spending implementation, loss-cap evidence and validation.')
st.write('Five-year horizon · BIL / IEF / LQD / VT · long only · no leverage. Benchmark: 60% VT / 40% LQD.')
st.info('Mandate: maximum 10% peak-to-trough investment drawdown; fully protect the next 12 months of spending; one late-August/September withdrawal up to 5% of reserve. Historical monthly drawdown is a screen, not a guaranteed loss cap. Every current ETF portfolio FAILS full live mandate approval because the protected spending account and hard cap are not demonstrated.')
st.caption('Book the approved annual dollar budget at the school-year decision date, capped at 5% of the reserve then; do not shrink that protected amount after losses. Treat withdrawals as external cash flows when measuring drawdown. BIL is not assumed to guarantee principal. Proposed separate cash/maturity-matched Treasury spending sleeve requires implementation beyond this ETF prototype.')
with st.sidebar:
    st.header('Stress controls')
    objective=st.number_input('Net annual return objective (%)',min_value=0.0,max_value=100.0,value=5.0,step=.5)/100
    recent=st.checkbox('Use last 36 monthly returns')
    override=st.checkbox('Override VT expected return',value=False)
    vt=st.number_input('VT annual expected return (%)',value=7.0,step=.5)/100
    costs=st.number_input('Annual implementation drag (basis points)',0,1000,25,25)
    reserve=st.slider('BIL minimum (%)',20,100,20,5)/100
    st.caption('Cost is an annual scenario haircut, not an estimated turnover fee. Fund expenses are already reflected in historical adjusted returns; avoid treating this as an additional fund expense.')
try:
    r=run(recent,costs,reserve,vt if override else None,objective)
    st.write(f"Active mandate: {objective:.1%} annual nominal net expected-return target; at least {reserve:.0%} BIL.")
    st.caption(f"Frozen prices: September 2021–September 2026, retrieved October 22, 2026. Active window: {r['window']}. Historical arithmetic estimates are not forecasts.")
    rows=[]
    for name,x in r['portfolios'].items():
        rows.append({'Portfolio':name,**{t:f'{w:.0%}' for t,w in zip(['BIL','IEF','LQD','VT'],x['weights'])},'Net estimate':f"{x['net_return']:.2%}",'Volatility':f"{x['volatility']:.2%}",'Historical max drawdown':f"{x['historical_max_drawdown']:.2%}",'Numerical screen':x['verdict'],'Full mandate':x['live_mandate_verdict'],'Failed rules':', '.join(k for k,v in x['rules'].items() if not v) or 'None'})
    frame=pd.DataFrame(rows)
    st.subheader('Mandate verdicts')
    st.dataframe(frame[['Portfolio','Net estimate','Historical max drawdown','Numerical screen','Failed rules']],hide_index=True,width='stretch')
    for item in rows:
        st.caption(f"{item['Portfolio']}: {item['Numerical screen']}; failed rules: {item['Failed rules']}.")
    st.error('Full live mandate: FAIL for every portfolio — protected spending account is not implemented and the hard 10% future loss cap is unproven.')
    st.subheader('Allocation and risk')
    st.dataframe(frame[['Portfolio','BIL','IEF','LQD','VT','Volatility']],hide_index=True,width='stretch')
    if not r['feasible']: st.error('STOP: no feasible constrained portfolio on the five-percentage-point grid. Do not lower the objective silently.')
    st.subheader('Decision and monitoring')
    decision=decision_for(r)
    st.write(decision['action'])
    st.write(decision['live_reason'])
    st.caption(decision['research_range'])
    r['decision']=decision
    st.write('Monitor net target under VT 6.5–7.5%, both covariance windows, costs, BIL reserve, source revisions and vintage availability. Suspend advancement on a failed rule or spending shortfall. Escalate at 8% drawdown (proposed early warning); stop the risk process and seek committee review at 10%. These triggers cannot guarantee execution before the limit. Grid search is not a continuous optimum; volatility is not a maximum-loss guarantee.')
    with st.expander('Point-in-time signal: TB3MS'):
        st.write('Admitted as rate-environment context only; it does not mechanically change weights or replace BIL returns. Lab 17 recorded August 2026 at 3.72% as known September 30, 2026; September 3.94% was unavailable then. These are preserved lab findings, not a newly retrieved live vintage.')
        st.markdown('[FRED source](https://fred.stlouisfed.org/series/TB3MS). Full timing, units and student checks: Lab17/lab17-data-card.md. Stop using the signal if release timing cannot be established.')
    with st.expander('Inspect estimates'):
        st.json(r['estimates'])
    st.download_button('Download current run',json.dumps(r,indent=2),'committee-run.json','application/json')
except (ValueError,OSError) as error:
    st.error(f'STOP: {error}')
