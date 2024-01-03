from pyspark.sql import SparkSession
from pyspark.sql.functions import length

# Create a Spark session
spark = SparkSession.builder.appName("WordLengthExample").getOrCreate()

file_path = r"C:\Users\HI\Documents\git\sample\Task\pyspark\ds_salaries.csv"
df = spark.read.format("csv").option("header", "true").load(file_path)

# Specify the column containing strings
string_column = "job_title"

# Calculate the number of characters in each word
wordsLengthsDF = df.select(length(string_column).alias('lengths'), string_column)

# Show the result
wordsLengthsDF.show()

