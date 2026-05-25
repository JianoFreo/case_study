# Google Business Intelligence Professional Certificate - Module 3

This repository contains a complete, beginner-friendly data visualization and dashboarding project.

# Google BI Dashboard

This repository is a self-contained Business Intelligence (BI) teaching and demo project implemented with Python and Jupyter Notebooks. It is intended for instructors, students, and practitioners who want an end-to-end example: synthetic data generation → data cleaning → exploratory analysis → visualizations → dashboard export → business insights and reports.

This README documents the project architecture, components, usage, common workflows, and troubleshooting tips.

**Table of contents**
- Purpose and scope
- Architecture and file layout
- Component descriptions (what each module/notebook does)
- Quickstart (local, reproducible steps)
- Running notebooks programmatically
- Common workflows and examples
- Troubleshooting and tips
- Extending the project

## Purpose and scope
This project provides:
- Four realistic synthetic datasets for BI practice (sales, census, medical, school enrollment).
- Reusable `src/` modules for generation, cleaning, visualization, and dashboard assembly.
- Six self-contained Jupyter Notebooks that are runnable independently and sequentially:
   - Generate data; Clean data; Explore data; Visualize; Build dashboard; Generate business insights.
- Exportable outputs: cleaned CSVs in `data/processed/`, dashboard HTML in `dashboards/`, and an executive summary in `reports/`.

## Architecture and file layout
Root-level layout (top-level paths):

- `notebooks/` — Jupyter notebooks (01–06) meant to be run interactively.
- `executed/` — executed copies of notebooks (stored for validation/inspection).
- `data/`
   - `generated/` — CSVs created by the data generator
   - `raw/` — placeholder for raw uploads
   - `processed/` — cleaned CSV outputs from the cleaning notebook
- `src/` — Python modules for reuse
   - `generate_data.py` — dataset generators and `generate_all()` orchestrator
   - `cleaning.py` — cleaning utilities (missingness reports, dedupe, numeric fixes, outlier capping)
   - `visualization.py` — small wrappers around Plotly/seaborn examples
   - `dashboard.py` — assembles KPIs + charts and exports an HTML dashboard
- `dashboards/` — exported HTML and screenshots
- `reports/` — `executive_summary.md`, `stakeholder_presentation.md` outputs
- `assets/` — images or static files used by notebooks/dashboards
- `requirements.txt` — pinned Python dependencies
- `.gitignore` — repo ignores

Architecture notes
- Notebooks are independent: each begins with a startup cell that finds the project root and ensures `src` is importable (it appends the root and `root/src` to `sys.path`). This allows running notebooks from `notebooks/`, `executed/`, or the repository root.
- `src/` contains domain logic so notebooks demonstrate usage rather than duplicate functions.

## Component descriptions

- `src/generate_data.py`
   - Functions: `make_barangay_census()`, `make_sales_orders()`, `make_medical_records()`, `make_school_enrollment()`, and `generate_all()`.
   - Behavior: synthesizes realistic fields (IDs, dates, amounts, categorical features), injects controlled missing values, duplicates, and outliers to create realistic cleaning exercises.

- `src/cleaning.py`
   - Key helpers: `report_missing(df)`, `drop_duplicates(df)`, `fix_numeric_types(df, cols)`, `fill_numeric_with_median(df, cols)`, `cap_outliers_iqr(df, column)`.
   - Intended to be explanatory and used as examples rather than production-grade pipelines.

- `src/visualization.py`
   - Plot wrappers for quick re-use (bar chart, line chart, donut/pie, scatter, heatmap). Notebooks call these for consistent styling.

- `src/dashboard.py`
   - `build_sample_dashboard(paths, out_html)` reads prepared CSVs, computes KPIs and chart objects, and writes an interactive HTML export. The dashboard is standalone and can be opened in a browser.

- `notebooks/01_generate_data.ipynb`
   - Runs `generate_all()` and writes CSVs to `data/generated/`.

- `notebooks/02_data_cleaning.ipynb`
   - Loads generated CSVs, demonstrates `report_missing`, deduplication, numeric coercion, median imputation for numeric columns, and IQR-based outlier capping, then writes cleaned CSVs to `data/processed/`.

- `notebooks/03_exploratory_analysis.ipynb`
   - Descriptive stats, group-by revenue analysis, trend/resampling examples, and correlation heatmaps.

- `notebooks/04_visualizations.ipynb`
   - Plotly/Matplotlib/Seaborn examples with reusable snippets and export suggestions.

- `notebooks/05_dashboard.ipynb`
   - Showcases `src.dashboard` usage and writes `dashboards/dashboard.html`.

- `notebooks/06_business_insights.ipynb`
   - KPI computation, top-n tables, and writes an `reports/executive_summary.md` with recommendations.

## Quickstart — local (recommended)
1. Create & activate a virtual environment (recommended):

    Windows PowerShell:
    ```powershell
    python -m venv .venv
    .\\.venv\\Scripts\\Activate.ps1
    pip install -r requirements.txt
    ```

    macOS / Linux:
    ```bash
    python3 -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt
    ```

2. Start Jupyter Lab/Notebook in the repository root:

    ```powershell
    jupyter lab
    ```

3. Open and run notebooks in order 01 → 06. Each notebook's top cell bootstraps imports and paths.

## Running notebooks programmatically (headless)
- To execute a single notebook and save an executed copy:

   ```bash
   jupyter nbconvert --to notebook --execute notebooks/02_data_cleaning.ipynb --output executed/02_data_cleaning.ipynb
   ```

- If you run into missing-package errors when executing with `nbconvert`, ensure `pip install -r requirements.txt` ran in the same Python environment used by `nbconvert`.

## Common workflows and examples
- Regenerate all datasets (script):

   ```bash
   python -c "from src.generate_data import generate_all; generate_all(n_each=1000, out_dir='data/generated')"
   ```

- Run cleaning programmatically (example):

   ```python
   from pathlib import Path
   import pandas as pd
   from src.cleaning import drop_duplicates, fill_numeric_with_median, cap_outliers_iqr

   sales = pd.read_csv('data/generated/sales_orders.csv')
   sales, removed = drop_duplicates(sales)
   sales = fill_numeric_with_median(sales, ['quantity','unit_price','total_amount'])
   sales = cap_outliers_iqr(sales, 'total_amount')
   sales.to_csv('data/processed/sales_orders_cleaned.csv', index=False)
   ```

## Troubleshooting
- ModuleNotFoundError: No module named 'src'
   - Ensure you started Jupyter from the repository root or run the top cell of the notebook which appends the project root and `root/src` to `sys.path`.
   - Alternatively, install the package in editable mode:

      ```bash
      pip install -e .
      ```

- `nbconvert` missing packages
   - Install requirements into the same Python environment used by the `nbconvert` process (e.g., Conda env or system Python). You can check which Python `nbconvert` uses by running `python -m pip --version` in the environment you call `jupyter` from.

- Files in use / move errors when reorganizing
   - Close open notebook tabs and stop running Python kernels before moving files. Use copy instead of move if you prefer not to interrupt running sessions.

## Extending the project
- Convert `src/` into a proper package with `pyproject.toml` and tests.
- Add CI to automatically run notebook execution and validate outputs on push.
- Add more datasets or connect to real data sources (CSV, SQL, APIs).

## Developer notes
- Notebook bootstrap: each notebook contains a robust path-discovery cell that appends the repository root and `root/src` to `sys.path`. That makes `from src import ...` work in interactive and headless contexts.
- Files expected to be present after running notebooks:
   - `data/generated/*.csv` (generated)
   - `data/processed/*_cleaned.csv` (cleaned)
   - `dashboards/dashboard.html` (export)
   - `reports/executive_summary.md` (report)

