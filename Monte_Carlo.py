import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt
from math import sqrt, exp


class MonteCarloEstimation:
    @staticmethod
    def Estimationcallprice(N, r, sigma, K, T, S):
        N = int(N)
        Z = np.random.randn(N)
        estimateur = [exp(-r * T) * max(0, S * exp((r - 0.5 * sigma**2) * T + sigma * sqrt(T) * Z[i]) - K) for i in range(N)]
        return np.mean(estimateur)

    @staticmethod
    def estivariance(N, r, sigma, K, T, S):
        e = []
        N = int(N)
        estimateur = MonteCarloEstimation.Estimationcallprice(N, r, sigma, K, T, S)
        for k in range(N):
            Z = np.random.randn()
            value = (exp(-r * T) * max(0, S * exp((r - 0.5 * sigma**2) * T + sigma * sqrt(T) * Z) - K) - estimateur)**2
            e.append(value)
        esti = sum(e)
        return esti / (len(e) - 1)

