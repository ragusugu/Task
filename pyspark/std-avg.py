from pyspark.sql import SparkSession
from pyspark.sql.functions import stddev, avg

spark = SparkSession.builder.appName("IntColumnStats").getOrCreate()
file_path = r"C:\Users\HI\Documents\git\sample\Task\pyspark\ds_salaries.csv"
column = "salary"

# Read CSV file into a DataFrame
df = spark.read.format("csv").option("header", "true").load(file_path)
df.printSchema()

# Correct the column casting
df = df.withColumn("salary", df.salary.cast('int'))

# Calculate stddev and avg
result = df.agg(stddev(column).alias("std"), avg(column).alias("avg"))

# Show the result
result.show()
