import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D

r0 = 1 # Radius of container in m
h0 = 2.5 # Height of liquid in container in m
H = 4 # Height of container in m
w = 6 # Angular speed in rad/s
g = 10 # Gravitation field in m/s/s

t = np.linspace(0, 2*np.pi, 36)
r = np.linspace(0, r0, 100)
z = np.linspace(0, H, 10)

# Container Cylindrical
z_c, t_c = np.meshgrid(z, t)
x_c = r0 * np.cos(t_c)
y_c = r0 * np.sin(t_c)

# Container Plane
r_p, t_p = np.meshgrid(r, t)
x_p = r_p * np.cos(t_p)
y_p = r_p * np.sin(t_p)
z_p = r_p * 0.0

# Liquid Surface
r_l, t_l = np.meshgrid(r, t)
x_l = r_l * np.cos(t_l)
y_l = r_l * np.sin(t_l)
z_l = h0 + ((w**2)/(2*g))*(r_l**2 - (r0**2/2))
print(z_l)

fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
ax.set_title('Rotating Liquid')
#ax.set_axis_off()
cyl = ax.plot_wireframe(x_c, y_c, z_c, color="gray", linestyle="dashed")
pl = ax.plot_wireframe(x_p, y_p, z_p, color="gray", linestyle="dashed")
sf = ax.plot_surface(x_l, y_l, z_l, cmap=cm.coolwarm, linewidth=0, antialiased=True, cstride=2, rstride=2)
plt.show()