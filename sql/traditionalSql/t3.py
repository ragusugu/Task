import psycopg2

dbname = "sugan"
user = "postgres"
password = "Sugan@123"
host = "localhost"
port = "5432"

try:
    # Establish a connection to the PostgreSQL database using psycopg2
    conn = psycopg2.connect(
        dbname=dbname,
        user=user,
        password=password,
        host=host,
        port=port
    )

    # Create a cursor object to interact with the database
    cursor = conn.cursor()

    # Create the table
    sql_create_table = """
         CREATE TABLE employee_history (
             employee_id INT,
             start_date DATE,
             end_date DATE,
             job_id VARCHAR(50),
             department_id INT
         );
         """
    cursor.execute(sql_create_table)

    # Insert data into the table
    insert = """ INSERT INTO employee_history (employee_id, start_date, end_date, job_id, department_id)
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
    cursor.execute(insert)

    # Execute the query using psycopg2
    sql_query = """
        SELECT employee_id
        FROM (
            SELECT employee_id, COUNT(DISTINCT job_id) AS job_count
            FROM employee_history
            GROUP BY employee_id
        ) AS job_counts
        WHERE job_counts.job_count >= 2;
    """
    cursor.execute(sql_query)

    # Fetch and print the result using psycopg2
    print("Employee IDs with more than or equal to two jobs:")
    for row in cursor.fetchall():
        print(row[0])

finally:
    # Close the connections in the 'finally' block to ensure they are always closed
    cursor.close()
    conn.close()
