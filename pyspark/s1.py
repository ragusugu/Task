# from audioop import avg
from audioop import avg
from statistics import stdev
from pyspark.sql import SparkSession

# Set your GCS bucket name and credentials file path
gcs_bucket_name = "saturam_test"
gcs_credentials_file = r"C:\Users\HI\Documents\git\sample\Task\task-data-404610-6c0225e1a962 (1).json"

# Create a Spark session with GCS configurations
spark = SparkSession.builder \
    .appName("sugan") \
    .config("spark.jars.packages", "com.google.cloud.spark:spark-bigquery-with-dependencies_2.12:0.20.0") \
    .config("spark.hadoop.google.cloud.auth.service.account.json.keyfile", gcs_credentials_file) \
    .getOrCreate()

# Read data from GCS into a PySpark DataFrame
gcs_path = "gs://{}/path/to/your/data".format(gcs_bucket_name)
df = spark.read.csv(gcs_path, header=True, inferSchema=True)

# Display the DataFrame schema
# df.printSchema()
try:
    df = spark.read.text(gcs_path)
    print("Connected to GCP successfully!")
except Exception as e:
    print("Failed to connect to GCP. Error:", str(e))
finally:
# Perform computation on the integer column (replace 'integer_column' with your actual column name)
# result = df.select(
#     avg("salary").alias("avg_integer_column"),
#     stdev("integer_column").alias("stddev_integer_column")
# )

# Show the result
# result.show()

# Stop the Spark session
 spark.stop()
