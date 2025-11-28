from dash import Dash, dcc, html
from figures.expense_map import expense_map_fig
from figures.expense_table import expense_table
from figures.daily_expense_chart import daily_expense_chart_fig
from figures.total_spend_bubble_chart import expense_category_bubble_chart_fig
from figures.indicators import (
    num_days_ind_fig, total_distance_ind_fig, total_spend_ind_fig, 
    avg_daily_spend_ind_fig, num_purchases_ind_fig, avg_daily_distance_ind_fig, 
    avg_daily_purchases_ind_fig
)
from figures.histogram import histogram_fig
from figures.box_plot import box_plot_fig
import callbacks # required for access to callbacks

app = Dash()

app.layout = html.Div(
    className='dashboard',
    children=[

        html.Div(
            className='dashboard-title',
            children='Western USA Bike Tour Expenses Dashboard'
        ),

        html.Div(
            className='explanation',
            children='I biked 4,737 kilometers from the Rocky Mountains to the Sonoran Desert across in 39 days. This dashboard visualizes my expenses along the way.'
        ),

        html.Div(
            className='default-fig-parent-container',
            children=[
                html.Div(
                    className='default-fig-container',
                    children=[
                        dcc.Graph(className='indicator', figure=num_days_ind_fig),
                        dcc.Graph(className='indicator', figure=total_distance_ind_fig),
                        dcc.Graph(className='indicator', figure=avg_daily_distance_ind_fig),
                        dcc.Graph(className='indicator', figure=total_spend_ind_fig),
                        dcc.Graph(className='indicator', figure=avg_daily_spend_ind_fig),
                        dcc.Graph(className='indicator', figure=num_purchases_ind_fig),
                        dcc.Graph(className='indicator', figure=avg_daily_purchases_ind_fig),
                    ]
                ),
            ],
        ),

        # Daily Expenses Bar Chart
        html.Div(
            className='default-fig-parent-container',
            children=[
                html.Div(className='default-fig-title', children='Daily Expenses'),
                html.Div(
                    className='default-fig-container',
                    children=dcc.Graph(figure=daily_expense_chart_fig),
                ),
            ]
        ),

        # Expense Category Bubble Chart
        html.Div(
            className='default-fig-parent-container',
            children=[
                html.Div(className='default-fig-title', children='Total Spend'),
                html.Div(
                    style={
                        "display": "flex",
                        "gap": "10px",
                        "justifyContent": "center",
                        "marginBottom": "10px"
                    },
                    children=[
                        html.Button("Expense Category", id="btn-category", n_clicks=0, className='bubble-chart-btn'),
                        html.Button("Store Type", id="btn-store-type", n_clicks=0, className='bubble-chart-btn'),
                    ]
                ),
                html.Div(
                    className='category-bubble-chart',
                    children=dcc.Graph(
                        id='category-bubble-chart', 
                        figure=expense_category_bubble_chart_fig(label='category')  # initial chart
                    ),
                ),
            ]
        ),

        # Histogram
        html.Div(
            className='default-fig-parent-container',
            children=[
                html.Div(className='default-fig-title', children='Distribution of Purchase Amounts'),
                html.Div(
                    className='default-fig-container',
                    children=dcc.Graph(figure=histogram_fig),
                )
            ]
        ),

        # Box Plot
        html.Div(
            className='default-fig-parent-container',
            children=[
                html.Div(className='default-fig-title', children='Shape of Purchase Amounts by Category (n≥5)'),
                html.Div(
                    className='default-fig-container',
                    children=dcc.Graph(figure=box_plot_fig),
                )
            ]
        ),

        # Expense Map
        html.Div(
            className='default-fig-parent-container',
            children=[
                html.Div(className='default-fig-title', children='Expense Map'),
                html.Div(
                    className='expense-map',
                    children=dcc.Graph(figure=expense_map_fig),
                )
            ]
        ),

        # Expense Table
        html.Div(
            className='default-fig-parent-container',
            children=[
                html.Div(className='default-fig-title', children='Expenses'),
                html.Div(
                    className='expense-table',
                    children=expense_table,
                ),
            ]
        ),

        html.Div(
            className='footer-container',
            children=html.A(
                'Visit my website bigmoneybiking.com', 
                href='https://www.bigmoneybiking.com', target='_blank'
            )
        )
        
    ]
)

if __name__ == '__main__':
    app.run(debug=True)