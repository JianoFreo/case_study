# Module 3 — Data Visualization & Dashboarding (Google BI Certificate)

Contents
- notebooks/Module3_Data_Visualization.ipynb — Colab-ready notebook with step-by-step code and dashboard export.\n
- scripts/generate_sample_datasets.py — script to generate sample CSVs for practice.\n
How to use (Google Colab)
1. Open https://colab.research.google.com and create a new notebook.\n2. In Colab, choose `File > Upload notebook` and upload `notebooks/Module3_Data_Visualization.ipynb`.\n3. Run the first cell (setup).\n4. Run the generator cell to create sample CSVs, or upload your own CSV.\n5. Run chart cells one by one.\n
How to use locally
1. (Optional) Create a Python venv and install dependencies: `pip install pandas plotly numpy`.\n2. Generate CSVs: `python scripts/generate_sample_datasets.py --rows 60 --out data`\n3. Open the notebook in Jupyter or convert the notebook to run locally.\n
Notes
- The notebook follows the module structure (overview, principles, tools, charts, dashboard).\n+- Change column names in the code cells to match your dataset.\n