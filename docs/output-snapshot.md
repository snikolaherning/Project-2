Codex assisted with code, calculation checks, and drafting.
The analysis and decision are mine; education, not investment advice.

# Visible committee output

Frozen inputs: 60 monthly returns, September 2021–September 2026; retrieved October 22, 2026. Default target 5% net, 25 bp implementation allowance, minimum 20% BIL, 10% observed monthly drawdown screen. Live recommendation: 0%; simulation research only.

| Portfolio | BIL / IEF / LQD / VT | Net estimate | Volatility | Historical drawdown | Numerical screen |
|---|---|---:|---:|---:|---|
| Equal weight | 25.0% / 25.0% / 25.0% / 25.0% | 2.97% | 7.50% | 15.94% | FAIL |
| Inverse volatility | 86.8% / 5.7% / 4.5% / 2.9% | 3.08% | 1.40% | 2.49% | FAIL |
| 60/40 benchmark | 0.0% / 0.0% / 40.0% / 60.0% | 6.56% | 12.29% | 23.91% | FAIL |
| Fixed pilot candidate | 75.0% / 0.0% / 0.0% / 25.0% | 5.42% | 3.83% | 6.58% | PASS |
| Student pilot 85/15 | 85.0% / 0.0% / 0.0% / 15.0% | 4.59% | 2.37% | 3.84% | FAIL |
| Constrained portfolio | 80.0% / 0.0% / 0.0% / 20.0% | 5.00% | 3.09% | 5.22% | PASS |

Full live mandate: FAIL for every portfolio. Protected spending and future loss cap remain unproven. For exact inputs and failed-rule booleans see [executed JSON](../results/committee-report.json). Historical sample figures are not forecasts or guarantees.

## November 19 forward-assumption challenge

Student BIL stress 2.75–3.25% / VT stress 6.5–7.5% is distinct from historical estimates. At BIL 3%, VT 6.5%: fixed 85/15 net estimate 3.275% (display 3.28%); no feasible five-point-grid allocation under the current screens. These are scenarios, not forecasts. See [supplemental output](../results/risk-review.json) and [student rationale](student-decisions.md). The original 4.5% gross-target experiment remains separate.
