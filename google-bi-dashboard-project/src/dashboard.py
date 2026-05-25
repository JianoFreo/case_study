"""
dashboard.py
Functions to assemble a Plotly dashboard and export to HTML
"""
from plotly.subplots import make_subplots
import plotly.graph_objects as go

def build_sample_dashboard(kpis, bar_df, line_df, donut_series, heat_df, scatter_df, out_html='dashboards/dashboard.html'):
    # kpis: dict of {name: value}
    fig = make_subplots(rows=3, cols=2, specs=[[{"type":"indicator","colspan":2}, None],[{"type":"xy"},{"type":"domain"}],[{"type":"xy"},{"type":"xy"}]], subplot_titles=("KPIs","","Bar Chart","Donut","Line Chart","Scatter"))
    # KPIs row
    i = 1
    for name, val in kpis.items():
        fig.add_trace(go.Indicator(mode='number', title={'text':name}, value=val), row=1, col=1)
        i += 1
    # Bar
    fig.add_trace(go.Bar(x=bar_df.iloc[:,0], y=bar_df.iloc[:,1], name='Bar'), row=2, col=1)
    # Donut
    fig.add_trace(go.Pie(labels=donut_series.index, values=donut_series.values, hole=0.4), row=2, col=2)
    # Line
    fig.add_trace(go.Scatter(x=line_df.iloc[:,0], y=line_df.iloc[:,1], mode='lines+markers'), row=3, col=1)
    # Scatter
    fig.add_trace(go.Scatter(x=scatter_df.iloc[:,0], y=scatter_df.iloc[:,1], mode='markers'), row=3, col=2)
    fig.update_layout(height=900, template='plotly_white', showlegend=False)
    fig.write_html(out_html)
    return out_html
