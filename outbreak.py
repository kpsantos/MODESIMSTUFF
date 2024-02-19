"""
Zombie Apocalypse


S' = sigma - beta*S*Z - delta_S*S
I' = beta*S*Z - rho*I - delta_I*I
Z' = rho*I - alpha*S*Z
R' = delta_S*S + delta_I*I + alpha*S*Z
"""
import numpy as np
from matplotlib import pyplot as plt 
from ODESolver import ForwardEuler

class SIZR:
    def __init__(
            self, sigma, beta, rho, delta_S, delta_I, alpha, S0, I0, Z0, R0
    ):
    
    #The Zombie Class
   # initial value: S0, Z0, I0, R0
    
        if isinstance(sigma, (float, int)):
            self.sigma = lambda t:sigma 
        elif callable(sigma):
            self.sigma = sigma
        
        if isinstance(beta, (float, int)):
            self.beta = lambda t:beta
        elif callable(beta):
            self.beta = beta

        if isinstance(rho, (float, int)):
            self.rho = lambda t:rho 
        elif callable(sigma):
            self.rho = rho

        if isinstance(delta_S, (float, int)):
            self.delta_S = lambda t:delta_S 
        elif callable(delta_S):
            self.delta_S = delta_S

        if isinstance(delta_I, (float, int)):
            self.delta_I = lambda t:delta_I
        elif callable(delta_I):
            self.delta_I = delta_I
        
        if isinstance(alpha, (float, int)):
            self.alpha = lambda t:alpha
        elif callable(alpha):
            self.alpha = alpha
        
        self.initial_conditions = [S0, I0, Z0, R0]

    def __call__(self, u, t): 
        """RHS of system of ODEs"""
        S, I, Z, R =  u

        return np.asarray([
            self.sigma(t) - self.beta(t)*S*Z - self.delta_S(t)*S,
            self.beta(t)*S*Z - self.rho(t)*I - self.delta_I(t)*I,
            self.rho(t)*I - self.alpha(t)*S*Z,
            self.delta_S(t)*S + self.delta_I(t)*I + self.alpha(t)*I
        ])
    
    if __name__ == "__main__":

        beta = pass