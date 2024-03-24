import abc

class Element:
    def __init__(self, name, type, node_1, node_2, branch):
        self.__name = name
        self.__type = type
        self.__node_1 = node_1
        self.__node_2 = node_2
        self.__branch = branch

    def get_name(self):
        return self.__name

    def get_type(self):
        return self.__type

    def get_node_1(self):
        return self.__node_1

    def get_node_2(self):
        return self.__node_2

    def get_branch(self):
        return self.__branch

    @abc.abstractmethod
    def get_conductance(self,U_element,I_element, time, h):
        return 0

    @abc.abstractmethod
    def get_EDS(self,U_element,I_element, time, h):
        return 0

    @abc.abstractmethod
    def get_J(self, time):
        return 0