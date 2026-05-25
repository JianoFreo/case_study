from __future__ import annotations

from pathlib import Path
import random
from typing import Dict

import numpy as np
import pandas as pd
from faker import Faker


FAKER = Faker('en_PH')


BARANGAYS = [
    'San Isidro', 'Poblacion', 'San Jose', 'Mabini', 'Rizal', 'Del Pilar', 'Maligaya',
    'Bagong Silang', 'Magsaysay', 'San Miguel', 'Sta. Cruz', 'Bayanihan'
]

PRODUCTS = ['Rice', 'Cooking Oil', 'Instant Noodles', 'Canned Sardines', 'Soap', 'Shampoo', 'Milk', 'Coffee']
CATEGORIES = ['Grocery', 'Personal Care', 'Beverage', 'Household']


def _introduce_quality_issues(df: pd.DataFrame, numeric_cols: list[str], duplicate_rows: int = 20) -> pd.DataFrame:
    df = df.copy()
    if numeric_cols:
        for col in numeric_cols:
            if len(df) > 20:
                sample_idx = df.sample(frac=0.05, random_state=42).index
                df.loc[sample_idx, col] = np.nan
    if len(df) > 10:
        dupes = df.sample(n=min(duplicate_rows, len(df) // 10), random_state=7)
        df = pd.concat([df, dupes], ignore_index=True)
    if numeric_cols:
        for col in numeric_cols:
            if pd.api.types.is_numeric_dtype(df[col]):
                idx = df.sample(n=max(1, len(df) // 100), random_state=11).index
                df.loc[idx, col] = df[col].median() * 8
    return df.sample(frac=1, random_state=99).reset_index(drop=True)


def make_barangay_census(n: int = 1000) -> pd.DataFrame:
    rows = []
    for i in range(n):
        barangay = random.choice(BARANGAYS)
        households = np.random.poisson(180) + 20
        population = households * np.random.randint(3, 6)
        median_income = int(np.clip(np.random.normal(18000, 7000), 8000, 90000))
        rows.append({
            'record_id': i + 1,
            'barangay': barangay,
            'city': random.choice(['Quezon City', 'Pasig', 'Cebu City', 'Davao City', 'Iloilo City', 'Bacolod City']),
            'households': households,
            'population': population,
            'median_income': median_income,
            'collection_date': FAKER.date_between(start_date='-2y', end_date='today')
        })
    df = pd.DataFrame(rows)
    return _introduce_quality_issues(df, ['households', 'population', 'median_income'])


def make_sales_orders(n: int = 1000) -> pd.DataFrame:
    rows = []
    for i in range(n):
        qty = max(1, int(np.random.poisson(4)))
        unit_price = float(np.round(np.random.uniform(35, 950), 2))
        amount = float(np.round(qty * unit_price, 2))
        rows.append({
            'order_id': f'SO-{100000+i}',
            'order_date': FAKER.date_between(start_date='-18m', end_date='today'),
            'customer_name': FAKER.name(),
            'barangay': random.choice(BARANGAYS),
            'product': random.choice(PRODUCTS),
            'category': random.choice(CATEGORIES),
            'quantity': qty,
            'unit_price': unit_price,
            'total_amount': amount,
            'payment_method': random.choice(['Cash', 'GCash', 'Card', 'Bank Transfer'])
        })
    df = pd.DataFrame(rows)
    return _introduce_quality_issues(df, ['quantity', 'unit_price', 'total_amount'])


def make_medical_records(n: int = 1000) -> pd.DataFrame:
    rows = []
    for i in range(n):
        age = int(np.clip(np.random.normal(36, 18), 0, 90))
        temperature = float(np.round(np.clip(np.random.normal(36.9, 0.7), 34.0, 42.0), 1))
        cholesterol = int(np.clip(np.random.normal(190, 45), 80, 420))
        rows.append({
            'visit_id': f'MED-{200000+i}',
            'visit_date': FAKER.date_between(start_date='-2y', end_date='today'),
            'patient_name': FAKER.name(),
            'age': age,
            'sex': random.choice(['Male', 'Female']),
            'barangay': random.choice(BARANGAYS),
            'diagnosis': random.choice(['Hypertension', 'Diabetes', 'Asthma', 'Fever', 'Checkup', 'Infection']),
            'temperature_c': temperature,
            'cholesterol_mgdl': cholesterol,
            'weight_kg': float(np.round(np.clip(np.random.normal(62, 14), 35, 140), 1))
        })
    df = pd.DataFrame(rows)
    return _introduce_quality_issues(df, ['age', 'temperature_c', 'cholesterol_mgdl', 'weight_kg'])


def make_school_enrollment(n: int = 1000) -> pd.DataFrame:
    rows = []
    for i in range(n):
        math = int(np.clip(np.random.normal(79, 12), 40, 100))
        english = int(np.clip(np.random.normal(81, 10), 45, 100))
        science = int(np.clip(np.random.normal(78, 11), 40, 100))
        rows.append({
            'student_id': f'STU-{300000+i}',
            'student_name': FAKER.name(),
            'birth_date': FAKER.date_of_birth(minimum_age=5, maximum_age=20),
            'grade_level': random.choice(['Grade 1', 'Grade 2', 'Grade 3', 'Grade 4', 'Grade 5', 'Grade 6', 'Grade 7', 'Grade 8', 'Grade 9', 'Grade 10']),
            'school_name': random.choice(['San Isidro Elementary School', 'Poblacion National High School', 'Mabini Integrated School', 'Rizal Elementary School']),
            'barangay': random.choice(BARANGAYS),
            'math_score': math,
            'english_score': english,
            'science_score': science,
            'attendance_rate': float(np.round(np.clip(np.random.normal(0.92, 0.06), 0.5, 1.0), 2))
        })
    df = pd.DataFrame(rows)
    return _introduce_quality_issues(df, ['math_score', 'english_score', 'science_score', 'attendance_rate'])


def generate_all(n_each: int = 1000, out_dir: str | Path | None = None) -> Dict[str, str]:
    out_path = Path(out_dir) if out_dir else Path.cwd() / 'data' / 'generated'
    out_path.mkdir(parents=True, exist_ok=True)
    outputs: Dict[str, str] = {}

    datasets = {
        'barangay_census.csv': make_barangay_census(n_each),
        'sales_orders.csv': make_sales_orders(n_each),
        'medical_records.csv': make_medical_records(n_each),
        'school_enrollment.csv': make_school_enrollment(n_each),
    }

    for filename, df in datasets.items():
        file_path = out_path / filename
        df.to_csv(file_path, index=False)
        outputs[filename] = str(file_path)

    return outputs
