# -*- coding: utf-8 -*-
"""
Created on Sat Sep 16 16:01:44 2023

@author: Dell 7490
"""

import time
import random
import csv
from sortingAlgorithm import sortingAlgorithm

def readValues():
    array=[]
    with open("selectionSort.csv",mode='r',newline='')as file:
        reader=csv.reader(file)
        for row in reader:
            for i in row:                
                number=int(i)
                array.append(number)
 
    return array


def generateRandom(max,min,size):
    array=[]
    for i in range(size):
        number=random.randint(min,max)
        array.append(number)
    return array
def calculateRunTime(start,end):
    return end-start

array=readValues()
print(array)
random.shuffle(array)
print(array)
start=1
end=len(array)
startTime=time.time()
sortedArr=sortingAlgorithm.insertionSort(array, start, end)
endTime=time.time()
runtime=calculateRunTime(startTime, endTime)
print(sortedArr)

