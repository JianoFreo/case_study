from __future__ import annotations

import plotly.express as px
import plotly.graph_objects as go


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
