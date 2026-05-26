from __future__ import annotations

import plotly.express as px
import plotly.graph_objects as go
import pandas as pd


def bar_chart(df, x, y, title):
    return px.bar(df, x=x, y=y, title=title)


def line_chart(df, x, y, title):
    return px.line(df, x=x, y=y, title=title)


def donut_chart(df, names, values, title):
    return px.pie(df, names=names, values=values, hole=0.45, title=title)


def scatter_chart(df, x, y, title):
    return px.scatter(df, x=x, y=y, title=title, trendline='ols')


def heatmap(corr, title='Correlation heatmap'):
    fig = go.Figure(data=go.Heatmap(z=corr.values, x=corr.columns, y=corr.index, colorscale='RdBu', zmid=0))
    fig.update_layout(title=title)
    return fig


def revenue_by_barangay(sales_df, barangay_col='barangay', revenue_col='total_amount', top_n=10, title=None):
    df = sales_df.copy()
    df[revenue_col] = pd.to_numeric(df[revenue_col], errors='coerce').fillna(0)
    if barangay_col not in df.columns:
        raise KeyError(f"Column '{barangay_col}' not found in dataframe")
    grouped = df.groupby(barangay_col)[revenue_col].sum().reset_index()
    grouped = grouped.sort_values(revenue_col, ascending=False).head(top_n)
    title = title or f"Top {top_n} Barangays by Revenue"
    fig = px.bar(grouped, x=barangay_col, y=revenue_col, title=title)
    fig.update_layout(xaxis_title='Barangay', yaxis_title='Revenue', template='plotly_white')
    return fig


def monthly_revenue_trend(sales_df, date_col='order_date', revenue_col='total_amount', freq='M', title=None):
    df = sales_df.copy()
    if date_col not in df.columns:
        raise KeyError(f"Column '{date_col}' not found in dataframe")
    df[date_col] = pd.to_datetime(df[date_col], errors='coerce')
    df[revenue_col] = pd.to_numeric(df.get(revenue_col, pd.Series([])), errors='coerce').fillna(0)
    df = df.dropna(subset=[date_col])
    ts = df.set_index(date_col).resample(freq)[revenue_col].sum().reset_index()
    title = title or 'Monthly Revenue Trend'
    fig = px.line(ts, x=date_col, y=revenue_col, title=title, markers=True)
    fig.update_layout(xaxis_title='Date', yaxis_title='Revenue', template='plotly_white')
    return fig


def payment_method_mix(sales_df, payment_col='payment_method', title=None):
    df = sales_df.copy()
    if payment_col not in df.columns:
        raise KeyError(f"Column '{payment_col}' not found in dataframe")
    counts = df[payment_col].fillna('Unknown').value_counts().reset_index()
    counts.columns = [payment_col, 'count']
    title = title or 'Payment Method Mix'
    fig = px.pie(counts, names=payment_col, values='count', hole=0.45, title=title)
    fig.update_traces(textposition='inside', textinfo='percent+label')
    fig.update_layout(template='plotly_white')
    return fig


def order_qty_vs_revenue(sales_df, qty_col='quantity', revenue_col='total_amount', title=None):
    df = sales_df.copy()
    if qty_col not in df.columns or revenue_col not in df.columns:
        raise KeyError(f"Columns '{qty_col}' and/or '{revenue_col}' not found in dataframe")
    df[qty_col] = pd.to_numeric(df[qty_col], errors='coerce').fillna(0)
    df[revenue_col] = pd.to_numeric(df[revenue_col], errors='coerce').fillna(0)
    title = title or 'Order Quantity vs Revenue'
    fig = px.scatter(df, x=qty_col, y=revenue_col, hover_data=[qty_col, revenue_col], title=title, trendline='ols')
    fig.update_layout(xaxis_title='Order Quantity', yaxis_title='Revenue', template='plotly_white')
    return fig
