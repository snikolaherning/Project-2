# Point-in-time data card — TB3MS

Decision role: rate-environment context relevant to BIL, with no automatic weight effect or predictive-return claim. Source: Board of Governors H.15, distributed by [FRED](https://fred.stlouisfed.org/series/TB3MS) and ALFRED. Definition: three-month Treasury bill secondary-market rate, monthly average of business days, discount basis; percent per annum, not seasonally adjusted. It is neither a monthly return nor BIL total return.

Availability rule: retrieve the decision-date ALFRED vintage and use the latest nonmissing observation actually in that file. Measurement month labels do not establish publication dates. No universal fixed lag is assumed. Date-only vintages establish availability by that day, not an exact intraday release time. Missing dots are excluded, never zero-filled. Revisions may occur; zero observed revisions is not evidence of permanence.

Raw snapshots retrieved November 19, 2026:
- [September 30 vintage CSV](../data/signal/TB3MS-vintage-2026-09-30.csv): latest measured month August 2026, 3.72%. September observation is absent.
- [October 29 vintage CSV](../data/signal/TB3MS-vintage-2026-10-29.csv): latest measured month September 2026, 3.94%.
- [URLs, retrieval dates and SHA-256 manifest](../data/signal/downloads.json).

signal_snapshot() reads these files; tests assert the availability boundary and values. App displays this computed comparison offline after dependency installation. Stop on missing/invalid vintage data rather than substitute a later observation. Hashes identify exact input bytes; they do not establish predictive value.

Historical student checks and revision comparison remain in [Lab 17 data card](../Lab17/lab17-data-card.md) and [live-checks.json](../Lab17/live-checks.json). Those October 29 findings are kept distinct from the new raw retrieval. Source page verified November 19; its then-current October observation is not substituted into the September decision vintage. FRED identifies the underlying series as public domain with citation requested; retain source attribution. ETF price redistribution permissions are a separate unresolved deployment issue.

November forward BIL judgment uses separately dated Fed projections and issuer fees, documented in [student decisions](student-decisions.md). It is not retroactively inserted into the 2024 training split. Using a real point-in-time context series does not make the revised adjusted-price temporal check a vintage-correct backtest.
