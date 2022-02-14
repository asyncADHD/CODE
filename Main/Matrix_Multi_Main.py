import numpy as np
import pandas as pd 
from datetime import datetime



s = datetime.now()

matrix = np.random.rand(50, 50)
matrix_a = matrix



def matrix_multi(matrix, matrix_b, n):
    for i in range(n):
        matrix = np.dot(matrix, matrix_b)
        
    return matrix



Muliplied_10_times = matrix_multi(matrix, matrix_a, 11)
write_multi_to_csv = pd.DataFrame(matrix)
write_multi_to_csv.to_csv('matrix_multi_50.csv')



e = datetime.now()

print (e-s)




