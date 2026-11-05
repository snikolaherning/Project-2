---
name: buffett-edgar
description: Write a Buffett-inspired SEC-only business-quality memo from the Lab 19 shared fact table and deterministic checks. Use for the legend panel, without price valuation.
---

Run `python3 scripts/panel.py TICKER` from the lab folder. All investors read the same five fiscal years and XBRL-tagged facts. Scripts use SEC EDGAR only, identifying Stefan sherning@purdue.edu. Never install FAskills or use paid data.

Checks: ROE at least 15% every year; owner earnings positive every year; owner earnings grew first to last. Owner earnings is operating cash flow minus total capex, a simplified proxy. ROE uses year-end equity.

Focus on consistent earning power, ROE, and owner earnings. Code owns every calculation; never estimate missing facts. Missing values stay not found and affected checks not known. Use only numbers printed in the script's table or threshold block, matching precision and USD-million units.

Write an educational simulation to `memos/TICKER/buffett.md`, with `**Verdict: own the business**`, `**Verdict: watch it**`, or `**Verdict: pass**`. Judge business quality, not stock price. Do not claim real investor endorsement, holdings, or current views. A screen passing is not proof of durable advantage or honest accounting. Missing owner earnings must be acknowledged when relevant.

Validate with `unsupported_numbers(memo, result)` in scripts/panel.py. This verifies numerical provenance, not semantic correctness. The app displays all investor memos side by side and validates each. For unseen tickers, create a fresh memo after reading the new output; never reuse another ticker's memo or fabricate the student's reflection.

Reference pages used for the classroom methodology: https://github.com/CinderZhang/FAskills/blob/main/financial-researcher/experts/ben_graham.md and https://github.com/CinderZhang/FAskills/blob/main/financial-researcher/experts/michael_burry.md . The lab's exact checks and no-price rule override their broader frameworks.
