from __future__ import annotations

from pathlib import Path

import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots


def build_sample_dashboard(paths: dict[str, str], out_html: str | Path) -> str:
    sales = pd.read_csv(paths['sales'])
    barangay = pd.read_csv(paths['barangay'])
    medical = pd.read_csv(paths['medical'])
    enrollment = pd.read_csv(paths['enrollment'])

    for frame, date_col in [(sales, 'order_date'), (medical, 'visit_date')]:
        if date_col in frame.columns:
            frame[date_col] = pd.to_datetime(frame[date_col], errors='coerce')

    revenue = float(sales['total_amount'].fillna(0).sum()) if 'total_amount' in sales.columns else 0.0
    orders = int(len(sales))
    avg_order = float(sales['total_amount'].fillna(0).mean()) if 'total_amount' in sales.columns else 0.0
    avg_attendance = float(enrollment['attendance_rate'].fillna(0).mean()) if 'attendance_rate' in enrollment.columns else 0.0

    monthly = sales.dropna(subset=['order_date']).copy()
    monthly = monthly.set_index('order_date').resample('M')['total_amount'].sum().reset_index() if not monthly.empty else pd.DataFrame({'order_date': [], 'total_amount': []})
    diagnosis = medical['diagnosis'].value_counts().reset_index()
    diagnosis.columns = ['diagnosis', 'count']

    fig = make_subplots(
        rows=2,
        cols=2,
        specs=[[{'type': 'indicator'}, {'type': 'indicator'}], [{'type': 'xy'}, {'type': 'xy'}]],
        subplot_titles=('Revenue', 'Orders', 'Monthly Revenue', 'Diagnoses')
    )

    fig.add_trace(go.Indicator(mode='number', value=revenue, title={'text': 'Total Revenue'}), row=1, col=1)
    fig.add_trace(go.Indicator(mode='number', value=orders, title={'text': 'Orders'}), row=1, col=2)
    if not monthly.empty:
        fig.add_trace(go.Scatter(x=monthly['order_date'], y=monthly['total_amount'], name='Monthly Revenue'), row=2, col=1)
    if not diagnosis.empty:
        fig.add_trace(go.Bar(x=diagnosis['diagnosis'], y=diagnosis['count'], name='Diagnoses'), row=2, col=2)

    fig.update_layout(height=900, title='Google BI Dashboard', showlegend=False)
    out_path = Path(out_html)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    fig.write_html(out_path)
    return str(out_path)
