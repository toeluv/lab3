import elements.Element as e
import math as m


class Current_source(e.Element):
    def __init__(self, name, type, current, phase, frequency, node_1, node_2, branch):
        super().__init__(name, type, node_1, node_2, branch)
        self.__current = current
        self.__phase = phase
        self.__frequency = frequency

    def get_current(self):
        return self.__current

    def get_phase(self):
        return self.__phase

    def get_frequency(self):
        return self.__frequency

    def get_J(self, time):
        if self.__frequency == 0:
            return self.__current
        else:
            return self.__current * m.sin(2 * m.pi * self.__frequency*time + m.radians(self.__phase))

    def get_conductance(self,U_element,I_element, time, h):
        return 1e-10