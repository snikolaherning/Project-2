Codex was used for implementation, calculation checks, and drafting.
The analysis and final decision are mine; education, not investment advice.

# Validation and AI use

## Executed automated evidence

Run `python committee.py` for all stress outputs. `results/committee-report.json` contains full precision, inputs, all portfolio verdicts and both windows. Scenarios cover historical windows, VT return assumptions, implementation drag and reserve constraints. These precomputed scenarios are AI-assisted development checks, not the human locked experiment.

Four engine tests passed on November 17: known-answer covariance, arithmetic costs, rule failures/infeasibility, and grid constraints. Python compilation passed. A Streamlit AppTest was added, but execution is pending because importing the previous lab environment stalled; rendered UI and fresh dependency installation are not yet verified. Data snapshot provenance and known-answer history are preserved in `Lab15 2/lab15-stability.md`, its source-evidence JSON, and `Lab17/lab17-data-card.md`. Historical student attestations are not new independent verification. No untouched holdout or live trading result is claimed.

## Locked Changed-Input Record — existing Lab 20 experiment

The updated main branch already contained the student's completed 5.0% to 4.5% objective experiment. See [original prediction and result](../lab20-changed-input.md), [before JSON](../evidence/before-5pct.json), and [after JSON](../evidence/after-4_5pct.json). Student confirmed AI-off authorship in this chat November 17. Do not represent the later docs/locked-prediction.md commit as preceding this already completed experiment. That local snapshot was made before this chat discovered the existing run, not before the original run.

Before: 80% BIL / 20% VT, 5.2545% gross expected return, 3.0937% annualized volatility. After: 85% BIL / 15% VT, 4.8394% gross return, 2.3654% volatility. Both JSON files preserve the same price hash, estimation inputs and reserve floor. Original lab engine omitted separately modeled costs and the new drawdown screen; these are not outputs of the committee engine's net-cost convention.

Allocation and directional predictions matched; expected return was higher than the predicted approximately 4.6%. The adoption prediction failed: fixed 85/15 with VT at 6.5% produces about 4.0301% with all-month BIL estimates, below 4.5%. The student subsequently chose simulation-only pilot. A lower target relaxes a requirement; it does not improve asset returns or establish protection from loss.

GitHub history shows the prediction file first appearing in 1ac1db6 and updated in cbe18ca. Student reports pushing the prediction before the original run. Execution timestamps are not embedded in the evidence, so independent chronological verification remains a limitation. No rerun is presented as an original locked experiment.

## Independent cold run — review recorded, successful retry pending

The updated Lab 20 record identifies Ross Dyson as the actual reviewer. Linda Li was an earlier partner reference and is not substituted for Ross's recorded activity. Ross found README routing to the investor panel, attempted no command, and did not record elapsed time. See [Lab 20 record](lab20-readiness.md). Code question and role swap are recorded there. A clean independent execution/retry is still needed; developer tests do not replace it.

## Source integrity check

Executed November 17: prices.csv and all four raw ETF JSON responses match every SHA-256 in the preserved download manifest; see results/source-integrity.json. This verifies snapshot integrity, not vendor accuracy or original point-in-time adjustment history.

## Independent cold run — NOT COMPLETE

Partner: Linda Li, as supplied by student. Record command attempted, first failure or none, elapsed time, result location, fix commit if applicable and retry result. Do not claim the developer's automated app test is an independent partner run.

## AI use and material dispositions

November 17, 2026: OpenAI Codex, model/version not exposed in this session, retrieved existing work, wrote the committee wrapper and UI, generated automated stress outputs, and drafted documents. Student analysis and recommendation require review. Earlier AI uses and student verifications remain attributed in the lab records.

Checked AI claim: the former student code explanation suggested a five-point grid bounded distance from the continuous optimum. The Lab 15 record explicitly corrected that unsupported claim; current app states only a grid minimum. The net-cost bridge subtracts basis points / 10,000, covered by a known-answer test. AI output is not independent validation.

## Limitations driving action

The hard 10% drawdown cap and protected spending requirement are not demonstrated; they block live adoption. Frozen adjusted histories may be revised and are not a true historical-vintage ETF backtest. Source retrieval needs no credentials, but Yahoo licensing/redistribution permissions were not established; retain educational source attribution and obtain permitted data before broader deployment. TB3MS vintage findings are preserved lab evidence, not newly fetched raw vintage data. A point-in-time context input does not demonstrate predictive value. Implementation drag is hypothetical, not measured execution slippage. No holdout performance claim.

## Student mandate clarification — November 17, 2026

Student selected a 10% maximum peak-to-trough investment loss, full protection of the next 12 months of spending, and one withdrawal in late August or September of up to 5% of the reserve. Operational interpretation: set the approved dollar spending budget at the annual decision date, with a 5% ceiling based on reserve value then; keep that dollar obligation protected after market losses. Measure investment drawdown on cash-flow-adjusted NAV so the annual withdrawal does not count as a market loss. This interpretation should be confirmed against the club's actual budget.

The historical screen uses monthly rebalanced constant weights, monthly adjusted total returns, and annual implementation drag divided by 12. Include starting NAV in the high-water mark. It is descriptive in-sample evidence, not a point-in-time trading backtest. Monthly observations can miss intramonth drawdowns. The search now rejects grid candidates exceeding 10% observed monthly drawdown in the active window. It does not simulate stop-order fills or certify a future hard cap.

Protecting spending requires a separately identified dollar account and due-date cash availability. A proposed cash or maturity-matched direct Treasury sleeve is outside the current ETF universe and has not yet been implemented. BIL alone is not evidence of complete principal protection. All current portfolios therefore FAIL full live mandate approval even if their numerical screen passes. Existing return and covariance results describe the ETF prototype, not a portfolio with a new protected sleeve; adding that sleeve requires recalculating expected return, risk and the mandate bridge.

Proposed monitoring: review cash-flow-adjusted drawdown each trading day; 8% is an analyst-proposed early-warning level, not a student-approved limit. At 10%, stop further risk deployment and refer allocation reduction to committee review. If the protected dollar account cannot meet the budget on time, stop approval. A stop trigger cannot guarantee a 10% maximum loss, so **reject live adoption under the hard cap today; pilot only in simulation with 0% live allocation**.

Sources: [TreasuryDirect: bills pay face value at maturity](https://www.treasurydirect.gov/marketable-securities/treasury-bills/); [SEC: stop price is not a guaranteed execution price](https://www.investor.gov/introduction-investing/general-resources/news-alerts/alerts-bulletins/investor-bulletins-14). Nominal maturity cash flows do not guarantee a stable daily market value or an inflation-adjusted spending amount.

