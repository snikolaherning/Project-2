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

## Ross Dyson's follow-up attempt — reported by Stefan

**Commands attempted:**

```sh
git clone https://github.com/snikolaherning/Project-2
cd "Project-2/Lab15 2"
pip install -r requirements.txt
python -m streamlit run app.py
```

**App opened:** No. Reported error: `ModuleNotFoundError: No module named 'streamlit'`. Ross reports the dependency could not be downloaded in the test environment. No exact pip installation error was supplied, so its underlying cause is unverified.

**Engine result:** Ross reports the engine ran from the fresh clone. Changing the objective from 5.0% to 4.5% produced 80/20 to 85/15 BIL/VT, expected return 5.25% to 4.84%, and volatility 3.09% to 2.37%, matching Stefan's saved JSON reports. This is engine-level reproduction, not a successful interactive app test. The exact command or code used for the engine comparison was not supplied.

**Elapsed time:** Ross reports approximately three seconds (two to clone, one to run). This breakdown does not account for the dependency-install attempt or interactive test, so total cold-run duration is not established.

**Readiness repair status:** The corrected root README and separate portfolio-tool entry point were uploaded and committed, as reported by Stefan. This follow-up used the older `Lab15 2` folder, not the repaired README command `python3 run_portfolio.py` from the repository root. Accordingly the new entry point has not been independently verified by Ross. The Streamlit installation blocker and interactive cold run remain unresolved; no clean cold run or complete Project 2 readiness is claimed. A missing module confirms an unavailable dependency, not proof that the repository is bug-free or that the failure is solely environmental.

**Next retry when feasible:** from the fresh repository root, follow only the README and run `python3 run_portfolio.py`. Preserve any dependency-install error. If the environment cannot download Streamlit, record that blocker rather than claim an app pass. The instructor allows truthful unresolved items for Lab 20.

## Final retry — corrected README entry point

Partner: Ross Dyson. Student-provided report.

Commands attempted:

```sh
git clone https://github.com/snikolaherning/Project-2
cd Project-2
python3 run_portfolio.py
```

The launcher created a fresh environment but stopped during dependency installation, before Streamlit launched. App opened: no. Interactive control/mandate-verdict test: not performed.

Reported error: `ERROR: No matching distribution found for streamlit==1.50.0`, followed by `CalledProcessError` from the launcher's pip installation step. Ross reports the test machine could not reach pypi.org because internet access was unavailable. That network explanation is partner-reported; the abbreviated error alone does not independently prove the cause or rule out other compatibility issues.

Elapsed time: approximately 12 seconds to setup failure, as reported by Ross.

**Final Lab 20 status:** the first navigation failure was addressed by the committed root README and portfolio launcher. Ross retried that exact entry point. The independent cold run is blocked at dependency download; no successful app launch or interactive test is claimed. Earlier engine-level reproduction matched the saved before/after numbers. Local Codex UI tests passed separately and do not replace the partner cold run. The open issue is recorded truthfully, as permitted by the Lab 20 floor; Project 2 is not represented as complete or approved.

Before Project 2 submission, retry on a machine with permitted PyPI access and a compatible Python version, then record successful app interaction or remaining errors. Preserve the failed attempt and its timing.
