from pyspark.sql import SparkSession

# Create a Spark session
spark = SparkSession.builder.appName("ColumnRenameExample").getOrCreate()
file_path = r"C:\Users\HI\Documents\git\sample\Task\pyspark\ds_salaries.csv"
df = spark.read.format("csv").option("header", "true").load(file_path)
old_column_name = "salary_in_usd"
new_column_name = "USD"

# Rename the column
df = df.withColumnRenamed(old_column_name, new_column_name)

# Show the updated DataFrame
df.show()
