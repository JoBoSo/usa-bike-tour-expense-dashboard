import pandas as pd
import sqlite3
import os

cur_dir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(cur_dir, "database.sqlite3")

def get_db_connection():
    return sqlite3.connect(db_path)


def get_expenses() -> pd.DataFrame:
    """
    Fetch all expenses sorted by date + time.
    Returns:
        pd.DataFrame
    """
    query = """
        SELECT 
            CAST(day AS INTEGER) AS day,
            CAST(date AS TEXT) AS date,
            CAST(time AS TEXT) AS time,
            COALESCE(cost_cad, 0.0) AS cost_cad,
            COALESCE(category, '') AS category,
            COALESCE(store_name, '') AS store_name,
            COALESCE(store_type, '') AS store_type,
            COALESCE(city, '') AS city,
            COALESCE(state, '') AS state,
            COALESCE(country, '') AS country,
            COALESCE(latitude, 0.0) AS latitude,
            COALESCE(longitude, 0.0) AS longitude
        FROM 
            expenses
        ORDER BY date ASC, time ASC;
    """

    conn = get_db_connection()
    df = pd.read_sql_query(query, conn)
    conn.close()

    # Convert date + time
    df["date"] = pd.to_datetime(df["date"], errors="coerce")
    df["time"] = pd.to_datetime(df["time"], format="%Y-%m-%dT%H:%M:%S", errors="coerce").dt.time

    return df


expenses = get_expenses()


def get_expense_categories() -> pd.DataFrame:
    """
    Get unique categories
    """
    query = "SELECT DISTINCT category FROM expenses"
    conn = get_db_connection()
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df


expense_categories = get_expense_categories()


def get_expense_category_totals() -> pd.DataFrame:
    """
    Group by category and sum cost
    """
    query = """
        SELECT category, SUM(cost_cad) AS total_cost_cad
        FROM expenses
        GROUP BY category;
    """
    conn = get_db_connection()
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df


expense_category_totals = get_expense_category_totals()


def get_store_type_totals() -> pd.DataFrame:
    """
    Group by store type and sum cost
    """
    query = """
        SELECT store_type, SUM(cost_cad) AS total_cost_cad
        FROM expenses
        GROUP BY store_type;
    """
    conn = get_db_connection()
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df


store_type_totals = get_store_type_totals()

# Debug printing if needed
# print(expenses.head())
# print(expense_categories)
# print(expense_category_totals)
# print(store_type_totals)
