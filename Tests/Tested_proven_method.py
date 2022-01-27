import numpy as np
import pandas as pd
import time



matrix_A = np.array([[5.89, 9.11, 6.95, 2.44], [1.06, 6.79, 5.75, 1.03], [2.84, 2.96, 3.01, 9.8], [2.78, 1.63, 4.1, 7.13]])
matrix_B = np.array([[9.86, 2.27, 9.8, 5.34], [9.99, 0.16, 1, 7.99], [0.46, 3.82, 9.49, 4.01], [1.6, 6.47, 4.13, 3.26]])



def multiply_matrix(matrix_A, matrix_B):
    matrix_C = np.zeros((4,4))
    for i in range(4):
        for j in range(4):
            for k in range(4):
                matrix_C[i][j] += matrix_A[i][k] * matrix_B[k][j]
    return matrix_C


product = multiply_matrix(matrix_A, matrix_B)