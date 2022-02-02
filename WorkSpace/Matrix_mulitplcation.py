import numpy as np
import pandas as pd
from datetime import datetime
import time 



matrix_a = np.random.randint(1, 10, size=(50, 50))
# matrix_b = np.random.rand(200,200)

# create a function to multiply n dimensions matrix
# def matrix_multiplction_n_times(matrix_a, matrix_b):
#     A_time_B = np.dot(matrix_a, matrix_b)
#     return A_time_B


multiplcation_start_time = datetime.now()

# muliply matrix_a by itself n times
def multiply_matrix_n_times(matrix_a, n):
    for i in range(n):
        matrix_a = np.dot(matrix_a, matrix_a)
        
    return matrix_a

run_multiplcation_10_times = multiply_matrix_n_times(matrix_a, 10)


# A_time_B = matrix_multiplction_n_times(matrix_a, matrix_b)
multiplcation_end_time = datetime.now()

inversion_start_time = datetime.now()
def inverse_matrix():
    matrix_A_inverse = np.linalg.inv(matrix_a)

    return matrix_A_inverse



matrix_A_inverse= inverse_matrix()
proof_of_inverse = matrix_A_inverse.dot(matrix_a)
inversion_end_time = datetime.now()
# these are commented out as they were used as proof of concept

# wirtie_proof_of_inverse = pd.DataFrame(proof_of_inverse)
# wirtie_proof_of_inverse.to_csv('proof_of_inverse.csv')
# # write_original_matrix_to_txt = pd.DataFrame(matrix_a)
# # write_original_matrix_to_txt.to_csv('Matrix_a_origonal_int.csv')
# # write_multiplcation_to_txt = pd.DataFrame(run_multiplcation_10_times)
# # write_multiplcation_to_txt.to_csv('Matrix_a_multiplcation_10_times_int.csv')


print ("Duration of multiplcation: {}".format(multiplcation_end_time - multiplcation_start_time))
print ("Duration of inversion: {}".format(inversion_end_time - inversion_start_time))


















