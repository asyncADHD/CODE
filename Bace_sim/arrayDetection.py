import numpy as np 
import pandas as pd 
from Genration import gen_GBM


S = 100 #stock price S_{0}
K = 98 # strike
T = 0.25 # time to maturity
r = 0.02 # risk free risk in annual %
q = 0.00 # annual dividend rate
sigma = 0.25 # annual volatility in %
steps = 100 # time steps
N = 100 # number of trials*



arr = gen_GBM(S, T, r, q, sigma, steps, N)




arr = np.where ( arr < 98 , 98 , arr) 
print (arr.mean())


