import plotly.graph_objects as go
import pandas as pd
import dataframes as dfs

df = dfs.expenses.to_pandas()

fig = go.Figure()

# Get unique categories for coloring
unique_categories = df['category'].unique()

# Add a trace for each category
for category in unique_categories:
    df_filtered = df[df['category'] == category]
    fig.add_trace(go.Bar(
        x=df_filtered['day'],
        y=df_filtered['cost_cad'],
        name=category,
        customdata=df_filtered[['store_name', 'category']],
        hovertemplate='<b>%{customdata[0]}</b><br>'
            +'%{customdata[1]}<br>$%{y:.2f}<extra></extra>',
    ))

# Update layout for stacked bars
fig.update_layout(
    barmode='stack', 
    margin=dict(l=0, r=0, t=0, b=0),
    xaxis_title='Day',
    yaxis_title='Cost (CAD)',
    paper_bgcolor='rgba(0,0,0,0)', 
    plot_bgcolor='rgba(0,0,0,0)',
    font_color='white',
    font_family='Poppins',
    width=1100,
    xaxis=dict(
        dtick='D1' # Show a tick for every day
    ),
)

daily_expenses_bar_chart_fig = fig
