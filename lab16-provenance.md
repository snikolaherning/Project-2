# Lab 16 — Provenance Gate

Stefan Herning | October 27, 2026 | Student run and partner activities recorded; GitHub delivery pending.

## Define and represent

Question: On the day a trade would have been made, what did the data actually say, and what arrived later?

Inputs are the 12-row fictional card-spend training table in the user-supplied Lab 16 assignment, not real retailer data. Decision date: March 31, 2026. Measured month identifies the period described; publication date identifies when this version became knowable. The date-only training convention includes publications on the decision date; it does not resolve intraday trading cutoffs.

## Implementation

asof.py uses only Python's standard library. Editable inputs are at the top. Rules are applied in order: quarantine missing tickers, remove exact economic duplicates, exclude publications after the decision date, then retain the latest surviving publication per ticker/month. Row IDs preserve provenance and are excluded from the duplicate key. The first exact duplicate occurrence is retained. Conflicting values with an identical ticker, month and publication date are refused as ambiguous.

The naive comparison uses the same quarantine and deduplication rules, then selects the latest publication without a decision-date cutoff. Signals use the percentage change from the immediately preceding calendar month to the latest measured month in each panel. Missing preceding months or zero denominators produce an unavailable signal, not an invented value.

## Known-answer validation — AI executed

| Step | Removed rows | Count |
| --- | --- | --- |
| Missing ticker | 11 | 1 |
| Exact duplicate | 7 | 1 |
| Published too late | 3, 8, 10 | 3 |
| Superseded available vintage | 2 | 1 |

Surviving rows: **1, 4, 5, 6, 9, 12**. Six removed plus six retained reconcile to twelve inputs.

| Ticker | As-of signal | Naive signal |
| --- | --- | --- |
| AAA | +1.98%, February | +5.83%, March |
| BBB | -1.02%, February | -5.15%, March |
| CCC | +0.91%, February | +1.82%, February revised |

Six automated tests pass: row funnel, known signals, April 15 equality with naive results, inclusive cutoff and revision selection, missing-month handling, and ambiguous-vintage refusal. These tests were executed by Codex. They are not student execution or a partner exchange. The saved decision date remains March 31.

## Student execution and AI quiz

The student pasted terminal output from running `python3 asof.py` with the March 31 decision date. Every funnel row and signal matched the known answers above.

The student chose revision selection as the least-clear block. Before receiving the explanation, the student answered why row 4 replaces row 2 despite a lower index:

> Rows 2 and 4 are the same observation (AAA, February), so the as-of logic keeps the most recently published version available by the March 31 cutoff. Row 4 came out March 25, later than row 2’s March 10, so it’s treated as a revision that replaces the older estimate; the index value doesn’t factor into the choice.

AI feedback: correct. The ticker/month key identifies the observation and publication date determines the available vintage, not the magnitude of the index.

## Partner exchange — student-reported

Partner: **Will Gao**. The student confirms completing the opening measured-month versus publication-date explanation and swapping roles in the partner activities. The student reports that the partner's file, changed to April 15, produced as-of signals equal to the naive signals for all three tickers, and that March 31 was restored afterward. These observations are student-reported, not independently witnessed by Codex.

Will's question: How does the code recognize a duplicate despite different row numbers?

Student answer:

> It ignores the row number and compares only the data fields (ticker, month measured, published date, and index value). If row 7 matches an earlier row on all of those, it’s flagged as an exact duplicate and dropped, since the row number is just a label, not part of the data.

The code implements this with `row[1:]`; row 7 duplicates row 6. The separate revision-selection quiz is recorded above.

## Student explanation and reflection

Why AAA's naive signal was unavailable on March 31:

> The +5.83% uses AAA’s March value, which wasn’t published until after March 31. A trader deciding on March 31 couldn’t have seen that number yet, so using it makes the backtest look better than anything you could actually have traded.

Most consequential rule:

> The publication cutoff mattered most. It removed three rows and changed every ticker’s signal: AAA drops from +5.83% to +1.98%, BBB from -5.15% to -1.02%, and even CCC is halved (+1.82% to +0.91%), apparently because the naive version picks up a February revision published after the cutoff.

What a naive backtest would claim:

> A backtest on the naive signals would make the strategy look far stronger than it is. The signals are bigger and point more clearly in the direction the data later moved, so the backtest would overstate returns and predictive power, since it’s effectively trading on information that didn’t exist yet.

AI qualification after the student's response: the publication-time reasoning is correct. AAA's March value was published April 10; CCC's February revision was published April 5. The naive comparison uses later measured months for AAA and BBB and a later vintage of the same month for CCC. BBB becomes less negative rather than numerically falling. Such leakage can exaggerate apparent predictive performance, but these index signals alone do not establish realized strategy returns or prove the direction or magnitude of performance bias. Trading rules, subsequent asset returns and costs would be needed to quantify it. No return backtest was performed in this lab.

## Run and delivery

From this folder:

```bash
python3 asof.py
python3 -m unittest -v test_asof
```

Required main delivery: GitHub links to asof.py and this completed Markdown. test_asof.py, results.txt and validation-log.txt are optional supporting evidence. No GitHub upload or Brightspace submission is claimed.

## AI disclosure

Codex implemented the filter, generated and executed tests, and drafted this working record from the assignment pasted by the student. Outputs are calculated, not hardcoded known answers. Student explanations are preserved above with AI feedback separately labeled; partner observations are attributed to the student. The prior labs are unchanged.
