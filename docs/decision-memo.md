Codex assisted with code, calculation checks, and drafting.
The analysis and decision are mine; education, not investment advice.

# University club reserve — committee decision

November 19, 2026 · Five-year horizon · Annual nominal USD estimates

**Authorize simulation-only research; allocate 0% live capital to this process.** Center the research on 85% BIL / 15% VT within a 10–20% VT / 80–90% BIL envelope. Reject live adoption: forward-return stresses fail, protected spending is not implemented, and the hard future loss cap is unproven. The envelope is not a claim every mix passes. A proposed four-week review protocol and explicit adoption gates are in the [committee pilot plan](committee-pilot-plan.md).

The intended user is a university club investment committee in a classroom case. Mandate: 5% annual nominal expected-return objective, at least 20% BIL, long-only fully invested weights, no leverage, maximum 10% peak-to-trough investment drawdown, and complete protection of the next 12 months of spending. Plan one late-August/September withdrawal up to 5% of reserve. Set that obligation in dollars at the annual budget date; market losses do not shrink it. Withdrawals are external cash flows, excluded from investment drawdown. No actual club account or dollar budget is claimed.

Universe: BIL, IEF, LQD and VT. Benchmark: 60% VT / 40% LQD. Equal weight and inverse volatility are transparent baselines. The constrained portfolio minimizes annualized sample volatility on a five-percentage-point grid subject to return, reserve and observed monthly drawdown screens. A grid minimum is not a continuous optimum.

Frozen adjusted prices span September 2021–September 2026, retrieved October 22: 61 prices and 60 returns. The recent window has 36 returns. Annual arithmetic means and sample volatilities are historical estimates, not forecasts. The current screen deducts a disclosed illustrative 25-basis-point annual implementation allowance; fund expenses already affect adjusted returns. Monthly-rebalanced drawdown can miss intramonth losses.

| Case | Fixed 85/15 net estimate | Numerical result | Constrained allocation |
|---|---:|---|---|
| 60-month historical base | 4.59% | FAIL | 80% BIL / 20% VT |
| 36-month historical window | 6.50% | PASS | 90% BIL / 10% VT |
| Student BIL 3%, VT 6.5%; full window | 3.275% | FAIL | No feasible grid mix |

The student's forward BIL stress range is 2.75–3.25%, base about 3.5%, with VT stress 6.5–7.5%. Dated Fed projections and the issuer fee inform this judgment, not a mechanical forecast of BIL returns. At 85% weight, a 100 bp BIL estimate change moves portfolio return 85 bp; an equal VT change moves it 15 bp. At VT 6.5%, the current target requires BIL 5.03% net of fund expenses before the portfolio allowance. All separately searched student scenarios yield no feasible five-point-grid mix under the screens. See [source/assumption bridge](student-decisions.md) and [risk challenge](risk-challenge.md).

The original AI-off Lab 20 experiment changed the **gross** target from 5% to 4.5%. Weights moved 80/20 to 85/15, expected return 5.2545% to 4.8394%, and volatility 3.0937% to 2.3654%. Directional predictions matched, but predicted adoption failed: fixed 85/15 with VT 6.5% and all-month BIL earns only 4.0301% gross. That experiment omitted today's separate cost allowance. The old 4.15% BIL trigger is not the current 5.03% requirement.

TB3MS is point-in-time rate context, not BIL total return or an automatic weight rule. The preserved raw September 30 ALFRED vintage ends at August, 3.72%; September's 3.94% appears in the later vintage. [Data card](signal-data-card.md) defines timing, units, source and revisions.

Every portfolio FAILS full live-mandate approval. Stress results and a retrospective 36/24-month training/test split cannot guarantee future loss protection. Refuse altered frozen inputs; reject failed candidates; stop infeasible scenarios or underfunded spending. An 8% warning is proposed; at 10% stop further risk deployment and seek review. Do not silently relax the mandate. Reconsider live use only after the pilot plan's protection, return, data-rights and release gates are met. Twenty-one developer tests and Linda's reported successful fresh-copy retry support reproducibility, not profitability. Full evidence and limitations: [validation record](validation-and-ai-use.md).
