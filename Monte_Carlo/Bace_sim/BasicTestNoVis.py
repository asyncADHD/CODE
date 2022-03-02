from time import time
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
from math import log, sqrt, pi, exp
from scipy.stats import norm
import pandas as pd
from pandas import DataFrame
from datetime import datetime, date
import time 

S = 100 #stock price S_{0}
K = 98 # strike
T = 0.25 # time to maturity
r = 0.02 # risk free risk in annual %
q = 0.00 # annual dividend rate
sigma = 0.25 # annual volatility in %
steps = 10 # time steps
N = 10000000 # number of trials*


S_T = datetime.now()

''' Using the geometric brownian motion to simulate the stock price paths '''

def geo_paths(S, T, r, q, sigma, steps, N):
    """
    Inputs
    #S = Current stock Price
    #K = Strike Price
    #T = Time to maturity 1 year = 1, 1 months = 1/12
    #r = risk free interest rate
    #q = dividend yield
    # sigma = volatility 

    Output
    # [steps,N] Matrix of asset paths 

    """
    dt = T/steps
    ST = np.log(S) +  np.cumsum(((r - q - sigma**2/2)*dt + sigma*np.sqrt(dt) * np.random.normal(size=(steps,N))),axis=0)
    
    return np.exp(ST)


def d1 (S, K, T, r, sigma):
    """
    Inputs
    #S = Current stock Price
    #K = Strike Price
    #T = Time to maturity 1 year = 1, 1 months = 1/12
    #r = risk free interest rate
    #q = dividend yield  is assumed as zero
    # sigma = volatility 
    
    Output
    # d1 = d1(S,K,T,r,q,sigma)

    """
    
    return(log(S/K) + (r + sigma**2/2.)*T)/(sigma*sqrt(T))

def d2(S,K,T,r,sigma):
    """
    Inputs
    #S = Current stock Price
    #K = Strike Price
    #T = Time to maturity 1 year = 1, 1 months = 1/12
    #r = risk free interest rate
    # sigma = volatility 
    
    Output
    # d2 = d2(S,K,T,r,sigma)
    
    """
    
    return d1(S,K,T,r,sigma)-sigma*sqrt(T)

def BlackScholesCall(S,K,T,r,sigma):    
    return S*norm.cdf(d1(S,K,T,r,sigma))-K*exp(-r*T)*norm.cdf(d2(S,K,T,r,sigma))


def BlackScholesPut(S,K,T,r,sigma):
    return K*exp(-r*T)-S+BlackScholesCall(S,K,T,r,sigma)



paths= geo_paths(S,T,r, q,sigma,steps,N)
print ("The price of the stock is: ", paths.mean())
print ("The stock max is: ", paths.max())
print ("The stock min is: ", paths.min())
print ("THe BlackScholes call price is: ", BlackScholesCall(geo_paths(S,T,r, q,sigma,steps,N).mean(),K,T,r,sigma))
print ("The BlackScholes put price is: ", BlackScholesPut(geo_paths(S,T,r, q,sigma,steps,N).mean(),K,T,r,sigma))



E_T = datetime.now()
Tot = E_T - S_T

print ("The time taken to run the code is: {}".format(Tot))