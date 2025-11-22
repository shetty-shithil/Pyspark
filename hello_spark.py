from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("hello") \
    .getOrCreate()

df = spark.range(0, 5)
df.show()

spark.stop()