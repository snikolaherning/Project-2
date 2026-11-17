# Developer cold run — November 17, 2026

Executor: Codex; not an independent student/partner test.

- Source: clean clone of project2-committee, commit 2ce4d001b68ccae82ccd9c5d525e56027247fe70.
- Environment: macOS arm64, Python 3.9.6; newly created .venv. Streamlit 1.50.0, pandas 2.3.3. Top-level requirements pinned to these verified versions; transitive environment snapshot in results/test-environment.txt.
- Command: `python3 run_portfolio.py` from repository root.
- First failure: dependencies installed, but Streamlit's first-use email prompt encountered EOF in a noninteractive shell; launcher exited with CalledProcessError (255).
- Fix: explicitly set headless mode and disable usage statistics in child environment and CLI. Add .gitignore because manual upload omitted the hidden file. Change stale fixed 5% header to reflect selected target. Split wide table into mandate verdicts and allocations; print failed rules separately. Add the student-selected 85/15 candidate while preserving prior 75/25 for comparison.
- Retry: launcher reached http://localhost:8515 and /_stcore/health returned `ok`; in-app browser displayed committee app, numerical verdicts and full live-mandate failure. No credentials or live finance transactions involved.
- Timing: first process launched about 15:49 Eastern; repaired server reached ready state before 15:51. Approximate wall time, not a timed independent-user measurement.
- Validation: `.venv/bin/python -m unittest discover -s tests -v`: nine tests passed, including interactive window/return/objective changes and infeasibility. Test uses 30-second initial rendering timeout; original 3-second timeout was insufficient for initial imports.
- Output: results/committee-report.json recreated from bundled data; no network data refresh. Tests do not establish future return, loss-cap or spending guarantees.
- Remaining: publish these fixes; independent reviewer must retry the published version and record command, elapsed time, first failure or none, and result location. Deployment and videos are not tested here.

Platform note: the system Python's LibreSSL produced a requests/urllib3 compatibility warning. Frozen-data committee operation passed; live SEC/FRED downloads are outside this cold-run claim. Prefer a maintained Python distribution for live data workflows.
