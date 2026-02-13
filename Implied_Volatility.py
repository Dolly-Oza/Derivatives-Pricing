"""Calculate Implied Volatility of an option using Newton-Raphson Method of root finding"""

from py_vollib.black_scholes import black_scholes as bs
from py_vollib.black_scholes.greeks.analytical import vega


def implied_vol(S0, K, T, r, market_price, flag="c", tol=0.00001):
    """Calculating the implied volatility of an European Option
    S0: stock price
    K: strike price
    T: time to maturity
    r: risk-free rate
    market_price: option price in the market
    """
    max_iter = 200  # max no. of iterations
    vol_old = 0.3  # initial guess
    for k in range(max_iter):
        bs_price = bs(flag, S0, K, T, r, vol_old)
        Cprime = vega(flag, S0, K, T, r, vol_old)*100
        C = bs_price - market_price

        vol_new = vol_old - C/Cprime
        new_bs_price = bs(flag, S0, K, T, r, vol_new)
        if (abs(vol_old - vol_new) < tol or abs(new_bs_price - market_price) < tol):
            break

    implied_vol = vol_new
    return implied_vol


S0, K, T, r = 146.63, 155.00, 44/365, 0.0662
market_price = 3.7
print(implied_vol(S0, K, T, r, market_price)*100)