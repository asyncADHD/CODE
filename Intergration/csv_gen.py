import pandas as pd
import numpy as np


data = np.random.rand(100, 100)

write_to_excel = pd.DataFrame(data)
write_to_excel.to_excel('intergration test.xlsx', sheet_name='Sheet1', index=False, header=False)