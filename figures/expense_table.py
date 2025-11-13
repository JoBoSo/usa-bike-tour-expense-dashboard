import dataframes as dfs
from dash import dash_table

df = (dfs.expenses).drop(['latitude', 'longitude'])

expense_table = dash_table.DataTable(
    data=(df).to_dicts(),
    style_data={
        'color': 'white',
        'backgroundColor': 'rgb(20, 20, 20)', 
        'border': '1px solid blue'
    },
    style_header={
        'color': 'white',
        'backgroundColor': 'rgb(0, 0, 0)',
        'border': '1px solid pink',
        'position': 'sticky',
        'top': 0,
        'zIndex': 1
    },
    style_table={
        'height': '200px',
        'overflow': 'auto'
    },
    sort_action='native',
)
