
import numpy as np
from datetime import datetime 

print( "%.16f" % float("1.953125e-02"))

x = 1

matrix = np.random.rand(700, 700)
matrix_b = matrix

while x < 26:
    time_s = datetime.now()
    matrix_multi = np.dot(matrix, matrix_b)
    time_e = datetime.now()
    print (x)
    print ("Duration of multiplcation: {}".format(time_e - time_s))
    x += 1
