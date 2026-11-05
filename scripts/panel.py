"""One SEC fact table shared by Buffett, Cathie Wood, and Burry."""
import argparse
import json
from pathlib import Path
import re
import edgar

ROOT = Path(__file__).resolve().parents[1]
INVESTORS = ('Buffett', 'Cathie Wood', 'Burry')
SLUGS = {'Buffett': 'buffett', 'Cathie Wood': 'wood', 'Burry': 'burry'}


def wood_threshold():
    skill = (ROOT / '.agents/skills/cathie-wood-edgar/SKILL.md').read_text()
    match = re.search(r'^Current-ratio threshold: ([0-9]+(?:\.[0-9]+)?)$', skill, re.M)
    if not match:
        raise ValueError('Current-ratio threshold missing from Cathie Wood skill.')
    value = float(match.group(1))
    if value <= 0:
        raise ValueError('Threshold must be positive.')
    return value


def status(condition):
    return 'not known' if condition is None else ('pass' if condition else 'fail')


def wood_checks(rows, threshold):
    """Explain this function to Anika: missing inputs produce not known."""
    latest_ratio = rows[-1]['current_ratio']['value']
    incomes = [row['net_income']['value'] for row in rows]
    first, last = incomes[0], incomes[-1]
    return {
        f'Current ratio at least {threshold:.1f}, latest year': status(
            None if latest_ratio is None else latest_ratio >= threshold),
        'Net income positive every year': edgar.every_check(incomes, lambda value: value > 0),
        'Net income grew first to last': status(
            None if first is None or last is None else last > first),
    }


def burry_checks(rows):
    comparisons = [(row['operating_cash_flow']['value'], row['net_income']['value']) for row in rows]
    cash_check = None if len(rows) != 5 or any(c is None or n is None for c, n in comparisons) else all(c >= n for c, n in comparisons)
    latest = rows[-1]
    liabilities, equity = latest['liabilities']['value'], latest['equity']['value']
    leverage_check = None if liabilities is None or equity is None or equity <= 0 else liabilities <= 2 * equity
    return {'Operating cash flow at least net income every year': status(cash_check),
            'Liabilities no more than twice equity, latest year': status(leverage_check)}


def analyze_panel(ticker, refresh=False, threshold=None):
    result = edgar.analyze(ticker, refresh)
    threshold = wood_threshold() if threshold is None else threshold
    result['thresholds'] = {'wood_current_ratio': threshold, 'buffett_roe_percent': 15, 'burry_liabilities_multiple': 2}
    result['panel'] = {'Buffett': result['checks'], 'Cathie Wood': wood_checks(result['rows'], threshold),
                       'Burry': burry_checks(result['rows'])}
    result['method'] += ' Current ratio = current assets / current liabilities; leverage = liabilities / equity. Nonpositive denominators are not known.'
    return result


def panel_table(result):
    return [{'Investor': investor, 'Check': check, 'Result': outcome}
            for investor, checks in result['panel'].items() for check, outcome in checks.items()]


def unsupported_numbers(memo, result):
    allowed = {edgar.number_key(str(row['fiscal_year'])) for row in result['rows']}
    for row in result['rows']:
        for metric in list(edgar.TAGS) + ['roe', 'owner_earnings', 'current_ratio', 'liabilities_to_equity']:
            if row[metric]['value'] is not None:
                allowed.add(edgar.number_key(edgar.display_value(metric, row[metric]['value'])))
    # Thresholds are explicitly printed by this script, including the probe setting.
    for key, value in result['thresholds'].items():
        allowed.add(edgar.number_key(f'{value:.1f}'))
        if key.endswith('percent'):
            allowed.add(edgar.number_key(f'{value:.1f}%'))
    return [match.group() for match in edgar.NUMBER.finditer(memo) if edgar.number_key(match.group()) not in allowed]


def memo_path(ticker, investor):
    return ROOT / 'memos' / ticker / (SLUGS[investor] + '.md')


def verdict(memo):
    match = re.search(r'Verdict:\s*(own the business|watch it|pass)', memo, re.I)
    return match.group(1).lower() if match else 'not written'


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('ticker')
    parser.add_argument('--refresh', action='store_true')
    parser.add_argument('--wood-threshold', type=float, help='Temporary probe override; default comes from the Wood skill.')
    args = parser.parse_args()
    result = analyze_panel(args.ticker, args.refresh, args.wood_threshold)
    print(result['company'])
    print(result['method'])
    print('Printed thresholds:', json.dumps(result['thresholds']))
    print(json.dumps(edgar.table(result), indent=2))
    print(json.dumps(panel_table(result), indent=2))
    target = ROOT / 'data' / (result['ticker'] + '-panel.json')
    target.write_text(json.dumps(result, indent=2))
    for investor in INVESTORS:
        path = memo_path(result['ticker'], investor)
        if path.exists():
            memo = path.read_text()
            print(investor, 'verdict:', verdict(memo), '; unsupported numbers:', unsupported_numbers(memo, result))


if __name__ == '__main__':
    main()
