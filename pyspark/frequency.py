from pyspark.sql import SparkSession
from pyspark.sql.functions import col

# Create a Spark session
spark = SparkSession.builder.appName("TopStringFreq").getOrCreate()
file_path = r"C:\Users\HI\Documents\git\sample\Task\pyspark\ds_salaries.csv"
df = spark.read.format("csv").option("header", "true").load(file_path)
string_column = "employment_type"

# Group by the string column and count occurrences
frequency_df = df.groupBy(string_column).count()

# Order by count in descending order and select the top 5
top_5_frequency = frequency_df.orderBy(col("count").desc()).limit(5)

# Show the result
top_5_frequency.show()