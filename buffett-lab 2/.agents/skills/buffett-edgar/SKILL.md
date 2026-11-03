---
name: buffett-edgar
description: Analyze a ticker using five fiscal years of SEC EDGAR facts, computed Buffett checks, and a Buffett-inspired business-quality memo.
---

# Buffett SEC Business Check

Run this command from the lab folder, replacing TICKER with the requested ticker:

python3 .agents/skills/buffett-edgar/scripts/edgar.py TICKER

Use --refresh to download current SEC facts instead of cached responses.

## Data and calculations

Use only SEC EDGAR data. Never install FAskills or use its paid data sources.
SEC requests identify Stefan, sherning@purdue.edu, in the User-Agent.

The bundled script prints the last five fiscal years of revenue, net income,
operating cash flow, capital spending, equity, ROE, and owner earnings.
Each input includes its XBRL tag; derived metrics identify their formulas.

Code performs all calculations:
- ROE = net income / year-end equity * 100.
- Owner earnings = operating cash flow - total capital spending.

Owner earnings is a simplified proxy, not an estimate of maintenance
capital spending.

Code evaluates these checks:
- ROE is at least 15% every year.
- Owner earnings are positive every year.
- Owner earnings increased from the first year to the last.

Missing inputs stay "not found". Checks requiring missing inputs are
"not known". Never replace missing data with zero or an estimate.

## Memo

Using only numbers printed by the script, write a short Buffett-inspired
educational memo and save it as memos/TICKER.md.

Choose one verdict: "own the business", "watch it", or "pass".

Judge business quality, not stock price. Do not use price data, price
targets, outside numerical facts, or invented scores.

Discuss earning power and consistency. Explain that the financial table
alone cannot establish a durable competitive advantage or management
quality.

If owner earnings are missing, explicitly say that you cannot judge
owner earnings.

Use the script's displayed precision. Dollar amounts are USD millions.
Do not calculate new numbers in the memo.

Validate the memo using unsupported_numbers(memo, result) from the
bundled script. Correct unsupported numbers before saving the final memo.
This check verifies numerical provenance, not whether the conclusions
follow from the numbers.

The student supplies their own sentence explaining whether they trust
the verdict and why.

## App and probes

Run the app with:

python3 -m streamlit run app.py

The app displays the chart, financial table, three checks, and saved memo.
It flags memo numbers that the script did not print.

Verify COST, then JPM. Missing JPM capital spending must leave owner
earnings "not found" and both owner-earnings checks "not known".

For the manual probe, add an unsupported ROE such as 40.0% to COST's memo,
confirm the warning, then remove the unsupported number.
