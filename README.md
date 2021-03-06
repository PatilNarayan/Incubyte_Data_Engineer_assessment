# Incubyte_Data_Engineer_assessment
![](https://img.shields.io/badge/OS-Linux-informational?style=flat&logo=linux&logoColor=white&color=2bbc8a)
![](https://img.shields.io/badge/Code-Python-informational?style=flat&logo=python&logoColor=white&color=2bbc8a)
![](https://img.shields.io/badge/Shell-Bash-informational?style=flat&logo=gnu-bash&logoColor=white&color=2bbc8a)
![](https://img.shields.io/badge/Tools-PostgreSQL-informational?style=flat&logo=postgresql&logoColor=white&color=2bbc8a)
![](https://img.shields.io/badge/Hortonworks%20-sandbox-%2375FF02)
![](https://img.shields.io/badge/Editor-Spyder-%2328FF02)
![](https://img.shields.io/badge/env-Anaconda--navigator-%2328FF02)

## Overview 
This repository contains implementation of given assessment.
The working of data pipeline is demonstarted using tools & Technologies listed below. 
Also, a dummy database has been created to demonstarte a simple data flow in different formats from server to the local system, 
using country-based row filteration.

## 🔧 Technologies & Tools
- Python 
- pyspark
- Hive
- [Pandas](https://pandas.pydata.org/docs/)
- Hortonworks Sandbox

🔸**Concepts:**
- Data processing
- Data visualization 
- ETL

🔸**Problem statement:**
- data extracting will be done by our Source System. They will pull the all the relevant customer data and will give us a Data file. 

## 🔹Working:
- Firstly in Hive database has been created with specified schema.
- Load sample data file in hive table with specific datatype.
- Import data from hive table to pyspark dataframe .
- checking the data format / describe 
- Data Visualization (show data).
- filtering data from dataframe. 
- after filter saving data in specific path.

## 🔹Screenshots:

- Hive Output
![Screenshot from 2021-10-17 10-57-03](https://user-images.githubusercontent.com/70795556/137617398-c4b73487-f30b-4c2d-ae13-2323bb13821f.png)
- pyspark Output
![Screenshot from 2021-10-17 12-43-38](https://user-images.githubusercontent.com/70795556/137617457-7cb43065-4b7c-466b-9a24-9e10c806c80d.png)
- PostgreSQL Table 
![Screenshot (127)](https://user-images.githubusercontent.com/70795556/137641441-8191cc5e-fcdc-4857-a1a8-50421ca463f3.png)
- pycharm output using postgreSQL
![Screenshot (128)](https://user-images.githubusercontent.com/70795556/137641443-3d05c3ea-5d30-4698-90d7-a5b1fa508f2c.png)

 
