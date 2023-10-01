# -*- coding: utf-8 -*-
"""
Created on Sat Sep 16 16:03:06 2023

@author: Dell 7490
"""

class sortingAlgorithm:
 
 @staticmethod
 def insertionSort(array,start,end):
    for i in range(start,end):
        key=array[i]
        j=i-1
        while j>=0 and array[j]>key:
            array[j+1]=array[j]
            j-=1
        array[j+1]=key
    return array


 @staticmethod
 def selectionSort(array,start,end):
     for i in range(start,end-1): 
         min=i
         for j in range(i+1, end):
             if(array[min]>array[j]):
                min=j
         array[min],array[i]=array[i],array[min]
     return array

 @staticmethod
 def bubble_sort(array,start,end):
     for i in range(start,end-1):
         for j in range(start,end-1-i):
             if array[j]>array[j+1]:
                 # array[j],array[j+1]=array[j+1],array[j]
                 temp=array[j]
                 array[j]=array[j+1]
                 array[j+1]=temp
     return array

 @staticmethod
 def mergeSort(array):
     length=len(array)
     if(length<=1):
         return array
     
     half=length//2
     leftHalf=array[:half]
     rightHalf=array[half:]
     
     leftHalf=sortingAlgorithm.mergeSort(leftHalf)
     rightHalf=sortingAlgorithm.mergeSort(rightHalf)
     
     return sortingAlgorithm.mergeArray(leftHalf, rightHalf)
     
     
     
 def mergeArray(leftHalf,rightHalf):
     array=[]
     i=0
     j=0
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

