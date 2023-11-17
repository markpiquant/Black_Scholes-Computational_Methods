import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt
from math import sqrt, exp


class BlackScholesModel:
    @staticmethod
    def PriceCallEuropeen(S0, K, r, sigma, T):
        d1 = (np.log(S0 / K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
        d2 = d1 - sigma * np.sqrt(T)
        callprice = S0 * norm.cdf(d1) - K * exp(-r * T) * norm.cdf(d2)
        return callprice
    @staticmethod
    def PriceCallAsiatique(S0, K, r, sigma, T, nombre_simul, nombre_points):
        ecart_t = T / nombre_points
        simulations = np.zeros((nombre_simul, nombre_points + 1))
        simulations[:, 0] = S0

        for i in range(1, nombre_points + 1):
            B_B = np.random.normal(0, sqrt(ecart_t), size=nombre_simul)
            simulations[:, i] = simulations[:, i - 1] * np.exp((r - 0.5 * sigma**2) * ecart_t + sigma * B_B)

        return np.exp(-r * T) * np.mean(np.maximum(0, np.mean(simulations[:, 1:], axis=1) - K))


