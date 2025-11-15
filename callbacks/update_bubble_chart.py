from dash import Output, Input, callback, callback_context
from figures.total_spend_bubble_chart import expense_category_bubble_chart_fig
import dataframes as dfs

@callback(
    Output("category-bubble-chart", "figure"),
    Output("btn-category", "className"),
    Output("btn-store-type", "className"),
    Input("btn-category", "n_clicks"),
    Input("btn-store-type", "n_clicks"),
)
def update_bubble_chart(n_cat, n_store):
    ctx = callback_context

    # Determine active tab
    if not ctx.triggered:
        active = "category"
    else:
        clicked = ctx.triggered[0]["prop_id"].split(".")[0]
        active = "category" if clicked == "btn-category" else "store_type"

    # Select the correct dataset and label
    if active == "category":
        df = dfs.expense_category_totals
        label = "category"
    else:
        df = dfs.store_type_totals
        label = "store_type"

    fig = expense_category_bubble_chart_fig(df=df, label=label)

    # Active button styling
    cat_class = "bubble-chart-btn active" if active == "category" else "bubble-chart-btn"
    store_class = "bubble-chart-btn active" if active == "store_type" else "bubble-chart-btn"

    return fig, cat_class, store_class