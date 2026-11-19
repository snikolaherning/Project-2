# Independent review — Linda Li

## Attribution and tested version

Report supplied by Stefan and attributed to Linda Li; Codex did not witness the review. Date: Tuesday November 17, 2026. Tested branch: project2-committee, commit [2ce4d00](https://github.com/snikolaherning/Project-2/commit/2ce4d001b68ccae82ccd9c5d525e56027247fe70), cloned rather than ZIP. Environment reported: Linux cloud sandbox, Python 3.13.18, no PyPI access. Help reported: none. This is a failed app cold-run attempt plus an engine/repository review, not a successful browser usability test.

## Command, failure and elapsed time

Command attempted: `python3 run_portfolio.py`. Pip could not reach pypi.org, preventing Streamlit installation; launcher failed. Full unittest discovery also could not import test_app.py without Streamlit. Linda reported “the other 9 tests ran”; the current test_committee.py defines eight engine tests, so that count is not independently reconciled. Do not claim nine independently passing engine tests from this statement. Codex's separate environment passes eight engine tests plus one AppTest.

App never became usable. Engine results reportedly available after roughly two minutes (15:59:56 to approximately 16:01:30 Eastern), in terminal output and JSON, not a browser. She described the window change as 60 to 36 months; this was an engine-input comparison corresponding to the checkbox, not interaction with a rendered checkbox. The exact fallback command was not supplied.

## Supplied engine evidence

[60-month JSON](../evidence/linda-2026-11-17/committee-run-60m.json) and [36-month JSON](../evidence/linda-2026-11-17/committee-run-36m.json) are preserved byte-for-byte. Neither is represented as a browser download because the app never launched. Codex compared all supplied fields against committee.run with matching settings, permitting rounding differences at relative 1e-10 / absolute 1e-12; [comparison and hashes](../results/reviewer-evidence-check.json).

| Portfolio | 60-month screen | 36-month screen |
|---|---|---|
| Equal weight | FAIL: return target and historical drawdown (15.94%) | PASS |
| Inverse volatility | FAIL: net return 3.08% | FAIL: net return 4.36% |
| Constrained | 80% BIL / 20% VT; net 5.00%; PASS | 90% BIL / 10% VT; net 5.70%; PASS |
| 60/40 benchmark | FAIL: BIL reserve and historical drawdown | FAIL: BIL reserve |
| Fixed 75/25 | PASS | PASS |

All full live-mandate verdicts remain FAIL: protected spending and hard future loss cap are unproven. A numerical screen is not full approval.

## Reviewer interpretation

Linda could find verdicts and failed rules in code, README and memo, but not on screen. Her understanding: simulation-only, 0% live capital, research range 10–20% VT / 80–90% BIL centered on 85/15. Stops: failed rule, infeasibility, unconfirmed data timing, spending shortfall or 10% drawdown; 8% is a proposed warning only. She understood the decision from repository documents; mismatch between 85/15 recommendation and the visible code's 75/25 candidate was the main confusion.

## Findings and response

- Missing 85/15 row: confirmed in tested commit 2ce4d00. A subsequent local fix adds “Student pilot 85/15”; it was not yet published when Linda reviewed. Do not claim she tested that fix.
- Different mandate.py rules: add explicit legacy Meridian banner to the file and console output, and a README map pointing to club rules in committee.py. Preserve earlier lab evidence.
- Unrelated root files: README now maps current vs historical files; CHECKOUT.md labeled historical. No historical records deleted.
- committee.py rewrote committed output: change default to ignored work/committee-report.json. Frozen results update only through explicit --output results/committee-report.json. Different runtimes may still differ slightly; compare with disclosed tolerance.
- Initial installation needs network: retain explicit PyPI requirement and add actionable launcher failure text plus engine-only fallback. Offline fallback does not validate the app.

## Retry still required

After publishing fixes, ask an independent reviewer with Python and PyPI access (or permitted installed dependencies) to follow the README in a clean folder, launch the browser app, change a control, read the resulting verdict, and record command, first failure or none, elapsed time, result location, tested commit and help received. This pending browser retry is separate from Ross Dyson's earlier Lab 20 navigation review and Linda's supplied engine review.

## Follow-up browser attempt — supplied November 17

Linda reports testing a ZIP labeled branch project2-committee commit 6382e54. First attempt: Linux sandbox, Python 3.10.12, PyPI proxy returned 403; no app launch. Second: macOS Apple Silicon, Python 3.9 (probably 3.9.6, unconfirmed patch level). Command: python3 run_portfolio.py. Packages installed but launch failed because port 8515 was already occupied. She opened the existing server, so the browser session cannot be attributed to the fresh ZIP or commit. Approximately 17 minutes elapsed, 4:38–4:55 p.m. Eastern.

Evidence: [60-month screenshot](../evidence/linda-browser-retry-2026-11-17/app-running-60mo-baseline.jpg), [36-month screenshot](../evidence/linda-browser-retry-2026-11-17/app-running-36mo.jpg), [downloaded 36-month JSON](../evidence/linda-browser-retry-2026-11-17/committee-run.json). The first screenshot shows the default window and inputs, not the allocation table; the second shows the selected recent window and verdicts. Numerical claims for both windows remain supported by the earlier JSON files. The supplied 36-month JSON matches all existing engine fields within relative 1e-10 / absolute 1e-12; see results/linda-browser-retry-check.json. This match does not prove server identity.

Reported interactions: constrained allocation 80% BIL / 20% VT → 90% BIL / 10% VT; numerical PASS → PASS; net 5.00% → 5.70%. Equal weight FAIL → PASS; student 85/15 FAIL → PASS. Full live mandate FAIL throughout. Linda understood simulation-only recommendation and failed rules. She identified static recommendation text as a remaining gap.

Assistance disclosure: Stefan asked Codex how to proceed from the editor; Codex instructed clicking Run and opening the local URL. Record this as launch assistance relayed during the attempt, not “no help.” No claim of an unassisted successful fresh launch is made.

Resolution prepared: launcher accepts --port 8516 to avoid the existing server without terminating unknown processes. Launcher, UI and downloaded JSON expose a code fingerprint to identify the copy. Decision panel now responds to numerical failures/pass/infeasibility while retaining 0% live allocation under the unproven full mandate. These changes require publication and a brief fresh-copy launch verification. Preserve the failed port attempt as useful evidence rather than rewriting it as success.

## Final targeted retry — fresh-copy launch confirmed

November 17, 2026: Stefan confirms that Linda's fresh copy launched successfully, the Terminal and browser fingerprints matched, and launch took approximately 14 minutes. Browser fingerprint: `b982296fa6a67012`; [supplied screenshot](../evidence/linda-fresh-launch-2026-11-17/app-fingerprint.jpg). The screenshot itself shows the browser fingerprint; the matching Terminal fingerprint and fresh-folder launch are student-reported confirmations, not independently captured Terminal evidence. The filename supplied by the student mentions port 8530, but the screenshot does not show a browser address bar and the exact final command was not supplied. Do not infer the port or command from the filename alone.

Outcome: successful independent fresh-copy launch, as reported, with supporting browser screenshot. Approximate elapsed time: 14 minutes. Prior browser evidence established window-control interaction and interpretation; this targeted retry resolves the previous server-identity uncertainty through matching fingerprints. No fresh control-change JSON was supplied for this final retry, and none is invented. Earlier setup/port failures and relayed Run-button assistance remain part of the record. This is a successful retry, not an unassisted first-attempt success.

The earlier “retry pending” entries describe historical status and are superseded by this outcome. Matching a source fingerprint identifies file contents; it does not prove financial validity, future loss protection or an untouched holdout. No further full review is required solely to repeat these checks.
