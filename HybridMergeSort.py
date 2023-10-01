# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 21:16:20 2023

@author: Dell 7490
"""
import random
import time 
import csv

def HybridMergeSort(array,n):
    arr=[]
    if(len(array)<=n):
       arr=insertionSort(array)
    else:
       arr= mergeSort(array)
    return arr
    

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
    i=j=0
    array=[]
    while i<len(leftHalf) and j<len(rightHalf):
        if(leftHalf[i]<rightHalf[j]):
            array.append(leftHalf[i])
            i+=1
        else:
             array.append(rightHalf[j])
             j+=1
    array.extend(leftHalf[i:])
    array.extend(rightHalf[j:])
     
    return array
        
    
    
def insertionSort(array):
    for i in range(1,len(array)):
        key=array[i]
        j=i-1
        while j>=0 and key<array[j]:
            array[j+1]=array[j]
            j-=1
        array[j+1]=key
    return array


def generateRandom(min,max,size):
    array=[]
    for i in range(size):
        num=random.randint(min, max)
        array.append(num)
    return array

array=generateRandom(-1500,1500,1000)

start=time.time()
sortedArr=HybridMergeSort(array,20)
end=time.time()

runtime=end-start

with open("HybribMergeSort.csv",mode='w',newline='') as file:
    writer=csv.writer(file)
    for i in range(len(sortedArr)):
        writer.writerow([i])
        
    
print(sortedArr)
print("Runtime is:",runtime,"seconds")


