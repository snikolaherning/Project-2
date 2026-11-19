# Student judgment and checked assumptions — November 19, 2026

Stefan selected BIL stress returns of 2.75–3.25% annually over the five-year horizon, base approximately 3.5%, and confirmed “retain simulation-only pilot and reject live adoption.” VT stress remains 6.5–7.5%. These are student judgments informed by sources, not market observations or guaranteed forward returns. Current mandate remains 5% annual net target for the committee screen, 20% BIL minimum, 10% investment drawdown limit and protected next-year spending. Original 4.5% target is the locked experiment's changed input.

## Source and bridge check

[September 16 Fed projections](https://www.federalreserve.gov/monetarypolicy/fomcprojtabl20260916.htm), verified November 19: federal-funds medians 4.1% for 2026, 4.1% for 2027, 3.9% for 2028, 3.6% for 2029, 3.2% longer run. The student-supplied low central-tendency values were verified; 2029 low is 3.1%. These are end-of-year appropriate-policy projections, not annual T-bill total-return forecasts.

[State Street BIL issuer page](https://www.ssga.com/us/en/individual/etfs/state-street-spdr-bloomberg-1-3-month-t-bill-etf-bil), fund information as of November 1, verified November 19: gross expense ratio 0.1352%, reasonably rounded to 0.14% in the student's rationale. Fund expenses are already reflected in adjusted returns; no extra subtraction is applied to historical means. Student BIL forward assumptions are treated as fund returns after fund expenses, with separate 25 bp implementation allowance at portfolio level.

An explicit approximate 2027–2031 proxy uses median year-end levels 4.1, 3.9, 3.6, 3.2, 3.2%, assuming the last two years equal longer run. Arithmetic average 3.60%, less 0.1352%, gives 3.4648%, approximately 3.5%. Low central-tendency path 3.6, 3.1, 3.1, 3.0, 3.0% averages 3.16%, less fee gives 3.0248%, approximately 3.0%. This is an analyst-explicit bridge supporting the student's broad judgment, not an exact source-derived expected BIL return: year-end levels differ from annual reinvestment rates, bill/funds spreads and within-year timing are omitted. The recession discount to 2.75% and upper stress endpoint 3.25% remain personal judgment. Source fields: data/assumption-sources.json.

## AI-output corrections that affect the decision

- Student estimated 85/15 at BIL 3% / VT 6.5% as “about 3.5%.” Correct gross bridge: .85×3% + .15×6.5% = 3.525%. Current 25 bp implementation allowance gives 3.275% net, materially below 5%.
- The earlier BIL break-even 4.1471% belongs to the original 4.5% **gross** target and VT 6.5%. It is not the current trigger. At 5% net and 25 bp drag, BIL must earn 5.0294%; at 4.5% net it must earn 4.4412%.
- BIL is the load-bearing estimate: 100 bp change in its return changes fixed portfolio return by 85 bp; equal VT change contributes 15 bp. This exposure calculation is not forecast confidence.
- Fixed-candidate failure is not universal infeasibility. The code separately searched each student scenario and found no feasible **five-point-grid** allocation under the stated screens. No claim is made about every continuous allocation or a guarantee of risk limits.

Student reasoning is preserved here alongside the AI-assisted checks and refinements; the supplemental scenarios are not a new AI-off locked experiment. The original locked prediction is unchanged. Student should personally review the bridges before recording, and explain why the negative evidence supports simulation-only research rather than live adoption.
