from method import *
from plots import *

def main():

    #Instances
    func = Function()
    direc = Direction(func)
    opt = Optimal_step_length(func, direc)
    npt = New_point(func, direc, opt)

    #Variables
    x1 = 2.6
    x2 = 6.3
    x1 = 0
    x2 = 0
    stop_criteria = np.e**-15 * 10**-15
    iterations = 0
    i = 0

    #Take care with the aproximations made by NumPy
    #Verify later how to change the tolerance since it can influantiate on the stop critaria
    x1_list = np.array([])
    x2_list = np.array([])
    z_list = np.array([])
    iterations_list = np.array([])
    iterations_list = np.insert(iterations_list, i, iterations)

    stop = float('inf')

    while (stop >= stop_criteria):
        previous_function = func.numeric_function(x1, x2)
        print(f"Previous point: {x1, x2}")
        print(f"Previous function value: {previous_function}")
        x1_list = np.insert(x1_list, i, x1)
        x2_list= np.insert(x2_list, i, x2)
        z_list = np.insert(z_list, i, previous_function)

        new_x1, new_x2 = npt.new_point(x1, x2)
        x1, x2 = new_x1, new_x2
        print(f"New point: {x1, x2}")

        next_function = func.numeric_function(x1, x2)
        stop = abs(next_function - previous_function)
        print(f"Actual stop value: {stop}")

        print(f"New function value: {next_function}")

        iterations += 1
        i += 1
        iterations_list = np.insert(iterations_list, i, iterations)
        print(f"Iterations: {iterations} \n")

    #Insert the last values too
    x1_list = np.insert(x1_list, iterations, x1)
    x2_list = np.insert(x2_list, iterations, x2)
    z_list = np.insert(z_list, iterations, func.numeric_function(x1, x2))

    aux = 1
    while (aux == 1):
        print("Which plot do you choose?\n")
        print("1. Surface\n2. Surface with the points\n3. Level curves\n4. Level curves with the path\n5. Iterations graph")
        choice = int(input("Select a number: "))

        if (choice == 1):
            plt1 = Plot(func)
            plt1.plot_figure()
            aux = 1
        
        elif (choice == 2):
            plt3 = Plot_3(func)
            plt3.plot_figure(x1_list, x2_list)
            aux = 1

        elif (choice == 3):
            plt2 = Plot_2(func)
            plt2.plot_figure()
            aux = 1
        
        elif (choice == 4):
            plt4 = Plot_4(func)
            plt4.plot_figure(x1_list, x2_list, z_list) 
            aux = 1


        elif (choice == 5):
            plt5 = Plot_5(func)
            plt5.plot_graph(iterations_list, z_list)
            aux = 1
        
        else:
            aux = 0




    # print(x1_list)
    # print(" ")
    # print(x2_list)
    # print(" ")
    # print(z_list)
    # print(" ")

    # #TESTES
    # print(f"Função simbólica: {func.f}")
    # print(f"Gradiente simbólico: {func.symbolic_gradient()}")
    # print(f"Valor numérico da função para x1, x2: {func.numeric_function(0, 0)}")
    # print(f"Valor numérico do gradiente para x1, x2: {func.numeric_gradient(0, 0)}")

    # print(f"Valor da direção (-gradiente): {direc.direction(0, 0)}")

    # print(f"New funtion: {opt.function_alpha(0, 0)}")
    # print(f"New funtion solved: {opt.minimize(0, 0)}")

    # print(f"New point: {npt.new_point(0, 0)}")

if __name__ == '__main__':
    main()