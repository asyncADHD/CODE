import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker



df = pd.read_csv(r'C:\Users\44786\Desktop\N_W_finace\CODE\ideaTesting\GBM_simulation.csv')

plt.plot(df)

plt.title('GBM Simulation')
plt.xlabel('Day')
plt.ylabel('Price')
plt.show()