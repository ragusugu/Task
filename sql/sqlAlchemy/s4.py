from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Date, Float
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
from urllib.parse import quote
from conn import conn

# Database connection parameters
# dbname = "sugan"
# user = "postgres"
# password = "Sugan@123"
# host = "localhost"
# port = "5432"
# e_password = quote(password)

# # Create an SQLAlchemy engine
# engine = create_engine(f"postgresql+psycopg2://{user}:{e_password}@{host}:{port}/{dbname}", echo=True)
engine=conn()
# Define the SQLAlchemy Base
Base = declarative_base()

# Define the Customer model
class Customer(Base):
    __tablename__ = 'customer'

    customer_id = Column(Integer, primary_key=True)
    cust_name = Column(String(255))
    cust_city = Column(String(255))
    grade = Column(Integer)
    salesman_id = Column(Integer, ForeignKey('salesman.salesman_id'))
    salesman = relationship('Salesman', back_populates='customers')

# Define the Salesman model
class Salesman(Base):
    __tablename__ = 'salesman'

    salesman_id = Column(Integer, primary_key=True)
    name = Column(String(255))
    customers = relationship('Customer', back_populates='salesman')

# Define the Order model
class Order(Base):
    __tablename__ = 'orders'

    ord_no = Column(Integer, primary_key=True)
    ord_date = Column(Date)
    purch_amt = Column(Float)
    customer_id = Column(Integer, ForeignKey('customer.customer_id'))

# Establish a connection to the PostgreSQL database using SQLAlchemy
# engine = create_engine('postgresql://postgres:Sugan@123@localhost:5432/sugan')
Base.metadata.create_all(engine)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# # Insert data into the tables
# insert_data = [
#     (3002, 'Nick Rimando', 'New York', 100, 5001),
#     (3007, 'Brad Davis', 'New York', 200, 5001),
#     (3005, 'Graham Zusi', 'California', 200, 5002),
#     (3008, 'Julian Green', 'London', 300, 5002),
#     (3004, 'Fabian Johnson', 'Paris', 300, 5006),
#     (3009, 'Geoff Cameron', 'Berlin', 100, 5003),
#     (3003, 'Jozy Altidor', 'Moscow', 200, 5007),
#     (3001, 'Brad Guzan', 'London', None, 5005)
# ]

# for item in insert_data:
#     customer = Customer(customer_id=item[0], cust_name=item[1], cust_city=item[2], grade=item[3], salesman_id=item[4])
#     session.merge(customer)

# # Commit the changes
# session.commit()

# Execute the query using SQLAlchemy
query_result = (
    session.query(
        Customer.cust_name,
        Customer.cust_city,
        Customer.grade,
        Salesman.name,
        Order.ord_no,
        Order.ord_date,
        Order.purch_amt
    )
    .outerjoin(Order, Customer.customer_id == Order.customer_id)
    .outerjoin(Salesman, Customer.salesman_id == Salesman.salesman_id)
    .filter(
        (Order.ord_no.is_(None)) |
        ((Order.purch_amt >= 2000) & (Customer.grade.isnot(None)))
    )
).all()

print("Query Result:")
for row in query_result:
    print(row)
# Execute the query using SQLAlchemy
query_result2 = (
    session.query(
        Customer.cust_name,
        Customer.cust_city,
        Order.ord_no,
        Order.ord_date,
        Order.purch_amt
    )
    .outerjoin(Order, Customer.customer_id == Order.customer_id)
    .filter((Customer.grade.isnot(None)) | (Order.customer_id.isnot(None)))
    .all()
)

# Print the result
print("Query Result 2:")
for row in query_result2:
    print(row)

# Close the session
session.close()
