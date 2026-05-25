# Google Business Intelligence — Module 3: Data Visualization & Dashboarding

Project repository for a beginner-friendly end-to-end BI dashboard built with Jupyter Notebook and open-source Python tools.

Project structure
```
google-bi-dashboard-project/
│
├── README.md
├── requirements.txt
├── .gitignore
├── data/
│   ├── raw/
   ├── processed/
   └── generated/
│
├── notebooks/
│   ├── 01_generate_data.ipynb
   ├── 02_data_cleaning.ipynb
   ├── 03_exploratory_analysis.ipynb
   ├── 04_visualizations.ipynb
   ├── 05_dashboard.ipynb
   └── 06_business_insights.ipynb
│
├── dashboards/
│   ├── dashboard.html
   └── dashboard_screenshots/
│
├── reports/
│   ├── executive_summary.md
│   └── stakeholder_presentation.md
│
├── src/
│   ├── generate_data.py
│   ├── cleaning.py
│   ├── visualization.py
│   └── dashboard.py
│
└── assets/
    └── images/
```

Overview
- This project generates four realistic Philippine-style datasets, cleans them, performs exploratory analysis, creates publication-quality visualizations, builds an interactive Plotly dashboard, and produces a short executive report.
- Everything runs from Jupyter Notebooks. Beginners can follow step-by-step comments and markdown explanations.

Installation
1. Create and activate a Python virtual environment (recommended).\n
2. Install dependencies:
```bash
pip install -r requirements.txt
```

How to run
1. Run `src/generate_data.py` or open `notebooks/01_generate_data.ipynb` and run all cells to generate data into `data/generated/`.
2. Open and run notebooks in order (01 → 06). Each notebook contains clear instructions.

Learning outcomes
- Synthetic data generation with Faker and NumPy
- Data cleaning with pandas
- Exploratory analysis and business insights
- Interactive visualizations with Plotly and Seaborn
- Exporting dashboards to HTML

Contact
This repository was generated as a complete beginner-friendly BI portfolio project.
