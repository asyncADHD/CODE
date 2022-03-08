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
n = 100
initial_price = 100
drift = .02
volatility = .25
time_period = 1/365 # Daily
total_time = 5

for i in range(0, n):
    simulations.append(GBM(initial_price, drift, volatility, time_period, total_time))

for sim in simulations:
    plt.plot(np.arange(0, len(sim.prices)), sim.prices)

def price_over_time(simulations):
    prices = []
    for sim in simulations:
        prices.append(sim.prices)
    return prices



DateArr = price_over_time(simulations)




print (DateArr[120:250])


# dateData = pd.DataFrame(price_over_time(simulations))
# dateData.to_csv('price_over_time.csv')
writer = pd.DataFrame(DateArr)
# writer.to_csv('price_over_time.csv')

plt.show()
