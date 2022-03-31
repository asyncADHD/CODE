from cv2 import mean
import pandas as pd 
import numpy as np 
import time 

arr1 = [1,2,3,4,5,6,7,8,9,10]


arr = [[1.1,1.11,3.1,3.1,3.1,3.1,3.1,3.1,3.1,3.1,3.1],[1.1,2.111,3.1,3.1,3.1,3.1,3.1,3.1,3.1,3.11,3.1],[1.1,3.1111,3.1,3.1,3.1,3.1,3.1,3.1,3.1,3.111,3.9],[1.1,2.11111,3.1,3.1,3.1,3.1,3.1,3.1,3.1,3.1111,3.1]]

# Function if the price at the end of the array is below "end price" return the strike price
def end_price_check(arr, end_price):
    for i in range(len(arr)):
        if arr[i][-1] < end_price:
            arr[i].append(end_price)
            
        else:
            pass
    return arr






        


# print (end_price_check(arr, 3.3))


def calc_av_len(arr):

    for i in range(len(arr)):
        len_arr = len(arr[i])
        av = np.mean(len_arr)
       
    return av



def return_vals_over_x_for_j_time(arr, x, j):
    z = 0
    for i in range(len(arr)):
        if arr[i][:] > x:
            z += 1
            print (z)
        else:
            pass


# This function is only for debugging purposes
def arr_format(arr):
    for i in range(len(arr)):
        print (arr[i])
        print ("\n")


val_return(arr, 3)