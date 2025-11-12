import polars as pl
import os

cur_dir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(cur_dir, "database.sqlite3")
uri = f"sqlite:///{db_path}"

def get_expenses(uri: str) -> pl.DataFrame:
    """
    Fetch all expenses from the expenses table.
    Args:
        uri (str): URI for the SQLite database.
    Returns:
        pl.DataFrame: DataFrame containing all expenses.
    """
    query = """
        SELECT 
            CAST(date AS TEXT) AS date,
            CAST(time AS TEXT) AS time,
            COALESCE(CAST(cost_cad AS REAL), 0.0) AS cost_cad,
            COALESCE(CAST(category AS TEXT), '') AS category,
            COALESCE(CAST(store_name AS TEXT), '') AS store_name,
            COALESCE(CAST(store_type AS TEXT), '') AS store_type,
            COALESCE(CAST(city AS TEXT), '') AS city,
            COALESCE(CAST(state AS TEXT), '') AS state,
            COALESCE(CAST(country AS TEXT), '') AS country,
            COALESCE(CAST(latitude AS REAL), 0.0) AS latitude,
            COALESCE(CAST(longitude AS REAL), 0.0) AS longitude
        FROM 
            expenses
        order by date asc, time asc
        ;
    """

    df = pl.read_database_uri(
        query=query, 
        uri=uri, 
        schema_overrides={
            "date": pl.Date,
            "time": pl.Time,
            "cost_cad": pl.Float64,
            "category": pl.String,
            "store_name": pl.String,
            "store_type": pl.String,
            "city": pl.String,
            "state": pl.String,
            "country": pl.String,
            "latitude": pl.Float64,
            "longitude": pl.Float64
            }
    )
    
    return df

expenses = get_expenses(uri)


def get_expense_categories(uri: str) -> pl.DataFrame:
    """
    Fetch distinct expense categories from the expenses table.
    Args:
        uri (str): URI for the SQLite database. 
    Returns:
        pl.DataFrame: DataFrame containing distinct expense categories.
    """
    query = "SELECT DISTINCT category FROM expenses"
    df = pl.read_database_uri(query, uri)
    return df

expense_categories = get_expense_categories(uri)


def get_expense_category_totals(uri: str) -> pl.DataFrame:
    """
    Fetch distinct expense categories from the expenses table.
    Args:
        uri (str): URI for the SQLite database. 
    Returns:
        pl.DataFrame: DataFrame containing distinct expense categories.
    """
    query = "SELECT category, sum(cost_cad) as total_cost_cad FROM expenses GROUP BY category"
    df = pl.read_database_uri(query, uri)
    return df

expense_category_totals = get_expense_category_totals(uri)


def get_store_type_totals(uri: str) -> pl.DataFrame:
    """
    Fetch distinct store types and their total expenses from the expenses table.
    Args:
        uri (str): URI for the SQLite database.
    Returns:
        pl.DataFrame: DataFrame containing distinct store types and their total expenses.
    """
    query = "SELECT store_type, sum(cost_cad) as total_cost_cad FROM expenses GROUP BY store_type"
    df = pl.read_database_uri(query, uri)
    return df

store_type_totals = get_store_type_totals(uri)


with pl.Config(
    tbl_rows=-1, 
    tbl_cols=-1, 
    fmt_str_lengths=1000, 
    tbl_width_chars=1000
):
    pass
#     print(expense_categories)

# print(expenses)