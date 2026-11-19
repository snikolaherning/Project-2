"""Interactive committee app. Launch: python -m streamlit run app.py"""
import json
import streamlit as st
import pandas as pd
from committee import run, decision_for, build_fingerprint
from risk_review import fixed_sensitivity, bil_break_even, shock_result, signal_snapshot, format_percent
st.set_page_config(page_title='Club reserve | Investment committee',layout='wide')
st.title('University club reserve — committee workspace')
try:
    st.caption(f"Build fingerprint: {build_fingerprint()[:16]} — compare with the launcher and downloaded JSON.")
except (OSError,ValueError) as error:
    st.error(f'STOP: required input/code file missing or invalid: {error}. Restore the complete verified project folder.')
    st.stop()
st.caption('Codex assisted with code, analysis checks and documentation. The analysis and decision belong to the student; education, not investment advice.')
st.warning('Research prototype: PILOT in simulation only. Live allocation: 0% pending protected spending implementation, loss-cap evidence and validation.')
st.write('Five-year horizon · BIL / IEF / LQD / VT · long only · no leverage. Benchmark: 60% VT / 40% LQD.')
st.info('Mandate: maximum 10% peak-to-trough investment drawdown; fully protect the next 12 months of spending; one late-August/September withdrawal up to 5% of reserve. Historical monthly drawdown is a screen, not a guaranteed loss cap. Every current ETF portfolio FAILS full live mandate approval because the protected spending account and hard cap are not demonstrated.')
st.caption('Book the approved annual dollar budget at the school-year decision date, capped at 5% of the reserve then; do not shrink that protected amount after losses. Treat withdrawals as external cash flows when measuring drawdown. BIL is not assumed to guarantee principal. Proposed separate cash/maturity-matched Treasury spending sleeve requires implementation beyond this ETF prototype.')
BASE={'objective':5.0,'recent':False,'override':False,'vt':7.0,'bil_override':False,'bil':3.5,'costs':25,'reserve':20}
def reset_base():
    for key,value in BASE.items():
        st.session_state[key]=value
for key,value in BASE.items():
    st.session_state.setdefault(key,value)
with st.sidebar:
    st.header('Scenario controls')
    st.button('Reset to base',on_click=reset_base)
    st.caption('Changing the target is a scenario, not committee approval to change the mandate. Base: 5% net target, 60 months, 20% BIL floor, 25 bp drag, historical means.')
    objective=st.number_input('Scenario net return target (%)',min_value=0.0,max_value=8.0,step=.5,key='objective')/100
    recent=st.checkbox('Use last 36 monthly returns',key='recent')
    override=st.checkbox('Override VT expected return',key='override')
    vt=st.number_input('VT annual expected return (%)',min_value=-10.0,max_value=15.0,step=.5,key='vt',disabled=not override)/100
    bil_override=st.checkbox('Override BIL expected return',key='bil_override')
    bil=st.number_input('BIL annual expected return (%)',min_value=-1.0,max_value=8.0,step=.25,key='bil',disabled=not bil_override)/100
    costs=st.number_input('Annual implementation drag (basis points)',min_value=0,max_value=200,step=25,key='costs')
    reserve=st.slider('BIL minimum (%)',20,100,step=5,key='reserve')/100
    st.caption('Drag is an annual scenario haircut, not measured turnover or an added fund expense. Historical adjusted returns already reflect fund expenses.')
    with st.expander('Locked inputs and defended bounds'):
        st.write('Locked: four-ETF universe; 60/40 VT/LQD benchmark; 5-point grid; long only; full investment; 10% loss limit; protected next-year spending; frozen price snapshot. Scenario target does not amend those policies.')
        st.write('Bounds are analyst-selected testing envelopes, not confidence intervals: target 0–8% spans the original 4.5% experiment; VT −10–15% tests pessimistic to optimistic forward means; BIL −1–8% permits low/negative and high rate regimes; cost 0–200 bp is a friction stress; BIL floor 20–100% never relaxes the mandate minimum. Historic means may lie outside override bounds and are labeled as estimates, not defended forecasts.')

try:
    r=run(recent,costs,reserve,vt if override else None,objective,bil_return=bil if bil_override else None)
    st.write(f"Active scenario: {objective:.1%} annual nominal net expected-return target; at least {reserve:.0%} BIL.")
    st.caption(f"Frozen prices: September 2021–September 2026, retrieved October 22, 2026. Active window: {r['window']}. Historical arithmetic estimates are not forecasts.")
    rows=[]
    for name,x in r['portfolios'].items():
        rows.append({'Portfolio':name,**{t:f'{w:.0%}' for t,w in zip(['BIL','IEF','LQD','VT'],x['weights'])},'Net estimate':format_percent(x['net_return']),'Volatility':format_percent(x['volatility']),'Historical max drawdown':format_percent(x['historical_max_drawdown']),'Numerical screen':x['verdict'],'Full mandate':x['live_mandate_verdict'],'Failed rules':', '.join(k for k,v in x['rules'].items() if not v) or 'None'})
    frame=pd.DataFrame(rows)
    st.subheader('Mandate verdicts')
    st.dataframe(frame[['Portfolio','Net estimate','Historical max drawdown','Numerical screen','Failed rules']],hide_index=True,width='stretch')
    for item in rows:
        st.caption(f"{item['Portfolio']}: {item['Numerical screen']}; failed rules: {item['Failed rules']}.")
    st.error('Full live mandate: FAIL for every portfolio — protected spending account is not implemented and the hard 10% future loss cap is unproven.')
    st.subheader('Allocation and risk')
    st.dataframe(frame[['Portfolio','BIL','IEF','LQD','VT','Volatility']],hide_index=True,width='stretch')
    if not r['feasible']: st.error('STOP: no feasible constrained portfolio on the five-percentage-point grid. Do not lower the objective silently.')
    with st.expander('Fixed 85/15: test the load-bearing BIL assumption'):
        st.write('Student judgment recorded November 19: BIL base 3.5%, stress 2.75–3.25%; VT stress 6.5–7.5%. These are forward scenarios informed by the September Fed projections, not guarantees. The frozen historical base is retained for reproducibility; use overrides to test these judgments.')
        st.write('A 1 percentage-point change in the BIL estimate moves expected portfolio return by 0.85 percentage points; a 1-point VT change moves it by 0.15. These are fixed-weight derivatives, not forecast confidence.')
        st.dataframe(pd.DataFrame([{'BIL assumption':f"{x['bil_assumption']:.1%}",'VT assumption':'6.5%','Net expected return':format_percent(x['net_return']),'Target':f'{objective:.1%}','Numerical return test':x['verdict']} for x in fixed_sensitivity(objective,costs)]),hide_index=True,width='stretch')
        st.write('Student stress: BIL 3.0%, VT 6.5% implies 3.525% before implementation drag, 3.275% after 25 bp. The original 4.15% BIL trigger applied to a 4.5% gross target, not the current 5% net default.')
        st.write(f'At VT 6.5% and cost {costs} bp, fixed 85/15 needs a BIL expected return of {bil_break_even(objective,.065,costs):.2%} to meet the current target. Levels in this table are analyst stress assumptions, not sourced forecasts. No reoptimization hides fixed-candidate failure.')
    with st.expander('Loss and spending failure probes'):
        st.write('Per $100 at the annual budget date: protect a fixed $5 for the next school-year withdrawal. An ETF reserve balance is not proof those dollars are principal-protected.')
        for name,shocks in [('VT −50%, others flat',[0,0,0,-.5]),('VT −100%, others flat',[0,0,0,-1]),('BIL −1%, IEF −15%, LQD −20%, VT −50%',[-.01,-.15,-.2,-.5])]:
            probe=shock_result([.85,0,0,.15],shocks)
            st.write(f"{name}: investment drawdown {probe['drawdown']:.2%}; 10% screen {'PASS' if probe['drawdown_screen'] else 'FAIL'}; assets after market move ${probe['assets_after_market_per_100']:.2f}, then ${probe['assets_after_withdrawal']:.2f} after the external $5 withdrawal.")
        st.caption('Analyst-designed one-period failure probes, not historical events or forecasts. No stop-order fills assumed. Withdrawals are excluded from investment drawdown. Protected account implemented: $0; full protection test FAIL.')
    st.subheader('Decision and monitoring')
    decision=decision_for(r)
    st.write(decision['action'])
    st.write(decision['live_reason'])
    st.caption(decision['research_range'])
    r['decision']=decision
    st.write('Monitor net target under VT 6.5–7.5%, both covariance windows, costs, BIL reserve, source revisions and vintage availability. Suspend advancement on a failed rule or spending shortfall. Escalate at 8% drawdown (proposed early warning); stop the risk process and seek committee review at 10%. These triggers cannot guarantee execution before the limit. Grid search is not a continuous optimum; volatility is not a maximum-loss guarantee.')
    with st.expander('Point-in-time signal: TB3MS'):
        vintages=signal_snapshot()
        before=vintages['2026-09-30'];later=vintages['2026-10-29']
        st.write(f"Raw ALFRED vintage as known September 30: latest measured month {before['latest_measured_month']}, {before['value_percent_per_annum']:.2f}% per annum. September observation available: {before['september_observation_present']}. October 29 comparison: {later['latest_measured_month']}, {later['value_percent_per_annum']:.2f}%.")
        st.caption('Frozen vintage CSVs retrieved November 19, 2026. Monthly measurement dates do not prove release dates. TB3MS is discount-basis rate context, not BIL total return; no automatic allocation effect or predictive claim. Missing/unverifiable vintage input stops this app rather than substituting later data.')
        st.markdown('[FRED source](https://fred.stlouisfed.org/series/TB3MS) · [Data card](https://github.com/snikolaherning/Project-2/blob/project2-committee/docs/signal-data-card.md)')
        r['signal_vintages']=vintages
    with st.expander('Inspect estimates'):
        st.json(r['estimates'])
    st.download_button('Download current run',json.dumps(r,indent=2),'committee-run.json','application/json')
except (ValueError,OSError) as error:
    st.error(f'STOP: {error}')
