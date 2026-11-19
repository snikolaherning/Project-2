# Driver controls and assumptions

Base reset restores: 5% net scenario target, 60 months, VT/BIL overrides off, 7% inactive VT field, 3.5% inactive BIL field, 25 bp drag, 20% BIL floor. Inactive fields never replace historical means. The student-approved forward BIL judgment is tested with explicit overrides; the historical base remains reproducible.

| Exposed control | Bounds | Reason |
|---|---|---|
| Scenario net target | 0–8% | Testing envelope including original 4.5% changed input; changing it is not mandate approval |
| Window | 60 or 36 returns | Preserved common monthly samples; 37 prices required for 36 returns |
| VT estimate override | −10–15% | Pessimistic to optimistic forward arithmetic means, not confidence limits |
| BIL estimate override | −1–8% | Tests low/negative and high-rate regimes; not a forecast interval |
| Annual implementation drag | 0–200 bp | Illustrative friction sensitivity, not measured costs or an added fund expense |
| BIL floor | 20–100% | Can tighten but cannot relax the mandate floor |

Locked: BIL/IEF/LQD/VT universe; 60/40 VT/LQD benchmark; long only, fully invested, no leverage; five-point grid; frozen data; hard 10% loss limit and complete next-year spending policy. Historical means can exceed override testing bounds and are labeled historical, not defended forecasts. The app cannot establish hard future loss protection or segregated spending; those full-mandate checks remain failed at every setting. Numerical PASS cannot turn them into live approval.

Reset is tested after changing window, target, both override switches and reserve. Stop/failed rules are visible. Nonfinite estimates fail explicitly; no silent objective relaxation, missing-value zero fill or automatic bypass of a risk rule occurs. Downloaded JSON includes exact inputs and fingerprint.
