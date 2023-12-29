from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from conn import conn

engine=conn()
# Define the database connection
# DATABASE_URL = "postgresql://username:password@localhost/dbname"
# engine = create_engine(DATABASE_URL, echo=True)

# Define the database models
Base = declarative_base()

class Employee(Base):
    __tablename__ = 'employee'
    emp_idno = Column(Integer, primary_key=True)
    emp_fname = Column(String(255))
    emp_lname = Column(String(255))
    emp_dept = Column(Integer, ForeignKey('department.dpt_code'))
    department = relationship("Department", back_populates="employees")

class Department(Base):
    __tablename__ = 'department'
    dpt_code = Column(Integer, primary_key=True)
    dpt_name = Column(String(255))
    dpt_allotment = Column(Integer)
    employees = relationship("Employee", back_populates="department")

# Create tables
Base.metadata.create_all(bind=engine)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Insert data into the employee and department tables
employee_data = [
    {'emp_idno': 127323, 'emp_fname': 'Michale', 'emp_lname': 'Robbin', 'emp_dept': 57},
    {'emp_idno': 526689, 'emp_fname': 'Carlos', 'emp_lname': 'Snares', 'emp_dept': 63},
    {'emp_idno': 843795, 'emp_fname': 'Enric', 'emp_lname': 'Dosio', 'emp_dept': 57},
    {'emp_idno': 328717, 'emp_fname': 'Jhon', 'emp_lname': 'Snares', 'emp_dept': 63},
    {'emp_idno': 444527, 'emp_fname': 'Joseph', 'emp_lname': 'Dosni', 'emp_dept': 47},
    {'emp_idno': 659831, 'emp_fname': 'Zanifer', 'emp_lname': 'Emily', 'emp_dept': 47},
    {'emp_idno': 847674, 'emp_fname': 'Kuleswar', 'emp_lname': 'Sitaraman', 'emp_dept': 57},
    {'emp_idno': 748681, 'emp_fname': 'Henrey', 'emp_lname': 'Gabriel', 'emp_dept': 47},
    {'emp_idno': 555935, 'emp_fname': 'Alex', 'emp_lname': 'Manuel', 'emp_dept': 57},
    {'emp_idno': 539569, 'emp_fname': 'George', 'emp_lname': 'Mardy', 'emp_dept': 27},
    {'emp_idno': 733843, 'emp_fname': 'Mario', 'emp_lname': 'Saule', 'emp_dept': 63},
    {'emp_idno': 631548, 'emp_fname': 'Alan', 'emp_lname': 'Snappy', 'emp_dept': 27},
    {'emp_idno': 839139, 'emp_fname': 'Maria', 'emp_lname': 'Foster', 'emp_dept': 57}
]

department_data = [
    {'dpt_code': 57, 'dpt_name': 'IT', 'dpt_allotment': 65000},
    {'dpt_code': 63, 'dpt_name': 'Finance', 'dpt_allotment': 15000},
    {'dpt_code': 47, 'dpt_name': 'HR', 'dpt_allotment': 240000},
    {'dpt_code': 27, 'dpt_name': 'RD', 'dpt_allotment': 55000},
    {'dpt_code': 89, 'dpt_name': 'QC', 'dpt_allotment': 75000}
]

# session.bulk_insert_mappings(Employee, employee_data)
# session.bulk_insert_mappings(Department, department_data)
# session.commit()
# Insert data into the employee and department tables using add() method
for emp_data in employee_data:
    employee = Employee(**emp_data)
    session.add(employee)

for dept_data in department_data:
    department = Department(**dept_data)
    session.add(department)

# Commit the changes
session.commit()



# Define and execute query1 using SQLAlchemy
query1 = session.query(Employee.emp_fname, Employee.emp_lname).filter(
    Employee.emp_dept.in_(
        session.query(Department.dpt_code).filter(Department.dpt_allotment > 50000)
    )
).all()

print("Query Result 1:")
for row in query1:
    print(row)

# Define and execute query2 using SQLAlchemy
query2 = session.query(Employee.emp_fname, Employee.emp_lname).filter(
    Employee.emp_dept == (
        session.query(Department.dpt_code).order_by(Department.dpt_allotment).offset(1).limit(1).scalar()
    )
).all()

print("Query Result 2:")
for row in query2:
    print(row)

# Close the session
session.close()
