Codex was used for implementation, calculation checks, and drafting.
The analysis and final decision are mine; education, not investment advice.

# Project 2 — University club reserve

Research prototype. Proposed recommendation: **pilot in simulation only; 0% live allocation** until the mandate and validation are complete. Stefan’s recorded decision is simulation-only; full live mandate approval remains rejected.

## Start

One-command setup and launch from the repository root: `python3 run_portfolio.py` (Windows: `py run_portfolio.py`). This installs dependencies and launches the current committee app. The earlier Lab 20 gross-cost-free app remains in portfolio-tool for evidence; its numbers differ from the current net-cost screen.

Python 3.9+ (tested on Python 3.9.6); no API key or network needed after dependency installation. From the repository root:

```sh
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m streamlit run app.py --server.headless=true --browser.gatherUsageStats=false
```

Open the local URL printed by Streamlit. Change a sidebar control and read the rule verdict and failed-rule column. Download the current JSON. The primary app uses frozen data; the separate historical company panel is available with `python -m streamlit run company_panel.py` and is not the portfolio decision engine.

Generate a comparison report: `python committee.py` writes ignored `work/committee-report.json`, leaving frozen submission evidence unchanged. Intentionally refresh the visible snapshot only with `python committee.py --output results/committee-report.json`. Validate: `python -m unittest discover -s tests -v`.

## Verify the copy you launched

If port 8515 is occupied, run `python3 run_portfolio.py --port 8516` (Windows: `py run_portfolio.py --port 8516`). Open the exact new URL printed by this command. Do not test the old server and call it a fresh-install result. The launcher and app display the same build fingerprint; compare them, and retain the complete build_sha256 in the downloaded JSON. A code fingerprint identifies file contents, not an independently verified Git commit.

The recommendation panel responds to current controls: reject 85/15 when it fails numerical rules, permit simulation-only pilot when it passes, and stop an infeasible scenario. Live allocation stays 0% because full mandate protection is unproven; a numerical pass never silently authorizes adoption.

## Which files matter

| Purpose | Current file |
|---|---|
| Start app | run_portfolio.py |
| Committee UI and club rules | app.py and committee.py |
| Decision and validation | docs/decision-memo.md and docs/validation-and-ai-use.md |
| Frozen visible output | results/committee-report.json |
| Original locked Lab 20 experiment | lab20-changed-input.md and evidence/before-5pct.json / after-4_5pct.json |
| Independent review | docs/independent-review-linda.md |

`mandate.py` is the legacy Meridian classroom example, not the club's mandate. CHECKOUT.md, company_panel.py, scripts/, memos/ and older lab folders preserve historical exercises. portfolio-tool/ preserves the original Lab 20 app; it is not the current launch path.

Initial setup requires internet access to PyPI. Once installed, the committee app uses bundled data without network access. A sandbox blocking PyPI cannot complete a fresh app cold run. In that case, record the failure; engine-only checks are available with `python3 -m unittest discover -s tests -p test_committee.py -v` and do not establish browser usability.

## Mandate and scope

University club reserve; five-year horizon; BIL/IEF/LQD/VT universe; 5% annual nominal expected-return target, modeled net of the explicit implementation drag; BIL minimum 20%; long only, fully invested. Benchmark 60% VT / 40% LQD. Minimize annualized sample volatility on a five-percentage-point grid. The net-of-cost target is a conservative Project 2 interpretation of the earlier gross lab target, disclosed as an illustrative conservative cost convention, not a measured fee. Risk and spending limits were supplied November 19; see the clarification below. No full mandate approval is claimed.

Historical inputs: monthly adjusted prices September 2021–September 2026, downloaded October 22, 2026. A 60-return and a 36-return window are available. Expected returns use monthly arithmetic mean ×12; volatility uses sample SD ×sqrt(12). No backtested out-of-sample performance or guaranteed returns are claimed. See `Lab15 2/lab15-stability.md` and `source-evidence` there for lineage. TB3MS is a point-in-time context signal only, not an ETF return or trading rule; see `Lab17/lab17-data-card.md`.

## Review

- Executed results: [committee-report.json](results/committee-report.json)
- [Decision memo](docs/decision-memo.md)
- [Validation and AI use](docs/validation-and-ai-use.md)
- [Submission manifest](docs/submission-manifest.md)
- [Remaining work](docs/readiness.md)
- [Student assumptions and checked bridges](docs/student-decisions.md)
- [Load-bearing risk challenge](docs/risk-challenge.md)
- [Recording workflow](docs/recording/recording-checklist.md)
- [Readable executed output](docs/output-snapshot.md)
- [Point-in-time signal card](docs/signal-data-card.md)

Earlier lab folders are retained for evidence. They contain historical instructions and status notes; this README defines the current app. Edition A/B are personal comparison materials, not required submission artifacts. The changed-input prediction must be written by the student with AI off and pushed before that specific experiment is run. Automated scenarios are not that record.

## Student mandate clarification — November 17, 2026

Student selected a 10% maximum peak-to-trough investment loss, full protection of the next 12 months of spending, and one withdrawal in late August or September of up to 5% of the reserve. Operational interpretation: set the approved dollar spending budget at the annual decision date, with a 5% ceiling based on reserve value then; keep that dollar obligation protected after market losses. Measure investment drawdown on cash-flow-adjusted NAV so the annual withdrawal does not count as a market loss. This interpretation should be confirmed against the club's actual budget.

The historical screen uses monthly rebalanced constant weights, monthly adjusted total returns, and annual implementation drag divided by 12. Include starting NAV in the high-water mark. It is descriptive in-sample evidence, not a point-in-time trading backtest. Monthly observations can miss intramonth drawdowns. The search now rejects grid candidates exceeding 10% observed monthly drawdown in the active window. It does not simulate stop-order fills or certify a future hard cap.

Protecting spending requires a separately identified dollar account and due-date cash availability. A proposed cash or maturity-matched direct Treasury sleeve is outside the current ETF universe and has not yet been implemented. BIL alone is not evidence of complete principal protection. All current portfolios therefore FAIL full live mandate approval even if their numerical screen passes. Existing return and covariance results describe the ETF prototype, not a portfolio with a new protected sleeve; adding that sleeve requires recalculating expected return, risk and the mandate bridge.

Proposed monitoring: review cash-flow-adjusted drawdown each trading day; 8% is an analyst-proposed early-warning level, not a student-approved limit. At 10%, stop further risk deployment and refer allocation reduction to committee review. If the protected dollar account cannot meet the budget on time, stop approval. A stop trigger cannot guarantee a 10% maximum loss, so **reject live adoption under the hard cap today; pilot only in simulation with 0% live allocation**.

Sources: [TreasuryDirect: bills pay face value at maturity](https://www.treasurydirect.gov/marketable-securities/treasury-bills/); [SEC: stop price is not a guaranteed execution price](https://www.investor.gov/introduction-investing/general-resources/news-alerts/alerts-bulletins/investor-bulletins-14). Nominal maturity cash flows do not guarantee a stable daily market value or an inflation-adjusted spending amount.


## November 19 decision checks

Use Reset to base to restore the frozen 60-month historical case. Scenario controls are bounded and the sidebar explains what is editable or locked. Student BIL stress 2.75–3.25% / VT stress 6.5–7.5% is distinct from the historical base; the confirmed live allocation remains 0%. BIL is the largest sensitivity. See docs/student-decisions.md for dated source checks and docs/risk-challenge.md for fixed-candidate stress and retrospective time split.

Generate supplemental checks: `python risk_review.py` (ignored work/risk-review.json). Intentionally refresh frozen evidence only with `python risk_review.py --output results/risk-review.json`. The raw ALFRED snapshots under data/signal/ make the point-in-time comparison runnable offline after package installation. The new fingerprint differs from Linda's November 17 evidence because the controls and risk checks changed; her historical successful run is retained, not relabeled as a test of later code.
