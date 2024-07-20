import matplotlib.pyplot as plt 
import numpy as np 
import sympy as sy  

global u
u = 10
global g
g = 10
global values
values = {}
global pts
n = 8

def f(x, theta): 
    return x*np.tan(theta) - g*x**2/(2*u**2*np.cos(theta)**2)

def x_range(x, theta):
    return u**2*np.sin(2*theta)/g

def integrating_area(theta):
    x = sy.Symbol("x")
    return sy.integrate(f(x, theta), (x, 0, x_range(x, theta)))

for i in range(n,0,-1):
    theta = (n-i)*np.pi/(2*n)
    values[theta] = integrating_area(theta)
max_area_angle = max(values, key = lambda x: values[x])
print("Angle of projection that gives the maximum area is -", max_area_angle, "radians")
print("The maximum area is - ", values[max_area_angle], "sq. units")

figure, axes = plt.subplots()
axes.set_aspect(1)
plt.xlim(-10,10)
plt.ylim(-10,10)
for theta in values.keys():
    x = np.linspace(-10, 10, 50)
    y = f(x, theta)
    if theta == max_area_angle: colour = "r"
    else: colour = "b"
    plt.plot(x,y, colour)
    if theta == max_area_angle: plt.fill_between(x, y, 0, color='red', alpha=.1)
plt.grid(True, linestyle =':')
plt.xlim([0, 10])
plt.ylim([0, 10])
plt.xlabel('x-axis')
plt.ylabel('y-axis')
 
plt.show()