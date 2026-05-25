"""
visualization.py
Reusable plotting helpers using Plotly and Matplotlib
"""
import plotly.express as px
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import seaborn as sns

def bar(df, x, y, title='Bar chart'):
    fig = px.bar(df, x=x, y=y, title=title, template='plotly_white')
    return fig

def line(df, x, y, title='Line chart'):
    fig = px.line(df, x=x, y=y, title=title, template='plotly_white', markers=True)
    return fig

def donut(series, title='Donut chart'):
    fig = px.pie(values=series.values, names=series.index, hole=0.4, title=title, template='plotly_white')
    return fig

def scatter(df, x, y, color=None, title='Scatter'):
    fig = px.scatter(df, x=x, y=y, color=color, title=title, template='plotly_white')
    return fig

def heatmap(df, x, y, z, title='Heatmap'):
    fig = px.density_heatmap(df, x=x, y=y, z=z, title=title, template='plotly_white')
    return fig
