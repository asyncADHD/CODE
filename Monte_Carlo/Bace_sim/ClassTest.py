
from unittest import result
import matplotlib.pyplot as plt
import numpy as np
import math
import pandas as pd 

class GBM:

    def simulate(self):
        while(self.total_time > 0):
            dS = self.current_price*self.drift*self.time_period + self.current_price*self.volatility*np.random.normal(0, math.sqrt(self.time_period))
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

simulations = []
n = 5
initial_price = 100
drift = .02
volatility = .25
time_period = 1/365 # Daily
total_time = 1

for i in range(0, n):
    simulations.append(GBM(initial_price, drift, volatility, time_period, total_time))

for sim in simulations:
    plt.plot(np.arange(0, len(sim.prices)), sim.prices)



def price_over_time(simulations):
    prices = []
    for sim in simulations:
        prices.append(sim.prices)
    return prices


prices = price_over_time(simulations)

def val_return(prices):
   result = []
   for i in range (0, len(prices)):
      for j in range (0, len(prices[i])):
         if prices[i][j] >= 140:
            result.append(j)
            pass
   return result

val_return(prices)
print (val_return(result))
plt.show()



# dateData = pd.DataFrame(price_over_time(simulations))
# dateData.to_csv('price_over_time.csv')
writer = pd.DataFrame(sim.prices)
# writer.to_csv('price_over_time.csv')

