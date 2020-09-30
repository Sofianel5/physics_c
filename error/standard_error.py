from statistics import mean, stdev
import math
from .error import MeasuredValue

def standard_deviation(datalist):
    # this is +/-
    # measuring diff mebers of a pop. and want to know how measurements are distributed
    if isinstance(datalist[0], MeasuredValue):
        x_hat = mean([x.value for x in datalist])
        return math.sqrt(sum([(x.value-x_hat)**2 for x in datalist])/len(datalist))
    else:
        return stdev(datalist)

def standard_error_of_mean(datalist):
    # this is +/-
    # used when measuring over and over to get a more precisce measurement
    return datalist[0].accuracy/math.sqrt(len(datalist)) 

if __name__ == "__main__":
    print(standard_deviation([
        MeasuredValue(8, "m", 1),
        MeasuredValue(12, "m", 1),
    ]))

    print(standard_deviation([
        MeasuredValue(11, "m", 1),
        MeasuredValue(12, "m", 1),
        MeasuredValue(8, "m", 1),
        MeasuredValue(9, "m", 1),
        MeasuredValue(10, "m", 1),
    ]))