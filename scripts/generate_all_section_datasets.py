"""
generate_all_section_datasets.py
Generates 9 sample CSV files — one per notebook/section.
Run: python scripts/generate_all_section_datasets.py --rows 60 --out data
"""
import argparse
import pandas as pd
import numpy as np
import random
import datetime
import os

def ensure_dir(d):
    if not os.path.exists(d):
        os.makedirs(d)

def gen_section_datasets(n_rows=60, out_dir='data', seed=42):
    random.seed(seed)
    np.random.seed(seed)
    ensure_dir(out_dir)

    # Section 1: Overview KPIs (time series + KPIs)
    dates = pd.date_range(end=pd.Timestamp.today(), periods=12, freq='M')
    overview = pd.DataFrame({
        'month': dates.strftime('%Y-%m-%d'),
        'active_users': (np.random.poisson(200, size=12) + 50).tolist(),
        'transactions': (np.random.poisson(500, size=12) + 100).tolist()
    })
    overview.to_csv(f'{out_dir}/section1_overview.csv', index=False)

    # Section 2: Visualization principles (example categories)
    cats = ['A','B','C','D','E']
    principles = pd.DataFrame({
        'category': cats,
        'value': np.random.randint(10,500,size=len(cats))
    })
    principles.to_csv(f'{out_dir}/section2_principles.csv', index=False)

    # Section 3: Tools (tool metadata)
    tools = pd.DataFrame([
        {'tool':'Apache Superset','best_for':'Analysts','cons':'Docker required'},
        {'tool':'Metabase','best_for':'Beginners','cons':'Limited advanced features'},
        {'tool':'Plotly/Dash','best_for':'Programmers','cons':'Requires Python'},
        {'tool':'Power BI Free','best_for':'Windows users','cons':'Sharing limited'}
    ])
    tools.to_csv(f'{out_dir}/section3_tools.csv', index=False)

    # Section 4: Customizable datasets (simple sales-like table)
    products = ['Widget A','Widget B','Gadget X']
    regions = ['North','South','East','West']
    orders = []
    start = datetime.date.today() - datetime.timedelta(days=365)
    for i in range(n_rows):
        od = start + datetime.timedelta(days=random.randint(0,364))
        qty = int(np.random.poisson(3))+1
        price = round(random.uniform(20,500),2)
        orders.append({
            'order_id': f'O{i+1}', 'order_date': od.isoformat(), 'product': random.choice(products),
            'quantity': qty, 'unit_price': price, 'total': round(qty*price,2), 'region': random.choice(regions)
        })
    pd.DataFrame(orders).to_csv(f'{out_dir}/section4_datasets.csv', index=False)

    # Section 5: Case study (barangay-like census)
    barangays = [f'Barangay {i+1}' for i in range(max(8, n_rows//8))]
    census = []
    for i in range(n_rows):
        total = int(abs(np.random.normal(1200,600)))+20
        employed = int(total * random.uniform(0.3,0.6))
        census.append({
            'barangay': random.choice(barangays), 'total_population': total, 'employed': employed,
            'with_water': int(random.random() > 0.1)
        })
    pd.DataFrame(census).to_csv(f'{out_dir}/section5_case_study.csv', index=False)

    # Section 6: Python code guide (time series admissions)
    dates = pd.date_range(end=pd.Timestamp.today(), periods=n_rows, freq='D')
    med = pd.DataFrame({
        'admission_date': dates.strftime('%Y-%m-%d'),
        'department': np.random.choice(['ER','Internal','Pediatrics','Surgery'], size=n_rows),
        'length_of_stay': np.random.poisson(3, size=n_rows)+1
    })
    med.to_csv(f'{out_dir}/section6_codeguide.csv', index=False)

    # Section 7: Stakeholders (KPIs per stakeholder)
    stakeholders = ['Executive','Analyst','Operations']
    rows = []
    for s in stakeholders:
        rows.append({'stakeholder': s, 'kpi1': random.randint(50,500), 'kpi2': random.randint(5,80)})
    pd.DataFrame(rows).to_csv(f'{out_dir}/section7_stakeholders.csv', index=False)

    # Section 8: Assessment (student submissions/sample grades)
    subs = []
    for i in range(1, n_rows+1):
        subs.append({'student_id': f'ST{i:03d}', 'project_score': random.randint(50,100), 'quizzes': random.randint(40,100)})
    pd.DataFrame(subs).to_csv(f'{out_dir}/section8_assessment.csv', index=False)

    # Section 9: Resources (links and type)
    resources = pd.DataFrame([
        {'name':'Storytelling with Data','type':'Book','url':'https://storytellingwithdata.com'},
        {'name':'Plotly Python','type':'Docs','url':'https://plotly.com/python'},
        {'name':'Metabase','type':'Tool','url':'https://www.metabase.com'}
    ])
    resources.to_csv(f'{out_dir}/section9_resources.csv', index=False)

    print(f'Generated 9 CSV files in {out_dir}')

if __name__ == '__main__':
    p = argparse.ArgumentParser()
    p.add_argument('--rows', type=int, default=60)
    p.add_argument('--out', type=str, default='data')
    args = p.parse_args()
    gen_section_datasets(n_rows=args.rows, out_dir=args.out)
