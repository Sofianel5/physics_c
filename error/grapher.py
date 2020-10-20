from error import MeasuredValue
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

datalist1 = (
    (MeasuredValue(1, "t(s)", 0), MeasuredValue(18, "x_a(m)", 0)),
    (MeasuredValue(2, "t(s)", 0), MeasuredValue(33, "x_a(m)", 0)),
    (MeasuredValue(3, "t(s)", 0), MeasuredValue(47, "x_a(m)", 0)),
    (MeasuredValue(4, "t(s)", 0), MeasuredValue(61, "x_a(m)", 0)),
    (MeasuredValue(5, "t(s)", 0), MeasuredValue(79, "x_a(m)", 0)),
)

datalist2 = (
    (MeasuredValue(1, "t(s)", 0), MeasuredValue(12, "x_b(m)", 0)),
    (MeasuredValue(2, "t(s)", 0), MeasuredValue(29, "x_b(m)", 0)),
    (MeasuredValue(3, "t(s)", 0), MeasuredValue(53, "x_b(m)", 0)),
    (MeasuredValue(4, "t(s)", 0), MeasuredValue(85, "x_b(m)", 0)),
    (MeasuredValue(5, "t(s)", 0), MeasuredValue(129, "x_b(m)", 0)),
)


class MeasurementDataList:
    def __init__(self, data):
        self.data = data
    
    @property 
    def x_list(self):
        return [x.value for x,y in self.data]
    
    @property 
    def y_list(self):
        return [y.value for x,y in self.data]
    
    @property 
    def x_err_list(self):
        return [x.accuracy for x,y in self.data]
    
    @property 
    def y_err_list(self):
        return [y.accuracy for x,y in self.data]
    
    def plot(self, xlabel="", ylabel="", title=""):
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.suptitle(title)
        plt.errorbar(self.x_list, self.y_list, yerr=self.y_err_list)
        z = np.polyfit(self.x_list, self.y_list, 1)
        p = np.poly1d(z)
        plt.plot(self.x_list,p(self.x_list),"r--")
        plt.show()

if __name__ == "__main__":
    info = MeasurementDataList(datalist)
    info.plot(xlabel="I(A)", ylabel="P(W)", title="P vs I")
    adj_data = [(MeasuredValue(x.value**2, "I", 0), y) for x, y in datalist]
    info = MeasurementDataList(adj_data)
    info.plot(xlabel="I(A)", ylabel="P(W)", title="P vs I^2")

    