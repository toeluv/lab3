import elements.Element as e

class Resistor(e.Element):
    def __init__(self, name, type, resistance, node_1, node_2, branch):
        super().__init__(name, type, node_1, node_2, branch)
        self.__resistance = resistance

    def get_resistance(self):
        return self.__resistance
    def get_conductance(self,U_element,I_element, time, h):
        return 1/self.__resistance