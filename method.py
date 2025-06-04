import sympy as sp
import numpy as np
import matplotlib.pyplot as plt


class Function:
    def __init__(self):
        self.x1, self.x2 = sp.symbols("x1 x2")
        # self.f = (self.x1 - 1)**2 + 2 * (2 * self.x2**2 - self.x1)**2
        self.f = ((self.x1 - (2 * 2.6 + 3 * 6.3) / 5)**2) / 4 + ((self.x2 - (3 * 2.6 + 2 * 6.3) / 5)**2) / 9 + 150

    #Gradiente simbolico
    def symbolic_gradient(self):
        delf_delx = sp.diff(self.f, self.x1)
        delf_dely = sp.diff(self.f, self.x2)
        return delf_delx, delf_dely

    #Funcao numerica (para que possam ser feitas as operacoes matematicas)
    def numeric_function(self, x1, x2):
        numeric_f = sp.lambdify((self.x1, self.x2), self.f, modules='numpy')
        return numeric_f(x1, x2)

    #Gradiente numerico
    def numeric_gradient(self, x1, x2):
        delf_delx, delf_dely = self.symbolic_gradient()
        numeric_delf_delx = sp.lambdify((self.x1, self.x2), delf_delx, modules='numpy')
        numeric_delf_dely = sp.lambdify((self.x1, self.x2), delf_dely, modules='numpy')
        return numeric_delf_delx(x1, x2), numeric_delf_dely(x1, x2)


class Direction:
    def __init__(self, func: Function):
        self.func = func

    def direction(self, x1, x2):
        # function = self.func.f
        delf_delx, delf_dely = self.func.numeric_gradient(x1, x2)
        return -delf_delx, -delf_dely


class Optimal_step_length:
    # minimize f(xi + alpha * Si)
    def __init__(self, func: Function, direc: Direction):
        self.direc = direc
        self.func = func
        self.alpha = sp.symbols("alpha")

    def function_alpha(self, x1, x2):
        function = self.func.f
        sym_x1, sym_x2 = self.func.x1, self.func.x2

        dir_x, dir_y = self.direc.direction(x1, x2)
        new_x1 = x1 + self.alpha * dir_x
        new_x2 = x2 + self.alpha * dir_y

        return function.subs({sym_x1: new_x1, sym_x2: new_x2})

    def minimize(self, x1, x2):
        function = self.function_alpha(x1, x2)
        derivative = sp.diff(function, self.alpha)

        ##Numeros complexos
        #all_roots = sp.solve(derivative, self.alpha)
        # real_roots = [
        #     r.evalf() for r in all_roots
        #     if abs(sp.im(r)) < 1e-8
        # ]
        # if not real_roots:
        #     raise ValueError("No real step‐length found.")

        # solved = sp.solve(derivative, self.alpha)

        all_roots = sp.solve(sp.simplify(derivative), self.alpha)

        real_roots = []
        tol = 1e-8
        for r in all_roots:
            rv = complex(r.evalf())
            if abs(rv.imag) < tol:           
                real_roots.append(rv.real)

        if not real_roots:
            raise ValueError("Nenhum alpha real encontrado")

        candidates = [ alpha for alpha in real_roots if alpha > 0 ]
        #(Acho que é melhor pegar apenas os valores positivos, uma vez que este método minimiza a função, e a direão é negativa)
        if not candidates:
            raise ValueError("Nenhum alpha positivo encontrado")

        opt_alpha = min(candidates)
        return opt_alpha

        # symbolic_alpha = solved[0]
        # num_alpha = float(symbolic_alpha)
        # return num_alpha

class New_point:
    def __init__(self, func: Function, direc: Direction, opt: Optimal_step_length):
        self.func = func
        self.direc = direc
        self.opt = opt

    def new_point(self, x1, x2):
        dir_x, dir_y = self.direc.direction(x1, x2)
        opt_alpha = self.opt.minimize(x1, x2)

        new_x1 = x1 + dir_x * opt_alpha
        new_x2 = x2 + dir_y * opt_alpha

        return new_x1, new_x2

