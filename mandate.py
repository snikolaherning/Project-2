"""Meridian's holdings-only mandate checker. Run: python3 mandate.py"""
from collections import defaultdict

# Editable inputs: redemption is in business days; weights are percentages.
HOLDINGS = {
    'Cash': ('none', 0, True),
    'Treasury bills': ('U.S. Treasury', 1, True),
    'Treasury 10-year note': ('U.S. Treasury', 1, True),
    'Global equity index fund': ('diversified fund', 2, False),
    'Investment-grade bond fund': ('diversified fund', 3, False),
    'Private real estate fund': ('diversified fund', 90, False),
    'Acme Corp bonds': ('Acme Corp', 4, False),
    'Acme Corp stock': ('Acme Corp', 1, False),
}
CANDIDATES = {
    'A': dict(zip(HOLDINGS, [2, 2, 10, 60, 26, 0, 0, 0])),
    'B': dict(zip(HOLDINGS, [1, 0, 0, 55, 20, 15, 5, 4])),
    'C': dict(zip(HOLDINGS, [1, 1, 0, 70, 20, 0, 0, 8])),
    'D': dict(zip(HOLDINGS, [100, 0, 0, 0, 0, 0, 0, 0])),
    # Lab 14 benchmark: holdings checker uses percent weights, not decimals.
    'E': dict(zip(HOLDINGS, [0, 0, 0, 60, 40, 0, 0, 0])),
}
RESERVE_SIZE = 100.0  # USD millions
QUARTERLY_DISTRIBUTION = 0.75  # USD millions
QUARTERS_TO_COVER = 4
LIQUIDITY_WINDOW = 5
MINIMUM_LIQUID_SHARE = 90.0
ISSUER_LIMIT = 8.0
EXEMPT_ISSUERS = {'none', 'U.S. Treasury', 'diversified fund'}
TOLERANCE = 1e-9


def reserve_minimum():
    return QUARTERS_TO_COVER * QUARTERLY_DISTRIBUTION / RESERVE_SIZE * 100


def check(weights):
    if set(weights) != set(HOLDINGS):
        raise ValueError('Each candidate must specify every holding exactly once.')
    company_weights = defaultdict(float)
    reserve = liquid = 0.0
    for holding, weight in weights.items():
        issuer, days, eligible = HOLDINGS[holding]
        if eligible:
            reserve += weight
        if days <= LIQUIDITY_WINDOW:
            liquid += weight
        if issuer not in EXEMPT_ISSUERS:
            company_weights[issuer] += weight
    total = sum(weights.values())
    lowest = min(weights.values())
    largest = max(company_weights.values(), default=0.0)
    return [
        ('Weights sum to 100', total, abs(total - 100) <= TOLERANCE),
        ('Long-only (lowest weight)', lowest, lowest >= -TOLERANCE),
        (f'Reserve >= {reserve_minimum():.1f}%', reserve,
         reserve >= reserve_minimum() - TOLERANCE),
        (f'Redeemable in {LIQUIDITY_WINDOW} days >= {MINIMUM_LIQUID_SHARE:.1f}%',
         liquid, liquid >= MINIMUM_LIQUID_SHARE - TOLERANCE),
        (f'Largest single company <= {ISSUER_LIMIT:.1f}%', largest,
         largest <= ISSUER_LIMIT + TOLERANCE),
    ]


def main():
    print(f'Reserve minimum: {reserve_minimum():.1f}%')
    for name, weights in CANDIDATES.items():
        print(f'\nCandidate {name}')
        failures = 0
        for label, value, passed in check(weights):
            print(f'  {label}: {value:.1f} {"pass" if passed else "FAIL"}')
            failures += not passed
        print('  Calendar-year loss: requires CIO clarification')
        print('  ' + (f'fails {failures} rule(s)' if failures
                       else 'passes every checkable rule'))
    print('\nScope: passes every checkable rule refers only to the five tests above;')
    print('it is not full mandate approval or a guarantee of returns or losses.')


if __name__ == '__main__':
    main()
