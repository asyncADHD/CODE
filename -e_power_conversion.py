import time
import numpy


import numpy as np
import random 
import pandas as pd
from datetime import datetime
import time

# print( "%.16f" % float("1.953125e-02"))
# DON'T TOUCH THIS CODE
matrix = np.random.rand(1000, 1000)
matrix_b = matrix


# Start the Timer for the multiplication
multiplcation_start_time = datetime.now()

def matrix_multi(matrix, matrix_b, n):
    for i in range(n):
        matrix = np.dot(matrix, matrix_b)
    return matrix


# Start the Timer for the multiplication
multiplcation_start_time = datetime.now()
time.sleep(1)
# Rn the multiplication 10 times
Muliplied_10_times = matrix_multi(matrix, matrix_b, 10)

# End the Timer for the multiplication
multiplcation_end_time = datetime.now()

print ("Duration of multiplcation: {}".format(multiplcation_end_time - multiplcation_start_time))
print ("\n")

# Start the Timer for the inversion
Inersion_start_time = datetime.now()

inverse = np.linalg.inv(matrix)

# End the Timer for the inversion
Inversion_end_time = datetime.now()

print ("Duration of inversion: {}".format(Inversion_end_time - Inersion_start_time))



def Proof_of_inv(matrix, inverse):
    proof_of_inverse = np.dot(inverse, matrix)
    return proof_of_inverse

'''Uncommect this to write the proof of inverse to a csv file
proof_of_inverse = Proof_of_inv(matrix, inverse)
wirtie_proof_of_inverse = pd.DataFrame(proof_of_inverse)
wirtie_proof_of_inverse.to_csv('proof_of_inverse.csv')'''


