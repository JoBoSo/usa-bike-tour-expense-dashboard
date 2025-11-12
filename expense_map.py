import plotly.graph_objects as go
import dataframes as dfs
import numpy as np

df = dfs.expenses.to_pandas()

fig = go.Figure(go.Scattermap(
    lat=df['latitude'],
    lon=df['longitude'],
    mode='markers', # Or 'lines', 'lines+markers'
    marker=dict(
        size=np.maximum(np.log(df['cost_cad'])*2.5, 4), 
        color='#00FFFF',
    ),
    text=df[['store_name', 'cost_cad', 'category']]
        .apply(lambda row: f"{row['store_name']}<br>Cost: ${row['cost_cad']:.2f}<br>Category: {row['category']}", axis=1),
    hoverinfo="text",
))

fig.update_layout(
    title_text='Expense Map',
    width=2000,
    height=450,
    map=dict(
        center=dict(lat=42, lon=-98),
        zoom=3.5,
    ),
    map_style="white-bg",
    map_layers=[
        {
            "below": 'traces',
            "sourcetype": "raster",
            "sourceattribution": "United States Geological Survey",
            "source": [
                "https://server.arcgisonline.com/arcgis/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}" 
            ]
        },
    ],
    margin={"r":0,"t":0,"l":0,"b":0}
)

expense_map_fig = fig
