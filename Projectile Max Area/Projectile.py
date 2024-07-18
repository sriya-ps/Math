import matplotlib.pyplot as plt 
import numpy as np 
import sympy as sy  

global u
u = 10
global g
g = 10

def f(x, theta): 
    return x*np.tan(theta) - g*x**2/(2*u**2*np.cos(theta)**2)

def x_range(x, theta):
    return u**2*np.sin(2*theta)/g
    
x = sy.Symbol("x")
theta = np.arctan(np.sqrt(2))
print(sy.integrate(f(x, theta), (x, 0, x_range(x, theta))))