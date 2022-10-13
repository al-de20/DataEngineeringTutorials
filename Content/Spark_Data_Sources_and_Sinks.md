# Module 4: Spark Data Sources and Sinks

## Spark Data Sources and Sinks.

Any processing engine, including Spark, must-read data from some data source. And that's what we mean by Spark Data Sources.

These data sources can be further categorized into two groups.

* External Data Sources
* Internal Data Sources

![img_36.png](img_36.png)

### External Data sources
Your data might be stored in some source systems such as Oracle or SQL Server Databases.

It might be stored at some application servers, such as your application logs.

However, all these systems are external to your Data Lake. You don't see them in this Data Lake conceptual diagram.

You cannot process the data from these systems unless you read them

and create a Spark DataFrame or a Dataset.

There are two approaches.

The **first approach** is to bring your data to the Data Lake and store them in your Lake's distributed storage. How you bring it to the lake is your choice.
The most commonly used approach is to use a suitable data **integration tool.**

The **second approach** is to use Spark Data Source API to directly connect with these external systems.
And Spark allows you to do it for a variety of source systems.

I prefer the first one for all my batch processing requirements
and the second one for all my stream processing requirements. Bringing data correctly and efficiently to your lake is a complex goal in itself.
We want to decouple the ingestion from the processing to improve manageability.
Your source system would have been designed for some specific purpose.
And the capacity of your source system would have been planned accordingly.

Now, if you want to connect your Spark workload to these systems, then you must have to replan your source system capacity
and the security aspects of those systems.We want to use the right tool for the right purpose.

A spark is an excellent tool for data processing. However, It wasn't designed to handle the complexities of Data Ingestion.

### Internal Data sources

So your internal data source is your distributed storage. It could be HDFS or cloud-based storage.

However, at the end of the day, your data is stored in these systems as a data file. The mechanics of reading data from HDFS or from cloud storage is the same. The difference lies in the data file format.

![img_37.png](img_37.png)

### Data Sink

The data sinks are the final destination of the processed data.

So you are going to load the data from an internal or an external source.

Then you will be handling it using the Spark APIs.

Once your processing is complete, you want to save the outcome to an internal or an external system.
And these systems could be a data file in your data lake storage, or it could be an external system such as a JDBC database,
or a NoSQL database.

Spark also allows you to directly write the data to a bunch of external sources such as JDBC databases,
Cassandra, and MongoDB.

However, we again do not recommend directly writing data to the external systems
for the same reasons as we do not directly read from these external systems.


## Spark DataFrameReader API.


![img_38.png](img_38.png)

The third most important thing is the Read Mode.

You can specify the Mode via the option method itself. Reading data from a source file,

especially the semi-structured data sources such as CSV, JSON, and XML, may encounter a corrupt or malformed record.

Read modes specify what will happen when Spark comes across a malformed record. Spark allows three read modes.
permissive dropMalformed and failFast

The **permissive Mode** is the default option.
This Mode sets all the fields to null when it encounters a corrupted record
and places the corrupted records in a string column called _corrupt_record.

The **dropMalformed** is going to remove the malformed record.
That means, you are ignoring the malformed records and only loading the well-formed records.

Finally, the **fail-fast** raises an exception and terminates immediately upon encountering a malformed record.

The last thing is the **schema.**

The schema is optional for two reasons.
DataFrameReader allows you to infer the schema in many cases.
So, if you are inferring the schema, then you may not provide an explicit schema.

Some data sources such as **Parquet** and **AVRO** comes with a **well-defined schema** inside the data source itself.
So, in those cases, you do not need to specify a schema. Once you are done setting the format, all necessary options, Mode,
and schema, you can call the load() method to read the data and create a DataFrame.

However, like any other tool, DataFrameReader also comes with some shortcuts and variations.
We have already seen one such shortcut in the earlier examples.

Instead of using the load method, we used the CSV() method.

![img_39.png](img_39.png)

That was a shortcut. However, I recommend avoiding shortcuts and follow the standard style.

Following the standard is going to add to your code maintainability.


## Reading CSV, JSON and Parquet files.

Reading CSV, JSON and Parquet files:

```

 flightTimeCsvDF = spark.read \
        .format("csv") \
        .option("header", "true") \
        .schema(flightSchemaStruct) \
        .option("mode", "FAILFAST") \
        .option("dateFormat", "M/d/y") \
        .load("data/flight*.csv")

    flightTimeCsvDF.show(5)
    logger.info("CSV Schema:" + flightTimeCsvDF.schema.simpleString())

    flightTimeJsonDF = spark.read \
        .format("json") \
        .schema(flightSchemaDDL) \
        .option("dateFormat", "M/d/y") \
        .load("data/flight*.json")

    flightTimeJsonDF.show(5)
    logger.info("JSON Schema:" + flightTimeJsonDF.schema.simpleString())

    flightTimeParquetDF = spark.read \
        .format("parquet") \
        .load("data/flight*.parquet")

    flightTimeParquetDF.show(5)
    logger.info("Parquet Schema:" + flightTimeParquetDF.schema.simpleString())
```
## Creating Spark DataFrame Schema.

![img_40.png](img_40.png)

### Defining a schema

DataFrame schema is all about setting the column name and appropriate data types.

Spark allows you to define Schema in two ways.

Programmatically and Using DDL String

### Programmatically
```
flightSchemaStruct = StructType([
        StructField("FL_DATE", DateType()),
        StructField("OP_CARRIER", StringType()),
        StructField("OP_CARRIER_FL_NUM", IntegerType()),
        StructField("ORIGIN", StringType()),
        StructField("ORIGIN_CITY_NAME", StringType()),
        StructField("DEST", StringType()),
        StructField("DEST_CITY_NAME", StringType()),
        StructField("CRS_DEP_TIME", IntegerType()),
        StructField("DEP_TIME", IntegerType()),
        StructField("WHEELS_ON", IntegerType()),
        StructField("TAXI_IN", IntegerType()),
        StructField("CRS_ARR_TIME", IntegerType()),
        StructField("ARR_TIME", IntegerType()),
        StructField("CANCELLED", IntegerType()),
        StructField("DISTANCE", IntegerType())
    ])
```
### Using DDL String

```
    flightSchemaDDL = """FL_DATE DATE, OP_CARRIER STRING, OP_CARRIER_FL_NUM INT, ORIGIN STRING, 
          ORIGIN_CITY_NAME STRING, DEST STRING, DEST_CITY_NAME STRING, CRS_DEP_TIME INT, DEP_TIME INT, 
          WHEELS_ON INT, TAXI_IN INT, CRS_ARR_TIME INT, ARR_TIME INT, CANCELLED INT, DISTANCE INT"""
```

And you set the previous defined schema using ***.schema(schema name)*** as shown below:
```
flightTimeCsvDF = spark.read \
        .format("csv") \
        .option("header", "true") \
        .schema(flightSchemaStruct) \
        .option("mode", "FAILFAST") \
        .option("dateFormat", "M/d/y") \
        .load("data/flight*.csv")

    flightTimeCsvDF.show(5)
    logger.info("CSV Schema:" + flightTimeCsvDF.schema.simpleString())

    flightTimeJsonDF = spark.read \
        .format("json") \
        .schema(flightSchemaDDL) \
        .option("dateFormat", "M/d/y") \
        .load("data/flight*.json")

    flightTimeJsonDF.show(5)
    logger.info("JSON Schema:" + flightTimeJsonDF.schema.simpleString())

    flightTimeParquetDF = spark.read \
        .format("parquet") \
        .load("data/flight*.parquet")
gfgh
    flightTimeParquetDF.show(5)
    logger.info("Parquet Schema:" + flightTimeParquetDF.schema.simpleString())
```

## Spark DataFrameWriter API.
The DataFrameWriter is a standardized API to work with a variety of internal and external data sources.

Here is the general structure of the DataFrameWriter API.

![img_41.png](img_41.png)


## Writing Your Data and Managing  Layout.
## Spark Databases and Tables.
## Working with Spark SQL Tables.

