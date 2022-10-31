from pyspark.sql import SparkSession
from pyspark.sql.types import *
from pyspark.sql.functions import *
from pyspark.sql.types import *

if __name__ == "__main__":
    spark = SparkSession.builder \
        .master("local[3]") \
        .appName("MyApp") \
        .getOrCreate()


#Seems this is a list of tuples
data_list = [("Ravi", "28", "1", "2002"),
             ("Abdul", "23", "5", "81"),  # 1981
             ("John", "12", "12", "6"),  # 2006
             ("Rosy", "7", "8", "63"),  # 1963
             ("Abdul", "23", "5", "81")]  # 1981
columns = ("Name", "Day", "Month", "Year")
df = spark.createDataFrame(data_list, columns)
# spark.createDataFrame(data_list).toDF("name", "day", "month", "year").repartition(3)
df.printSchema()

df2 = df.withColumn("ID", monotonically_increasing_id()) \
    .withColumn("Day", col("Day").cast(IntegerType())) \
    .withColumn("Month", col("Month").cast(IntegerType())) \
    .withColumn("Year", col("Year").cast(IntegerType())) \
    .withColumn("Year", expr("CASE WHEN Year < 21 THEN Year + 2000 WHEN Year < 100 THEN Year + 1900 ELSE Year END")) \
    .withColumn("DOB", expr("to_date(concat(Day,'/',Month,'/',Year),'d/M/y')")) \
    .drop("Day","Month","Year")\
    .dropDuplicates(["Name","DOB"])\
    .sort(desc("DOB")) #Works!
    #.sort(col("dob").desc()) Works!
    #.sort(expr("DOB desc")) Doesn't work


df2.show()

