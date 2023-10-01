# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 09:31:41 2023

@author: Dell 7490
"""

import time
import random
import csv
def generateRandom(max,min,size):
    array=[]
    for i in range(size):
        number=random.randint(min,max)
        array.append(number)
    return array

def selectionSort(array,start,end):
    for i in range(start,end-1): 
        min=i
        for j in range(i+1, end):
            if array[min]<array[j]:
               min=j
        array[i],array[min]=array[min],array[i]
    return array;

arr=generateRandom(1500,-1500,10)
startTime=time.time()
sortedarray=selectionSort(arr, 0, len(arr))
endTime=time.time()
runtime=endTime-startTime
# for csv
with open ("selectionSort.csv",mode='w',newline='') as file:
    writer=csv.writer(file)
    for i in sortedarray:
        writer.writerow([i])

print(sortedarray)
print(runtime)





 




