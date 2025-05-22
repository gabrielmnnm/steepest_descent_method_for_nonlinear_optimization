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


func = Function()
direc = Direction(func)
opt = Optimal_step_length(func, direc)
npt = New_point(func, direc, opt)

x1 = 2.6
x2 = 6.3

stop_criteria = np.e**-15
iterations = 0
i = 0

x1_list = []
x2_list = []
z_list = []
iterations_list = []
iterations_list.insert(i, iterations)

stop = float('inf')
grad_x, grad_y = func.numeric_gradient(x1, x2)

# while (stop >= stop_criteria):
# while (i < 30):
while(grad_x or grad_y >= stop_criteria):
    previous_function = func.numeric_function(x1, x2)
    print(f"Previous point: {x1, x2}")
    print(f"Previous function value: {previous_function}")
    x1_list.insert(i, x1)
    x2_list.insert(i, x2)
    z_list.insert(i, previous_function)

    new_x1, new_x2 = npt.new_point(x1, x2)
    x1, x2 = new_x1, new_x2
    print(f"New point: {x1, x2}")

    next_function = func.numeric_function(x1, x2)

    grad_x, grad_y = func.numeric_gradient(x1, x2)
    print(f"Actual stop value: {grad_x, grad_y}")
    # stop = abs(next_function - previous_function)
    # print(f"Actual stop value: {stop}")

    print(f"New function value: {next_function}")

    iterations += 1
    i += 1
    iterations_list.insert(i, iterations)
    print(f"Iterations: {iterations} \n")

#inserir os últimos valores também
x1_list.insert(iterations, x1)
x2_list.insert(iterations, x2)
z_list.insert(iterations, func.numeric_function(x1, x2))

# print(x1_list)
# print(" ")
# print(x2_list)
# print(" ")
# print(z_list)
# print(" ")

# #inverte a ordem das listas
# ##Para as curvas de nivel, os valores de z deve m ser crescentes
# print(iterations_list)
# print(" ")
# x1_list_reverse = x1_list[::-1]
# x2_list_reverse = x2_list[::-1]
# z_list_reverse = z_list[::-1]

# print(x1_list_reverse)
# print(" ")
# print(x2_list_reverse)
# print(" ")
# print(z_list_reverse)
# print(" ")

# for j in range(len(x1_list)):
#     print(x1_list[j])
#     j += 1

# print(" ")

# for j in range (len(x2_list)):
#     print(x2_list[j])
#     j += 1

# print(" ")

# for j in range (len(z_list)):
#     print(z_list[j])
#     j += 1

# #TESTES
# print(f"Função simbólica: {func.f}")
# print(f"Gradiente simbólico: {func.symbolic_gradient()}")
# print(f"Valor numérico da função para x1, x2: {func.numeric_function(0, 0)}")
# print(f"Valor numérico do gradiente para x1, x2: {func.numeric_gradient(0, 0)}")

# print(f"Valor da direção (-gradiente): {direc.direction(0, 0)}")

# print(f"New funtion: {opt.function_alpha(0, 0)}")
# print(f"New funtion solved: {opt.minimize(0, 0)}")

# print(f"New point: {npt.new_point(0, 0)}")
