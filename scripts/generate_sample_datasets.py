"""
generate_sample_datasets.py
Create four synthetic CSV datasets for Module 3 exercises.
Run: python scripts/generate_sample_datasets.py --rows 60
"""
import argparse
import pandas as pd
import numpy as np
import random
import datetime

def generate(n_rows=60, seed=42, out_dir='.'):
    random.seed(seed)
    np.random.seed(seed)
    barangays = [f'Barangay {i+1}' for i in range(max(10, n_rows//6))]

    # Barangay census
    b = []
    for i in range(n_rows):
        name = random.choice(barangays)
        total = int(abs(np.random.normal(1500, 800))) + 50
        male = int(total * random.uniform(0.48, 0.52))
        female = total - male
        households = int(total / random.uniform(3.0, 5.0))
        employed = int(total * random.uniform(0.25, 0.6))
        unemployed = total - employed
        with_electricity = int(random.choice([1,0]) or 1)
        with_water = int(random.choice([1,0]) or 1)
        age_0_14 = int(total * random.uniform(0.2,0.35))
        age_15_64 = int(total * random.uniform(0.55,0.7))
        age_65_plus = total - age_0_14 - age_15_64
        b.append({
            'barangay_name': name, 'total_population': total, 'male': male, 'female': female,
            'households': households, 'employed': employed, 'unemployed': unemployed,
            'with_electricity': with_electricity, 'with_water': with_water,
            'age_0_14': age_0_14, 'age_15_64': age_15_64, 'age_65_plus': age_65_plus
        })
    df_barangay = pd.DataFrame(b)
    df_barangay.to_csv(f'{out_dir}/barangay_census.csv', index=False)

    # Sales orders
    products = ['Widget A','Widget B','Gadget X','Gadget Y','Service Z']
    regions = ['North','South','East','West']
    statuses = ['completed','pending','returned']
    start = datetime.date.today() - datetime.timedelta(days=365)
    orders = []
    for i in range(n_rows):
        order_date = start + datetime.timedelta(days=random.randint(0,364))
        qty = int(abs(np.random.poisson(3))) + 1
        unit_price = round(random.uniform(50,1500),2)
        total_amount = round(qty * unit_price,2)
        orders.append({
            'order_id': f'ORD{1000+i}', 'order_date': order_date.isoformat(), 'customer_id': f'C{random.randint(100,999)}',
            'product_name': random.choice(products), 'category': 'General', 'quantity': qty,
            'unit_price': unit_price, 'total_amount': total_amount, 'region': random.choice(regions), 'status': random.choice(statuses)
        })
    df_orders = pd.DataFrame(orders)
    df_orders.to_csv(f'{out_dir}/sales_orders.csv', index=False)

    # Medical
    diagnoses = ['Flu','Injury','Diabetes','Hypertension','Infection']
    depts = ['ER','Internal','Pediatrics','Surgery']
    med = []
    for i in range(n_rows):
        adm = start + datetime.timedelta(days=random.randint(0,364))
        los = max(1, int(np.random.poisson(3)))
        outcome = random.choice(['discharged','transferred','deceased'])
        med.append({
            'patient_id': f'P{2000+i}', 'admission_date': adm.isoformat(), 'discharge_date': (adm + datetime.timedelta(days=los)).isoformat(),
            'age': int(abs(np.random.normal(40,20)))+1, 'gender': random.choice(['M','F']), 'diagnosis': random.choice(diagnoses),
            'department': random.choice(depts), 'length_of_stay': los, 'outcome': outcome, 'barangay': random.choice(barangays)
        })
    df_med = pd.DataFrame(med)
    df_med.to_csv(f'{out_dir}/medical_records.csv', index=False)

    # School enrollment
    grades = [f'Grade {g}' for g in range(1,13)]
    enroll = []
    for i in range(n_rows):
        sy = random.choice(['2022-2023','2023-2024'])
        grade = random.choice(grades)
        scholarship = random.choice(['yes','no'])
        guardian_income = int(abs(np.random.normal(15000,8000)))
        enroll.append({
            'student_id': f'S{3000+i}', 'school_year': sy, 'grade_level': grade, 'section': random.choice(['A','B','C']),
            'gender': random.choice(['M','F']), 'age': int(abs(np.random.normal(12,3)))+5, 'barangay': random.choice(barangays),
            'enrollment_status': random.choice(['enrolled','dropped']), 'scholarship': scholarship, 'guardian_income': guardian_income
        })
    df_school = pd.DataFrame(enroll)
    df_school.to_csv(f'{out_dir}/school_enrollment.csv', index=False)

    print(f'Generated CSVs in {out_dir}')

if __name__ == '__main__':
    p = argparse.ArgumentParser()
    p.add_argument('--rows', type=int, default=60)
    p.add_argument('--out', type=str, default='.')
    args = p.parse_args()
    generate(n_rows=args.rows, out_dir=args.out)
