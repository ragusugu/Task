from flask import session
from numpy import row_stack
from sqlalchemy import Float, create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from urllib.parse import quote

# Database connection parameters
dbname = "sugan"
user = "postgres"
password = "Sugan@123"
host = "localhost"
port = "5432"
e_password = quote(password)

# Create an SQLAlchemy engine
engine = create_engine(f"postgresql+psycopg2://{user}:{e_password}@{host}:{port}/{dbname}", echo=True)

# Create an SQLAlchemy base class
Base = declarative_base()

class Salesman(Base):
    __tablename__ = 'salesman'

    salesman_id = Column(Integer, primary_key=True)
    name = Column(String(255))
    city = Column(String(255))
    commission = Column(Float)

try:
    # Create the table in the database
    Base.metadata.create_all(engine)

    # Create a session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()

    # Truncate the table before inserting data
    Salesman.__table__.drop(engine, checkfirst=True)
    Base.metadata.create_all(engine)

    # Insert data into the salesman table
    salesmen_data = [
        (5001, 'James Hoog', 'New York', 0.15),
        (5002, 'Nail Knite', 'Paris', 0.13),
        (5005, 'Pit Alex', 'London', 0.11),
        (5006, 'Mc Lyon', 'Paris', 0.14),
        (5007, 'Paul Adam', 'Rome', 0.13),
        (5003, 'Lauson Hen', 'San Jose', 0.12)
    ]

    for data in salesmen_data:
        salesman = Salesman(salesman_id=data[0], name=data[1], city=data[2], commission=data[3])
        session.add(salesman)
    session.commit()
    
    # Execute the first query
    query1_result = session.query(Salesman).filter(Salesman.commission.between(0.10, 0.12)).all()
    print("Query 1 Result:")
    for row in query1_result:
        print(row.salesman_id, row.name, row.city, row.commission)

    # Execute the second query
    query2_result = session.query(Salesman).filter(Salesman.commission.between(0.12, 0.14)).\
        with_entities(Salesman.commission).all()
    average_commission = sum(row.commission for row in query2_result) / len(query2_result)
    print("\nQuery 2 Result:")
    print("Average Commission:", average_commission)

except Exception as e:
    print("Error:", e)
    print("Failed to connect to the database.")
    # Rollback the changes in case of an exception
    session.rollback()
else:
    print("Connected to the database successfully.")

finally:
    # Close the session in the 'finally' block to ensure it happens regardless of success or failure
    if session:
        session.close()
