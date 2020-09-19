# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 11:11:00 2020

@author: Anaji
"""

def find_mean(arr):
    length = len(arr)
    sum_elements=0
    for i in range (0,length):
        sum_elements = arr[i]+sum_elements
    # print(sum_elements)
    # print(length)
    mean= sum_elements/(length)
    return mean
data=[1,2,3,4]  
answer =find_mean(data)
print(answer)

# print('sagar')