# Locked Changed-Input Prediction

Received from Stefan in chat November 17, 2026. Preserved verbatim below. Student confirmation that this was authored with AI closed remains required; receipt in chat alone does not independently establish that condition. No run of the 4.5% objective has been executed by Codex before this commit.

## Change

Return objective: **5.0% → 4.5%** (annual expected return). Everything else stays the same: club universe, all 60 months, 20% BIL minimum.

## What I expect

- **Falls:** VT weight (20% → about 15%), expected return (5.25% → about 4.6%), volatility (3.09% → about 2.3%).
- **Rises:** BIL weight and reserve share (80% → about 85%).
- **Stays the same:** IEF and LQD at 0%.

A lower target means the app needs less VT to hit it, so it swaps VT for safer BIL.

## Does my recommendation change?

Yes, a little. At 5%, I'd only pilot 75/25 because it missed the target when VT returned 6.5%. At 4.5%, I expect 85/15 to meet the target even then, so I'd be ready to adopt it. My 10% loss limit and yearly withdrawal plan stay the same.

---

## Frozen execution specification — recorded by Codex before execution

Code: committee.run(recent=False, cost_bps=25, reserve=0.20, vt_return=None, objective=0.05), then identical call with objective=0.045. Four-ETF universe BIL/IEF/LQD/VT; frozen 60 monthly returns; five-percentage-point grid; 10% historical monthly drawdown screen; all other mandate policies unchanged. Target is net of the current 25-basis-point annual implementation drag. Report gross and net returns separately. The student's quoted 5.25% starting return is retained, not corrected after the fact; current baseline may differ in precision/cost convention.

The additional 6.5% VT robustness claim will be assessed separately from the one-input comparison, with other 60-month estimates held fixed. This is not the primary changed-input run. Any numerical pass does not establish protected spending or guarantee future drawdown below 10%; record actual full-mandate decision effect separately from the predicted adoption.

Execution gate: this prediction must be committed and pushed to GitHub before the run. Do not amend the prediction after results are known.

## Later provenance clarification

After fetching updated main, Codex discovered this same experiment was already run and documented in lab20-changed-input.md. This snapshot is not the original pre-run prediction commit and must not be used to establish original chronology. Student confirmed AI-off authorship November 17. See docs/validation-and-ai-use.md.
