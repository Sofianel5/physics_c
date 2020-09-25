import math
import sympy

class MeasuredValue:
    def __init__(self, value, unit,accuracy):
        self.value = value 
        self.accuracy = accuracy 
        self.unit = unit
    def __str__(self):
        return f"{self.value} {self.unit} +/- {self.accuracy} {self.unit}"

    @property 
    def relative_error(self):
        return self.accuracy/self.value 

    def multiply_fractional_error(self, other, dependent=False, print=False):
        if not dependent:
            return math.sqrt((other.accuracy/self.value)**2 + (self.accuracy/self.value)**2)
        raise Exception("Not yet implemented")
    
    def multiply_absolute_error(self, other, dependent=False, print=True):
        result = self.value * other.value
        if not dependent:
            return self.multiply_fractional_error(other, dependent, print=False) * result
        raise Exception("Not yet implemented")

    def add_absolute_error(self, other, dependent=False):
        if not dependent: 
            return math.sqrt((other.accuracy)**2 + (self.accuracy)**2)
        raise Exception("Not yet implemented")
    

def main():
    sympy.init_printing()
    d = MeasuredValue(400, "m", 0.1)
    t = MeasuredValue(63.2, "s", 0.005)
    print(d.multiply_absolute_error(t))

if __name__=="__main__":
    main()