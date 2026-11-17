Codex assisted with code, validation and documentation. The analysis and decision are Stefan’s; education, not investment advice.

# Project 2 — portfolio readiness

**Committee ask: pilot 85% BIL / 15% VT, not adoption.** The nominal objective for the changed-input experiment is 4.5% annually with at least 20% BIL reserves. Full mandate compliance, including the stated 10% loss limit and withdrawal needs, remains unresolved. This is a Lab 20 readiness repair, not a claim that all Project 2 requirements are complete.

## One-command cold run

Install Python 3.9+ first. Download the repository using Code → Download ZIP and unzip, or clone it. Open Terminal/PowerShell in the extracted repository folder (the folder containing this README and run_portfolio.py), then run:

```sh
python3 run_portfolio.py
```

On Windows, use `py run_portfolio.py` if `python3` is unavailable. The launcher creates a local environment and installs pinned Streamlit from PyPI; first launch needs internet access. It then starts the portfolio app on port 8515. Open http://localhost:8515 if the browser does not open automatically. Stop another app using that port before launching, or record the exact port error. Stop this app with Ctrl+C.

**This is the portfolio entry point.** The older root app.py is the Lab 19 company panel and is not the portfolio cold run. It is preserved as supporting coursework.

The bundled club CSV loads automatically: BIL, IEF, LQD and VT. No manual file upload, API key or paid source is needed. Start at 4.5% return objective, 20% reserves, only BIL reserve eligible, all months. Read both allocation tables and the green implemented-constraint verdict, plus the yellow unresolved-full-mandate warning. Change the return objective to 5.0% and back to 4.5% to reproduce the recorded comparison. The as-loaded/current columns compare estimates under the same objective; they are not the before/after objective comparison. Download each separate run as JSON.

## Visible decision and evidence

- [Decision memo](docs/decision-memo.md)
- [Visible before/after output](docs/output-snapshot.md)
- [Validation and AI use](docs/validation-and-ai-use.md)
- [Lab 20 cold-run record](docs/lab20-readiness.md)
- [Original locked prediction and appended result](lab20-changed-input.md)
- [Before/after JSON evidence](evidence)
- Portfolio source: [app](portfolio-tool/app.py), [engine](portfolio-tool/portfolio.py), [bundled prices](portfolio-tool/prices.csv), [source evidence](portfolio-tool/source-evidence).

## Limitations and remaining Project 2 work

The experiment changes the client objective; it does not improve underlying fund returns. Historical arithmetic return estimates are not forecasts. The implemented search enforces long-only weights, full investment, the return objective and reserve floor on a five-point grid. It does not guarantee future returns, maximum losses or withdrawal coverage. Fees are not separately modeled. Full baseline comparisons, point-in-time signal integration, broader stress, final mandate/benchmark specification, and videos/transcripts/manifest remain to be audited and completed. See the validation document. Do not infer completion from a successful app launch.
