# Derivative Pricing & Volatility Modeling
## Project Overview

This project implements the Black-Scholes Model for pricing European options on Canara Bank (NSE) and calculates Implied Volatility using the Newton-Raphson method.

The model is built in Python and demonstrates practical understanding of derivative pricing and numerical methods used in quantitative finance.

### 1. Black-Scholes Pricing

Prices European Call and Put options using inputs:

Stock Price (S)

Strike Price (K)

Time to Expiry (T)

Risk-Free Rate (r)

Volatility (σ)

### 2. Implied Volatility Estimation

Uses Newton-Raphson root-finding method

Utilizes analytical Vega for faster convergence

Solves for volatility given market option price

## Results

Black-Scholes Price:

Call Option = 3.19

Put Option = 10.33

Implied Volatility: 23.04%

## Tools & Libraries Used

Python

NumPy

SciPy

py_vollib
