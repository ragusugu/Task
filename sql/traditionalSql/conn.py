import psycopg2
from urllib.parse import quote

def conn():
    # Database connection parameters
    dbname = "sugan"
    user = "postgres"
    password = "Sugan@123"
    host = "localhost"
    port = "5432"

    # Connect to the PostgreSQL database
    connection = psycopg2.connect(
        dbname=dbname,
        user=user,
        password=password,
        host=host,
        port=port
    )

    return connection