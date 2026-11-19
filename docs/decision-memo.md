Codex assisted with code, calculation checks, and drafting.
The analysis and decision are mine; education, not investment advice.

# University club reserve — committee decision

November 19, 2026 · Five-year horizon · Annual nominal USD estimates

**Committee ask: authorize a simulation-only pilot; allocate 0% of live capital to this process.** Center research on 85% BIL / 15% VT within a 10–20% VT / 80–90% BIL envelope. This is a research range, not a claim that every mix passes. Reject live adoption until the spending protection and hard loss limit can be demonstrated. The app rejects 85/15 under failing inputs and stops infeasible scenarios.

The club mandate targets 5% annual nominal expected return, at least 20% BIL, long-only fully invested allocations, no leverage, and a maximum 10% peak-to-trough investment drawdown. Protect the next 12 months of spending, with one late-August/September withdrawal up to 5% of reserve. Model that budget as a fixed dollar obligation set at the annual decision date; withdrawals are external cash flows, not investment losses. The current app applies an explicit 25-basis-point annual implementation allowance and screens the return target net of it; the original Lab 20 exercise omitted this allowance. It is an illustrative conservative assumption, not measured execution cost or an additional fund expense.

Universe: BIL, IEF, LQD and VT. Benchmark: 60% VT / 40% LQD. Equal weight and inverse volatility are transparent baselines. The constrained portfolio minimizes annualized sample volatility over a five-percentage-point grid, subject to the return target, reserve floor and observed monthly drawdown screen. A grid minimum is not a continuous optimum. All comparisons use common inputs and reveal failed rules.

Prices are frozen monthly adjusted values from September 2021 through September 2026, retrieved October 22, 2026: 61 prices, 60 returns. The shorter window has 36 returns. Monthly arithmetic means ×12 are historical estimates, not forecasts; sample standard deviations ×√12 are annualized volatility. Drawdown uses a constant-weight, monthly-rebalanced path including starting NAV and monthly cost drag. It can miss intramonth losses and is in-sample evidence.

| Scenario | 85/15 net estimate | Numerical screen | Constrained BIL/IEF/LQD/VT |
|---|---:|---|---|
| 60 months, default | 4.59% | FAIL | 80% / 0% / 0% / 20% |
| 36 months, default | 6.50% | PASS | 90% / 0% / 0% / 10% |
| 36 months, VT 7% | 4.51% | FAIL | 65% / 0% / 0% / 35% |
| 36 months, VT 6.5% | 4.44% | FAIL | 50% / 0% / 10% / 40% |
| 36 months, VT 7%, cost 100 bp | 3.76% | FAIL | 35% / 0% / 0% / 65% |
| 36 months, VT 7%, BIL floor 90% | 4.51% | FAIL | Infeasible |

The 85/15 candidate estimates 4.59% net under default inputs, below 5%; the recent window estimates 6.50%. Neither demonstrates future safety. Changing return estimates changes expected returns and selected allocations, not the observed historical return path. Reoptimization after a stress does not establish survival of the fixed candidate.

The original locked Lab 20 experiment lowered the target from 5% to 4.5% with all other lab inputs fixed. Weights moved 80/20 to 85/15, gross expected return 5.2545% to 4.8394%, and volatility 3.0937% to 2.3654%. Directional predictions matched. The adoption prediction failed: fixed 85/15 with VT at 6.5% and the all-month BIL estimate yields only 4.0301% gross. A lower target relaxes a requirement; it does not improve asset returns.

The student's November 19 forward judgment is BIL 2.75–3.25% under stress (base about 3.5%) and VT 6.5–7.5%. Dated Fed projections and the BIL issuer fee inform, but do not mechanically determine, these fund-return assumptions. At BIL 3% and VT 6.5%, 85/15 earns 3.525% before implementation drag and 3.275% net. BIL's 85% weight carries most estimate sensitivity. At VT 6.5%, the current net target requires BIL 5.03%; the older 4.15% trigger belonged to the different gross-target experiment. Each student scenario was separately reoptimized and yielded no feasible five-point-grid allocation under the current screens. See [assumptions and corrections](student-decisions.md) and [risk challenge](risk-challenge.md).

TB3MS is admitted as point-in-time rate context only. At the September 30 decision date the recorded ALFRED vintage ended at August, 3.72%; September's 3.94% was not yet available. It is a discount-basis quoted rate, not BIL total return or a mechanical trading signal. See [data card](signal-data-card.md).

All current portfolios FAIL full live mandate approval: a protected dollar spending account is not implemented and the hard future 10% loss cap is unproven. An ETF reserve and stop trigger do not guarantee either. Monitor net-target shortfalls across VT 6.5–7.5%, both windows, costs, reserve breaches and source timing. An 8% drawdown warning is proposed; at 10% stop further risk deployment and seek committee review. Quarantine unverified data and stop on underfunded spending or infeasibility. Adoption requires those protections, permitted data use and robust returns, not merely a numerical PASS.

Linda's final fresh-copy retry succeeded in about 14 minutes with matching source fingerprints, as confirmed by Stefan; earlier setup failures remain documented. The expanded developer test suite targets return sensitivity, source timing, reset behavior and loss/spending failures. A retrospective 36/24-month training/test split was added; it is not an untouched holdout. No live performance or guarantee is claimed. Full methods, original prediction history and limitations: [validation record](validation-and-ai-use.md).
