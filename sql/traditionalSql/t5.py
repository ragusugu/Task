# import psycopg2
# from psycopg2 import sql
from conn import conn

con=conn()
# Create a cursor object to execute SQL queries
cursor = con.cursor()

# Create the employee table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS employee (
        emp_idno SERIAL PRIMARY KEY,
        emp_fname VARCHAR(255),
        emp_lname VARCHAR(255),
        emp_dept INT
    )
""")

# Create the department table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS department (
        dpt_code SERIAL PRIMARY KEY,
        dpt_name VARCHAR(255),
        dpt_allotment INT
    )
""")

# Insert data into the employee table
cursor.execute("""
    INSERT INTO employee (emp_idno, emp_fname, emp_lname, emp_dept)
VALUES
    (127323, 'Michale', 'Robbin', 57),
    (526689, 'Carlos', 'Snares', 63),
    (843795, 'Enric', 'Dosio', 57),
    (328717, 'Jhon', 'Snares', 63),
    (444527, 'Joseph', 'Dosni', 47),
    (659831, 'Zanifer', 'Emily', 47),
    (847674, 'Kuleswar', 'Sitaraman', 57),
    (748681, 'Henrey', 'Gabriel', 47),
    (555935, 'Alex', 'Manuel', 57),
    (539569, 'George', 'Mardy', 27),
    (733843, 'Mario', 'Saule', 63),
    (631548, 'Alan', 'Snappy', 27),
    (839139, 'Maria', 'Foster', 57);
""")

# Insert data into the department table
cursor.execute("""
INSERT INTO department (dpt_code, dpt_name, dpt_allotment)
VALUES
    (57, 'IT', 65000),
    (63, 'Finance', 15000),
    (47, 'HR', 240000),
    (27, 'RD', 55000),
    (89, 'QC', 75000);
""")
# Define and execute query1
query1 = """
SELECT emp_fname, emp_lname
FROM employee
WHERE emp_dept IN (
    SELECT dpt_code
    FROM department
    WHERE dpt_allotment > 50000
);
"""
cursor.execute(query1)
result1 = cursor.fetchall()
print("Query Result 1:")
for row in result1:
 print(row)

query2 = """
SELECT emp_fname, emp_lname
FROM employee
WHERE emp_dept = (
    SELECT dpt_code
    FROM department
    ORDER BY dpt_allotment
    LIMIT 1 OFFSET 1
);
"""
cursor.execute(query2)
result2 = cursor.fetchall()
print("Query Result 1:")
for row in result2:
  print(row)

# Commit the changes
con.commit()

# Close the cursor and connection
cursor.close()
con.close()
