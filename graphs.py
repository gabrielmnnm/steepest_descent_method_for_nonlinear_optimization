import sympy as sp
from typing import Sequence
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from steepest_descent import Function

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

        ax.set_xlabel('eixo X')
        ax.set_ylabel('eixo Y')
        ax.set_zlabel('f(x, y)')
        ax.set_title('superficie')

        plt.show()

class Plot_2:
    def __init__(self, func: Function, xs: Sequence[float], ys: Sequence[float], zs: Sequence[float]):
        self.func = func
        self.x1 = np.linspace(2, 6.5, 2500)
        self.x2 = np.linspace(2, 6.5, 2500)

        self.levels = list(zs)
        if len(xs) != len(ys):
            raise ValueError("xs and ys must have the same length")
        self.points = list(zip(xs, ys))

    # def plot_figure(self):
    #     X, Y = np.meshgrid(self.x1, self.x2)
    #     Z = self.func.numeric_function(X, Y)
    #     fig, ax = plt.subplots(1, 1, figsize=(8, 6), tight_layout=True)

    #     CS = ax.contour(self.x1, self.x2, Z, levels=self.levels)
    #     ax.clabel(CS, inline=True, fmt='z = %1.5f', fontsize=8)

    #     xs, ys = zip(*self.points)
    #     ax.scatter(xs, ys, c='g', label='Pontos')
    #     ax.plot(xs, ys, linestyle='-', marker='o', color='k', label='Caminho')

    #     ax.legend()
    #     ax.grid()

    #     plt.show()

    def plot_figure(self):
      X, Y = np.meshgrid(self.x1, self.x2)
      Z    = self.func.numeric_function(X, Y)

      fig, ax = plt.subplots(figsize=(8,6), tight_layout=True)

      zmin, zmax = Z.min(), Z.max()
      levs = np.linspace(zmin, zmax, 50)
      CS = ax.contour(self.x1, self.x2, Z, levels=levs)
      ax.clabel(CS, inline=True, fmt='z = %1.3f', fontsize=8)

      xs, ys = zip(*self.points)
      ax.scatter(xs, ys,    c='g', label='Pontos')
      ax.plot(   xs, ys, '-ok',       label='Caminho')
      # margin = 0.5
      # ax.set_xlim(min(xs)-margin, max(xs)+margin)
      # ax.set_ylim(min(ys)-margin, max(ys)+margin)

      ax.legend()
      ax.grid()
      plt.show()

    def plot_graph(self, z, it):
        plt.plot(it, z, "o-r", linewidth = 2, label="teste")
        plt.show()

# def main():

#     func = Function()
#     plot = Plot(func)

#     plot.plot_figure()
#         #4.819999999999999, 4.819999999999999, 4.819999999999997,
#     xs = (4.820000000000003, 4.819999999999962, 4.820000000000043, 4.819999999999565, 4.820000000000502, 4.819999999995015, 4.820000000005759, 4.819999999942903, 4.820000000065978, 4.8199999993459866, 4.820000000755748, 4.819999992508639, 4.820000008656683, 4.81999991419062, 4.820000099157505, 4.819999017101226, 4.820001135794138, 4.819988741440599, 4.820013009890863, 4.819871039456819, 4.820149021072119, 4.818522828622609, 4.821706953591651, 4.803079822522751, 4.8395522050848205, 4.626188767096711, 5.04395964691047, 2.6)

#     #4.080000000000002, 4.080000000000002, 4.080000000000002,
#     ys = (4.08000000000002, 4.0800000000000365, 4.080000000000223, 4.0800000000004335, 4.0800000000025465, 4.080000000004984, 4.080000000029161, 4.080000000057096, 4.080000000334017, 4.080000000654012, 4.08000000382598, 4.08000000749136, 4.080000043824463, 4.080000085809378, 4.080000501984872, 4.080000982898773, 4.080005749957828, 4.0800112585593995, 4.0800658625724955, 4.080128960543179, 4.080754419177609, 4.081477171377389, 4.088641452557738, 4.096920177477248, 4.17898303824191, 4.2738112329032925, 5.213795712484236, 6.3)

#     #4.080000000000002, 4.080000000000002, 4.080000000000002,
#     zs = (150.0, 150.00000000000003, 150.00000000000034, 150.000000000004, 150.00000000004576, 150.0000000005243, 150.00000000600556, 150.0000000687905, 150.0000007879572, 150.00000902561177, 150.00010338336878, 150.00118419905422, 150.0135643422776, 150.15537200504414, 151.7797)

#     plt_2 = Plot_2(func, xs, ys, zs)
#     plt_2.plot_figure()

#     iterations = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29)
#     new_zs = (151.7797, 150.15537200504414, 150.0135643422776, 150.00118419905422, 150.00010338336878, 150.00000902561177, 150.0000007879572, 150.0000000687905, 150.00000000600556, 150.0000000005243, 150.00000000004576, 150.000000000004, 150.00000000000034, 150.00000000000003, 150.0, 150.0, 150.0, 150.0, 150.0, 150.0, 150.0, 150.0, 150.0, 150.0, 150.0, 150.0, 150.0, 150.0, 150.0, 150.0)

#     plt_2.plot_graph(new_zs, iterations)
#     # plt_2.plot_figure()

# if __name__ == "__main__":
#     main()

