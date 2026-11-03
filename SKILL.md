buffett-lab 2/.agents/skills/buffett-edgar/SKILL.md---
name: buffett-edgar
description: Analyze a ticker with five fiscal years of SEC EDGAR facts, deterministic Buffett checks, and a short Buffett-style business-quality memo. Use for this SEC-only lab; excludes stock-price valuation.
---

Run `python3 .agents/skills/buffett-edgar/scripts/edgar.py TICKER` from the lab folder. Use `--refresh` to retrieve current SEC facts. Requests identify Stefan, sherning@purdue.edu. Never install FAskills or use its paid data services.

Read the printed table and checks. Code owns all arithmetic. Annual periods match exact start/end dates; later 10-K comparatives may revise values. Missing tags stay `not found`; missing inputs make checks `not known`. Never fill gaps from memory. ROE is net income divided by year-end equity. Owner earnings is explicitly a simplified operating-cash-flow minus total-capital-spending proxy; maintenance capex cannot be inferred reliably from these facts.

Write a short memo to `memos/TICKER.md` in a Buffett-inspired voice, labeled as an educational simulation. Choose **own the business**, **watch it**, or **pass** based on business quality, not price. Discuss consistency, earning power, and the limits of judging a durable moat or management from this table alone. Use only printed numerical values, in USD millions and the printed percentage precision. Do not invent scores, growth rates, price targets, outside facts, or holdings. If owner earnings are missing, explicitly say you cannot judge owner earnings.

Call `unsupported_numbers(memo, result)` from the bundled script to verify the saved memo and correct unsupported numbers. This is a numeric provenance check, not proof that a number is attributed to the correct metric. The Streamlit app reads the same saved memo and lets the student edit it for the manual probe.

The student supplies their own trust/decision sentence after discussing the evidence; do not fabricate their reflection.

Reference philosophy: https://github.com/CinderZhang/FAskills/blob/main/financial-researcher/experts/warren_buffett.md . Use its emphasis on understandable businesses, durable advantages, and owner earning power. The lab overrides its paid data, price forecasts, and valuation requirements.
