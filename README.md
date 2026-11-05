# Lab 19 — Legend Panel

Student: Stefan (sherning@purdue.edu). Partner: Anika.

Instructor clarification reported by Stefan: replace Graham fully with Cathie Wood, keeping the same assigned checks. Wood's skill explicitly distinguishes these classroom defensive rules from her actual investment method. Discussion completed and Lab 18 COST app loading confirmed by Stefan.

## Run

From this folder:

```sh
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python scripts/panel.py COST
.venv/bin/python scripts/panel.py NVDA
.venv/bin/python -m streamlit run app.py --server.port 8519
.venv/bin/python -m unittest discover -s scripts -p test_panel.py -v
```

Open Codex in this folder to discover the three skills under `.agents/skills`. Ask each investor skill to read the shared script output and write its own memo. This app reads the saved AI-written memos; it does not call a paid model API or generate unseen-ticker memos automatically.

The app retains the Lab 18 owner-earnings/net-income chart, tagged table, Buffett checks, SEC source, editable memo, number warning, and disclosure. It adds current assets, current liabilities, total liabilities, two ratios, Wood and Burry checks, three verdicts and side-by-side memos, and warnings for all memos. The original Lab 18 folder is preserved separately.

## Data and missing-value rules

SEC EDGAR only, keyless, with Stefan's identity header. Raw SEC responses are cached in data; Refresh retrieves new data. Annual periods must match exact dates and annual durations. Later 10-K comparative facts may revise prior values. ROE uses year-end equity; owner earnings is OCF minus total capital spending, a simplified proxy rather than estimated maintenance capex. All financial displays are USD millions except percentages and ratios. XBRL tags and filing provenance remain available.

NVIDIA's recent narrower `PaymentsToAcquirePropertyPlantAndEquipment` facts are not found. SEC reports a broader `PaymentsToAcquireProductiveAssets` series, which is not silently substituted for the narrower definition. Consequently owner earnings and the affected Buffett checks remain not found/not known. This is a tag-definition limitation, not a claim NVIDIA spends nothing on productive assets. A broader proxy would need a documented rule change and validation. Missing values never become zero. Current ratio and liabilities/equity with nonpositive denominators are not known.

## Project 2 company selection

Fund: VT, from the earlier BIL/IEF/LQD/VT universe; student chose VT for this lab.

Company: NVIDIA, ticker NVDA, CIK 0001045810. Vanguard's VT fact sheet, holdings as of September 30, 2026, lists NVIDIA as the largest holding at 4.6%. Checked November 5, 2026. This is the latest issuer fact sheet verified for this exercise, not a claim about intraday holdings.

Source: https://workplace.vanguard.com/assets/corp/fund_communications/pdf_publish/us-products/fact-sheet/F3141.pdf

## Known-answer verification

COST current ratios: 1.02, 1.07, 0.97, 1.03, 1.06.
COST liabilities/equity: 2.11, 1.75, 1.96, 1.64, 1.49.

At the saved current-ratio threshold of 2.0: Buffett passes all three checks; Wood passes the earnings checks and fails liquidity; Burry passes both checks. Calculations matched every supplied reference value. Reference values occur in the test, never the production calculations.

The actual Wood SKILL.md threshold was changed to 1.0 and COST rerun: all Wood checks passed. It was restored to 2.0 with the student subsequently choosing to retain 2.0. Machine-readable evidence: data/threshold-probe.json. The app also offers a temporary threshold input, clearly labeled when saved memos describe a different setting. A revised retained setting requires rerunning/revising the corresponding memo.

NVDA: Buffett passes ROE, owner-earnings checks not known; Wood passes all checks; Burry fails cash backing and passes liabilities/equity. Six memos were written from printed values and passed numerical provenance validation. Tests inject 40.0% separately into every investor's memo. The validator checks matching values, not whether each claim is justified or attributed to the right metric.

## Student checkout still to complete

- At minute thirty, open Brightspace → Quizzes → Lab 19.
- Review the panel in the browser on COST and NVDA; personally test the temporary threshold and unprinted-number warning.
- State the retained threshold and why; add the line under Wood's memo. The student retained 2.0; see the Wood memos and CHECKOUT.md.
- Explain `wood_checks()` in scripts/panel.py line by line to Anika without AI, including missing-input handling; swap.
- Argue the NVDA bull and bear cases from this panel, two sentences each, then swap.
- Supply the Project 2 screening decision with a specific condition and reflect on agreement/splits and threshold sensitivity.
- Save those statements using the app's checkout fields or add them to CHECKOUT.md. Do not submit the pending items as completed.
- Upload the complete folder to GitHub, including `.agents` and scripts; submit links to the three SKILL.md files, scripts/edgar.py, scripts/panel.py, app.py, COST/NVDA memos and completed checkout evidence as requested by the quiz. No GitHub publication is performed automatically.

## Why the personas split

They apply different rules to identical facts: earning power for Buffett, assigned liquidity and earnings rules for Wood, cash backing and liabilities for Burry. These are three analyses using a shared fact table, not three independent confirmations of the same proposition. A threshold change can change a verdict without changing the business.

Methodology sources: https://github.com/CinderZhang/FAskills/blob/main/financial-researcher/experts/ben_graham.md and https://github.com/CinderZhang/FAskills/blob/main/financial-researcher/experts/michael_burry.md . Broader source-page valuation, news and paid-data requests are excluded by the lab rules.

## Checkout status update

Stefan confirmed the code-explanation swap and bull/bear role swap with Anika, supplied both cases, retained the assigned threshold, and supplied a conditional screening decision. See CHECKOUT.md for the recorded responses and qualifications. Earlier workflow checklist entries describe the required activities; GitHub publication and Brightspace submission still remain.
