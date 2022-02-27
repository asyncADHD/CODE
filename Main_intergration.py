from nbformat import write
import numpy as np
import random 
import pandas as pd
from datetime import datetime
import time

# print( "%.16f" % float("1.953125e-02"))


data = pd.read_excel("intergration test.xls")
matrix = np.array(pd.read_excel('intergration test.xls'))
matrix_b = np.array(data)



def matrix_multi(matrix, matrix_b, n):
    for i in range(n):
        matrix = np.dot(matrix, matrix_b)
    return matrix


# Run the multiplication n times
Muliplied_n_times = matrix_multi(matrix, matrix_b, 10)

# Inverse the matrix
inverse = np.linalg.inv(matrix)

# Method to prove the inverse
def Proof_of_inv(matrix, inverse):
    proof_of_inverse = np.dot(inverse, matrix)
    return proof_of_inverse




write_to_excel = pd.DataFrame(Muliplied_n_times)
f = open('intergration test.xlsx', 'w')
write_to_excel.to_excel(f, sheet_name='Sheet1', index=False, header=False)
f.close()










