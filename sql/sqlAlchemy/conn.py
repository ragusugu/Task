from urllib.parse import quote
from sqlalchemy import create_engine

def conn():
    # Database connection parameters
    dbname = "sugan"
    user = "postgres"
    password = "Sugan@123"
    host = "localhost"
    port = "5432"
    e_password = quote(password)

    # Create an SQLAlchemy engine
    engine = create_engine(f"postgresql+psycopg2://{user}:{e_password}@{host}:{port}/{dbname}", echo=True)
    return engine
# # C:\Users\HI\Documents\git\sample\Task\sql\conn.py

# def conn():
#     return "Connection successful!"
