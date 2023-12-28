from sqlalchemy import create_engine, Column, Integer, Date, String, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from urllib.parse import quote
from sqlalchemy import text


# Database connection parameters
dbname = "sugan"
user = "postgres"
password = "Sugan@123"
host = "localhost"
port = "5432"
e_password = quote(password)

# Create an SQLAlchemy engine
engine = create_engine(f"postgresql+psycopg2://{user}:{e_password}@{host}:{port}/{dbname}", echo=True)
# Declare a Base class for models
Base = declarative_base()

# Define the EmployeeHistory model
class EmployeeHistory(Base):
    __tablename__ = "employee_history"
    employee_id = Column(Integer, primary_key=True)
    start_date = Column(Date, primary_key=True)
    end_date = Column(Date)
    job_id = Column(String(50))
    department_id = Column(Integer)

# Create all tables in the engine
Base.metadata.create_all(engine)

# Create a session to interact with the database
Session = sessionmaker(bind=engine)
session = Session()

# Insert data using SQLAlchemy ORM
session.execute(text("""INSERT INTO employee_history (employee_id, start_date, end_date, job_id, department_id)
VALUES
    (102, '2001-01-13', '2006-07-24', 'IT_PROG', 60),
    (101, '1997-09-21', '2001-10-27', 'AC_ACCOUNT', 110),
    (101, '2001-10-28', '2005-03-15', 'AC_MGR', 110),
    (201, '2004-02-17', '2007-12-19', 'MK_REP', 20),
    (114, '2006-03-24', '2007-12-31', 'ST_CLERK', 50),
    (122, '2007-01-01', '2007-12-31', 'ST_CLERK', 50),
    (200, '1995-09-17', '2001-06-17', 'AD_ASST', 90),
    (176, '2006-03-24', '2006-12-31', 'SA_REP', 80),
    (176, '2007-01-01', '2007-12-31', 'SA_MAN', 80),
    (200, '2002-07-01', '2006-12-31', 'AC_ACCOUNT', 90);
"""
))

# Execute the query using SQLAlchemy ORM
result = session.query(EmployeeHistory.employee_id) \
                .group_by(EmployeeHistory.employee_id) \
                .having(func.count(EmployeeHistory.job_id.distinct()) >= 2) \
                .all()

# Print the results
print("Employee IDs with more than or equal to two jobs:")
for row in result:
    print(row.employee_id)

# Close the session
session.close()
