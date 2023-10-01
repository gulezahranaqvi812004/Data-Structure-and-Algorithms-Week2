# -*- coding: utf-8 -*-
"""
Created on Sat Sep 16 15:01:35 2023

@author: Dell 7490
"""
import random
import time
import csv
def generateRandom(min,max,size):
    array=[]
    for i in range(size):
        number=random.randint(min, max)
        array.append(number)
    return array

def mergeSort(array):
    length=len(array)
    if(length<=1):
        return array
    
    half=length//2
    leftHalf=array[:half]
    rightHalf=array[half:]
    
    leftHalf=mergeSort(leftHalf)
    rightHalf=mergeSort(rightHalf)
    
    return mergeArray(leftHalf, rightHalf)
    
    
    
def mergeArray(leftHalf,rightHalf):
    array=[]
    i=0
    j=0
    while i<len(leftHalf) and j<len(rightHalf):
        if leftHalf[i]>rightHalf[j]:
            array.append(leftHalf[i])
            i+=1
        else:
            array.append(rightHalf[j])
            j+=1
        
    array.extend(leftHalf[i:])
    array.extend(rightHalf[j:])
    return array


arr = generateRandom(-1500,1500,10)

start=time.time()
sorted_arr = mergeSort(arr)
end=time.time()

runtime=end-start

print(sorted_arr)

with open("mergeSort.csv",mode='w',newline='') as file:
       writer=csv.writer(file)
       for i in sorted_arr:
         writer.writerow([i])
print("Runtime is",runtime, "seconds")
        
 
        
        
        
        
        
        
        
