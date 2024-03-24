import json
import elements.Element_fabric as ef
from Solver import Solver
import matplotlib.pyplot as plt


def show_plot(scheme_elements, element_name, U_0, I_br):
    choice_element = None
    for element in scheme_elements:
        if element.get_name() == element_name:
            choice_element = element
            break

    count = int(model_settings["simulation_time"] // (model_settings["step"] * (1e-6)))
    I = []
    U = []
    for i in range(len(I_br)):
        I_matrix = I_br[i]
        I.append(I_matrix[choice_element.get_branch() - 1][0])
        U_matrix = U_0[i]
        if choice_element.get_node_2() == 0:
            U.append(U_matrix[choice_element.get_node_1() - 1][0])
        else:
            U.append(U_matrix[choice_element.get_node_1() - 1][0] - U_0[i][choice_element.get_node_2() - 1][0])

    time = [(i * model_settings["step"] * (1e-6)) for i in range(count + 1)]

    plt.plot(time, U, time, I)
    plt.xlabel("Время, с")
    plt.ylabel("Измеряемая величина")
    plt.legend(["Напряжение на элементе, В", "Ток через элемент, А"])
    plt.title("Напряжение и ток на элементе - " + choice_element.get_name())
    plt.grid()
    plt.show()


with open('test4.json') as json_file:
    data = json.load(json_file)
print(data)

model_settings = data["model_settings"]
scheme_elements = []

for element in data["scheme_elements"]:
    scheme_elements.append(ef.Element_fabric.element_fabric(element))

print(scheme_elements)

solver = Solver(model_settings["step"], model_settings["simulation_time"], model_settings["branch_count"],
                model_settings["nodes_count"], scheme_elements)

U0, I = solver.solve()

show_plot(scheme_elements, model_settings["show_measurements_on"], U0, I)
