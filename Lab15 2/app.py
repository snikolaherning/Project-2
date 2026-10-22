"""Streamlit controls and presentation; all portfolio math lives in portfolio.py."""
import hashlib
import importlib
import io
import json
import streamlit as st
import portfolio

# Re-read editable engine inputs on every rerun, including after a source edit.
p = importlib.reload(portfolio)
st.set_page_config(page_title='Portfolio stability | Lab 15', layout='wide')
st.title('Portfolio stability')
st.caption('Built with AI help, a learning demonstration, not investment advice.')

with st.sidebar:
    st.header('Mandate')
    objective = st.number_input('Expected return objective (%)', value=6.5, step=0.1, key='objective') / 100
    minimum = st.number_input('Reserve minimum (%)', min_value=0.0, max_value=100.0, value=3.0, step=1.0, key='reserve') / 100
    upload = st.file_uploader('Monthly adjusted prices (CSV)', type=['csv'])
    recent = st.checkbox('Use last 36 monthly returns', key='recent', disabled=upload is None)
    st.caption('Five-point grid; long-only; weights sum to 100%. No automatic lowering of the objective.')

try:
    if upload is None:
        identity = 'meridian'
        loaded = dict(names=p.SLEEVES, returns=p.EXPECTED_RETURNS,
                      volatilities=p.VOLATILITIES, correlations=p.CORRELATIONS)
        active = loaded
        default_reserves = p.RESERVE_INDICES
        st.info('Meridian: course training values. Objective assumes CPI 2.5% + 4%.')
    else:
        raw = upload.getvalue()
        identity = hashlib.sha256(raw).hexdigest()[:12]
        loaded = p.estimate_from_csv(io.BytesIO(raw))
        active = p.estimate_from_csv(io.BytesIO(raw), last_36=recent)
        default_reserves = ()
        st.info(f"Your universe: {active['label']}. {active['return_months']} returns; {active['start']} to {active['end']}.")
        if loaded['return_months'] < 60:
            st.warning('Fewer than 60 monthly returns: 61 price observations are needed for a full five years of returns. Disclose coverage.')
        st.caption('CSV cannot prove prices are adjusted. Record each ticker’s source, download date and coverage. Tick reserve-eligible assets yourself.')
    st.subheader('Return estimates and reserve eligibility')
    returns, reserves = [], []
    for i, name in enumerate(active['names']):
        col1, col2 = st.columns([3, 1])
        # Window/source keys reset return boxes when loading another dataset/window.
        key = f'return_{identity}_{bool(recent and upload is not None)}_{i}'
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
                  reserve_indices=reserves, current_returns=returns, last_36=bool(recent and upload is not None),
                  as_loaded=baseline, current=current, largest_change_points=movement,
                  csv_sha256=None if upload is None else hashlib.sha256(raw).hexdigest())
    st.download_button('Download this run as JSON', json.dumps(report, indent=2), 'portfolio-run.json', 'application/json')
except (ValueError, UnicodeError) as error:
    st.error(str(error))
