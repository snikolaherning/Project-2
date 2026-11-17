# Lab 20 — Locked Changed-Input Prediction

**Input:** Return objective (club universe, all 60 months, 20% BIL minimum, everything else unchanged)

**Old value and units:** 5.0% per year (nominal expected return)

**New value and units:** 4.5% per year (nominal expected return)

**Expected direction of the decision numbers:** VT weight falls (20% to about 15%). BIL weight and reserve share rise (80% to about 85%). Expected return falls (5.25% to about 4.6%) but stays at or above 4.5%. Volatility falls (3.09% to about 2.3%). IEF and LQD stay at 0%.

**Expected effect on my decision:** The decision changes slightly. At 5%, I’d only pilot 75/25 because it missed the target with VT at 6.5%. At 4.5%, I expect 85/15 to hit the target even then, so I’d be ready to adopt it. My 10% loss limit and yearly withdrawal plan stay the same.

## Actual result — appended after the run

Partner: Ross Dyson. Stefan reports committing the prediction before running the change. Original prediction above is preserved verbatim. This record does not independently establish the run timestamp; retain the original GitHub commit history.

| Metric | Before: 5.0% objective | After: 4.5% objective |
|---|---:|---:|
| BIL weight | 80% | 85% |
| IEF weight | 0% | 0% |
| LQD weight | 0% | 0% |
| VT weight | 20% | 15% |
| Expected nominal annual return | 5.2545% | 4.8394% |
| Annualized volatility | 3.0937% | 2.3654% |
| Reserve-eligible weight | 80% | 85% |

The two downloaded JSON reports have the same CSV hash, return estimates, universe, reserve eligibility, 20% minimum, and full-window flag. Only the objective differs. The JSON does not record the number of return observations, so the stated 60-month coverage requires the underlying CSV/app coverage evidence.

**Prediction comparison:** allocation and directions matched. The predicted after-return of about 4.6% was below the actual 4.8394%; predicted volatility of about 2.3% was close to the actual 2.3654%. Expected return and reserves meet the two constraints implemented in this run. This is not full mandate approval or a guarantee of return or loss limits.

**Decision effect:** the predicted move from pilot to adopt is not supported by the proposed stress condition. Holding the after-run weights fixed, changing VT's expected return to 6.5%, while retaining the printed BIL estimate, yields approximately 4.0301% expected return, below the revised 4.5% objective. This is an AI-calculated supplemental fixed-allocation check, not a second student-performed app run or a reoptimized portfolio. The 10% loss limit and withdrawal plan are not validated by these reports. Stefan's final decision and reversal condition remain to be supplied.

**Setup correction:** initial screenshots used the Meridian training universe and 3% reserve minimum. They were identified as a setup mismatch and were not used as evidence for the club-universe prediction. The downloaded JSON reports above are the corrected club runs.

Evidence files: [before](evidence/before-5pct.json), [after](evidence/after-4_5pct.json).
