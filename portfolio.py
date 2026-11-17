"""Meridian training risk engine. Annual decimal inputs; run python3 portfolio.py.
AI-assisted implementation. Inputs are course training values, not market estimates.
"""
import math

SLEEVES = ['Treasury bills', 'Treasury 10-year note',
           'Investment-grade bond fund', 'Global equity index fund']
EXPECTED_RETURNS = [0.035, 0.043, 0.050, 0.080]
VOLATILITIES = [0.005, 0.070, 0.060, 0.160]
CORRELATIONS = [[1.00, 0.10, 0.05, 0.00],
                [0.10, 1.00, 0.80, -0.10],
                [0.05, 0.80, 1.00, 0.25],
                [0.00, -0.10, 0.25, 1.00]]
OBJECTIVE_RETURN = 0.065  # Assumed CPI 2.5% + real objective 4%.
RESERVE_INDICES = (0, 1)


def covariance_matrix(volatilities, correlations):
    n = len(volatilities)
    if not n or any(not math.isfinite(v) or v <= 0 for v in volatilities):
        raise ValueError('Volatilities must be finite and positive.')
    if len(correlations) != n or any(len(row) != n for row in correlations):
        raise ValueError('Correlation dimensions must match volatilities.')
    for i in range(n):
        for j in range(n):
            r = correlations[i][j]
            if not math.isfinite(r) or not -1 <= r <= 1:
                raise ValueError('Every correlation must be between -1 and 1.')
            if not math.isclose(r, correlations[j][i], abs_tol=1e-12):
                raise ValueError('Correlation table must be symmetric; edit both cells.')
        if not math.isclose(correlations[i][i], 1, abs_tol=1e-12):
            raise ValueError('Diagonal correlations must equal 1.')
    # Semidefinite Cholesky check: valid pairwise ranges alone are insufficient.
    lower = [[0.0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i + 1):
            residual = correlations[i][j] - sum(lower[i][k] * lower[j][k] for k in range(j))
            if i == j:
                if residual < -1e-10:
                    raise ValueError('Correlation matrix must be positive semidefinite.')
                lower[i][j] = math.sqrt(max(0.0, residual))
            elif lower[j][j] > 1e-10:
                lower[i][j] = residual / lower[j][j]
            elif abs(residual) > 1e-10:
                raise ValueError('Correlation matrix must be positive semidefinite.')
    return [[correlations[i][j] * volatilities[i] * volatilities[j]
             for j in range(n)] for i in range(n)]


def validate_weights(weights, n):
    if len(weights) != n or any(not math.isfinite(w) or w < 0 for w in weights):
        raise ValueError('Supply one finite nonnegative weight per sleeve.')
    if not math.isclose(sum(weights), 1.0, abs_tol=1e-9):
        raise ValueError('Decimal weights must sum to 1.')


def expected_return(weights, returns):
    validate_weights(weights, len(returns))
    if any(not math.isfinite(r) for r in returns):
        raise ValueError('Expected returns must be finite.')
    return sum(w * r for w, r in zip(weights, returns))


def portfolio_volatility(weights, covariance):
    validate_weights(weights, len(covariance))
    if any(len(row) != len(weights) for row in covariance):
        raise ValueError('Covariance matrix must be square.')
    # Both (i,j) and (j,i) appear, supplying the factor of two for cross terms.
    variance = sum(weights[i] * weights[j] * covariance[i][j]
                   for i in range(len(weights)) for j in range(len(weights)))
    if not math.isfinite(variance) or variance < -1e-12:
        raise ValueError('Invalid portfolio variance.')
    return math.sqrt(max(0.0, variance))


def inverse_volatility_weights(volatilities):
    if not volatilities or any(not math.isfinite(v) or v <= 0 for v in volatilities):
        raise ValueError('Inverse volatility requires positive finite volatilities.')
    inverse = [1 / v for v in volatilities]
    return [v / sum(inverse) for v in inverse]


def reserve_weight(weights, indices=RESERVE_INDICES):
    return sum(weights[i] for i in indices)


def meets_objective(value, objective):
    return value >= objective - 1e-12


def baselines():
    return {'Benchmark': [0, 0, 0.4, 0.6],
            'Equal weight': [1 / len(SLEEVES)] * len(SLEEVES),
            'Inverse volatility': inverse_volatility_weights(VOLATILITIES)}


def main():
    try:
        covariance = covariance_matrix(VOLATILITIES, CORRELATIONS)
        print('COURSE TRAINING VALUES | annual returns/risk | objective 6.50%')
        print('Order: ' + ' / '.join(SLEEVES))
        for name, weights in baselines().items():
            ret = expected_return(weights, EXPECTED_RETURNS)
            risk = portfolio_volatility(weights, covariance)
            print(f'\n{name}: weights ' + ' / '.join(f'{w * 100:.1f}%' for w in weights))
            print(f'Return {ret * 100:.2f}% | volatility {risk * 100:.2f}% | '
                  f'reserve {reserve_weight(weights) * 100:.1f}% | '
                  f'meets objective: {"yes" if meets_objective(ret, OBJECTIVE_RETURN) else "no"}')
        print('\nReturn-target success is not full mandate compliance. Run mandate.py.')
    except ValueError as error:
        raise SystemExit(f'INPUT ERROR: {error}')



def grid_weights(n, remaining=20, prefix=()):
    """All long-only fully invested allocations on the five-percentage-point grid."""
    if n == 1:
        yield tuple(x / 20 for x in prefix + (remaining,))
    else:
        for units in range(remaining + 1):
            yield from grid_weights(n - 1, remaining - units, prefix + (units,))


def search(returns, volatilities, correlations, objective, reserve_minimum, reserve_indices):
    """Minimum risk on the discrete grid, not a continuous global optimum.

    Exact numerical ties keep the first allocation in grid order. No objective
    relaxation, leverage, shorting or uninvested remainder is allowed.
    """
    n = len(returns)
    if not 2 <= n <= 6 or len(volatilities) != n:
        raise ValueError('Search supports two to six assets with matching inputs.')
    if any(not math.isfinite(x) for x in returns + [objective, reserve_minimum]):
        raise ValueError('Return and mandate inputs must be finite.')
    if not 0 <= reserve_minimum <= 1:
        raise ValueError('Reserve minimum must be between 0 and 100%.')
    indices = tuple(reserve_indices)
    if len(set(indices)) != len(indices) or any(i not in range(n) for i in indices):
        raise ValueError('Reserve asset indices must be distinct and valid.')
    covariance = covariance_matrix(volatilities, correlations)
    best = None
    for weights in grid_weights(n):
        ret = expected_return(weights, returns)
        reserve = reserve_weight(weights, indices)
        if not meets_objective(ret, objective) or reserve < reserve_minimum - 1e-12:
            continue
        risk = portfolio_volatility(weights, covariance)
        if best is None or risk < best['volatility'] - 1e-12:
            best = dict(weights=list(weights), expected_return=ret,
                        volatility=risk, reserve_weight=reserve)
    return best


def estimate_from_csv(source, last_36=False):
    """Monthly adjusted prices -> annual arithmetic estimates. No silent cleaning.

    Last 36 means 36 returns from 37 prices. Sample SD/correlation use n-1.
    Input must have consecutive months, oldest first, and positive prices.
    All assets use exactly the same rows. Zero-volatility series are refused.
    """
    import csv
    import io
    import statistics
    from datetime import date
    from pathlib import Path
    if hasattr(source, 'read'):
        raw = source.read()
    else:
        raw = Path(source).read_bytes()
    text = raw.decode('utf-8-sig') if isinstance(raw, bytes) else raw
    rows = list(csv.reader(io.StringIO(text)))
    if len(rows) < 4:
        raise ValueError('Need a header and at least three monthly price rows.')
    names = [x.strip() for x in rows[0][1:]]
    if not 3 <= len(names) <= 6 or any(not x for x in names) or len(set(names)) != len(names):
        raise ValueError('Provide three to six unique ticker columns after the date.')
    dates, prices = [], []
    for line, row in enumerate(rows[1:], 2):
        if len(row) != len(names) + 1:
            raise ValueError(f'Row {line}: missing or extra cells; do not silently fill prices.')
        try:
            day = date.fromisoformat(row[0].strip())
            values = [float(x) for x in row[1:]]
        except ValueError:
            raise ValueError(f'Row {line}: use ISO dates and numeric prices.') from None
        if any(not math.isfinite(x) or x <= 0 for x in values):
            raise ValueError(f'Row {line}: prices must be positive and finite.')
        month = day.year * 12 + day.month
        if dates and month != dates[-1].year * 12 + dates[-1].month + 1:
            raise ValueError('Dates must be oldest first, one row per consecutive month.')
        dates.append(day); prices.append(values)
    monthly = [[b / a - 1 for a, b in zip(previous, current)]
               for previous, current in zip(prices, prices[1:])]
    if last_36:
        if len(monthly) < 36:
            raise ValueError('Last-36 comparison needs at least 37 monthly prices.')
        monthly = monthly[-36:]
    columns = list(zip(*monthly))
    means = [statistics.mean(x) for x in columns]
    stds = [statistics.stdev(x) for x in columns]
    if any(s <= 1e-12 for s in stds):
        raise ValueError('Zero-volatility series: check adjusted prices and fund suitability.')
    correlations = [[sum((a - means[i]) * (b - means[j]) for a, b in zip(columns[i], columns[j]))
                     / ((len(monthly) - 1) * stds[i] * stds[j])
                     for j in range(len(names))] for i in range(len(names))]
    # Floating arithmetic can put a mathematically unit diagonal just outside +/-1.
    correlations = [[max(-1.0, min(1.0, x)) for x in row] for row in correlations]
    volatilities = [x * math.sqrt(12) for x in stds]
    covariance_matrix(volatilities, correlations)
    return dict(names=names, returns=[x * 12 for x in means],
                volatilities=volatilities, correlations=correlations,
                price_rows=len(prices), return_months=len(monthly),
                start=dates[-len(monthly)-1].isoformat(), end=dates[-1].isoformat(),
                label='Historical arithmetic estimate, not a forecast')


def largest_weight_change(first, second):
    if first is None or second is None:
        return None
    return max(abs(a - b) for a, b in zip(first['weights'], second['weights'])) * 100


if __name__ == '__main__':
    main()
