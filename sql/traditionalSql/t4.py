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

    # Create the table (if not exists)
    sql_create_table = """
    CREATE TABLE IF NOT EXISTS customer (
        customer_id INT PRIMARY KEY,
        cust_name VARCHAR(255),
        cust_city VARCHAR(255),
        grade INT,
        salesman_id INT
    );
    """
    cursor.execute(sql_create_table)

    # Insert data into the table (if not exists)
    insert_data = """
    INSERT INTO customer (customer_id, cust_name, cust_city, grade, salesman_id)
    VALUES
        (3002, 'Nick Rimando', 'New York', 100, 5001),
        (3007, 'Brad Davis', 'New York', 200, 5001),
        (3005, 'Graham Zusi', 'California', 200, 5002),
        (3008, 'Julian Green', 'London', 300, 5002),
        (3004, 'Fabian Johnson', 'Paris', 300, 5006),
        (3009, 'Geoff Cameron', 'Berlin', 100, 5003),
        (3003, 'Jozy Altidor', 'Moscow', 200, 5007),
        (3001, 'Brad Guzan', 'London', NULL, 5005)
    ON CONFLICT (customer_id) DO NOTHING;
    """
    cursor.execute(insert_data)
    conn.commit()

    # Execute the query using psycopg2
    sql_query = """
    SELECT
        c.cust_name,
        c.cust_city,
        c.grade,
        s.name,
        o.ord_no,
        o.ord_date,
        o.purch_amt
    FROM
        customer c
    LEFT JOIN
        orders o ON c.customer_id = o.customer_id
    LEFT JOIN
        salesman s ON c.salesman_id = s.salesman_id
    WHERE
        (
            o.ord_no IS NULL OR
            (o.purch_amt >= 2000 AND c.grade IS NOT NULL)
        );
    """
    cursor.execute(sql_query)
    query_result = cursor.fetchall()
    print("Query Result 1:")
    for row in query_result:
        print(row)

    # Execute the query using psycopg2
    sql_query1 = """select c.cust_name,c.cust_city, o.ord_no, o.ord_date, o.purch_amt
    from customer c
    full outer join orders o 
    on c.customer_id = o.customer_id
    where c.grade IS NOT NULL OR o.customer_id IS NOT NULL;
  """
    cursor.execute(sql_query1)
    query_result1 = cursor.fetchall()
    print("Query Result 2:")
    for row in query_result1:
        print(row)
        
except psycopg2.Error as e:
    print("Error:", e)
    print("Failed to connect to the database.")
else:
    print("Connected to the database successfully.")

finally:
    # Close the connections in the 'finally' block to ensure they are always closed
    cursor.close()
    conn.close()
