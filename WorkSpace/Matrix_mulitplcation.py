import numpy as np
import pandas as pd
import time 








matrix_a = np.random.rand(1000,1000)
matrix_b = np.random.rand(1000,1000)




# create a function to multiply n dimensions matrix

def matrix_multiplction_n_times(matrix_a, matrix_b):
    A_time_B = np.dot(matrix_a, matrix_b)
    return A_time_B


A_time_B = matrix_multiplction_n_times(matrix_a, matrix_b)

time_end = time.time()



def inverse_matrix():
    matrix_A_inverse = np.linalg.inv(matrix_a)

    return matrix_A_inverse


matrix_A_inverse= inverse_matrix()

proof_of_inverse = matrix_A_inverse.dot(matrix_a)

write_to_txt = pd.DataFrame(proof_of_inverse)
#write_to_txt.to_csv('inverse_matrix_1000.csv')





# All the prints







print ("New matrix A:")
print (matrix_a)
print ("\n")
print ("New matrix B:")
print (matrix_b)
print ("\n")
print ("Matrix A times matrix B:")
print (A_time_B)












print ('\n')
# print ('\n')
# print (product)
print ("Matrix A inverse:")
print (matrix_A_inverse)
print ('\n')

print ('\n')
print (proof_of_inverse)

