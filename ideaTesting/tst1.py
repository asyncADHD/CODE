
import numpy as np 
import math
import pandas as pd



arr = [[1,2,3],[3,3,3],[1,1,1]]


x = 3



for i in range(len(arr)):
    if x in arr[i]:
        # print the psoition of x in the array
        print("dummy")

        


def enumerate_list(arr):
    for i, x in enumerate(arr):
        print(i, x)
    
def enumrate_dict(arr):
    x = 2
    for i in range(len(arr)):
        if x in arr[i]:
            print (arr.index(x))
        else:
            print("dummy")
