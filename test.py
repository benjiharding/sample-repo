import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D


def ackley(x, y, cmap):
    pi = np.pi
    u, v = np.meshgrid(x, y)
    exp1 = -0.2 * np.sqrt(0.5 * (u**2 + v**2))
    exp2 = 0.5 * (np.cos(2*pi*u) + np.cos(2*pi*v))
    fxy = -20 * np.exp(exp1) - np.exp(exp2) + np.exp(1) + 20
    # plot the function
    fig = plt.figure()
    ax = fig.gca(projection="3d")
    surf = ax.plot_surface(u, v, fxy, cmap=cmap)
    return surf


def holder_table(x, y, cmap):
    pi = np.pi
    u, v = np.meshgrid(x, y)
    exp1 = np.abs(1-(np.sqrt(u**2+v**2)/pi))
    fxy = -1 * np.abs(np.sin(u)*np.cos(v) * np.exp(exp1))
    # plot the function
    fig = plt.figure()
    ax = fig.gca(projection="3d")
    surf = ax.plot_surface(u, v, fxy, cmap=cmap)
    return surf


def rosenbrock(x, y, a, b, cmap):
    u, v = np.meshgrid(x, y)
    fxy = (a-u)**2 + b*(v-u**2)**2
    # plot the function
    fig = plt.figure()
    ax = fig.gca(projection="3d")
    surf = ax.plot_surface(u, v, fxy, cmap=cmap)
    return surf


x = np.arange(-5, 5, 0.1)
y = np.arange(-5, 5, 0.1)
# rosenbrock(x, y , 5 ,10 ,'viridis')
ackley(x, y, 'coolwarm')

# x1 = np.arange(-10, 10, 0.1)
# y1 = np.arange(-10, 10, 0.1)
# holder_table(x1, y1, 'coolwarm')

plt.show()
