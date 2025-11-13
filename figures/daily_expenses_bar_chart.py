import plotly.express as px
import dataframes as dfs

fig = px.bar(
    dfs.expenses, 
    x="date", 
    y="cost_cad", 
    color="category",
    hover_name="store_name",
    width=1230,
    template='plotly_dark',
)

daily_expenses_bar_chart_fig = fig