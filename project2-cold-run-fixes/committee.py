"""Committee calculations: frozen historical snapshot, no network or AI calls."""
from pathlib import Path
import json
import csv
import hashlib
import portfolio as p
ROOT = Path(__file__).resolve().parent
PRICES = ROOT / 'Lab15 2' / 'prices.csv'

DRAWDOWN_LIMIT = .10
SPENDING_RATE = .05

def build_fingerprint():
    digest=hashlib.sha256()
    for name in ['app.py','committee.py','portfolio.py','Lab15 2/prices.csv']:
        digest.update(name.encode())
        digest.update((ROOT/name).read_bytes())
    return digest.hexdigest()

def decision_for(result):
    pilot=result['portfolios']['Student pilot 85/15']
    failed=[name for name,passed in pilot['rules'].items() if not passed]
    if not result['feasible']:
        action='STOP this scenario: no constrained grid allocation passes the numerical screens.'
    elif failed:
        action='REJECT 85/15 under these inputs; simulation research only. Failed screens: '+', '.join(failed)+'.'
    else:
        action='PILOT 85/15 in simulation only: it passes the current numerical screens.'
    return dict(action=action,live_allocation=0.0,
                live_reason='Live adoption remains rejected: protected spending and the hard future 10% loss cap are unproven.',
                research_range='10–20% VT / 80–90% BIL is a research envelope, not a claim every mix passes.')


def drawdown_path(returns):
    """Unitized investment NAV: external spending is not an investment loss."""
    nav = peak = 1.0
    maximum = 0.0
    for value in returns:
        if value < -1:
            raise ValueError('Return below -100%.')
        nav *= 1 + value
        peak = max(peak, nav)
        maximum = max(maximum, 1 - nav / peak)
    return maximum

def historical_drawdown(weights, recent=False, cost_bps=25):
    with PRICES.open() as source:
        rows=list(csv.reader(source))[1:]
    prices=[[float(x) for x in row[1:]] for row in rows]
    monthly=[[b/a-1 for a,b in zip(previous,current)] for previous,current in zip(prices,prices[1:])]
    if recent:
        monthly=monthly[-36:]
    returns=[sum(w*x for w,x in zip(weights,row))-cost_bps/10000/12 for row in monthly]
    return drawdown_path(returns)

def spending_coverage(reserve_value, approved_budget):
    if reserve_value < 0 or approved_budget < 0:
        raise ValueError('Amounts must be nonnegative.')
    return reserve_value >= approved_budget


def evaluate(weights, estimates, cost_bps=25, objective=.05, reserve=.20, recent=False):
    gross = p.expected_return(weights, estimates['returns'])
    volatility = p.portfolio_volatility(weights, p.covariance_matrix(estimates['volatilities'], estimates['correlations']))
    net = gross - cost_bps / 10000
    drawdown = historical_drawdown(weights,recent,cost_bps) if len(weights)==4 else None
    rules = {'Fully invested': abs(sum(weights)-1)<1e-9,
             'Long only': min(weights)>=0,
             'BIL reserve floor': weights[0]>=reserve-1e-12,
             'Net expected return target': net>=objective-1e-12}
    if drawdown is not None:
        rules['Historical monthly drawdown <= 10%'] = drawdown <= DRAWDOWN_LIMIT+1e-12
    return dict(historical_max_drawdown=drawdown,
                live_mandate_verdict='FAIL: protected spending account not implemented; hard loss cap unproven',weights=list(weights),gross_return=gross,net_return=net,volatility=volatility,
                rules=rules,verdict='PASS' if all(rules.values()) else 'FAIL')

def run(recent=False, cost_bps=25, reserve=.20, vt_return=None, objective=.05):
    if not 0<=cost_bps<=1000 or not 0<=reserve<=1 or not 0<=objective<=1:
        raise ValueError('Costs, reserve and objective outside supported bounds.')
    estimates=p.estimate_from_csv(PRICES,last_36=recent)
    if vt_return is not None:
        estimates['returns'][-1]=vt_return
    mixes={'Equal weight':[.25]*4,'Inverse volatility':p.inverse_volatility_weights(estimates['volatilities']),
           '60/40 benchmark':[0,0,.4,.6],'Fixed pilot candidate':[.75,0,0,.25],'Student pilot 85/15':[.85,0,0,.15]}
    # Apply observed drawdown constraint during selection, not only after choosing.
    feasible=[]
    for weights in p.grid_weights(4):
        if weights[0] < reserve-1e-12 or p.expected_return(weights,estimates['returns']) < objective+cost_bps/10000-1e-12:
            continue
        if historical_drawdown(weights,recent,cost_bps) <= DRAWDOWN_LIMIT+1e-12:
            feasible.append(weights)
    covariance=p.covariance_matrix(estimates['volatilities'],estimates['correlations'])
    best=min(feasible,key=lambda w:p.portfolio_volatility(w,covariance)) if feasible else None
    if best is not None:
        mixes['Constrained portfolio']=list(best)
    return dict(build_sha256=build_fingerprint(),window='36 months' if recent else '60 months',cost_bps=cost_bps,reserve_minimum=reserve,
                objective=objective,estimates=estimates,portfolios={name:evaluate(w,estimates,cost_bps,objective,reserve,recent) for name,w in mixes.items()},
                feasible=best is not None, spending_policy={'annual_withdrawal_cap':SPENDING_RATE,'timing':'late August or September','protected_next_12_month_budget':True,'drawdown_limit':DRAWDOWN_LIMIT,'drawdown_basis':'cash-flow-adjusted NAV; monthly historical observations only'})

def report():
    scenarios={
      'historical_60':run(), 'historical_36':run(True),
      'vt_7_recent':run(True,vt_return=.07),
      'vt_6_5_recent':run(True,vt_return=.065),
      'cost_100bps':run(True,cost_bps=100,vt_return=.07),
      'reserve_90':run(True,reserve=.90,vt_return=.07)}
    return {'status':'Research prototype; human evidence incomplete',
            'recommendation':'PILOT in simulation only; 0% live allocation pending protected spending implementation, loss-cap evidence and validation',
            'candidate_range':'10–20% VT / 80–90% BIL for simulation, centered on the student-selected 85/15; not an approved live allocation',
            'stop':'Stop live allocation if any mandate test fails, data timing is unverified, protected spending is underfunded, or drawdown reaches 10%. A hard 10% maximum loss is not guaranteed.',
            'scenarios':scenarios}

if __name__=='__main__':
    import argparse
    parser=argparse.ArgumentParser(description='Write a reproducible developer report without changing frozen submission evidence.')
    parser.add_argument('--output',type=Path,default=ROOT/'work'/'committee-report.json',help='Output path; defaults to ignored work/committee-report.json. Use --output results/committee-report.json only when intentionally refreshing the frozen snapshot.')
    args=parser.parse_args()
    destination=args.output
    destination.parent.mkdir(parents=True,exist_ok=True)
    destination.write_text(json.dumps(report(),indent=2)+'\n')
    print(destination.resolve())
