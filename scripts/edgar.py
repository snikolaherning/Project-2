"""SEC-only Buffett lab: deterministic annual facts, checks, and memo validation."""
import argparse
import datetime as dt
import json
from pathlib import Path
import re
import time
import urllib.request

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / 'data'
USER_AGENT = 'Stefan sherning@purdue.edu'
TAGS = {
    'revenue': ['RevenueFromContractWithCustomerExcludingAssessedTax', 'Revenues', 'SalesRevenueNet'],
    'net_income': ['NetIncomeLoss', 'ProfitLoss'],
    'operating_cash_flow': ['NetCashProvidedByUsedInOperatingActivities'],
    'capital_spending': ['PaymentsToAcquirePropertyPlantAndEquipment'],
    'liabilities': ['Liabilities'],
    'current_assets': ['AssetsCurrent'],
    'current_liabilities': ['LiabilitiesCurrent'],
    'equity': ['StockholdersEquity', 'StockholdersEquityIncludingPortionAttributableToNoncontrollingInterest'],
}


def download(url, path, refresh=False):
    """Cache raw SEC responses; fail visibly rather than substitute another source."""
    if refresh or not path.exists():
        time.sleep(0.2)
        req = urllib.request.Request(url, headers={'User-Agent': USER_AGENT})
        with urllib.request.urlopen(req, timeout=45) as response:
            raw = response.read()
        parsed = json.loads(raw)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(parsed))
    return json.loads(path.read_text())


def annual(fact):
    if fact.get('form') not in ('10-K', '10-K/A') or not fact.get('start'):
        return False
    days = (dt.date.fromisoformat(fact['end']) - dt.date.fromisoformat(fact['start'])).days
    return 330 <= days <= 385


def facts_for(facts, tag):
    return facts.get('facts', {}).get('us-gaap', {}).get(tag, {}).get('units', {}).get('USD', [])


def select_value(facts, metric, start, end):
    """Match the actual fiscal period, not fy (which can label later comparatives)."""
    for tag in TAGS[metric]:
        candidates = [f for f in facts_for(facts, tag)
                      if f.get('form') in ('10-K', '10-K/A') and f['end'] == end
                      and (not f.get('start') if metric in ('equity', 'liabilities', 'current_assets', 'current_liabilities')
                           else annual(f) and f['start'] == start)]
        if candidates:
            f = max(candidates, key=lambda v: (v.get('filed', ''), v.get('accn', '')))
            return {'value': f['val'], 'tag': 'us-gaap:' + tag,
                    'filed': f.get('filed'), 'accession': f.get('accn')}
    return {'value': None, 'tag': 'not found'}


def year_row(facts, year, start, end):
    """The function to explain to your partner: missing facts remain None."""
    row = {'fiscal_year': year, 'start': start, 'end': end}
    for metric in TAGS:
        row[metric] = select_value(facts, metric, start, end)
    income, equity = row['net_income']['value'], row['equity']['value']
    cash, capex = row['operating_cash_flow']['value'], row['capital_spending']['value']
    row['roe'] = {'value': income / equity * 100 if income is not None and equity is not None and equity > 0 else None,
                  'tag': 'derived: net_income / year-end equity * 100'}
    row['owner_earnings'] = {'value': cash - capex if cash is not None and capex is not None else None,
                             'tag': 'derived: operating_cash_flow - capital_spending'}
    assets, current_liabilities = row['current_assets']['value'], row['current_liabilities']['value']
    liabilities = row['liabilities']['value']
    row['current_ratio'] = {'value': assets / current_liabilities if assets is not None and current_liabilities is not None and current_liabilities > 0 else None,
                            'tag': 'derived: us-gaap:AssetsCurrent / us-gaap:LiabilitiesCurrent'}
    row['liabilities_to_equity'] = {'value': liabilities / equity if liabilities is not None and equity is not None and equity > 0 else None,
                                    'tag': 'derived: us-gaap:Liabilities / equity'}
    return row


def every_check(values, predicate):
    if len(values) != 5 or any(v is None for v in values):
        return 'not known'
    return 'pass' if all(predicate(v) for v in values) else 'fail'


def analyze(ticker, refresh=False):
    ticker = ticker.strip().upper()
    if not re.fullmatch(r'[A-Z0-9.-]{1,12}', ticker):
        raise ValueError('Enter a valid ticker.')
    index = download('https://www.sec.gov/files/company_tickers.json', DATA / 'company_tickers.json', refresh)
    company = next((v for v in index.values() if v['ticker'].upper() == ticker), None)
    if not company:
        raise ValueError('Ticker not found in SEC index.')
    cik = str(company['cik_str']).zfill(10)
    url = 'https://data.sec.gov/api/xbrl/companyfacts/CIK' + cik + '.json'
    facts = download(url, DATA / ('CIK' + cik + '.json'), refresh)
    # OCF supplies fiscal boundaries; never confuse quarterly periods with years.
    periods = {}
    for f in facts_for(facts, 'NetCashProvidedByUsedInOperatingActivities'):
        if annual(f):
            key = (f['start'], f['end'])
            if key not in periods or f.get('filed', '') < periods[key].get('filed', ''):
                periods[key] = f
    chosen = sorted(periods.items(), key=lambda p: p[0][1])[-5:]
    if len(chosen) != 5:
        raise ValueError('Five annual operating cash-flow periods were not found.')
    rows = [year_row(facts, f.get('fy', int(end[:4])), start, end)
            for (start, end), f in chosen]
    oe = [r['owner_earnings']['value'] for r in rows]
    checks = {'ROE at least 15% every year': every_check([r['roe']['value'] for r in rows], lambda v: v >= 15),
              'Owner earnings positive every year': every_check(oe, lambda v: v > 0),
              'Owner earnings grew first to last': 'not known' if any(v is None for v in oe)
              else ('pass' if oe[-1] > oe[0] else 'fail')}
    return {'ticker': ticker, 'company': company['title'], 'source': url,
            'method': 'USD millions; ROE uses year-end equity; owner earnings is an OCF minus total capex proxy, not estimated maintenance capex.',
            'rows': rows, 'checks': checks}


def display_value(metric, value):
    if value is None:
        return 'not found'
    if metric in ('current_ratio', 'liabilities_to_equity'):
        return f'{value:.2f}'
    return f'{value:.2f}%' if metric == 'roe' else f'{value / 1_000_000:,.1f}'


def table(result):
    out = []
    for row in result['rows']:
        r = {'FY': str(row['fiscal_year'])}
        for metric in list(TAGS) + ['roe', 'owner_earnings', 'current_ratio', 'liabilities_to_equity']:
            r[metric] = display_value(metric, row[metric]['value'])
            r[metric + '_tag'] = row[metric]['tag']
        out.append(r)
    return out


NUMBER = re.compile(r'(?<![\w])[-+]?\d[\d,]*(?:\.\d+)?%?(?![\w])')


def number_key(token):
    # Numeric equality, but percentages cannot masquerade as dollar values.
    from decimal import Decimal
    return (Decimal(token.replace(',', '').rstrip('%')), token.endswith('%'))


def unsupported_numbers(memo, result):
    allowed = {number_key(str(r['fiscal_year'])) for r in result['rows']}
    for row in result['rows']:
        for metric in list(TAGS) + ['roe', 'owner_earnings', 'current_ratio', 'liabilities_to_equity']:
            if row[metric]['value'] is not None:
                allowed.add(number_key(display_value(metric, row[metric]['value'])))
    return [m.group() for m in NUMBER.finditer(memo) if number_key(m.group()) not in allowed]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('ticker')
    parser.add_argument('--refresh', action='store_true')
    args = parser.parse_args()
    result = analyze(args.ticker, args.refresh)
    target = ROOT / 'data' / (result['ticker'] + '-analysis.json')
    target.write_text(json.dumps(result, indent=2))
    print(result['company'] + '\n' + result['method'])
    print(json.dumps(table(result), indent=2))
    print(json.dumps(result['checks'], indent=2))
    print('Saved:', target)


if __name__ == '__main__':
    main()
