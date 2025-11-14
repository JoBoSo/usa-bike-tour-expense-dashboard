from dash import Dash, dcc, html
from figures.expense_map import expense_map_fig
from figures.expense_table import expense_table
from figures.daily_expense_chart import daily_expense_chart_fig
from figures.category_total_bubble_chart import expense_category_bubble_chart_fig
from figures.store_type_total_bubble_chart import store_type_total_bubble_chart_fig

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

        # Daily Expenses Bar Chart
        html.Div(
            className='daily-expense-chart-container',
            children=[
                html.Div(className='default-fig-title', children='Daily Expenses'),
                html.Div(
                    className='daily-expense-chart',
                    children=dcc.Graph(figure=daily_expense_chart_fig),
                ),
            ]
        ),

        # Expense Category Bubble Chart
        html.Div(
            className='category-bubble-chart-container',
            children=[
                html.Div(className='default-fig-title', children='Total Expenses by Category'),
                html.Div(
                    className='category-bubble-chart',
                    children=dcc.Graph(figure=expense_category_bubble_chart_fig),
                ),
            ]
        ),

        # Expense Map
        html.Div(
            className='expense-map-container',
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
            className='expense-table-container',
            children=[
                html.Div(className='default-fig-title', children='Expenses'),
                html.Div(
                    className='expense-table',
                    children=expense_table,
                ),
            ]
        ),
        
        # html.Div(
        #     style={
        #         'display': 'flex',
        #         'justifyContent': 'center',
        #         'alignItems': 'center', 
        #         'border': '2px solid #000',
        #     },
        #     children=dcc.Graph(figure=store_type_total_bubble_chart_fig),
        # ),

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