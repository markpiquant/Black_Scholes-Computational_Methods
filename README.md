# Black_Scholes-Computational_Methods
Basic implementation of Black-Scholes model pricing for vanillas and implementation of Computational methods (Monte Carlo &amp; Finites differences)

### Repository Overview

This repository contains two primary classes that are instrumental in the field of computational finance:

    1. BlackScholesModel Class: This class is designed to compute the pricing of both European and Asian call options. It now includes a new method, PriceCallAsiatique, which allows for the pricing of Asian call options. This is in addition to the existing method for European call options. The inclusion of both types of options within a single class provides a comprehensive tool for those interested in option pricing models.

    2. MonteCarloEstimation Class: Complementing the BlackScholesModel, this class offers a computational approach to pricing both European and Asian call options. It utilizes Monte Carlo simulation methods, providing a different perspective and method for option valuation compared to the analytical approach of the BlackScholesModel.

### Testing and Examples

For users looking to test and see these new features in action, we have provided an example script named exemple-utilisation.py. This script demonstrates the practical application of both European and Asian call pricing functionalities, and serves as a guide for implementing these methods in your projects. 


### Upcoming Features

Looking ahead, there are plans to expand the computational methods offered in this repository. A 'Finite Difference Method' for Asian call option pricing is in development and will be added soon. This method will provide yet another approach for users to explore and apply in their computational finance analyses.