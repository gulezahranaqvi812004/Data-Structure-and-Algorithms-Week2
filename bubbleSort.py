# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 07:55:25 2023

@author: Dell 7490
"""


#Bubble sort
import time
import random
import csv
def generateRandom(min,max,size):
  
    array=[0]*size
    for i in range(0,len(array)):
        number=random.randint(min,max)
        array.append(number)
    return array
        
        
def bubble_sort(array,start,end):
    for i in range(start,end-1):
        for j in range(start,end-1-i):
            if array[j]>array[j+1]:
                # array[j],array[j+1]=array[j+1],array[j]
                temp=array[j]
                array[j]=array[j+1]
                array[j+1]=temp
    return array



arr=generateRandom(-1500,1500,10)

start_time=time.time()
sortedArray=bubble_sort(arr,0,len(arr))
end_time=time.time()

runtime=end_time-start_time
#for csv file

with open ("lab2DSA.csv",mode='w',newline='') as file:
    writer=csv.writer(file)
    for i in sortedArray:
        writer.writerow([i])
  

print(sortedArray)
print(len(arr))
print("Runtime is",runtime," seconds")

           
            
                
                
                
                
                
                
                
                
            