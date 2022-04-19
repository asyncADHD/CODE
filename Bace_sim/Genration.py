from importlib.resources import path
from time import time
import numpy as np
import matplotlib.pyplot as plt
from math import log, sqrt, pi, exp
from scipy.stats import norm
import pandas as pd
from datetime import datetime, date


S = 100 #stock price S_{0}
K = 98 # strike
T = 5 # time to maturity
r = 0.02 # risk free risk in annual %
q = 0.00 # annual dividend rate
sigma = 0.25 # annual volatility in %
steps = 100 # time steps
N = 100 # number of trials*


def gen_GBM(S, T, r, q, sigma, steps, N):
    """
    Inputs
    #S = Current stock Price

   #K = Strike Price
    #T = Time to maturity 1 year = 1, 1 month = 1/12
    #r = risk free interest rate
    #q = dividend yield
    # sigma = volatility 
    
    Output
    # [steps,N] Matrix of asset paths 
    
    """
    dt = T/steps
    ST = np.log(S) +  np.cumsum(((r - q - sigma**2/2)*dt + sigma*np.sqrt(dt) * np.random.normal(size=(steps,N))),axis=0)
    
    return np.exp(ST)
 
    
conv_bond = gen_GBM(S, T, r, q, sigma, steps, N)

""" Replacing the final price with the strike price if it is less than the strike price """
conv_exp = np.where ( conv_bond < 98 , 98 , conv_bond)

print (conv_exp.mean())
print (conv_exp.min())
print (conv_exp.max())
