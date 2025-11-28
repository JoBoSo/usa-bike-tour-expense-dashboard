import pandas as pd
import plotly.graph_objects as go
import dataframes as dfs

df = dfs.expenses

fig = go.Figure()

fig.add_trace(go.Histogram(
    x=df["cost_cad"],
    nbinsx=30,
    marker_color='#FF00FF',
    opacity=0.9,
    hovertemplate='$%{x:.2f}±<br>Purchases: %{y}<extra></extra>',
))

fig.update_layout(
    title={
        'x': 0.5,
        'xanchor': 'center',
        'y': 0.9,
        'yanchor': 'top',
        'font': {'weight': "bold", "size": 20}
    },
    xaxis=dict(
        fixedrange=True,
        title='Purchase Amount (CAD)'
    ),
    yaxis=dict(
        fixedrange=True,
        title='Purchases'
    ),
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    font=dict(
        family="Poppins",
        size=16,
        color="white",
    ),
    margin=dict(l=0, r=0, t=0, b=0),
    width=900,
    height=400,
    dragmode='pan',
)

histogram_fig = fig
