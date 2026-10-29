# Lab 17 — Rates provenance and Project 2 admission

Stefan Herning | October 29, 2026 | Student verification and decision record.

## Client and series

University club reserve, five-year horizon, 5% nominal expected-return target and at least 20% in Treasury-bill funds. Student agreed to use a Treasury-bill rate; Codex selected TB3MS as a relevant series for the BIL reserve sleeve. It can describe the rate environment; it is not a replacement for BIL adjusted-price total returns.

## Data card: TB3MS

- Source: Board of Governors of the Federal Reserve System, H.15 Selected Interest Rates, distributed by FRED/ALFRED, Federal Reserve Bank of St. Louis.
- Source link: https://fred.stlouisfed.org/series/TB3MS
- Measure: three-month Treasury bill secondary market rate, monthly average of business days, discount basis.
- Units: percent per annum, not seasonally adjusted. A value of 3.94 is 3.94%, not 394% or a monthly return. Discount-basis yield is not an ETF total return.
- Timing: month labels indicate the measured month, not publication dates. The FRED page observed October 29 lists September 2026 at 3.94 and an update on October 1, 2026 at 3:16 p.m. CDT. This establishes a specific example of next-month availability, not a universal fixed release lag.
- Revisions: FRED states all data are subject to revision. Report observed vintage-comparison counts; do not infer that zero observed revisions means revisions are impossible.
- Download/retrieval date: October 29, 2026. Each app series also shows its actual cached download date.
- Student personally checked and confirmed three values against the FRED page: July 2026 3.73; August 2026 3.72; September 2026 3.94.

## Method

Separate cached functions download today's FRED CSV and the requested ALFRED vintage. Missing dots become missing observations and are excluded. The app counts today's nonmissing measured dates later than the last vintage date and compares numeric values on common measured dates for revisions, using a 1e-9 tolerance. Counts cover entire downloaded histories; chart-start date affects charts only. If no historical observation exists, latest-known date and later-observation count are unavailable rather than invented. A date-only vintage establishes availability by a day, not intraday publication time.

## Live verification — Codex executed

All four October 5, 2026 vintages match the assignment: BAA September 6.47; FEDFUNDS September 3.75; DGS10 October 2 at 5.28; MORTGAGE30US October 1 at 7.28. PAYEMS January 15, 2025 shows December 2024 at 159,536 versus today's same-month 158,316, with 381 revised common dates across full histories.

TB3MS as known September 30, 2026 ends at August 2026, 3.72. The current download ends at September 2026, 3.94: one later observation and zero revised common dates in this comparison. On October 29, vintage and current both end at September, 3.94, with zero later observations and zero revisions. These are executed download results, not hard-coded app outputs. Source values may update; live-checks.json preserves the comparison snapshot. Student reproduced these checks in the app: screenshots confirm the four-series known answer, PAYEMS vintage and revision count, and September 30 TB3MS comparison. The student separately confirmed the December 2024 PAYEMS matching-date values and the October 29 TB3MS comparison.

## Code explanation and partner review

Partner: Will Gao. The student confirmed the line-by-line explanation and role swap. The same question served as the code question and the data-card challenge to the revisions field; these are not represented as two separate questions.

Question: “Why not just use today’s revised value, since it’s more accurate than the first release?”

The student's explanation was that today's data contains later revisions and releases, so filtering measured dates alone leaves information unavailable at the decision date. ALFRED's requested vintage preserves the historical information set. Following AI feedback, the precise rule is the latest release available by the decision date, which may already incorporate revisions—not always the first release.

Two-sentence response, refined with AI feedback: Today's revised value may be more accurate, but it was not necessarily available when the decision was made. Our PAYEMS check showed December 2024 at 159,536 as known on January 15, 2025 versus 158,316 today, so requesting the decision-date vintage prevents later corrections from leaking into the historical decision.

The initial student response used a GDP illustration; that illustration is not relied on here because the app's PAYEMS comparison supplies directly checked evidence.

## Student decision: admit with an as-of rule

Admit TB3MS as a rate-environment input relevant to the BIL reserve sleeve, not as an ETF total-return series. The student's reasons were its H.15 source and clearly defined units. Our checked comparison found zero revisions; this does not establish that revisions never occur.

For each decision date, retrieve the ALFRED vintage for that date and use its latest nonmissing available observation. Do not assume that a month label means the value was already published, or that simply excluding the current month is sufficient. A previous month's value can also be unavailable until release.

The student's reversal condition is unexpected vintage revisions or release gaps longer than assumed: quarantine the input until its timing and handling are investigated and corrected. Revisions alone do not invalidate properly retrieved historical vintages, but they warrant checking the implementation before continued use.

## Student reflection

“The September 30 vintage ended at August, which showed the September TB3MS value wasn’t published yet because it’s a monthly average that only comes out after the month ends (early October). Using today’s data would have leaked the September row, dated 2026-09-01, so the decision would have used a full-month T-bill average that nobody could see on September 30.”

The observed September release supports this specific timing example, not a universal fixed publication schedule. This demonstrates an information leak; no trading backtest was run to quantify its effect on returns.

## Opening partner explanation

The student confirmed the no-screen discussion and role swap with Will Gao. The connection explained was that BIL holds short-term Treasury bills, so Treasury-bill rates such as TB3MS help describe the reserve sleeve’s earning environment. Precision added with AI feedback: TB3MS is a discount-basis quoted rate, not BIL’s realized total return; fund expenses, holdings and reinvestment timing can make the fund’s return differ.

## AI use and delivery

Codex built the app, checked downloads and drafted the data card. Student checks and partner dialogue above are recorded from student reports; AI refinements are identified explicitly. GitHub upload and Brightspace Lab 17 submission are pending. Primary files are asof_app.py, this Markdown and requirements.txt; README and live-checks.json support reproducibility.
