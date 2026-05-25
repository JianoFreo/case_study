"""
Basic test script: loads each generated CSV and prints shape and sample.
Run: python scripts/test_data_and_notebooks.py
"""
import os
import pandas as pd

files = [
    'data/section1_overview.csv',
    'data/section2_principles.csv',
    'data/section3_tools.csv',
    'data/section4_datasets.csv',
    'data/section5_case_study.csv',
    'data/section6_codeguide.csv',
    'data/section7_stakeholders.csv',
    'data/section8_assessment.csv',
    'data/section9_resources.csv'
]

def check():
    ok = True
    for f in files:
        print('---', f)
        if not os.path.exists(f):
            print('MISSING:', f)
            ok = False
            continue
        df = pd.read_csv(f)
        print('shape:', df.shape)
        print(df.head(2).to_string(index=False))
    return ok

if __name__ == '__main__':
    all_ok = check()
    if all_ok:
        print('\nAll files present and readable.')
    else:
        print('\nSome files are missing or unreadable.')
