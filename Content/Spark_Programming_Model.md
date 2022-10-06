# Module 2: Spark Programming Model

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
## Understanding your Execution Plan
## Unit Testing Spark Application