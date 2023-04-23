from pyspark.sql import SparkSession

# creating spark object
spark = SparkSession.builder.master('local').appName('TEST').getOrCreate()

print("Spark object Created")