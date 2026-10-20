# Lab 14 — Meridian portfolio baselines

Stefan Herning | Prepared October 20, 2026 | Completed individual calculations and reported partner validation; GitHub delivery pending

## Define and represent

Question: What does each simple portfolio earn and risk, and does any meet the Meridian mandate?
All numerical inputs in portfolio.py are course-authored annual training values, not market estimates. Assumed CPI of 2.5% plus the 4% real objective gives the classroom 6.5% target. The calculation does not separately model fees or guarantee future realized returns. Engine weights/returns/volatilities are decimals; mandate.py uses percentage weights. Bills and 10-year Treasuries are reserve-eligible under the supplied case classifications.

## AI implementation and verification

Codex implemented portfolio.py from the Lab 14 instruction, copied the existing Lab 13 checker into this folder and added candidate E, then executed the checks. The original Lab 13 file and submitted Project 1 package were not edited. Six automated checks pass; see validation-log.txt. These are AI-executed checks, not evidence of student or partner completion.

| Portfolio | Expected return | Volatility | Reserve weight | Meets return target? |
| --- | --- | --- | --- | --- |
| Benchmark | 6.80% | 10.46% | 0.0% | Yes |
| Equal weight | 5.20% | 5.21% | 50.0% | No |
| Inverse volatility | 3.77% | 1.05% | 90.3% | No |

The correlation probe raises both IG/equity cells from 0.25 to 0.50 and yields 11.00% benchmark volatility. A correlation of 1.3 and an asymmetric table are refused. The saved engine retains 0.25. Additional checks reject inconsistent joint correlation matrices. Candidate E fails only the 3% reserve rule among the five holdings checks. No baseline meets both the expected-return objective and reserve minimum; the checker still cannot establish full mandate compliance or resolve S9's loss requirement.

## Student work completed in this conversation

The following records student responses and pasted terminal output, distinct from Codex's automated checks above. AI supplied prompts, commands and feedback; no AI-off partner exchange is claimed.

### Hand volatility calculation

Student answers: bond variance contribution `5.76 × 10^-4`; equity contribution `0.009216`; cross term `0.001152`; volatility `10.46135746` percent. These imply variance `0.010944` and agree with the benchmark. A separate hand calculation of expected return was not supplied.

Asked whether raising correlation from 0.25 to 1 increases risk, the student answered:

> rise, heavily correlated portfolios limit diversification, and diversification helps to take away risk

AI clarification: diversification reduces some risks; it does not remove all risk. This particular benchmark's volatility is below equity's but above bonds'.

### Student-run evidence

The student pasted successful terminal output for `python3 portfolio.py` and `python3 mandate.py`: all three baselines match the table; candidate E fails only the reserve check, with 0.0% against 3.0%. A-D retain their prior verdicts.

Using AI-supplied commands on temporary copies of the correlation table, the student then reported:

- Both IG/equity cells set to 0.50: `Benchmark volatility: 11.00%`.
- Both cells set to 1.3: `Correctly refused: Every correlation must be between -1 and 1.`

These commands did not modify the saved inputs. They test the student's own engine, not a partner's file.

### Code quiz: square root after variance

The student selected the square-root step as least clear and answered the quiz before receiving the explanation:

> squaring turns percent into percent squared and the square root brings it back to plain percent, so risk and return sit on the same scale and can be compared directly

AI feedback: correct units reasoning; expected return measures the average outcome while volatility measures variability.

### Reflection: inverse volatility

> T bills have near zeero volatility so 1/volatility becomes enormous for them and swamps every other asset's score, pushing weight into cash

The case uses Treasury bills with 0.5% annual volatility, not literally zero volatility; the engine refuses zero volatility for inverse weighting.

### Reflection: first baseline for the CIO

The student initially suggested an after-cost return shortfall. AI feedback pointed out that no separate cost estimate was supplied and that the demonstrated failure is the reserve constraint. The student's revised answer:

> The 60/40 benchmark (S4), because it’s the yardstick the CIO already judges against and its 6.80% expected return clears the 6.50% target, but it holds 0% in reserves against the required 3%, so it fails the reserve constraint (S3).

## Partner validation — student-reported

Partner: **Anika Rao**. The student reports completing the code explanation and swap-and-break with this partner.

Partner question: Why does the code take a square root?

Student answer:

> its because portfolio math naturally produces variance in squared units, so the square root converts it back to volatility in percent, comparable to returns.

The student confirms that the partner's baseline results matched, the partner's file refused the invalid correlation of 1.3, and the change was undone afterward. These are student-reported partner observations, not tests independently witnessed by Codex.

## Sources

- [Lab 14 instructions and training inputs](https://github.com/CinderZhang/FIN43900-Fall2026/blob/main/lessons/week-09/lab-14-portfolio-baselines.md), accessed October 20, 2026.
- [Week 9 handout and independent benchmark digits](https://github.com/CinderZhang/FIN43900-Fall2026/blob/main/lessons/week-09/student-handout.md), accessed October 20, 2026.
- Existing Lab 13 mandate.py supplied in the student's local course work folder; copied without changing A-D or mandate rules, adding E only.

## Delivery

Upload this Markdown, portfolio.py, mandate.py and supporting results/tests to the student's GitHub repository and provide the required file links. This package has not been published or submitted. Keep Project 1's submitted snapshot intact.

Before Thursday, the student's separate Project 2 mandate is still needed to select their own fund universe and data. Meridian is the training case, not a substitute for that mandate.
