# Module 3: Spark SQL

The most convenient method to use Spark is via Spark SQL.

In this lecture, I am going to create a Spark SQL example.

This example will help you understand How to use Spark SQL inside your PySpark application.

I have created the below code:

```
import sys
from pyspark.sql import SparkSession
from lib.logger import Log4j

if __name__ == "__main__":
    spark = SparkSession \
        .builder \
        .master("local[3]") \
        .appName("HelloSparkSQL") \
        .getOrCreate()

    logger = Log4j(spark)

    if len(sys.argv) != 2:
        logger.error("Usage: HelloSpark <filename>")
        sys.exit(-1)

    surveyDF = spark.read \
        .option("header", "true") \
        .option("inferSchema", "true") \
        .csv(sys.argv[1])
```
You can execute SQL expression only on a table or view.
Spark allows you to register your DataFrame as a View.

We start with the DataFrame and createOrReplaceTempView. Supply the view name:

```
surveyDF.createOrReplaceTempView("survey_tbl")
```

That's all. Now you have a view, and you can execute your SQL expressions against this view.

```
countDF = spark.sql("select Country, count(1) as count from survey_tbl where Age<40 group by Country")
```
The SQL() method takes your Spark SQL expression and returns a DataFrame.And the best part, Spark SQL, is as performant as the DataFrames.
So, using SQL, you are not going to pay any additional performance cost.
