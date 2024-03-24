import linalg as linalg


def transpose(M: linalg.Matrix) -> linalg.Matrix:
    mlist = linalg.as_list(M)
    result = linalg.zeroes(M.shape[1], M.shape[0])

    for line_index, line in enumerate(mlist):
        for row_index, row in enumerate(line):
            result[row_index][line_index] = row

    return result


class Solver:
    def __init__(self, step, simulation_time, branch_count, nodes_count, elements):
        self.__step = step
        self.__simulation_time = simulation_time
        self.__branch_count = branch_count
        self.__nodes_count = nodes_count
        self.__elements = elements
        self.__A = []
        for node in range(1, self.__nodes_count, 1):
            self.__A.append([0 for i in range(1, self.__branch_count + 1, 1)])
        for element in self.__elements:
            if element.get_node_1() != 0:
                self.__A[element.get_node_1() - 1][element.get_branch() - 1] = 1
            if element.get_node_2() != 0:
                self.__A[element.get_node_2() - 1][element.get_branch() - 1] = -1
        self.__A = linalg.Matrix(self.__A)
        print("Matrix A: ")
        print(self.__A)

    def solve(self):
        U0 = []
        I = []
        U0.append(linalg.zeroes(self.__nodes_count, 1))
        I.append(linalg.zeroes(self.__branch_count, 1))
        print(U0)
        print(I)
        for i in range(1, int(self.__simulation_time // (self.__step * (1e-6))) + 1, 1):
            newU0, newI = self.step(U0[i - 1], I[i - 1], i * self.__step * (1e-6))
            U0.append(newU0)
            I.append(newI)

        return U0, I

    def step(self, U0_old, I_old, time):
        Y = linalg.zeroes(self.__branch_count, self.__branch_count)
        E = linalg.zeroes(self.__branch_count, 1)
        J = linalg.zeroes(self.__branch_count, 1)
        for element in self.__elements:
            u1 = U0_old[element.get_node_1() - 1][0]
            u2 = 0 if element.get_node_2()==0 else U0_old[element.get_node_2() - 1][0]
            U_element =u1-u2
            I_element = I_old[element.get_branch() - 1][0]
            Y[element.get_branch() - 1][element.get_branch() - 1] = element.get_conductance(U_element, I_element, time, self.__step)
            E[element.get_branch() - 1][0] = element.get_EDS(U_element, I_element, time,  self.__step)
            J[element.get_branch() - 1][0] = element.get_J(time)
        print("Matrix Y: ")
        print(Y)
        print("Matrix E: ")
        print(E)
        print("Matrix J: ")
        print(J)
        U_0 = (linalg.inv((self.__A @ Y) @ transpose(self.__A))) @ (- self.__A @ (J + Y @ E))
        I = (Y @ ((transpose(self.__A) @ U_0) + E)) + J
        print("U_0")
        print(U_0)
        print("I")
        print(I)
        return U_0, I
