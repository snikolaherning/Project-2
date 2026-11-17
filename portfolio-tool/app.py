"""Streamlit controls and presentation; all portfolio math lives in portfolio.py."""
import hashlib
import importlib
import io
import json
from pathlib import Path
import streamlit as st
import sys
sys.path.insert(0, str(Path(__file__).resolve().parent))
import portfolio

# Re-read editable engine inputs on every rerun, including after a source edit.
p = importlib.reload(portfolio)
st.set_page_config(page_title='Portfolio stability | Lab 15', layout='wide')
st.title('Project 2 portfolio readiness — pilot')
st.caption('Codex assisted with code, checks and documentation. The analysis and decision are Stefan’s; education, not investment advice.')
st.caption('Built with AI help, a learning demonstration, not investment advice.')

with st.sidebar:
    st.header('Mandate')
    objective = st.number_input('Expected return objective (%)', value=4.5, step=0.1, key='objective') / 100
    minimum = st.number_input('Reserve minimum (%)', min_value=0.0, max_value=100.0, value=20.0, step=1.0, key='reserve') / 100
    upload = st.file_uploader('Monthly adjusted prices (CSV)', type=['csv'])
    recent = st.checkbox('Use last 36 monthly returns', key='recent', disabled=False)
    st.caption('Five-point grid; long-only; weights sum to 100%. No automatic lowering of the objective.')

try:
    raw = upload.getvalue() if upload is not None else (Path(__file__).resolve().parent / 'prices.csv').read_bytes()
    identity = hashlib.sha256(raw).hexdigest()[:12]
    loaded = p.estimate_from_csv(io.BytesIO(raw))
    active = p.estimate_from_csv(io.BytesIO(raw), last_36=recent)
    default_reserves = tuple(i for i, name in enumerate(active['names']) if name == 'BIL')
    st.info(f"Club universe: {active['label']}. {active['return_months']} returns; {active['start']} to {active['end']}.")
    st.caption('Bundled prices load automatically. Only BIL counts as reserve by default. Rates are historical estimates, not current yields or forecasts.')
    st.subheader('Return estimates and reserve eligibility')
    returns, reserves = [], []
    for i, name in enumerate(active['names']):
        col1, col2 = st.columns([3, 1])
        # Window/source keys reset return boxes when loading another dataset/window.
        key = f'return_{identity}_{bool(recent)}_{i}'
        returns.append(col1.number_input(f'{name} expected return (%)', value=active['returns'][i]*100, step=1.0, key=key)/100)
        if col2.checkbox(f'{name} counts as reserve', value=i in default_reserves, key=f'eligible_{identity}_{i}'):
            reserves.append(i)
    st.caption('The as-loaded answer keeps original return estimates and all months. Both answers use the same current mandate and reserve classifications.')
    baseline = p.search(list(loaded['returns']), loaded['volatilities'], loaded['correlations'], objective, minimum, reserves)
    current = p.search(returns, active['volatilities'], active['correlations'], objective, minimum, reserves)
    def show_result(column, label, result):
        with column:
            st.subheader(label)
            if result is None:
                st.warning('no mix meets the objective')
                st.caption('No grid allocation satisfies both objective and reserve constraint.')
                return
            st.success('PASS: implemented expected-return and reserve constraints. Full mandate compliance remains unverified.')
            st.table({'Asset': active['names'], 'Weight (%)': [f'{w*100:.2f}' for w in result['weights']]})
            st.metric('Expected return', f"{result['expected_return']:.2%}")
            st.metric('Volatility', f"{result['volatility']:.2%}")
            st.metric('Reserve-eligible weight', f"{result['reserve_weight']:.2%}")
    left, right = st.columns(2)
    show_result(left, 'As loaded (all months)', baseline)
    show_result(right, 'Current inputs', current)
    movement = p.largest_weight_change(baseline, current)
    st.metric('Largest weight change (percentage points)', 'N/A' if movement is None else f'{movement:.2f}')
    st.caption('Minimum risk among five-point grid allocations, not a continuous optimum. A 3% reserve floor requires at least 5% on this grid. Estimates omit separately modeled costs and do not guarantee returns or losses.')
    report = dict(universe=active['names'], objective=objective, reserve_minimum=minimum,
                  reserve_indices=reserves, current_returns=returns, last_36=bool(recent),
                  as_loaded=baseline, current=current, largest_change_points=movement,
                  csv_sha256=hashlib.sha256(raw).hexdigest())
    st.subheader('Committee decision: pilot 85% BIL / 15% VT; do not adopt yet')
    st.write('Fixed candidate; not a recommendation to use the optimizer output at every control setting. Reconsider adoption only if it meets the 4.5% target under both BIL estimation windows with VT at 6.5%, and the loss/withdrawal requirements are separately validated.')
    recent_estimates = p.estimate_from_csv(io.BytesIO(raw), last_36=True)
    bil_index, vt_index = active['names'].index('BIL'), active['names'].index('VT')
    stress_all = .85 * loaded['returns'][bil_index] + .15 * .065
    stress_recent = .85 * recent_estimates['returns'][bil_index] + .15 * .065
    breakeven_bil = (.045 - .15 * .065) / .85
    st.write(f'Fixed 85/15 candidate with VT at 6.5%: all-month BIL stress return {stress_all:.2%}; recent BIL stress return {stress_recent:.2%}; BIL break-even estimate {breakeven_bil:.4%}. These are fixed-weight arithmetic scenarios, not reoptimized portfolios.')
    st.warning('Full mandate verdict: UNRESOLVED. Historical volatility does not enforce the 10% loss limit or establish withdrawal coverage. Costs, broader stress and other Project 2 requirements remain incomplete.')
    st.download_button('Download this run as JSON', json.dumps(report, indent=2), 'portfolio-run.json', 'application/json')
except (ValueError, UnicodeError) as error:
    st.error(str(error))
