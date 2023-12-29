from flask import Flask
from urllib.parse import quote
from sqlalchemy import create_engine

def create_app():
    app = Flask(__name__)

    # Database connection parameters
    dbname = "sugan"
    user = "postgres"
    password = "Sugan@123"
    host = "localhost"
    port = "5432"
    e_password = quote(password)

    # Create an SQLAlchemy engine
    app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql+psycopg2://{user}:{e_password}@{host}:{port}/{dbname}"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    return app
