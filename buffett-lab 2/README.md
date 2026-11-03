# Lab 18 — Stefan; partner Linda Li

SEC User-Agent: Stefan sherning@purdue.edu. No API key or paid data source.

From this folder:

```sh
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python .agents/skills/buffett-edgar/scripts/edgar.py COST
.venv/bin/python -m streamlit run app.py
```

Open Codex in this folder. The skill is in `.agents/skills/buffett-edgar/` (a repository skill discovery location). Ask: “Use $buffett-edgar on COST and save the memo.” The script computes; the AI writes the judgment using only printed values. Name and description are loaded for discovery; full instructions are loaded when selected, saving context.

The app uses cached raw SEC responses when available. Refresh retrieves them again. All dollar values displayed are USD millions. ROE uses year-end equity. Owner earnings is operating cash flow minus total capital spending, a simplified proxy rather than an estimate of maintenance spending. Missing inputs never become zero. Each reported input includes its XBRL tag; derived metrics state their formulas. The JSON retains filing/accession provenance.

Required student work:
- Open Brightspace → Quizzes → Lab 18 at minute twenty.
- Check COST's table against the instructor's reference (the pasted assignment omitted its numerical table).
- Enter JPM and observe missing capital spending/owner earnings and unknown owner-earnings checks.
- Add `40.0%` to COST's memo in the app. Observe the warning; remove it afterward.
- In a fresh browser AI chat without this skill, ask: “Is Costco a Buffett business? Give its ROE for the last five years.” Compare sources and definitions yourself.
- Explain `year_row()` line by line to Linda, then swap. `select_value()` returns `None` when no matching fact exists; derived values preserve missing inputs.
- Add your own trust/decision sentence under the memo. The app reflection field is for discussion; add the final sentence to the saved memo.
- Submit individually with GitHub links to SKILL.md, edgar.py, app.py, and the memo. No repository has been published for you.

Numbers belong in code because identical inputs should yield repeatable calculations and explicit missing-data behavior. Judgment remains with the model. A matching number can still be used in the wrong context: the app's numeric check does not establish semantic correctness.

References: [Buffett philosophy](https://github.com/CinderZhang/FAskills/blob/main/financial-researcher/experts/warren_buffett.md), [SEC API](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [Codex skills](https://developers.openai.com/codex/skills), [Streamlit chart](https://docs.streamlit.io/develop/api-reference/charts/st.line_chart).
