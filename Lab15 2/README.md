# Lab 15 portfolio stability

Python 3.9+; tested with Streamlit 1.50.0. Engine uses only the standard library.

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python portfolio.py
python -m streamlit run app.py
```

For the already installed local environment, from this folder:

```bash
../../work/lab15-env/bin/python -m streamlit run app.py --server.port 8515
```

Start on Meridian: 6.5% objective, 3% minimum. Change equity return 8 to 7, inspect the 25-point change, then restore 8 before the correlation test. Edit both IG/equity correlation cells in portfolio.py to 0.50, save and refresh; restore 0.25 afterward.

Upload prices.csv for the proposed club universe; set objective 5%, minimum 20%, tick only BIL as reserve eligible. Read all-month results, then toggle last 36. Return edits reset when switching data/window; reserve classification persists. Both displayed allocations use the same current mandate. Download run JSON for evidence.

Run `python -m unittest -v test_lab15` for the engine tests. Record student/partner activities in lab15-stability.md. Do not claim the draft is a completed checkout.
