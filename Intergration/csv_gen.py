import pandas as pd



data = [1,2,3,4,5,5,6,7,8,9,10]
data1 = pd.DataFrame(data)
write_csv = data1.to_csv('test.csv')