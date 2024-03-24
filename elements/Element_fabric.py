import elements.Voltage_source as vs
import elements.Capacitor as c
import elements.Current_source as cs
import elements.Inductor as i
import elements.Resistor as r


class Element_fabric:
    @staticmethod
    def element_fabric(element):
        if element["type"] == "voltage_source":
            return vs.Voltage_source(element["name"], element["type"], element["voltage"], element["phase"],
                                     element["frequency"], element["node_1"], element["node_2"], element["branch"])
        elif element["type"] == "current_source":
            return cs.Current_source(element["name"], element["type"], element["current"], element["phase"],
                                     element["frequency"], element["node_1"], element["node_2"], element["branch"])
        elif element["type"] == "resistor":
            return r.Resistor(element["name"], element["type"], element["resistance"], element["node_1"],
                              element["node_2"], element["branch"])
        elif element["type"] == "capacitor":
            return c.Capacitor(element["name"], element["type"], element["capacity"], element["node_1"],
                               element["node_2"], element["branch"])
        elif element["type"] == "inductor":
            return i.Inductor(element["name"], element["type"], element["inductance"], element["node_1"],
                              element["node_2"], element["branch"])

