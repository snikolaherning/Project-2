# Lab 17 — Rates as known then

Python 3.9+, Streamlit and pandas; curl must be on PATH (included on macOS). Downloads use the public CSV endpoints, with no key or account. The app makes one current and one historical request per selected series and caches each for one hour. No retry substitutes current data for historical data.

```bash
python3 -m pip install -r requirements.txt
python3 -m streamlit run asof_app.py
```

Existing local course environment:

```bash
../../work/lab15-env/bin/python -m streamlit run asof_app.py --server.port 8517
```

Test October 5, 2026 on all four defaults. Then add PAYEMS and use January 15, 2025. For the student's own series, replace PAYEMS with TB3MS and compare September 30, 2026 with today. Keep the same chart-start date. Comparison counts use full histories, not just the chart window. Missing observations are excluded, not filled with zero. The detail table aligns the last 36 dates for manual inspection.

An unknown series shows its own error without stopping other series. Values remain in their native source units. No backtest or Project 2 admission decision is made automatically.
