# Video 2 — Code walkthrough

Preparation script, NOT a transcript. Record the screen with webcam on and clear audio throughout. Maximum 5:00; aim for 4:00–4:40. Open the files/functions below before recording. Explain in your own words; do not claim you wrote code unaided.

[0:00 — editor on screen; both opening statements]

Codex helped me implement the app, check calculations, and draft documentation.
The analysis and decision are mine; this is education, not investment advice.

[0:15 — run_portfolio.py]

The README leads to this launcher. It creates a local virtual environment, installs the pinned requirements and starts Streamlit. Initial installation needs internet access to PyPI. Headless mode avoids an onboarding prompt. The port argument allows a fresh copy to run without connecting to an old server. The launcher and app show a matching source fingerprint; that identifies file contents, not financial validity.

[0:55 — portfolio.py: estimate_from_csv]

This function reads monthly adjusted prices. It rejects nonpositive prices, duplicate or missing months, and malformed rows instead of silently filling data. Sixty-one prices produce sixty returns. The short window uses thirty-six returns from thirty-seven prices.

For each asset, monthly return is the price ratio minus one. Arithmetic mean times twelve supplies the annual return estimate. Sample standard deviation times square root of twelve supplies annualized volatility. Both windows are historical estimates, not forecasts.

[1:40 — portfolio.py: covariance_matrix and portfolio_volatility]

The covariance table combines volatility and correlation. Portfolio variance sums all weighted covariance terms, including both off-diagonal directions, then volatility takes the square root. Averaging individual volatilities would ignore how the assets move together. The code validates symmetry and positive semidefiniteness.

[2:15 — committee.py: run, evaluate, historical_drawdown]

The run function supplies equal weight, inverse volatility, the benchmark, the older fixed candidate and my 85/15 candidate. It enumerates fully invested long-only allocations in five-percentage-point steps. Candidates must meet the net return target, BIL floor and observed monthly drawdown screen. It chooses the lowest annualized volatility among those grid candidates, or returns infeasible.

Evaluate subtracts basis points divided by ten thousand from gross expected return. Historical drawdown compounds the weighted monthly path, tracks its running high and measures the worst fall. Starting NAV is included. This monthly-rebalanced, in-sample screen does not guarantee a future ten-percent cap or show intramonth losses.

[3:10 — committee.py: decision_for; app.py]

The bounded driver panel labels fixed policies, enables BIL and VT overrides, and has a tested base reset. Override bounds are analyst testing envelopes, not statistical intervals. The UI passes the controls into the engine. The decision function rejects 85/15 when its numerical rules fail, permits simulation-only pilot when they pass, and stops an infeasible scenario. It never changes the zero live allocation because spending protection and the hard future cap are unproven. Downloads retain inputs, verdicts and the source fingerprint.

[3:45 — tests and validation document]

Twenty developer tests passed: eight original engine checks, three UI/decision/reset checks, and nine risk/provenance/time-split checks. They cover known covariance and cost answers, source-price reconstruction, actual vintage availability, BIL sensitivity and break-even, crash and spending probes, reset and decision transitions. A future-price mutation confirms training-only selection in the retrospective split. Linda's successful fresh-copy retry is separate evidence, based on the reported matching fingerprints and screenshot.

There is no untouched holdout performance claim. A working app and passing arithmetic tests do not establish a profitable or adoptable process.
