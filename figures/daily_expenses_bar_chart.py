import plotly.graph_objects as go
import dataframes as dfs
import numpy as np

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

daily_total_df = df.groupby('day', as_index=False)['cost_cad'].sum().sort_values('day')

fig.add_trace(go.Scatter(
    x=daily_total_df['day'],
    y=np.cumsum(daily_total_df['cost_cad']), 
    mode='lines+markers',
    name='Cumulative Line',
    line=dict(color='red', width=2),
    marker=dict(size=8, color='red'),
    yaxis='y2' ,
))

# Update layout for stacked bars
fig.update_layout(
    barmode='stack', 
    margin=dict(l=0, r=0, t=0, b=0),
    xaxis_title='Day',
    yaxis_title='Daily Cost (CAD)',
    paper_bgcolor='rgba(0,0,0,0)', 
    plot_bgcolor='rgba(0,0,0,0)',
    font_color='white',
    font_family='Poppins',
    width=1150,
    xaxis=dict(
        tickmode='array',
        tickvals=list(range(1, df['day'].max()+1)),
        ticktext=[str(i) for i in range(1, df['day'].max()+1)],
        fixedrange=True,  # Disable panning/zooming on the x-axis
        range=[df['day'].min()-0.5, df['day'].max()+0.5],   
    ),
    yaxis=dict(
        tickmode='array',
        tickvals=list(range(0, int(daily_total_df['cost_cad'].max()), 50)) + [int(daily_total_df['cost_cad'].max())-(int(daily_total_df['cost_cad'].max())%50)+50],
        range=[0, int(daily_total_df['cost_cad'].max())+(int(daily_total_df['cost_cad'].max())%50)],
        fixedrange=True,  # Disable panning/zooming on the y-axis
    ),
    yaxis2=dict(
        title='Cumulative Cost (CAD)',
        overlaying='y',
        side='right',
        showgrid=False,
        fixedrange=True,  # Disable panning/zooming on the y-axis
        tickvals=list(range(0, int(daily_total_df['cost_cad'].sum()), 500)) + [int(daily_total_df['cost_cad'].sum())-(int(daily_total_df['cost_cad'].sum())%500)+500],
        range=[0, int(daily_total_df['cost_cad'].sum())+(int(daily_total_df['cost_cad'].sum())%500)],
    ),
    legend=dict(
        x=1.08,  # x-coordinate (e.g., 1.1 places it to the right of the plot)
        y=1,    # y-coordinate (e.g., 1 places it at the top)
        xanchor="left", # Which part of the legend box anchors to the x-coordinate
        yanchor="top"   # Which part of the legend box anchors to the y-coordinate
    ),
    dragmode='pan',
)

daily_expenses_bar_chart_fig = fig
