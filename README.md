# [Tutorials](https://github.com/al-de20/DateEngineeringTutorials/)
Welcome to ....

# [Spark Execution Model and Architecture](https://github.com/al-de20/DateEngineeringTutorials/blob/main/Content/Spark_Execution_Model_and_Architecture.md)
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

Later on in one the test projects, you will see how the spark conf looks like and how to set the number of threads when Spark is run locally in a laptop for instance.

![image](https://user-images.githubusercontent.com/110751151/194175118-8c719833-ce82-43c1-8044-e2c8c9324a0b.png)

spark.master = local[3] indicates that no cluster will be used and 3 threads will be created to handle the processing.

<img width="894" alt="image" src="https://user-images.githubusercontent.com/110751151/194173789-545e8375-cad7-4a3e-91fa-adebeea1c715.png">

The cluster mode is designed to submit your application to the cluster and let it run. Once an application is submitted to run in cluster mode,
a session cab be disconected and the dirver nor slaves will be impacted. So, the cluster mode is meant for submitting long-running jobs to the cluster.

## Spark Execution Models - When to use what?

<img width="837" alt="image" src="https://user-images.githubusercontent.com/110751151/194176240-37118848-0867-43e9-b0fa-da0f753c1f71.png">

## Working with PySpark Shell

On terminal session, lunch pyspark. You'll see somethig similar to this:

<img width="847" alt="image" src="https://user-images.githubusercontent.com/110751151/194179870-4d1d1029-afcd-45e3-9fc9-9f3fce43e25b.png">

Apache Spark is a well-designed system, and it generates a lot of metrics, logs, and other information to monitor and investigate things about your application. A bunch of information is available to you via Spark Context web UI. On the same screenshot you will see the url address to the spark web UI. When you open it, you will see the following screen when clicking Event Timeline:


Spark started an executor driver process. We do not see a separate driver and executor processes because we are in a local cluster,and everything is running inside a single JVM. The JVM is a combination of driver and executors. And that's what we see here.


<img width="938" alt="image" src="https://user-images.githubusercontent.com/110751151/194185057-73166f97-ba3d-4fd2-8152-20fbc16988c4.png">


When you click on the Executors tab, you'll se additional details like the Memory usage and thread assigment (8 cores/threads in this case).

![image](https://user-images.githubusercontent.com/110751151/194185297-91429ed9-bf46-4227-84e5-a4f6361a12d2.png)

## Working with Notebooks in Cluster

This mode of operation is mostly used by data scientists and data analysts for interactive exploration directly in a production cluster.
In most cases, you are going to prefer using a notebook for its web-based interface and graph capabilities.

## Working with Spark Submit

This mode of operation is mostly used for executing a packaged Spark application on a production cluster. Next screenshot will show how to submit a pyspark file to a cluster. Look at the spark-submit argument.

spark-submit --master yarn --deploy-mode cluster pi.py 100

<img width="837" alt="image" src="https://user-images.githubusercontent.com/110751151/194187220-c5261a32-e8c5-4bfd-b4d1-fd006d3c284e.png">

* Key options for spark-submit:

![image](https://user-images.githubusercontent.com/110751151/194188223-29eff731-cd6f-41cd-a4ed-73b2217066f0.png)
![image](https://user-images.githubusercontent.com/110751151/194188252-63b757ce-7c4a-44aa-8f71-7381c6862aaf.png)
![image](https://user-images.githubusercontent.com/110751151/194188323-d2a477fd-6a3e-41b5-b5b7-c755b8ba63c5.png)
![image](https://user-images.githubusercontent.com/110751151/194188342-d4766509-3102-48f5-8e3f-fbdf3926ac41.png)
![image](https://user-images.githubusercontent.com/110751151/194188395-39489aff-6e39-4152-a0fc-429f805fa656.png)
![image](https://user-images.githubusercontent.com/110751151/194188468-0d34a8ea-9a7b-4daa-889a-4fa3dc8fd3ad.png)
![image](https://user-images.githubusercontent.com/110751151/194188831-e0fbff2c-207e-4798-b871-36bb00f7a961.png)


# Section 4: Spark Programming Model

## Creating Spark Project Build Configuration

In this section, we are going to create and run our first Spark program. We will create a Spark Project and define our project Build Configuration.

I will be using PyCharm as my development IDE. So I am assuming that you already have PyCharm.  

You will also need Python, and I recommend you to get Anaconda Python installed on your machine. These two items are the prerequisite of Spark Programming using the IDE.You should also download Spark binaries and set your SPARK_HOME environment variable.


<img width="809" alt="image" src="https://user-images.githubusercontent.com/110751151/194189493-52d1da35-f3ff-4119-842e-bf0061191103.png">


<img width="809" alt="image" src="https://user-images.githubusercontent.com/110751151/194191532-e403ba79-6837-45f5-ae10-a21d3813ea21.png">
<img width="813" alt="image" src="https://user-images.githubusercontent.com/110751151/194191620-cb1bea46-356a-4a05-bc25-51480b95cb2b.png">
<img width="815" alt="image" src="https://user-images.githubusercontent.com/110751151/194191723-aea975ce-d17f-4174-98b4-b3cc12b4e53c.png">

So let's start the PyCharm IDE.

We are going to create a new project.

Give a name to your project.

And chose your Python interpreter and the Virtual environment.

We are going to use a conda environment, so make sure you selected conda in this box.

We will use Python 3.9.

The next box has already picked up the conda file location.

Let's create the project. Wait for a few minutes while conda configures a virtual environment for you.

<img width="565" alt="image" src="https://user-images.githubusercontent.com/110751151/194191306-c3d5cf36-bf55-4be1-98ea-c89a5f699038.png">

But before you do anything, let's install some necessary packages.

Go to Pycharm->Preference and look for your project name.

Select the interpreter. Make sure you are using a conda package manager. So, these are the default packages that are already included in your project. However, this is not enough. We need PySpark also.

![image](https://user-images.githubusercontent.com/110751151/194192163-d1b05dff-9924-425f-8ed4-d77e0a66f0a7.png)


![image](https://user-images.githubusercontent.com/110751151/194192286-7f87f4ad-27c9-4494-977a-12ffedc4abec.png)

Let's add pyspak by using the search bar and then click on Install package at the botton left corner.

<img width="647" alt="image" src="https://user-images.githubusercontent.com/110751151/194192448-88325959-f7c4-4548-bb51-4d9fd410989c.png">

Let's add pytest for unit testing.

<img width="650" alt="image" src="https://user-images.githubusercontent.com/110751151/194192713-f9252ca5-a2a9-46ef-a9ca-2d8418585ff1.png">

Now, let's create the main program.

Right-click on your project, go to new, and create a Python File, give it a name.


![image](https://user-images.githubusercontent.com/110751151/194192911-e5a1ec71-1fcc-4aa9-9c30-ac07f2dac0e2.png)


Let's import the below. You need this line in every Spark program.

From pyspark.sql, import everything.

And, let's create the main entry point of my PySpark program.

I am going to print a Hello message and run it once.

<img width="832" alt="image" src="https://user-images.githubusercontent.com/110751151/194195607-85cd9a20-2e52-46f1-b9e8-0bf301054338.png">



## Configuring Spark Project Application Logs

We already created a basic Spark project and also added dependencies. However, a proper application must have some kind of application logging.
So, we are going to configure the Spark application log. Spark project make use of Log4J, and we also want to use the same for our Spark applications.

<img width="832" alt="image" src="https://user-images.githubusercontent.com/110751151/194199017-f3ecc1af-5db6-456f-b0c2-7dd7eb71bfe4.png">

So, let me open my Spark project and add a Log4J properties file. I already have a preconfigured log4j.properties file. Let me add it to the project root directory.

Let's look at the file content. The content of this file is pretty much standard. Let me quickly explain a few things. The Log4J works almost the same way as Python logs.

In the most basic setup, the Log4J has got three components.

* 1. Logger: The Logger is the set of APIs which we are going to use from our application.
* 2. Configurations: Configurations are defined in the log4j properties file, and they are loaded by the loggers at runtime. 
* 3. Appenders: Appenders are the output destinations, such as Console and a log file.

![image](https://user-images.githubusercontent.com/110751151/194199789-ba55dba0-60cc-42ad-878b-ba242ecef7c5.png)

So, I have defined the root category at the top. For any hierarchy or category, we define two things.

The first thing is the log level, and the second thing is the list of appenders.

Log4J supports multiple log levels, such as DEBUG, INFO, WARN, and ERROR. I am setting the root category as WARN.

So, at the topmost level, we only want to see the warnings and errors. We do not want to see the info and debug messages. And we want these messages to go to the Console. So, I am setting the appender as Console.

The next thing is to define the console appender, which I am doing here. All these configurations are standard, and they remain the same in most of the projects. So, the first  two sections (Logs to console and console appender)together will set the root level log4J configuration and they will stop all the log messages sent by the Spark and other packages except warning and errors.

![image](https://user-images.githubusercontent.com/110751151/194201176-9ebd5a78-9a05-4cd4-a3bf-dd11829b6e49.png)

However, we want to change the behavior of our application. So, I am defining the second log level specific to my application. This level is defined as guru.learningjournal.spark.examples. This is the name that is going to be used when using the Logger in my application.

So, the application level log will be set to INFO. And I want to send these logs to console and file appenders. We want application-level logs to go to the console and log file both.

![image](https://user-images.githubusercontent.com/110751151/194201262-b6c7d521-8dbd-4b60-a084-21a92673d14a.png)

We already defined the console appender. So, I am setting the file appender here. The rest of the settings below this level are some recommendations by the Spark Log4J configuration template.

![image](https://user-images.githubusercontent.com/110751151/194201678-0d35cbd6-166a-4d4c-b463-d9541d1a280b.png)



## Creating Spark Session
## Configuring Spark Session
## Data Frame Introduction
## Data Frame Partitions and Executors
## Spark Transformation and Actions
## Spark Jobs Stages and Task
## Undertanding your Execution Plan
## Unit Testing Spark Application


# Spark Structured API Foundation
# Spark Data Sources and Sinks
# Spark Dataframe and Dataset Transformation
# Aggregations in Apache Spark
# Spark Dataframe Joins
![image](https://user-images.githubusercontent.com/110751151/193691655-acd03105-1618-4bab-b9b9-0e857854994c.png)
