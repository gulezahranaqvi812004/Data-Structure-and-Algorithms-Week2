# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 21:05:08 2023

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

def insertionSort(array,start,end):
    for i in range(start,end):
        key=array[i]
        j=i-1
        while j>=0 and array[j]<key:
            array[j+1]=array[j]
            j-=1
        array[j+1]=key
    
    
    return array
         
array=generateRandom(1500, -1500,10 )
start=1
end=len(array)
startTime=time.time()
sortedArray=insertionSort(array,start,end)
endTime=time.time()
runtime=endTime-startTime


with open("InsertionSort.csv", mode='w',newline='') as file:
   writer=csv.writer(file)
   for i in sortedArray:
     writer.writerow([i])
     

print(sortedArray)
print("Run time: ",runtime, " seconds")



   


