from error import MeasuredValue
import matplotlib.pyplot as plt

datalist = (
    (MeasuredValue(1.5, "I", 0), MeasuredValue(270, "W", 50)),
    (MeasuredValue(2, "I", 0), MeasuredValue(380, "W", 50)),
    (MeasuredValue(2.5, "I", 0), MeasuredValue(620, "W", 50)),
    (MeasuredValue(3.0, "I", 0), MeasuredValue(830, "W", 50)),
    (MeasuredValue(3.5, "I", 0), MeasuredValue(1280, "W", 50)),
    (MeasuredValue(4, "I", 0), MeasuredValue(1600, "W", 50)),
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
        plt.show()

if __name__ == "__main__":
    info = MeasurementDataList(datalist)
    info.plot(xlabel="I(A)", ylabel="P(W)", title="P vs I")
    adj_data = [(MeasuredValue(x.value**2, "I", 0), y) for x, y in datalist]
    info = MeasurementDataList(adj_data)
    info.plot(xlabel="I(A)", ylabel="P(W)", title="P vs I^2")

    