"""
generate_data.py
Generates four synthetic datasets (Barangay census, Sales orders, Medical records, School enrollment)
Saves CSVs under data/generated/
"""
from faker import Faker
import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta
import os

fake = Faker('en_PH')

def ensure_dir(path):
    os.makedirs(path, exist_ok=True)

def make_barangay_census(n=1000, out_dir='data/generated'):
    rows = []
    barangays = [f'Barangay {i+1}' for i in range(100)]
    for i in range(n):
        b = random.choice(barangays)
        total_pop = max(20, int(abs(np.random.normal(1500, 800))))
        male = int(total_pop * random.uniform(0.48,0.52))
        female = total_pop - male
        employed = int(total_pop * random.uniform(0.25,0.6))
        households = int(total_pop / random.uniform(3,5))
        with_electricity = np.random.choice([1,0], p=[0.95,0.05])
        with_water = np.random.choice([1,0], p=[0.9,0.1])
        age_0_14 = int(total_pop * random.uniform(0.18,0.35))
        age_15_64 = int(total_pop * random.uniform(0.55,0.7))
        age_65_plus = total_pop - age_0_14 - age_15_64
        rows.append({
            'barangay_name': b,
            'total_population': total_pop,
            'male': male,
            'female': female,
            'households': households,
            'employed': employed,
            'unemployed': total_pop - employed,
            'with_electricity': with_electricity,
            'with_water': with_water,
            'age_0_14': age_0_14,
            'age_15_64': age_15_64,
            'age_65_plus': age_65_plus
        })
    df = pd.DataFrame(rows)
    # introduce missing values
    for col in ['households','with_water']:
        df.loc[df.sample(frac=0.02).index, col] = np.nan
    # duplicates
    dup = df.sample(frac=0.01)
    df = pd.concat([df, dup], ignore_index=True)
    # outliers: add a few extreme populations
    for _ in range(3):
        idx = random.randint(0, len(df)-1)
        df.at[idx,'total_population'] = df.at[idx,'total_population'] * 10
    ensure_dir(out_dir)
    path = os.path.join(out_dir, 'barangay_census.csv')
    df.to_csv(path, index=False)
    return path

def make_sales_orders(n=1000, out_dir='data/generated'):
    products = ['Rice Cooker','Shirt','Sari-Sari Kit','Widget A','Widget B','Gadget X']
    regions = ['NCR','Ilocos','Cagayan Valley','Central Luzon','CALABARZON','Bicol']
    rows = []
    start = datetime.now() - timedelta(days=365)
    for i in range(n):
        order_date = start + timedelta(days=random.randint(0,364))
        qty = int(np.random.poisson(3)) + 1
        unit_price = round(random.uniform(50,5000),2)
        total_amount = round(qty * unit_price,2)
        rows.append({
            'order_id': f'ORD{100000+i}',
            'order_date': order_date.strftime('%Y-%m-%d'),
            'customer_id': f'C{random.randint(1000,9999)}',
            'product_name': random.choice(products),
            'category': 'General',
            'quantity': qty,
            'unit_price': unit_price,
            'total_amount': total_amount,
            'region': random.choice(regions),
            'status': random.choice(['completed','pending','returned'])
        })
    df = pd.DataFrame(rows)
    # missing
    df.loc[df.sample(frac=0.02).index, 'region'] = np.nan
    # duplicates
    df = pd.concat([df, df.sample(frac=0.01)], ignore_index=True)
    # outliers
    df.loc[df.sample(frac=0.001).index, 'total_amount'] *= 50
    ensure_dir(out_dir)
    path = os.path.join(out_dir, 'sales_orders.csv')
    df.to_csv(path, index=False)
    return path

def make_medical_records(n=1000, out_dir='data/generated'):
    diagnoses = ['Flu','Diabetes','Hypertension','Infection','Injury']
    departments = ['ER','Internal','Pediatrics','Surgery']
    rows = []
    start = datetime.now() - timedelta(days=365)
    for i in range(n):
        adm = start + timedelta(days=random.randint(0,364))
        los = int(np.random.poisson(3)) + 1
        dis = adm + timedelta(days=los)
        rows.append({
            'patient_id': f'P{200000+i}',
            'admission_date': adm.strftime('%Y-%m-%d'),
            'discharge_date': dis.strftime('%Y-%m-%d'),
            'age': int(abs(np.random.normal(40,20)))+1,
            'gender': random.choice(['M','F']),
            'diagnosis': random.choice(diagnoses),
            'department': random.choice(departments),
            'length_of_stay': los,
            'outcome': random.choice(['discharged','transferred','deceased']),
            'barangay': f'Barangay {random.randint(1,100)}'
        })
    df = pd.DataFrame(rows)
    df.loc[df.sample(frac=0.02).index, 'diagnosis'] = np.nan
    df = pd.concat([df, df.sample(frac=0.01)], ignore_index=True)
    for _ in range(2):
        idx = random.randint(0, len(df)-1)
        df.at[idx,'length_of_stay'] *= 10
    ensure_dir(out_dir)
    path = os.path.join(out_dir, 'medical_records.csv')
    df.to_csv(path, index=False)
    return path

def make_school_enrollment(n=1000, out_dir='data/generated'):
    grades = [f'Grade {g}' for g in range(1,13)]
    rows = []
    for i in range(n):
        sy = random.choice(['2022-2023','2023-2024'])
        grade = random.choice(grades)
        rows.append({
            'student_id': f'S{300000+i}',
            'school_year': sy,
            'grade_level': grade,
            'section': random.choice(['A','B','C']),
            'gender': random.choice(['M','F']),
            'age': int(abs(np.random.normal(12,3)))+5,
            'barangay': f'Barangay {random.randint(1,100)}',
            'enrollment_status': random.choice(['enrolled','dropped']),
            'scholarship': random.choice(['yes','no']),
            'guardian_income': int(abs(np.random.normal(15000,8000)))
        })
    df = pd.DataFrame(rows)
    df.loc[df.sample(frac=0.02).index, 'guardian_income'] = np.nan
    df = pd.concat([df, df.sample(frac=0.01)], ignore_index=True)
    for _ in range(2):
        idx = random.randint(0, len(df)-1)
        df.at[idx,'guardian_income'] *= 10
    ensure_dir(out_dir)
    path = os.path.join(out_dir, 'school_enrollment.csv')
    df.to_csv(path, index=False)
    return path

def generate_all(n_each=1000, out_dir='data/generated'):
    ensure_dir(out_dir)
    paths = {}
    paths['barangay'] = make_barangay_census(n_each, out_dir)
    paths['sales'] = make_sales_orders(n_each, out_dir)
    paths['medical'] = make_medical_records(n_each, out_dir)
    paths['school'] = make_school_enrollment(n_each, out_dir)
    return paths

if __name__ == '__main__':
    print('Generating datasets (1000 rows each) in data/generated/...')
    p = generate_all(1000, out_dir='data/generated')
    for k,v in p.items():
        print(k, '->', v)
