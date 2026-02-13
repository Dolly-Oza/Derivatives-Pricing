# Implementing the black-scholes formula in python

import numpy as np
from scipy.stats import norm

# defining the variables

S = 146.63  # Underlying Price
K = 155.00  # Strike Price
T = 44/365  # Time to Expiration
r = 0.0662  # Risk-Free Rate
sigma = 0.2938  # Volatility


def blackScholes(r, S, K, T, sigma, type="C"):
    "Calculate BS option price for a call/put"
    d1 = (np.log(S/K) + (r + sigma**2/2)*T)/(sigma*np.sqrt(T))
    d2 = d1 - sigma*np.sqrt(T)
    try:
        if type == "C":
            price = S*norm.cdf(d1) - K*np.exp(-r*T)*norm.cdf(d2)
        elif type == "P":
            price = K*np.exp(-r*T)*norm.cdf(-d2) - S*norm.cdf(-d1)
        return price

    except:
        print("Please confirm all option parameters above.")

print("Option Price for Call Option is: ", round(
    blackScholes(r, S, K, T, sigma, type="C"), 2))
print("Option Price for Put Option is: ", round(
    blackScholes(r, S, K, T, sigma, type="P"), 2))
