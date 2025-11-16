import polars as pl
import plotly.graph_objects as go
import dataframes as dfs 

df = dfs.expenses

x_col="category"
# x_col="store_type"

# Filter to only include store_type with 5+ data points
category_counts = df.group_by(x_col).len()
valid_categories = category_counts.filter(pl.col("len") >= 5)[x_col]
df_filtered = df.filter(pl.col(x_col).is_in(valid_categories))

fig = go.Figure()

fig.add_trace(go.Box(
    x=df_filtered[x_col],
    y=df_filtered["cost_cad"],
    boxpoints='all',
    jitter=0.5,
    pointpos=0,
    marker=dict(color='#00FFFF', opacity=0.4),
    line=dict(color='#FF00FF', width=3),
    boxmean=True,
    fillcolor='rgba(255, 0, 255, 0.2)',
    customdata=df_filtered["store_name"],
    hovertemplate='%{customdata}: $%{y:.2f}<extra></extra>',
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
        title='Expense Category'
    ),
    yaxis=dict(
        fixedrange=True,
        title='Purchase Amount (CAD)'
    ),
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    font=dict(
        family="Poppins",
        size=16,
        color="white",
    ),
    margin=dict(l=0, r=0, t=0, b=0),
    width=1100,
    height=500,
    boxgap=0.0,
    dragmode='pan',
)

fig.update_yaxes(
    zeroline=True,
    zerolinecolor='rgba(255, 255, 255, 0.2)',
    gridcolor='rgba(255, 255, 255, 0.1)',
    tickfont=dict(color='white'),
)

box_plot_fig = fig