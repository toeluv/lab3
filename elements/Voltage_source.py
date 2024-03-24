from elements.Element import Element
import math as m


class Voltage_source(Element):
    def __init__(self, name, type, voltage, phase, frequency, node_1, node_2, branch):
        super().__init__(name, type, node_1, node_2, branch)
        self.__voltage = voltage
        self.__phase = phase
        self.__frequency = frequency

    def get_voltage(self):
        return self.__voltage

    def get_phase(self):
        return self.__phase

    def get_frequency(self):
        return self.__frequency

    def get_EDS(self,U_element,I_element, time,h):
        if self.__frequency == 0:
            return self.__voltage
        else:
            return self.__voltage * m.sin(2 * m.pi * self.__frequency*time + m.radians(self.__phase))

    def get_conductance(self,U_element,I_element, time,h):
        return 1e10
