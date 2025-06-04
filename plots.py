import sympy as sp
from typing import Sequence
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from method import Function

#Simple 3D plot
class Plot:
    def __init__(self, func: Function):
        self.func = func
        self.x = np.linspace(-10, 10, 2500)
        self.y = np.linspace(-10, 10, 2500)

    def plot_figure(self):
        X, Y = np.meshgrid(self.x, self.y)
        Z = self.func.numeric_function(X, Y)

        fig = plt.figure(figsize=(10, 7))
        ax = fig.add_subplot(111, projection='3d')
        ax.plot_surface(X, Y, Z, cmap='viridis')
        ax.set_xlim(-10, 10)
        ax.set_ylim(-10, 10)
        # ax.set_zlim(-15, 15)

        ax.set_xlabel('X axis')
        ax.set_ylabel('Y axis')
        ax.set_zlabel('f(x, y)')
        ax.set_title('Surface')

        plt.show()

#Level Curves plot
class Plot_2:
    def __init__(self, func: Function):
        self.func = func
        self.x1 = np.linspace(-10, 10, 2500)
        self.x2 = np.linspace(-10, 10, 2500)

    def plot_figure(self):
      X, Y = np.meshgrid(self.x1, self.x2)
      Z = self.func.numeric_function(X, Y)

      fig, ax = plt.subplots(figsize=(8,6), tight_layout=True)

      #Define the contour levels
      zmin, zmax = Z.min(), Z.max()
      levs = np.linspace(zmin, zmax, 25)
      CS = ax.contour(self.x1, self.x2, Z, levels=levs)
      ax.clabel(CS, inline=True, fmt='z = %1.3f', fontsize=8)

      # ax.set_xlim(-5, 5)
      # ax.set_ylim(-5, 5)

      ax.set_xlabel('X axis')
      ax.set_ylabel('Y axis')
      ax.set_title('Level curves')

      ax.grid()
      plt.show()

    def plot_graph(self, z, it):
        plt.plot(it, z, "o-r", linewidth = 2, label="teste")
        plt.show()

#3D plot with points
class Plot_3:
    def __init__(self, func: Function):
        self.func = func
        self.x1 = np.linspace(-10, 10, 2500)
        self.x2 = np.linspace(-10, 10, 2500)

    def plot_figure(self, xs_arr, ys_arr):
        X, Y = np.meshgrid(self.x1, self.x2)
        Z = self.func.numeric_function(X, Y)

        fig = plt.figure(figsize=(10, 7))
        ax = fig.add_subplot(111, projection='3d')
        ax.plot_surface(X, Y, Z, cmap='viridis', alpha=0.6)
        ax.set_xlim(-10, 10)
        ax.set_ylim(-10, 10)
        # ax.set_zlim(0, 250)

        # print(xs_arr)
        # print(ys_arr)

        # xs_arr = np.arange(10, -11, -1)
        # ys_arr = np.arange(-10, 11, 1)
        zs_arr = self.func.numeric_function(xs_arr, ys_arr)

        # print(zs_arr)

        #para personalizar a cor, dá para colocar o nome em c=..., pois não está no formato fmt string
        ax.scatter(xs_arr, ys_arr, zs_arr, c='r', marker='o')
        ax.plot(xs_arr, ys_arr, zs_arr, c='k')

        ax.set_xlabel('X axis')
        ax.set_ylabel('Y axis')
        ax.set_zlabel('f(x, y)')
        ax.set_title('Surface')

        ax.grid()
        plt.show()

#Level curves plot with points
class Plot_4:
    def __init__(self, func: Function):
        self.func = func
        self.x1 = np.linspace(-10, 10, 2500)
        self.x2 = np.linspace(-10, 10, 2500)

    def plot_figure(self, xs_arr, ys_arr, zs_arr):
        X, Y = np.meshgrid(self.x1, self.x2)
        Z = self.func.numeric_function(X, Y)
        fig, ax = plt.subplots(figsize=(8, 6), tight_layout=True)

        #Define the contour levels
        zmin, zmax = Z.min(), Z.max()
        levs = np.linspace(zmin, zmax, 25)
        CS = ax.contour(self.x1, self.x2, Z, levels=levs)
        ax.clabel(CS, inline=True, fmt='z = %1.3f', fontsize=8)

        #Draw the points
        point_size = 30
        ax.scatter(xs_arr, ys_arr, point_size, c='r', marker='o')

        #Draw the path
        ax.plot(xs_arr, ys_arr, 'k--')

        # #Be able to set de zoom automatically (probably on a real ide this will be possible without setting too restric limits)
        # ax.set_xlim(0, 10)
        # ax.set_ylim(0, 10)

        ax.set_xlabel('X axis')
        ax.set_ylabel('Y axis')
        ax.set_title('Level curves')

        ax.grid()
        plt.show()

#Iterations graph
class Plot_5:
    def __init__(self, func: Function):
        self.func = func

    def plot_graph(self, iteration, z_arr):
        plt.plot(iteration, z_arr, "o-r", linewidth = 2, label="teste")
        plt.grid()
        plt.show()

