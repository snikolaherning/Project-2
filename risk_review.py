"""Decision-focused fixed-allocation checks; scenario assumptions, not forecasts."""
from pathlib import Path
import csv
import hashlib
import json
import math
from decimal import Decimal, ROUND_HALF_UP

ROOT=Path(__file__).resolve().parent
PILOT=[.85,0,0,.15]

def format_percent(value):
    """Display two decimal percentage points; suppress sub-1e-10-point float noise."""
    points=Decimal(str(round(value*100,10)))
    return str(points.quantize(Decimal('0.01'),rounding=ROUND_HALF_UP))+'%'


def expected_net(bil,vt,cost_bps=25):
    if not all(math.isfinite(x) for x in [bil,vt,cost_bps]):
        raise ValueError('Scenario inputs must be finite.')
    return .85*bil+.15*vt-cost_bps/10000

def bil_break_even(target,vt,cost_bps=25):
    return (target+cost_bps/10000-.15*vt)/.85

def fixed_sensitivity(target=.05,cost_bps=25,vt=.065):
    # BIL levels span reinvestment environments, not a probabilistic forecast interval.
    rows=[]
    for bil in [.02,.03,.04,.05]:
        net=expected_net(bil,vt,cost_bps)
        rows.append(dict(bil_assumption=bil,vt_assumption=vt,cost_bps=cost_bps,
                         net_return=net,target=target,shortfall=max(0,target-net),
                         verdict='PASS' if net>=target-1e-12 else 'FAIL'))
    return rows

def shock_result(weights,asset_shocks,spending_budget=5):
    """One-period mark-to-market loss per $100 before external spending; no stop fills."""
    if len(weights)!=4 or len(asset_shocks)!=4 or not math.isclose(sum(weights),1,abs_tol=1e-9):
        raise ValueError('Four shocks and fully invested weights required.')
    if any(not math.isfinite(x) for x in weights+asset_shocks) or min(weights)<0 or min(asset_shocks)<-1:
        raise ValueError('Invalid shock or weights.')
    investment_return=sum(w*x for w,x in zip(weights,asset_shocks))
    after_market=100*(1+investment_return)
    return dict(asset_shocks=asset_shocks,investment_return=investment_return,
                drawdown=max(0,-investment_return),drawdown_screen=investment_return>=-.1-1e-12,
                assets_after_market_per_100=after_market,
                fixed_spending_obligation=spending_budget,
                assets_after_withdrawal=after_market-spending_budget,
                protected_dollars_implemented=0,
                spending_protection_verdict='FAIL: no separately protected account',
                note='Withdrawal reduces assets but is excluded from investment drawdown. ETF liquidity is not principal protection.')

def signal_snapshot():
    records={}
    for vintage in ['2026-09-30','2026-10-29']:
        path=ROOT/'data'/'signal'/f'TB3MS-vintage-{vintage}.csv'
        with path.open() as handle:
            rows=list(csv.reader(handle))[1:]
        values=[(day,float(value)) for day,value in rows if value not in ['.','']]
        if not values or any(day>vintage for day,value in values):
            raise ValueError('Invalid vintage observation boundary.')
        day,value=values[-1]
        records[vintage]=dict(latest_measured_month=day,value_percent_per_annum=value,
                              raw_sha256=hashlib.sha256(path.read_bytes()).hexdigest(),
                              september_observation_present=any(day=='2026-09-01' for day,value in values))
    return records

def temporal_review(source=None,cost_bps=25,target=.05):
    """Retrospective time split, NOT an untouched holdout or point-in-time backtest."""
    import io
    import portfolio as p
    import committee as c
    path=Path(source) if source else c.PRICES
    with path.open() as handle:
        rows=list(csv.reader(handle))
    if len(rows)!=62:
        raise ValueError('Time-split review requires the frozen 61-price snapshot.')
    # 37 prices -> first 36 returns; holdout uses the next 24 returns.
    stream=io.StringIO()
    csv.writer(stream).writerows(rows[:38])
    estimate=p.estimate_from_csv(io.StringIO(stream.getvalue()))
    prices=[[float(x) for x in row[1:]] for row in rows[1:]]
    monthly=[[b/a-1 for a,b in zip(a,b)] for a,b in zip(prices,prices[1:])]
    train,test=monthly[:36],monthly[36:]
    covariance=p.covariance_matrix(estimate['volatilities'],estimate['correlations'])
    def path_returns(weights,values):
        return [sum(w*x for w,x in zip(weights,row))-cost_bps/10000/12 for row in values]
    best=None
    for weights in p.grid_weights(4):
        if weights[0]<.20-1e-12 or p.expected_return(weights,estimate['returns'])<target+cost_bps/10000-1e-12:
            continue
        if c.drawdown_path(path_returns(weights,train))>.10+1e-12:
            continue
        risk=p.portfolio_volatility(weights,covariance)
        if best is None or risk<best[0]-1e-12:
            best=(risk,list(weights))
    mixes={'Equal weight':[.25]*4,'Inverse volatility':p.inverse_volatility_weights(estimate['volatilities']),
           '60/40 benchmark':[0,0,.4,.6],'Student pilot 85/15':PILOT}
    if best is not None:
        mixes['Training-selected constrained portfolio']=best[1]
    output={}
    for name,weights in mixes.items():
        values=path_returns(weights,test)
        growth=math.prod(1+x for x in values)
        output[name]=dict(weights=weights,test_months=len(test),
                          compounded_return=growth-1,
                          annualized_compounded_return=growth**(12/len(test))-1,
                          historical_test_drawdown=c.drawdown_path(values))
    return dict(training_return_months=len(train),test_return_months=len(test),
                training_start=rows[1][0],training_end=rows[37][0],test_end=rows[-1][0],
                training_estimates=estimate,training_feasible=best is not None,
                results=output,
                limitation='Retrospective split of an already inspected revised adjusted-price snapshot. Weights selected only from training inputs but this is not an untouched holdout, statistical significance or a vintage-correct trading backtest. No spending withdrawals modeled.')


def review_report():
    import committee
    student=[]
    for bil in [.0275,.03,.0325,.035]:
        for vt in [.065,.075]:
            student.append(dict(bil=bil,vt=vt,gross_return=.85*bil+.15*vt,net_return=expected_net(bil,vt),
                                target=.05,return_screen=expected_net(bil,vt)>=.05-1e-12))
    return dict(
        student_assumption_grid=student,
        build_sha256=committee.build_fingerprint(),
        status='Supplemental AI-assisted validation; not a new human locked experiment',
        sensitivity_per_1pp={'BIL_portfolio_return_pp':.85,'VT_portfolio_return_pp':.15},
        break_even=[dict(target=t,vt_assumption=.065,cost_bps=25,bil_required=bil_break_even(t,.065)) for t in [.05,.045]],
        fixed_85_15_return_stress=fixed_sensitivity(),
        analyst_shock_scenarios={
            'equity_minus_50_others_flat':shock_result(PILOT,[0,0,0,-.5]),
            'equity_minus_100_others_flat':shock_result(PILOT,[0,0,0,-1]),
            'joint_market_shock':shock_result(PILOT,[-.01,-.15,-.20,-.5])},
        shock_assumption_source='Analyst-designed failure probes, not historical events or forecasts. No probabilities attached.',
        signal_vintages=signal_snapshot(),retrospective_time_split=temporal_review(),
        source_backed_proxy=json.loads((ROOT/'data'/'assumption-sources.json').read_text()))

if __name__=='__main__':
    import argparse
    parser=argparse.ArgumentParser()
    parser.add_argument('--output',type=Path,default=ROOT/'work'/'risk-review.json')
    path=parser.parse_args().output
    path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(json.dumps(review_report(),indent=2)+'\n')
    print(path.resolve())
