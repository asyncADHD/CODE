import numpy as np
import pandas as pd 



def matrix_multiplcation(Matrix, Matrix_A, n):
    for i in range(n):
        Matrix_A = np.dot(Matrix_A, Matrix_B)
    return Matrix_A