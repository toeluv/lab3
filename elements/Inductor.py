import elements.Element as e


class Inductor(e.Element):

    def __init__(self, name, type, inductance, node_1, node_2, branch):
        super().__init__(name, type, node_1, node_2, branch)
        self.__inductance = inductance

    def get_inductance(self):
        return self.__inductance

    def get_conductance(self, U_element, I_element, time, h):
        if time==0:
            return 0
        else:
            return (h * (1e-6)) / (2 * self.__inductance)

    def get_EDS(self, U_element, I_element, time, h):
        return (((2 * self.__inductance) / (h * (1e-6)))*I_element+U_element)
