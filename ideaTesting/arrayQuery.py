import pandas as pd
import numpy as np
import math


arr = np.array([[1,1,1],[2,140,2],[3,3,3]])


def arrayQuery(arr):
    """
    This function takes in a nD array and returns the first instace of 140 if there is one 
    """
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] == 140:
                return i,j
    return None

qur_arr = arrayQuery(arr)
print(qur_arr)
