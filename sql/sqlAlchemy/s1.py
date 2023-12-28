from sqlalchemy import asc, create_engine, Column, Integer, Numeric, Date, desc, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import date
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

# Define the "Order" class representing the "orders" table
class Order(Base):
    __tablename__ = 'orders'

    ord_no = Column(Integer, primary_key=True)
    purch_amt = Column(Numeric)
    ord_date = Column(Date)
    customer_id = Column(Integer)
    salesman_id = Column(Integer)

try:
    # Create the table in the database
    Base.metadata.create_all(engine)

    # Create a session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()

    # Insert data into the "orders" table
    data_to_insert = [
        (70001, 150.5, date(2012, 10, 5), 3005, 5002),
        (70009, 270.65, date(2012, 9, 10), 3001, 5005),
        (70002, 65.26, date(2012, 10, 5), 3002, 5001),
        (70004, 110.5, date(2012, 8, 17), 3009, 5003),
        (70007, 948.5, date(2012, 9, 10), 3005, 5002),
        (70005, 2400.6, date(2012, 7, 27), 3007, 5001),
        (70008, 5760, date(2012, 9, 10), 3002, 5001),
        (70010, 1983.43, date(2012, 10, 10), 3004, 5006),
        (70003, 2480.4, date(2012, 10, 10), 3009, 5003),
        (70012, 250.45, date(2012, 6, 27), 3008, 5002),
        (70011, 75.29, date(2012, 8, 17), 3003, 5007),
        (70013, 3045.6, date(2012, 4, 25), 3002, 5001)
    ]

    for row in data_to_insert:
        order = Order(ord_no=row[0], purch_amt=row[1], ord_date=row[2], customer_id=row[3], salesman_id=row[4])
        session.add(order)

    session.commit()

    # Perform the first select query
    result1 = (
        session.query(Order.salesman_id, func.max(Order.purch_amt).label('max_purchase'))
        .filter(Order.purch_amt < 2000)
        .group_by(Order.salesman_id)
        .order_by(desc('max_purchase'))
        .limit(5)
        .all()
    )

    print("Result 1:")
    for row in result1:
        print(row)

    # Perform the second select query
   
    result2 = (
        session.query(Order.salesman_id, func.min(Order.purch_amt).label('min_purchase'))
        .filter(Order.purch_amt > 100)
        .group_by(Order.salesman_id)
        .order_by(asc('min_purchase'))  # Order by ascending min_purchase
        .limit(5)
        .all()
    )

    print("Result 2:")
    for row in result2:
        print(row)

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
