# BigDota2
Big Data project

Technologies used: Spark, Hive
The DataBricks cluster is used to run spark
AWS is used for hosting the data in S3 and to maintain the instances

Instructions to run the code:
Spark.py file should be run on the databricks cluster notebooks.
The Hive files can be run on the Cloudera VM and starting the hive shell by using the respective beeline command and adding the Jason SERDE_dependencies.jar file, followed by executing the hive queries/file 

The Description:
Spark.py - contains the data profiling and analytics code for the project that runs on databricks cluster.

Other .py files are used to scrape,collect data from the Dota2 API and www.dotabuff.com
The .hive files contain the code for creating a player,match table and running various anaytic queries on the tables created.
