#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 17 12:28:00 2021

@author: patilnarayan
"""

from pyspark import SparkContext
from pyspark.sql import SQLContext

sc = SparkContext('local','example')  # if using locally
sqlContext = SQLContext(sc)


df=sqlContext.sql("select * from hospital.patients")

df.show()


df.where(df.Country=='IND').show()
    