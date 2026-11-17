Codex assisted with calculations, code and documentation. The analysis and decision are Stefan’s; education, not investment advice.

# Decision memo — November 17, 2026

## Student decision, preserved

Pilot 85/15 instead of adopting it. I’d reverse that if the mix still returns at least 4.5% with VT at 6.5%, using both the all-month and recent BIL estimates. That would make it adopt. If T-bill returns fall below about 4.15%, I’d reject it.

## Interpretation and limitations

Pilot means further testing, not a real-money allocation authorization. The 85% BIL / 15% VT candidate fails the specified all-month-BIL stress. Passing both expected-return stresses would satisfy the student's proposed return hurdle, but adoption also requires validating loss limits, withdrawals, costs and the remaining mandate. About 4.15% is a scenario-specific BIL expected-return break-even point, not a guaranteed realized-return floor or a reason to reject every possible allocation.

# Visible output — Lab 20

Historical club estimates; 60 monthly returns, 2021-09-30 to 2026-09-30. Risk is sample volatility annualized; returns are arithmetic annualized means. No separately modeled costs.

| Metric | 5.0% objective | 4.5% objective |
|---|---:|---:|
| BIL / VT | 80% / 20% | 85% / 15% |
| IEF / LQD | 0% / 0% | 0% / 0% |
| Expected return | 5.2545% | 4.8394% |
| Volatility | 3.0937% | 2.3654% |
| Reserve share | 80% | 85% |
| Return/reserve checks | pass | pass |
| Full mandate verdict | unresolved | unresolved |

Fixed 85/15 stress with VT at 6.5%: all-month BIL estimate 3.5943% produces 4.0301%; recent BIL estimate 4.3660% produces 4.6861%. The latter is a historical recent-window estimate, not today's yield. BIL break-even estimate: 4.1471%. Below that level, the fixed candidate misses 4.5% under this specific stress. This is not a universal rejection threshold.

## Reflection

Ross found that the root README pointed at the investor panel rather than the portfolio tool; that navigation failure was not obvious from working locally. Separately, the stress analysis revealed dependence on BIL's estimated return as well as VT's. A recent-window historical estimate cannot be assumed to persist. The historical sample and 2.3654% volatility do not establish a maximum loss; we have not proved that the estimate understates true risk or independently counted bear markets.

Stefan will retain the five-point grid, supplied price dataset and volatility risk measure before the deadline, disclose their limitations, and avoid rebuilding the engine. The code explanation and role swap with Ross were confirmed by Stefan.
