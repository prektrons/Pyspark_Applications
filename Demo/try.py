from pyspark.sql import SparkSession

# creating spark object
spark = SparkSession.builder.master('local').appName('TEST').getOrCreate()

print("Spark object Created")

# SparkContext is the entry point to any spark functionality. pyspark.SparkContext is an entry point to the PySpark
# functionality that is used to communicate with the cluster and to create an RDD, accumulator, and broadcast variables

# Parallelizing the spark application distributes the data across the multiple nodes and is used to process the data
# in the Spark ecosystem.
rdd = spark.sparkContext.parallelize([1, 2, 3])
print(rdd.first())
