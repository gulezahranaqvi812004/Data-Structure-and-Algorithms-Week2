# -*- coding: utf-8 -*-
"""
Created on Sat Sep 16 21:01:14 2023

@author: Dell 7490
"""
import csv
def readValues():
    array=[]
    with open("values.csv",mode='r',newline='')as file:
        reader=csv.reader(file)
        for row in reader:
            for i in row:                
                number=int(i)
                array.append(number)
 
    return array

