import polars as pl
import plotly.graph_objects as go
import dataframes as dfs 

df=dfs.expenses

# totals
total_spend=df.select(pl.col("cost_cad").sum()).item()
num_days=df.select(pl.col("day").max()).item()
num_purchases=df.height

# daily avgs
avg_daily_spend=total_spend/num_days
avg_num_purchases=num_purchases/num_days

# 100 km avgs
# avg_spend_per_100km=total_spend/4737*100
# avg_purchases_per_100km=num_purchases/4737*100

def create_indicator(value, prefix="", suffix="", title="", decimals=0):
    fig = go.Figure()

    fig.add_trace(go.Indicator(
        mode = "number",
        value = value,
        number = {
            'prefix': prefix, 
            'suffix': suffix, 
            'valueformat': f',.{decimals}f',
            'font': {
                'family': "Poppins",
                'size': 16,
                'color': "white",
            },
        },
        domain = {'x': [0, 1], 'y': [0, 0.6]},
    ))

    fig.update_layout(
        title={
            'text': title, 
            'x':0.5, 
            'xanchor': 'center', 
            'y': 0.7,
            'yanchor': 'middle', 
            'font': {'weight': "bold", "size": 16}
        },
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(
            family="Poppins",
            size=16,
            color="white",
        ),
        width=130,
        height=55,
        margin=dict(l=0, r=0, t=0, b=0),
    )

    return fig

num_days_ind_fig = create_indicator(num_days, prefix="", suffix="", title="Days")
total_distance_ind_fig = create_indicator(4737, prefix="", suffix=" km", title="Distance")
total_spend_ind_fig = create_indicator(total_spend, prefix="$", suffix=" CAD", title="Cost")
num_purchases_ind_fig = create_indicator(num_purchases, prefix="", suffix="", title="Purchases")
avg_daily_distance_ind_fig = create_indicator(4737/num_days, prefix="", suffix=" km", title="Distance/Day")
avg_daily_spend_ind_fig = create_indicator(avg_daily_spend, prefix="$", suffix=" CAD", title="Cost/Day")
avg_daily_purchases_ind_fig = create_indicator(avg_num_purchases, prefix="", suffix="", title="Purchases/Day", decimals=1)
