# [Tutorials](https://github.com/al-de20/DateEngineeringTutorials/)
Welcome to ....

# Spark Execution Model and Architecture
## Execution Methods
* Interactive Clients
  * spark-shell, Notebook (best for exploration or during development)  
* Submit Job
  * spark-submit, Databricks Notebook, Rest API
  
* Excecution Methods:
<img width="829" alt="image" src="https://user-images.githubusercontent.com/110751151/193713263-5d2dc233-735d-47b0-9548-ba116413dd92.png">

## Spark Distributed Processing Model

<img width="1108" alt="image" src="https://user-images.githubusercontent.com/110751151/193714744-ddb64ea5-f823-454e-8125-7f6313c2c8b7.png">

Spark is a distributed processing engine. Spark applies a master-salve achitecture to every application it is going to create a master process for your application. This master process is then going to create a bunch of slaves to distribute the work and complete your job.
You can think of these as runtime containers with some dedicated CPU and memory.

In Spark terminology,the master is a driver,and the slaves are the executors.The Spark engine is going to ask for a container from the underlying cluster manager to start the driver process.Once started,the driver is again going to ask for some more containers to start the executor process.

## Spark Execution Modes
* Client (Spark shell and Notebooks)
* Cluster


<img width="900" alt="image" src="https://user-images.githubusercontent.com/110751151/194173014-c3e8aeb8-b0db-45ee-b2d4-a6ea4efd0000.png">

As the Driver is created locally the moment the session is disconected, slaves are killed. So this aproach is for interactive work.

Later on in one the test projects, you will see the spark conf looks like and how the set the number of threads when Spark in run locally in laptop for instance.

![image](https://user-images.githubusercontent.com/110751151/194175118-8c719833-ce82-43c1-8044-e2c8c9324a0b.png)

spark.master = local[3] indicates that no cluster will be used and 3 thread will be created to handle the processing.

<img width="894" alt="image" src="https://user-images.githubusercontent.com/110751151/194173789-545e8375-cad7-4a3e-91fa-adebeea1c715.png">

The cluster mode is designed to submit your application to the cluster and let it run. Once an application is submitted to run in cluster mode,
a session cab be disconected and the dirver nor slaves will be impacted. So, the cluster mode is meant for submitting long-running jobs to the cluster.

## Spark Execution Models - When to use what?

<img width="837" alt="image" src="https://user-images.githubusercontent.com/110751151/194176240-37118848-0867-43e9-b0fa-da0f753c1f71.png">

## Working with PySpark Shell

<img width="847" alt="image" src="https://user-images.githubusercontent.com/110751151/194179797-9a34307a-b367-4633-9b00-8fb7d674eaf0.png">

On terminal session, lunch pyspark. You'll see somethig similar to this:

<img width="847" alt="image" src="https://user-images.githubusercontent.com/110751151/194179870-4d1d1029-afcd-45e3-9fc9-9f3fce43e25b.png">

Apache Spark is a well-designed system, and it generates a lot of metrics, logs, and other information to monitor and investigate things about your application. A bunch of information is available to you via Spark Context web UI. On the same screenshot you will see the url address to the spark web UI. When you open it, you will see the following screen when clicking Event Timeline:

<img width="679" alt="image" src="https://user-images.githubusercontent.com/110751151/194180343-c0ab38c6-e4e4-4731-9e1d-e4c0c3fbafc7.png">




# Spark Programming Model
# Spark Structured API Foundation
# Spark Data Sources and Sinks
# Spark Dataframe and Dataset Transformation
# Aggregations in Apache Spark
# Spark Dataframe Joins
![image](https://user-images.githubusercontent.com/110751151/193691655-acd03105-1618-4bab-b9b9-0e857854994c.png)
