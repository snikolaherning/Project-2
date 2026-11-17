Codex was used for implementation, calculation checks, and drafting.
The analysis and final decision are mine; education, not investment advice.

# Committee decision memo — draft for student approval

November 17, 2026. Intended user: university club investment committee. Decision horizon: five years; estimates are annual, nominal USD returns.

**Committee ask: approve a simulation-only pilot, with 0% live allocation today.** Carry forward the updated student choice of 85% BIL / 15% VT, with a 10–20% VT / 80–90% BIL simulation research range; this range is a research envelope, not a validated allocation recommendation. Earlier student-approved Lab 15 judgment favored testing 75% BIL / 25% VT and rejected adopting the historically optimized 95/5 mix.

The mandate targets 5% annually and at least 20% Treasury-bill funds. The app compares equal weight and inverse volatility with a constrained minimum-volatility portfolio, alongside the 60/40 VT/LQD benchmark. Each has explicit rule results. Historical prices are frozen as retrieved October 22; changing windows changes estimates, not realized future performance. The proposed Project 2 target is net of a 25-basis-point annual implementation drag; this additional conservative convention needs student approval.

| Scenario | Fixed 75/25 net estimate | Fixed historical max drawdown | Numerical verdict | Constrained BIL/IEF/LQD/VT |
|---|---:|---:|---|---|
| historical_60 | 5.42% | 6.58% | PASS | 80% / 0% / 0% / 20% |
| historical_36 | 8.09% | 1.36% | PASS | 90% / 0% / 0% / 10% |
| vt_7_recent | 4.77% | 1.36% | FAIL | 65% / 0% / 0% / 35% |
| vt_6_5_recent | 4.65% | 1.36% | FAIL | 50% / 0% / 10% / 40% |
| cost_100bps | 4.02% | 1.42% | FAIL | 35% / 0% / 0% / 65% |
| reserve_90 | 4.77% | 1.36% | FAIL | Infeasible |

These stresses challenge a fixed candidate as well as showing reoptimization. Reoptimizing after each stress does not establish that a previously chosen allocation survives. The drag is a scenario allowance, not a measured turnover estimate; fund expenses already affect adjusted returns. No claim of realized after-tax performance is made.

TB3MS supplies point-in-time rate context for BIL. Use the last observation available in the decision-date ALFRED vintage; monthly observation labels alone do not prove availability. It has no automatic weight effect. The preserved September 30 lab comparison excludes the not-yet-released September observation.

Do not advance to live adoption until protected spending and compliance with the stated loss limit are demonstrated, the existing locked experiment chronology is documented, and an independent user reproduces the app. Monitor reserve breaches, net target shortfalls across VT assumptions of 6.5–7.5%, both estimation windows, costs and source timing. Stop on infeasibility, a failed implemented rule, or unverified timing; quarantine suspect data. Annualized volatility cannot cap losses. The coarse grid may miss better or feasible continuous allocations. No untouched holdout has been demonstrated.

## Student mandate clarification — November 17, 2026

Student selected a 10% maximum peak-to-trough investment loss, full protection of the next 12 months of spending, and one withdrawal in late August or September of up to 5% of the reserve. Operational interpretation: set the approved dollar spending budget at the annual decision date, with a 5% ceiling based on reserve value then; keep that dollar obligation protected after market losses. Measure investment drawdown on cash-flow-adjusted NAV so the annual withdrawal does not count as a market loss. This interpretation should be confirmed against the club's actual budget.

The historical screen uses monthly rebalanced constant weights, monthly adjusted total returns, and annual implementation drag divided by 12. Include starting NAV in the high-water mark. It is descriptive in-sample evidence, not a point-in-time trading backtest. Monthly observations can miss intramonth drawdowns. The search now rejects grid candidates exceeding 10% observed monthly drawdown in the active window. It does not simulate stop-order fills or certify a future hard cap.

Protecting spending requires a separately identified dollar account and due-date cash availability. A proposed cash or maturity-matched direct Treasury sleeve is outside the current ETF universe and has not yet been implemented. BIL alone is not evidence of complete principal protection. All current portfolios therefore FAIL full live mandate approval even if their numerical screen passes. Existing return and covariance results describe the ETF prototype, not a portfolio with a new protected sleeve; adding that sleeve requires recalculating expected return, risk and the mandate bridge.

Proposed monitoring: review cash-flow-adjusted drawdown each trading day; 8% is an analyst-proposed early-warning level, not a student-approved limit. At 10%, stop further risk deployment and refer allocation reduction to committee review. If the protected dollar account cannot meet the budget on time, stop approval. A stop trigger cannot guarantee a 10% maximum loss, so **reject live adoption under the hard cap today; pilot only in simulation with 0% live allocation**.

Sources: [TreasuryDirect: bills pay face value at maturity](https://www.treasurydirect.gov/marketable-securities/treasury-bills/); [SEC: stop price is not a guaranteed execution price](https://www.investor.gov/introduction-investing/general-resources/news-alerts/alerts-bulletins/investor-bulletins-14). Nominal maturity cash flows do not guarantee a stable daily market value or an inflation-adjusted spending amount.


## Updated student decision from Lab 20

The updated repository records the student choosing simulation-only pilot of 85/15 rather than adoption. The original gross-return comparison and reflection are preserved in docs/lab20-decision-memo.md. This committee build adds 25 basis points of annual drag and a historical drawdown screen; distinguish those results from the original experiment. Passing return hurdles alone does not resolve the full mandate.

## Control-dependent interpretation

The 10–20% VT research range is not a promise of numerical feasibility. The app now rejects 85/15 under failing inputs, permits simulation-only pilot when its numerical screens pass, and stops infeasible scenarios. These changes do not override the live mandate failure or authorize capital.
