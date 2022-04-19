# Dependancies
import matplotlib.pyplot as plt
import numpy as np
from math import log, sqrt, pi, exp
import pandas as pd 
from scipy.stats import norm






class GBM:

    def simulate(self):
        while(self.total_time > 0):
            dS = self.current_price*self.drift*self.time_period + self.current_price*self.volatility*np.random.normal(0, sqrt(self.time_period))
            self.prices.append(self.current_price + dS)
            self.current_price += dS
            self.total_time -= self.time_period

    def __init__(self, initial_price, drift, volatility, time_period, total_time):
        # Initialize fields
        self.initial_price = initial_price
        self.current_price = initial_price
        self.drift = drift
        self.volatility = volatility
        self.time_period = time_period
        self.total_time = total_time
        self.prices = []
        # Simulate the diffusion process
        self.simulate()   # Simulate the diffusion proces


# Variables

strike  = 98
n = 50
initial_price = 100
drift = .02
volatility = .25
time_period = 1/365 # Daily
total_time = 1
simulations =[]
x = 0 
CB_Call_Price = 140
CB_Put_Price = 60
x_call = 0
x_put = 0
# Ensure that n_call and n_put are the same as n number of gebrations or the program will fail
n_call = 50
n_put = 50

##### Black Scholes Call and Put Variables #####

S = initial_price
K = strike 
T = total_time
r = 0.02
q = 0 
sigma = volatility



# List initialization
call_CB_price = []
call_CB_death_gen_num = []
call_CB_index = []

put_CB_price = []
put_CB_death_gen_num = []
put_CB_day = []


for i in range(n):
    simulations.append(GBM(initial_price, drift, volatility, time_period, total_time))
 
def Price_Over_Time(simulations):
    prices = []
    for sim in simulations:
        prices.append(sim.prices)
    return prices

SIMS = Price_Over_Time(simulations)

def end_price_check(SIMS, end_price):
    for i in range(len(SIMS)):
        if SIMS[i][-1] < end_price:
            SIMS[i].append(end_price)
        else:
            pass
    return SIMS

mean_val_list = []    

def calc_mean(SIMS):
    for i in range(len(SIMS)):
        
        mean_val_list.append(SIMS[i][-1])
    return np.mean(mean_val_list)
    
end_price = end_price_check(SIMS, strike)


for sim in simulations:
    plt.plot(np.arange(len(sim.prices)), sim.prices)


def CB_call_function(arr, price, days):
    count = 0
    for i in arr:
        if i >= price:
            count = count + 1
            if count == days:
                call_CB_index.append(arr.index(i))
                call_CB_price.append(i)
                call_CB_death_gen_num.append(x_call)
                return count, call_CB_price, call_CB_death_gen_num, call_CB_index
            else:
                pass
        else:
            count = 0

def CB_put_function(arr, price, days):
    count = 0 
    for i in arr:
        if i <= price:
            count += 1
            if count == days:
                put_CB_price.append(i)
                put_CB_death_gen_num.append(x_put)
                put_CB_day.append(arr.index(i))
                return count, put_CB_price, put_CB_death_gen_num, put_CB_day
            else:
                pass
        else:
            count = 0
            




# Call CB check
while n_call > x_call:
    CB_call_function(SIMS[x_call][180:], CB_Call_Price, 20)
    x_call = x_call + 1

# PUT CB check
while n_put > x_put:
    CB_put_function(SIMS[x_put][180:], CB_Put_Price, 20)
    x_put = x_put + 1




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



print ("The Generation's that die are genration's: ", call_CB_death_gen_num)
print ('\n')
print ("The price of the bond's when they are called are : ", call_CB_price)
print ('\n')
print("The day the CB's are called : ", call_CB_index)
print ('\n')




print ("The Generation's that die are genration's: ", put_CB_death_gen_num)
print ('\n')
print ("The price of the bond's when they are called are : ", put_CB_price)
print ('\n')
print("The day the CB's are called : ", put_CB_day)
print ('\n')


print ("THe BlackScholes call price is: ", BlackScholesCall(calc_mean(SIMS).mean(),K,T,r,sigma))
print ("The BlackScholes put price is: ", BlackScholesPut(calc_mean(SIMS).mean(),K,T,r,sigma))
print ("\n")
print ("Mean of the simulations is: ", calc_mean(SIMS).mean())

user_input_graph = input ("Would you like to see the graph again? (y/n)")
user_input_graph = user_input_graph.lower()
if user_input_graph == "y":
    plt.show()
else:
    pass

user_input_csv = input ("Would you like a csv file of the prices gens? (y/n)")
user_input_csv = user_input_csv.lower()
if user_input_csv == "y":
    df = pd.DataFrame(SIMS)
    df.to_csv('GBM_prices.csv', index=False, header=False)
else:
    pass

user_input_mean = input ("Would you like to see the mean end value of the price? (y/n)")
user_input_mean = user_input_mean.lower()
if user_input_mean == "y":
    print ("The mean end value of the price is : ", calc_mean(SIMS))
else:
    pass


