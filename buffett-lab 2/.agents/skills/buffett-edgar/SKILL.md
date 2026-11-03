---
name: buffett-edgar
description: Analyze a ticker using five fiscal years of SEC EDGAR facts, computed Buffett checks, and a business-quality memo.
---

Run `python3 .agents/skills/buffett-edgar/scripts/edgar.py TICKER`
from the lab folder.

Use only SEC EDGAR data. Never install FAskills or use paid data.
The script identifies Stefan, sherning@purdue.edu, in its User-Agent.

Code computes every number and all three checks:
- ROE at least 15% every year.
- Owner earnings positive every year.
- Owner earnings grew from first year to last.

ROE uses net income divided by year-end equity.
Owner earnings is a simplified operating cash flow minus total
capital spending proxy, not estimated maintenance capital spending.

Missing inputs remain "not found"; checks requiring them are
"not known". Never estimate missing values.

Using only the script's printed numbers, write a short
Buffett-inspired educational memo to `memos/TICKER.md`.
Choose "own the business", "watch it", or "pass".
Judge business quality, not stock price. Do not use price data.
Discuss limitations: the table alone cannot establish a durable
competitive advantage or management quality.

If owner earnings are missing, say you cannot judge owner earnings.
Use printed values and precision, with dollar amounts in USD millions.
Validate the memo with the script's `unsupported_numbers()` function.
The student supplies their own trust/reflection sentence.
