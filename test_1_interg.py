
import pandas as pd
import numpy as np



'''
- get the data from the csv file
- run basic tests on the data
- write back to the csv file
'''


# get the data from excel file

data = pd.read_excel('int_test_1.xls')

matrix_a = np.array(data.iloc[:,0:4])

matrix_b = np.array(data.iloc[:,0:4])



matrix_dot_product = np.dot(matrix_a, matrix_b)

print (matrix_dot_product)

write_data_back_to_excel = pd.DataFrame(matrix_dot_product)
write_to_excel = write_data_back_to_excel.to_excel('int_test_2_out.xlsx', sheet_name='Sheet1', index=False, header=False)
print ("yay it worked")

