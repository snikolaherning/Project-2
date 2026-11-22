Codex was used for implementation, calculation checks, and drafting.
The analysis and final decision are mine; education, not investment advice.

# Validation and AI use

## Executed automated evidence

Run `python committee.py` for all stress outputs. `results/committee-report.json` contains full precision, inputs, all portfolio verdicts and both windows. Scenarios cover historical windows, VT return assumptions, implementation drag and reserve constraints. These precomputed scenarios are AI-assisted development checks, not the human locked experiment.

Twenty-one tests passed November 19 in a newly installed environment (Python 3.9.6, Streamlit 1.50.0 and pandas 2.3.3). Eight original engine checks, three UI/decision/reset checks and ten risk/provenance/time-split checks target both arithmetic and the load-bearing decision. The November 17 clean launch initially failed at Streamlit onboarding, then succeeded after the recorded fix. Linda's reported fresh-copy retry is separate evidence, with limitations preserved. Final test log: results/test-run.txt; supplemental outputs: results/risk-review.json. These are AI-executed developer checks, not independent partner attestations.

Data snapshot provenance and known-answer history remain in `Lab15 2/lab15-stability.md`, its source-evidence JSON, and `Lab17/lab17-data-card.md`. Historical student attestations are not new independent verification. The later retrospective 36/24 split is not an untouched holdout or live trading result.

## Locked Changed-Input Record — existing Lab 20 experiment

The updated main branch already contained the student's completed 5.0% to 4.5% objective experiment. See [original prediction and result](../lab20-changed-input.md), [before JSON](../evidence/before-5pct.json), and [after JSON](../evidence/after-4_5pct.json). Student confirmed AI-off authorship in this chat November 17. Do not represent the later docs/locked-prediction.md commit as preceding this already completed experiment. That local snapshot was made before this chat discovered the existing run, not before the original run.

Before: 80% BIL / 20% VT, 5.2545% gross expected return, 3.0937% annualized volatility. After: 85% BIL / 15% VT, 4.8394% gross return, 2.3654% volatility. Both JSON files preserve the same price hash, estimation inputs and reserve floor. Original lab engine omitted separately modeled costs and the new drawdown screen; these are not outputs of the committee engine's net-cost convention.

Allocation and directional predictions matched; expected return was higher than the predicted approximately 4.6%. The adoption prediction failed: fixed 85/15 with VT at 6.5% produces about 4.0301% with all-month BIL estimates, below 4.5%. The student subsequently chose simulation-only pilot. A lower target relaxes a requirement; it does not improve asset returns or establish protection from loss.

Verified original history: [prediction-only commit 1ac1db6](https://github.com/snikolaherning/Project-2/blob/1ac1db60000506f8ccc1ae932d9a9b9ca4abaa7b/lab20-changed-input.md), November 17 at 14:05:29 Eastern, contains only the prediction and no result/evidence files. [Result commit cbe18ca](https://github.com/snikolaherning/Project-2/blob/cbe18ca833584940f6f1ea121774194226d8b699/lab20-changed-input.md), 14:27:39 Eastern, appends the actual outcome. Commit order is independently inspectable. Student reports pushing the prediction before the original run. Execution timestamps are not embedded in the evidence, so independent chronological verification remains a limitation. No rerun is presented as an original locked experiment.

## Independent cold run — successful fresh-copy retry reported

Ross Dyson's Lab 20 review found incorrect README routing; no execution or elapsed time was recorded. Linda Li subsequently reviewed commit 2ce4d00 independently as reported by Stefan. Her Linux sandbox blocked PyPI, so the app could not install or render. Her supplied 60/36-month engine results and repository findings are preserved in [Linda's review](independent-review-linda.md); Codex's numeric comparison is in results/reviewer-evidence-check.json. She understood the simulation-only decision but identified the missing 85/15 row and legacy mandate confusion. A follow-up attempt supplied browser screenshots and JSON; installation on the Mac succeeded but port 8515 was occupied, and the browser used an unidentified pre-existing server. This establishes browser interaction, not a clean launch of the fresh ZIP. See the follow-up section of Linda’s review. Stefan subsequently confirmed Linda’s fresh-copy launch with matching Terminal/browser fingerprint b982296fa6a67012, approximately 14 minutes. The browser screenshot is preserved; Terminal match is a student-reported attestation. Earlier engine-only review is not counted as browser use.

## Source integrity check

Executed November 17: prices.csv and all four raw ETF JSON responses match every SHA-256 in the preserved download manifest; see results/source-integrity.json. This verifies snapshot integrity, not vendor accuracy or original point-in-time adjustment history.

## AI use and material dispositions

November 17, 2026: OpenAI Codex, model/version not exposed in this session, retrieved existing work, wrote the committee wrapper and UI, generated automated stress outputs, and drafted documents. Stefan supplied the mandate, AI-off prediction, simulation-only decision and reviewer attestations. Recording scripts are AI-assisted drafts for personal review; they are not transcripts or evidence that a video exists. Earlier AI uses and student verifications remain attributed in the lab records.

Checked AI claim: the former student code explanation suggested a five-point grid bounded distance from the continuous optimum. The Lab 15 record explicitly corrected that unsupported claim; current app states only a grid minimum. The net-cost bridge subtracts basis points / 10,000, covered by a known-answer test. AI output is not independent validation.

## Limitations driving action

The hard 10% drawdown cap and protected spending requirement are not demonstrated; they block live adoption. Frozen adjusted histories may be revised and are not a true historical-vintage ETF backtest. Source retrieval needs no credentials, but Yahoo licensing/redistribution permissions were not established; retain educational source attribution and obtain permitted data before broader deployment. Raw decision-date ALFRED CSVs were retrieved November 19, hashed, and tested for availability boundaries; the original student lab evidence remains separate. A point-in-time context input does not demonstrate predictive value. Implementation drag is hypothetical, not measured execution slippage. The retrospective temporal check is explicitly not an untouched holdout or vintage-correct performance claim.

## Student mandate clarification — November 17, 2026

Student selected a 10% maximum peak-to-trough investment loss, full protection of the next 12 months of spending, and one withdrawal in late August or September of up to 5% of the reserve. Operational interpretation: set the approved dollar spending budget at the annual decision date, with a 5% ceiling based on reserve value then; keep that dollar obligation protected after market losses. Measure investment drawdown on cash-flow-adjusted NAV so the annual withdrawal does not count as a market loss. This interpretation should be confirmed against the club's actual budget.

The historical screen uses monthly rebalanced constant weights, monthly adjusted total returns, and annual implementation drag divided by 12. Include starting NAV in the high-water mark. It is descriptive in-sample evidence, not a point-in-time trading backtest. Monthly observations can miss intramonth drawdowns. The search now rejects grid candidates exceeding 10% observed monthly drawdown in the active window. It does not simulate stop-order fills or certify a future hard cap.

Protecting spending requires a separately identified dollar account and due-date cash availability. A proposed cash or maturity-matched direct Treasury sleeve is outside the current ETF universe and has not yet been implemented. BIL alone is not evidence of complete principal protection. All current portfolios therefore FAIL full live mandate approval even if their numerical screen passes. Existing return and covariance results describe the ETF prototype, not a portfolio with a new protected sleeve; adding that sleeve requires recalculating expected return, risk and the mandate bridge.

Proposed monitoring: review cash-flow-adjusted drawdown each trading day; 8% is an analyst-proposed early-warning level, not a student-approved limit. At 10%, stop further risk deployment and refer allocation reduction to committee review. If the protected dollar account cannot meet the budget on time, stop approval. A stop trigger cannot guarantee a 10% maximum loss, so **reject live adoption under the hard cap today; pilot only in simulation with 0% live allocation**.

Sources: [TreasuryDirect: bills pay face value at maturity](https://www.treasurydirect.gov/marketable-securities/treasury-bills/); [SEC: stop price is not a guaranteed execution price](https://www.investor.gov/introduction-investing/general-resources/news-alerts/alerts-bulletins/investor-bulletins-14). Nominal maturity cash flows do not guarantee a stable daily market value or an inflation-adjusted spending amount.


## Browser-retry fixes

Add alternate --port, display matching source fingerprints in launcher/app/JSON, and respond to numerical verdicts in the recommendation panel. At full-window default inputs 85/15 is rejected numerically; recent-window default inputs permit simulation-only pilot. Infeasibility stops the scenario. Full mandate failure and 0% live allocation remain unchanged. The final targeted retry is now confirmed by Stefan: matching Terminal/browser fingerprint, fresh copy, approximately 14 minutes. See Linda’s review for the screenshot and limits of the attestation.

## Recording and freeze boundary

The original Lab 20 output is gross and cost-free; current committee output subtracts the illustrative annual implementation allowance. Do not mix their targets or results. The current default remains 5% net, while 4.5% is the locked experiment's changed input. The simulation research range does not imply numerical compliance at every setting. Scenario-dependent reject/pilot/stop is separate from the stable 0% live allocation.

Scripts in docs/recording/ are preparation material. Replace nothing in the historical prediction. Preserve actual spoken transcripts after recording; do not submit scripts as transcripts. Videos, durations, timestamp indices, access checks and final commit-specific manifest links remain pending.

## November 19 rubric-focused upgrade

Bounded driver panel now identifies locked assumptions, includes BIL and VT overrides, disables inactive controls, and resets all scenario inputs to the documented base. Bounds are disclosed testing envelopes, not confidence intervals. The 10% hard loss/spending policies cannot be relaxed through scenario controls. The default historical case is preserved for reproducibility; student forward judgments are separate overrides and saved stress scenarios.

Highest-risk tests and executed results: [risk-challenge.md](risk-challenge.md), results/risk-review.json and tests/test_risk_review.py. A 36/24 retrospective temporal split prevents future-price mutation from changing training selection, but the dataset was already inspected, so it is not an untouched holdout. ETF CSV values and month-end labels were reconstructed against every raw adjclose observation; no silent filling was found. ALFRED raw vintage files now support an executable point-in-time availability test.

Student ownership: Stefan supplied the BIL range and rationale and reconfirmed simulation-only pilot on November 19. Codex checked the primary-source numbers and corrected the gross/net and trigger bridges; see student-decisions.md. Fed end-year policy projections are not forecasts of annual BIL returns. Model/version was not exposed in this session. Supplemental stress work is AI-assisted and is not relabeled AI-off or retroactively inserted into the original prediction.

Both required videos and the professor's November 19 email require screen recording, webcam on, clear audio; Video 3 begins with the running app. Scripts and checklist now state this. Recordings and actual transcripts remain the student's final communication evidence.

## Final input-refusal and decision gates

The committee engine now checks the frozen CSV and raw ETF hashes at runtime, not only in a test. A positive-looking corrupted price is deliberately injected into a temporary copy; verify_snapshot refuses it. signal_snapshot also verifies each raw vintage against its retrieval hash. Missing build inputs produce a visible STOP message. Source-file integrity is not a claim of adversarial security: manifests can be deliberately versioned, and source accuracy still needs judgment.

The [committee pilot plan](committee-pilot-plan.md) proposes four weekly simulation reviews, with 0% live allocation and explicit stop/reconsideration gates. It is a proposed protocol, not completed activity. The analyst cannot convert a numerical PASS or completion of research reviews into live approval. This operationalizes the committee ask while preserving the student's decision and unproven hard mandate constraints.
