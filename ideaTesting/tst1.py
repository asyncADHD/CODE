
import numpy as np 
import math
import pandas as pd









arr = [[1.1,1.11,3.1,3.1,3.1,3.1,3.1,3.1,3.1,3.1,3.1],[1.1,2.111,3.1,3.1,3.1,3.1,3.1,3.1,3.1,3.11,3.1],[1.1,3.1111,3.1,3.1,3.1,3.1,3.1,3.1,3.1,3.111,3.9],[1.1,2.11111,3.1,3.1,3.1,3.1,3.1,3.1,3.1,3.1111,3.1]]





def val_return (arr, condition):
    for count, values in enumerate(arr):
        for i in values:
            if i > condition:
                price = []
                price.append(i)
                print (price)
            else:
                pass
        

def val_return_2 (arr, conn):
    for count, values in enumerate(arr):
        print ("Start of loop")
        
        print ("\n")
        print("count", count)
        print ("--"  *  15)
      

        for i in values:
            print ("for i in values: print i", i)
            print ("\n")



def val_return_3 (arr, conn):
    for count, values in enumerate(arr):
        for i in values:
            if i > conn:
                print (count)
                print (i)
            else:
                pass

def val_return_4 (arr, conn):
    for count, values in enumerate(arr):
        z = 0
        for i in values:
            
            if i > conn:
                z += 1
                    
            else:
                continue
    print (z)

   

    

val_return_4(arr, 3)


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
