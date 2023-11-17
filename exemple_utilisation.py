from Black_scholes import BlackScholesModel
from Monte_Carlo import MonteCarloEstimation
import matplotlib.pyplot as plt
from math import sqrt, exp
import numpy as np
from scipy.stats import norm

# Exemple d'utilisation
S0, K, r, sigma, T = 100, 100, 0.05, 0.1, 2
prix_call_europeen = BlackScholesModel.PriceCallEuropeen(S0, K, r, sigma, T)
prix_call_asiatique = BlackScholesModel.PriceCallAsiatique(S0, K, r, sigma, T, 10000, 100)

print("Prix Call Européen:", prix_call_europeen)
print("Prix Call Asiatique:", prix_call_asiatique)

# Script pour montrer la convergence des estimateurs de Black Scholes vers la valeur donnée par la formule de Black Scholes
def plot_convergence():
    r, sig, K, S, T, alpha = 0.05, 0.1, 100, 100, 2, 0.05
    quantile = norm.ppf(1 - alpha / 2)
    X = np.linspace(50, 1000, 30)
    borne_inf, valeur_predite, borne_sup, vraievaleur = [], [], [], []

    for n in X:
        e = MonteCarloEstimation.Estimationcallprice(n, r, sig, K, T, S)
        a = MonteCarloEstimation.estivariance(n, r, sig, K, T, S)
        borne_inf.append(e - quantile * sqrt(a / n))
        valeur_predite.append(e)
        borne_sup.append(e + quantile * sqrt(a / n))
        vraievaleur.append(BlackScholesModel.PriceCallEuropeen(S, K, r, sig, T))

    plt.plot(X, borne_inf, label='borne_inf')
    plt.plot(X, valeur_predite, label='valeur prédite')
    plt.plot(X, borne_sup, label='borne_sup')
    plt.plot(X, vraievaleur, label='Prix_formule_BS')
    plt.xlabel('nombre de simulations')
    plt.ylabel('Prix du call')
    plt.title('Convergence du prix de l\'estimateur de monte carlo vers la valeur donnée par BS')
    plt.legend()
    plt.grid()
    plt.show()

plot_convergence()
