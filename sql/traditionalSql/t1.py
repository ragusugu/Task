import psycopg2
from datetime import date

# Database connection parameters
dbname = "sugan"
user = "postgres"
password = "Sugan@123"
host = "localhost"
port = "5432"

try:
    # Establish a connection to the PostgreSQL database
    conn = psycopg2.connect(
        dbname=dbname,
        user=user,
        password=password,
        host=host,
        port=port
    )

    # Create a cursor object to interact with the database
    cursor = conn.cursor()

    # Create the "orders" table
    create_table_query = """
    CREATE TABLE IF NOT EXISTS orders (
        ord_no SERIAL PRIMARY KEY,
        purch_amt NUMERIC,
        ord_date DATE,
        customer_id INT,
        salesman_id INT
    );
    """
    cursor.execute(create_table_query)

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


    # SQL query for inserting data into the "orders" table
    insert_query = """
    INSERT INTO orders (ord_no, purch_amt, ord_date, customer_id, salesman_id) VALUES (%s, %s, %s, %s, %s);
    """

    # Execute the query for each row of data
    for row in data_to_insert:
        cursor.execute(insert_query, row)

    conn.commit()

    select_query = """
SELECT salesman_id, MAX(purch_amt) AS max_purchase
FROM orders
WHERE purch_amt < 2000
GROUP BY salesman_id
ORDER BY max_purchase desc 
LIMIT 5;

    """

    # Execute the query
    cursor.execute(select_query)

    # Fetch all the rows
    rows = cursor.fetchall()
    print("Number of rows fetched:", len(rows))
    # Print the result
    for row in rows:
        print(row)
    
    select_query1 = """
SELECT salesman_id, min(purch_amt) AS min_purchase
FROM orders
WHERE purch_amt > 100
GROUP BY salesman_id
ORDER BY min_purchase asc 
LIMIT 5;

    """

    # Execute the query
    cursor.execute(select_query1)

    # Fetch all the rows
    rows = cursor.fetchall()
    print("Number of rows fetched:", len(rows))
    # Print the result
    for row in rows:
        print(row)

except psycopg2.Error as e:
    print("Error:", e)
    print("Failed to connect to the database.")
else:
    print("Connected to the database successfully.")

finally:
    # Close the cursor and connection in the 'finally' block to ensure it happens regardless of success or failure
    if cursor:
        cursor.close()
    if conn:
        conn.close()
