import numpy as np
import pandas as pd








matrix_A = np.array([[7.06, 5.8, 3.02, 0.14], [8.14, 0.45, 8.63, 3.74 ], [8.71, 9.5, 5.25, 0.54], [4.69, 6.23, 2.64, 8.3]])
matrix_B = np.array([[5.33, 2.9, 7.75, 7.61], [7.09, 4.14, 7.9, 9.62], [0.56, 3.64, 7.67, 5.92], [2.98, 6.48, 2.79, 8.25]])


print (matrix_A)
print ('\n')
print (matrix_B)


def multiply_matrix(matrix_A, matrix_B):
    matrix_C = np.zeros((4,4))
    for i in range(4):
        for j in range(4):
            for k in range(4):
                matrix_C[i][j] += matrix_A[i][k] * matrix_B[k][j]
    return matrix_C

product = multiply_matrix(matrix_A, matrix_B)

print ('\n')
print (product)