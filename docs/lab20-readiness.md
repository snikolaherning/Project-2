# Lab 20 — Project 2 Readiness

Student: Stefan. Partner: Ross Dyson.

## Ross's review of Stefan's repository

Ross reports that the root README and app lead to Lab 19's legend panel rather than a Project 2 portfolio app. His review identifies missing or undemonstrated Project 2 launch/mandate verdict, decision memo, validation and AI-use record, and visible decision snapshot. These are unresolved readiness findings, not evidence that the portfolio process passed.

- Command attempted: None. Ross stopped at the README; no execution test is claimed.
- First navigation/readiness failure: README directs the reviewer to the Lab 19 investor panel instead of the portfolio decision.
- Execution error, if any: not yet reported.
- Elapsed time: not recorded.
- Result location: Lab 19 panel described by README; Project 2 portfolio decision not established by the review.

## Stefan's review of Ross's repository

Stefan reports no README was present. No documented launch command was available. Exact elapsed time and any additional action remain to be recorded; no successful run is claimed.

## Changed-input record

See lab20-changed-input.md and the two JSON evidence files. Original prediction preserved, actual result appended. The adoption prediction is not established under its proposed VT stress assumption.

## Still required

- Cold-run command and time recorded honestly: none attempted, time not recorded.
- Code explanation, Ross’s question and Stefan’s answer recorded; role swap confirmed.
- Fix the first README/entry-point failure, push, and have Ross retry; record remaining unresolved items. No fix or rerun claimed yet.
- Final decision and reversal condition recorded in decision-memo.md.
- Reflection recorded in decision-memo.md.

AI use: Codex inspected downloaded reports, compared settings and results, calculated the separately labeled fixed-allocation stress check, and organized this evidence. The prediction was supplied by Stefan and is preserved, not rewritten. Partner activity claims are based on student reports.

## Code explanation — student report

Ross asked: Why not just average the funds’ volatilities to get the portfolio’s risk?

Stefan answered: Averaging ignores how the funds move together, so the code uses the covariance table, which lets a mix of funds that don’t move in sync come out less risky than its parts.

AI clarification: portfolio variance is the weighted covariance calculation; volatility is its square root. Diversification can reduce risk, but does not guarantee a portfolio is less volatile than every individual fund. Stefan confirms the role swap completed.

## Readiness repair prepared

Added a separate portfolio-tool folder, bundled club CSV, one-command launcher, explicit partial mandate verdict, visible output, and root README routing. Local tests are to be reported separately. GitHub upload/commit and Ross’s independent retry are still pending; no successful partner rerun is claimed. Code explanation and role swap are now confirmed by Stefan. Final decision and reflection are in decision-memo.md.
