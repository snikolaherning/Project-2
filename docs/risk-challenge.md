# Load-bearing claim validation — November 19, 2026

Purpose: test whether 85/15 can meet the objective without ignoring the largest exposure, and whether observed low volatility justifies the hard loss mandate. This supplements, rather than rewrites, the original AI-off experiment. Source assumptions and student ownership: [student decisions](student-decisions.md).

## Fixed-return sensitivity

For fixed 85/15, expected net return = 0.85×BIL + 0.15×VT − annual implementation drag. At VT 6.5% and 25 bp drag, BIL at 2.75%, 3.00%, 3.25% gives net 3.0625%, 3.2750%, 3.4875%, respectively. Even the upper student stress with VT 7.5% yields 3.6375%, below 5%. BIL needs 5.0294% to reach the current 5% net target with VT 6.5%; this is a required return, not a forecast. Full results in [risk-review.json](../results/risk-review.json).

The code separately reoptimizes each student scenario. No feasible grid allocation meets all current expected-return, reserve and historical drawdown screens. A coarse-grid infeasibility claim is not a proof of continuous infeasibility. The committee must not silently lower the target or relax its mandate to manufacture PASS.

## Loss and spending attacks

One-period analyst-designed shocks, not historical events or probability estimates:
- VT −50%, other assets flat: fixed 85/15 loses 7.5%.
- VT −100%, other assets flat: loses 15%, violating the hard 10% limit even before execution/slippage concerns.
- BIL −1%, IEF −15%, LQD −20%, VT −50%: 85/15 loses 8.35% (zero IEF/LQD exposures in this candidate).

Per $100 at annual budget date, the fixed spending obligation is $5. After a 7.5% market loss, assets are $92.50, then $87.50 after the withdrawal. Investment drawdown is 7.5%, not 12.5%; external withdrawals must not be mistaken for investment losses. The $5 obligation does not shrink with market losses. Protected dollar account actually implemented remains $0, so complete spending protection FAILS. Liquidity and a large BIL weight do not establish a principal guarantee.

## Retrospective temporal check

Training: first 36 monthly returns, September 2021–September 2024 price endpoints. Test: next 24 returns through September 2026. Weights are selected using training means/covariance/drawdown only, frozen at test start and rebalanced monthly. The training-selected grid portfolio was 65% BIL / 35% VT. Its test annualized compounded return was approximately 8.25%, maximum monthly test drawdown 2.01%; fixed 85/15 approximately 5.67% and 0.71%. Favorable test figures do not overturn failures under forward stress or the hard mandate.

This is a retrospective split of data already inspected and later adjusted by the vendor, not an untouched holdout, statistical proof, or vintage-correct backtest. No spending withdrawals are included. A mutation test changes only future prices and verifies training estimates and selected weights stay unchanged. Test annualized compounded returns are a different convention from optimization's annual arithmetic expected-return estimate.

## Tests and disposition

Tests cover covariance known answers, cost units, drawdown starting high-water mark, cash-flow separation, fixed budget coverage, reserve failures, infeasibility, finite-input rejection, BIL-vs-VT sensitivity, algebraic break-even, crash breach, raw adjusted-price reconstruction, real ALFRED availability boundaries, time-split isolation, interactive controls and full base reset. These target the decision's highest-risk claims, not merely app startup.

Disposition: retain simulation-only pilot with 0% live allocation; reject live adoption. Source/forecast uncertainty and the hard mandate are reasons for the action, not footnotes excusing it.
