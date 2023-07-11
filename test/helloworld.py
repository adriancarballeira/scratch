import sys

from pyspark.sql import SparkSession


if __name__ == "__main__":
    """
        Usage: helloworld
    """
    spark = SparkSession\
        .builder\
        .appName("helloworld")\
        .getOrCreate()

    print("hello world")

    spark.stop()