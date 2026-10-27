"""Lab 16: fictional training values, not market data. Run python3 asof.py.
AI-assisted implementation; all outputs are calculated from editable inputs.
"""
from datetime import date

DECISION_DATE = '2026-03-31'
# Row number is provenance, not part of the economic duplicate key.
# Columns: row number, ticker, month measured, publication date, index.
ROWS = [
    (1, 'AAA', '2026-01', '2026-02-10', 101.0),
    (2, 'AAA', '2026-02', '2026-03-10', 104.0),
    (3, 'AAA', '2026-03', '2026-04-10', 109.0),
    (4, 'AAA', '2026-02', '2026-03-25', 103.0),
    (5, 'BBB', '2026-01', '2026-02-10', 98.0),
    (6, 'BBB', '2026-02', '2026-03-10', 97.0),
    (7, 'BBB', '2026-02', '2026-03-10', 97.0),
    (8, 'BBB', '2026-03', '2026-04-10', 92.0),
    (9, 'CCC', '2026-01', '2026-02-10', 110.0),
    (10, 'CCC', '2026-02', '2026-04-05', 112.0),
    (11, '', '2026-02', '2026-03-10', 99.0),
    (12, 'CCC', '2026-02', '2026-03-10', 111.0),
]


def clean_rows(rows):
    """Rules 1 and 2; keep the first occurrence of an exact duplicate."""
    quarantine = [r for r in rows if not r[1].strip()]
    valid = [r for r in rows if r[1].strip()]
    seen, unique, duplicates = set(), [], []
    for row in valid:
        key = row[1:]  # Same values with a different row number are duplicates.
        if key in seen:
            duplicates.append(row)
        else:
            seen.add(key)
            unique.append(row)
    return unique, quarantine, duplicates


def latest_vintages(rows):
    """Rule 4: select one latest publication per ticker and measured month.

    Caller must first impose the decision-date cutoff for an as-of result.
    Conflicting values with the same publication date are ambiguous, not revisions.
    """
    latest = {}
    for row in rows:
        key = (row[1], row[2])
        previous = latest.get(key)
        if previous is None or date.fromisoformat(row[3]) > date.fromisoformat(previous[3]):
            latest[key] = row
        elif row[3] == previous[3] and row[4] != previous[4]:
            raise ValueError(f'Conflicting same-date publications for {key}')
    panel = sorted(latest.values(), key=lambda r: (r[1], r[2]))
    kept = {r[0] for r in panel}
    replaced = [r for r in rows if r[0] not in kept]
    return panel, replaced


def asof_panel(rows, decision_date):
    unique, quarantine, duplicates = clean_rows(rows)
    cutoff = date.fromisoformat(decision_date)
    late = [r for r in unique if date.fromisoformat(r[3]) > cutoff]
    knowable = [r for r in unique if date.fromisoformat(r[3]) <= cutoff]
    panel, replaced = latest_vintages(knowable)
    funnel = [('Quarantined: no ticker', quarantine),
              ('Exact duplicate', duplicates),
              ('Published after ' + decision_date, late),
              ('Older vintage replaced by a revision', replaced)]
    return panel, funnel


def naive_panel(rows):
    # Same cleaning and revision policy, but deliberately ignore the time cutoff.
    unique, _, _ = clean_rows(rows)
    return latest_vintages(unique)[0]


def signals(panel):
    result = {}
    for ticker in sorted({r[1] for r in panel}):
        history = sorted((r for r in panel if r[1] == ticker), key=lambda r: r[2])
        current = history[-1]
        year, month = map(int, current[2].split('-'))
        previous_month = f'{year - 1}-12' if month == 1 else f'{year}-{month - 1:02d}'
        previous = next((r for r in history if r[2] == previous_month), None)
        value = None if previous is None or previous[4] == 0 else (current[4] / previous[4] - 1) * 100
        result[ticker] = (current[2], value)
    return result


def main():
    panel, funnel = asof_panel(ROWS, DECISION_DATE)
    print('FICTIONAL TRAINING DATA | Decision date: ' + DECISION_DATE)
    print(f'Input rows: {len(ROWS)}')
    for label, removed in funnel:
        print(f'{label}: removed {len(removed)}; rows ' + ', '.join(str(r[0]) for r in removed))
    print('As-of panel rows: ' + ', '.join(str(r[0]) for r in panel))
    print('\nRow | Ticker | Month measured | Published on | Index')
    for number, ticker, month, publication, value in panel:
        print(f'{number} | {ticker} | {month} | {publication} | {value:.1f}')
    actual, naive = signals(panel), signals(naive_panel(ROWS))
    def formatted(item):
        if item is None:
            return 'unavailable: no panel history'
        month, value = item
        return f'{value:+.2f}% ({month})' if value is not None else f'unavailable ({month}: previous month absent or zero)'
    print('\nTicker | As-of signal | Naive signal (ignores publication cutoff)')
    for ticker in sorted(set(actual) | set(naive)):
        print(f'{ticker} | {formatted(actual.get(ticker))} | {formatted(naive.get(ticker))}')


if __name__ == '__main__':
    main()
