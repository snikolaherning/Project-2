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


if __name__ == '__main__':
    main()
