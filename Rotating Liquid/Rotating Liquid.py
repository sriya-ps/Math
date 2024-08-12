import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D

c_r = 2 # Radius of container
c_h = 6 # Height of container
l_h = 3 # Height of liquid in container
t = np.linspace(0, 2*np.pi, 24)
r = np.linspace(0, c_r, 100)
z = np.linspace(0, c_h, 2)

# Container
z_c, t_c = np.meshgrid(z, t)
x_c = c_r * np.cos(t_c)
y_c = c_r * np.sin(t_c)

# Liquid Surface
r_l, t_l = np.meshgrid(r, t)
x_l = r_l * np.cos(t_l)
y_l = r_l * np.sin(t_l)
z_l = 1 + r_l ** 2

fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
ax.set_title('Rotating Liquid')
ax.set_axis_off()
cyl = ax.plot_wireframe(x_c, y_c, z_c, color="gray", linestyle="dashed")
sf = ax.plot_surface(x_l, y_l, z_l, cmap=cm.coolwarm, linewidth=0, antialiased=True, cstride=2, rstride=2)
plt.show()


