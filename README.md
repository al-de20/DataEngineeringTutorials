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





# Spark Programming Model
# Spark Structured API Foundation
# Spark Data Sources and Sinks
# Spark Dataframe and Dataset Transformation
# Aggregations in Apache Spark
# Spark Dataframe Joins
![image](https://user-images.githubusercontent.com/110751151/193691655-acd03105-1618-4bab-b9b9-0e857854994c.png)
