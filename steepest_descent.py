import sympy as sp
import numpy as np
import matplotlib.pyplot as plt


class Function:
    def __init__(self):
        self.x1, self.x2 = sp.symbols("x1 x2")
        self.f = self.x1 - self.x2 + 2 * (
            self.x1**2) + 2 * self.x1 * self.x2 + (self.x2**2)

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

        solved = sp.solve(derivative, self.alpha)

        #improve this to accept cases where there are more than 1 solutions
        #(I think that is better to get only the positive solution, since in this method I want to minimize, and the direction is negative)
        symbolic_alpha = solved[0]
        num_alpha = float(symbolic_alpha)
        return num_alpha


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


func = Function()
direc = Direction(func)
opt = Optimal_step_length(func, direc)
npt = New_point(func, direc, opt)

x1 = 0
x2 = 0
stop_criteria = np.e**-15
iterations = 0

stop = float('inf')

while (stop >= stop_criteria):
    previous_function = func.numeric_function(x1, x2)
    print(f"Previous point: {x1, x2}")
    print(f"Previous function value: {previous_function}")

    new_x1, new_x2 = npt.new_point(x1, x2)
    x1, x2 = new_x1, new_x2
    print(f"New point: {x1, x2}")

    next_function = func.numeric_function(x1, x2)
    stop = abs(next_function - previous_function)
    print(f"Actual stop value: {stop}")
    iterations = iterations + 1

    print(f"New function value: {next_function}")
    print(f"Iterations: {iterations} \n")

# #TESTES
# print(f"Função simbólica: {func.f}")
# print(f"Gradiente simbólico: {func.symbolic_gradient()}")
# print(f"Valor numérico da função para x1, x2: {func.numeric_function(0, 0)}")
# print(f"Valor numérico do gradiente para x1, x2: {func.numeric_gradient(0, 0)}")

# print(f"Valor da direção (-gradiente): {direc.direction(0, 0)}")

# print(f"New funtion: {opt.function_alpha(0, 0)}")
# print(f"New funtion solved: {opt.minimize(0, 0)}")

# print(f"New point: {npt.new_point(0, 0)}")
