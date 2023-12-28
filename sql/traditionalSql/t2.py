import psycopg2

dbname = "sugan"
user = "postgres"
password = "Sugan@123"
host = "localhost"
port = "5432"

# post="hi"
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

    # Create the salesman table if it does not exist
    sql_create_table = '''
        CREATE TABLE IF NOT EXISTS salesman (
            salesman_id INT PRIMARY KEY,
            name VARCHAR(255),
            city VARCHAR(255),
            commission FLOAT
        );
    '''
    cursor.execute(sql_create_table)

    # Insert data into the salesman table
    insert_query = """
        INSERT INTO salesman (salesman_id, name, city, commission)
        VALUES
            (5001, 'James Hoog', 'New York', 0.15),
            (5002, 'Nail Knite', 'Paris', 0.13),
            (5005, 'Pit Alex', 'London', 0.11),
            (5006, 'Mc Lyon', 'Paris', 0.14),
            (5007, 'Paul Adam', 'Rome', 0.13),
            (5003, 'Lauson Hen', 'San Jose', 0.12);
    """
    cursor.execute(insert_query)

    # Execute the first query
    query1 = """
        SELECT salesman_id, name, city, commission
        FROM salesman
        WHERE commission BETWEEN 0.10 AND 0.12;
    """
    cursor.execute(query1)
    result1 = cursor.fetchall()
    print("Query 1 Result:")
    for row in result1:
        print(row)

    # Execute the second query
    query2 = """
        SELECT AVG(commission) AS avg_commission
        FROM salesman
        WHERE commission BETWEEN 0.12 AND 0.14;
    """
    cursor.execute(query2)
    result2 = cursor.fetchall()
    print("\nQuery 2 Result:")
    for row in result2:
        print(row)

    # Commit the changes and close the connection
    conn.commit()
finally:
    # Close the connection in the 'finally' block to ensure it's always closed
    conn.close()
