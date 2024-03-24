import elements.Element as e


class Capacitor(e.Element):
    def __init__(self, name, type, capacity, node_1, node_2, branch):
        super().__init__(name, type, node_1, node_2, branch)
        self.__capacity = capacity

    def get_capacity(self):
        return self.__capacity

    def get_conductance(self, U_element, I_element, time, h):
        return (2 * self.__capacity) / (h * (1e-6))

    def get_EDS(self, U_element, I_element, time, h):
        return -(((h * (1e-6)) / (2 * self.__capacity)) * I_element + U_element)
