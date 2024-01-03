from pyspark.sql import SparkSession
from pyspark.sql.functions import col
from pyspark.sql.types import FloatType

# Create a Spark session
spark = SparkSession.builder.appName("NumericColumnStats").getOrCreate()

# Read your CSV file into a DataFrame
file_path = r"C:\Users\HI\Documents\git\sample\Task\pyspark\ds_salaries.csv"
df = spark.read.format("csv").option("header", "true").load(file_path)
numeric_column = "salary"

# Convert the StringType column to FloatType
df = df.withColumn(numeric_column, col(numeric_column).cast(FloatType()))

# Calculate summary statistics using approxQuantile
quantiles = df.stat.approxQuantile(numeric_column, [0.0, 0.25, 0.5, 0.75, 1.0], 0.01)

# Extract the values for each quantile
min_value, q25, median, q75, max_value = quantiles

# Display the results
print(f"Min: {min_value}")
print(f"25th Percentile: {q25}")
print(f"Median: {median}")
print(f"75th Percentile: {q75}")
print(f"Max: {max_value}")
