Codex was used for implementation, calculation checks, and drafting.
The analysis and final decision are mine; education, not investment advice.

# Project 2 — University club reserve

Research prototype. Proposed recommendation: **pilot in simulation only; 0% live allocation** until the mandate and validation are complete. Student must review and adopt the final recommendation.

## Start

One-command setup and launch from the repository root: `python3 run_portfolio.py` (Windows: `py run_portfolio.py`). This installs dependencies and launches the current committee app. The earlier Lab 20 gross-cost-free app remains in portfolio-tool for evidence; its numbers differ from the current net-cost screen.

Python 3.10+; no API key or network needed after dependency installation. From the repository root:

```sh
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m streamlit run app.py
```

Open the local URL printed by Streamlit. Change a sidebar control and read the rule verdict and failed-rule column. Download the current JSON. The primary app uses frozen data; the separate historical company panel is available with `python -m streamlit run company_panel.py` and is not the portfolio decision engine.

Recreate visible output: `python committee.py`. Validate: `python -m unittest discover -s tests -v`.

## Mandate and scope

University club reserve; five-year horizon; BIL/IEF/LQD/VT universe; 5% annual nominal expected-return target, modeled net of the explicit implementation drag; BIL minimum 20%; long only, fully invested. Benchmark 60% VT / 40% LQD. Minimize annualized sample volatility on a five-percentage-point grid. The net-of-cost target is a conservative Project 2 interpretation of the earlier gross lab target, requiring student approval. Risk and spending limits were supplied November 17; see the clarification below. No full mandate approval is claimed.

Historical inputs: monthly adjusted prices September 2021–September 2026, downloaded October 22, 2026. A 60-return and a 36-return window are available. Expected returns use monthly arithmetic mean ×12; volatility uses sample SD ×sqrt(12). No backtested out-of-sample performance or guaranteed returns are claimed. See `Lab15 2/lab15-stability.md` and `source-evidence` there for lineage. TB3MS is a point-in-time context signal only, not an ETF return or trading rule; see `Lab17/lab17-data-card.md`.

## Review

- Executed results: [committee-report.json](results/committee-report.json)
- [Decision memo](docs/decision-memo.md)
- [Validation and AI use](docs/validation-and-ai-use.md)
- [Submission manifest](docs/submission-manifest.md)
- [Remaining work](docs/readiness.md)

Earlier lab folders are retained for evidence. They contain historical instructions and status notes; this README defines the current app. Edition A/B are personal comparison materials, not required submission artifacts. The changed-input prediction must be written by the student with AI off and pushed before that specific experiment is run. Automated scenarios are not that record.

## Student mandate clarification — November 17, 2026

Student selected a 10% maximum peak-to-trough investment loss, full protection of the next 12 months of spending, and one withdrawal in late August or September of up to 5% of the reserve. Operational interpretation: set the approved dollar spending budget at the annual decision date, with a 5% ceiling based on reserve value then; keep that dollar obligation protected after market losses. Measure investment drawdown on cash-flow-adjusted NAV so the annual withdrawal does not count as a market loss. This interpretation should be confirmed against the club's actual budget.

The historical screen uses monthly rebalanced constant weights, monthly adjusted total returns, and annual implementation drag divided by 12. Include starting NAV in the high-water mark. It is descriptive in-sample evidence, not a point-in-time trading backtest. Monthly observations can miss intramonth drawdowns. The search now rejects grid candidates exceeding 10% observed monthly drawdown in the active window. It does not simulate stop-order fills or certify a future hard cap.

Protecting spending requires a separately identified dollar account and due-date cash availability. A proposed cash or maturity-matched direct Treasury sleeve is outside the current ETF universe and has not yet been implemented. BIL alone is not evidence of complete principal protection. All current portfolios therefore FAIL full live mandate approval even if their numerical screen passes. Existing return and covariance results describe the ETF prototype, not a portfolio with a new protected sleeve; adding that sleeve requires recalculating expected return, risk and the mandate bridge.

Proposed monitoring: review cash-flow-adjusted drawdown each trading day; 8% is an analyst-proposed early-warning level, not a student-approved limit. At 10%, stop further risk deployment and refer allocation reduction to committee review. If the protected dollar account cannot meet the budget on time, stop approval. A stop trigger cannot guarantee a 10% maximum loss, so **reject live adoption under the hard cap today; pilot only in simulation with 0% live allocation**.

Sources: [TreasuryDirect: bills pay face value at maturity](https://www.treasurydirect.gov/marketable-securities/treasury-bills/); [SEC: stop price is not a guaranteed execution price](https://www.investor.gov/introduction-investing/general-resources/news-alerts/alerts-bulletins/investor-bulletins-14). Nominal maturity cash flows do not guarantee a stable daily market value or an inflation-adjusted spending amount.

