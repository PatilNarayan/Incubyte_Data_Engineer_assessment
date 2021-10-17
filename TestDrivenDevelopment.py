#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 17 12:28:00 2021

@author: patilnarayan
"""

# importing necessary libraries
from pyspark import SparkContext
from pyspark.sql import SQLContext

sc = SparkContext('local','example')  # if using locally
sqlContext = SQLContext(sc)

# fetching tables from hive tables
df=sqlContext.sql("select * from hospital.patients")

# visualization Data
df.show()

#customers as per Country 
# India patients extracting
# change in 'IND' if you want any other country data
df.where(df.Country=='IND').show()
    
