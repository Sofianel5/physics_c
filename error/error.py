import math
from sympy import *

class MeasuredValue:
    def __init__(self, value, unit,accuracy):
        self.value = value 
        self.accuracy = accuracy 
        self.unit = unit
    def __str__(self):
        return f"{self.value} {self.unit} +/- {self.accuracy} {self.unit}"
 
    @property 
    def relative_error(self, should_print=False):
        # dimentionless (expressed as value NOT % for this calculation)
        if should_print:
            print(r"""\frac{\delta y}{y}=\frac{top}{bottom}""".replace("top", str(self.accuracy).replace("bottom", str(self.value))))
        return self.accuracy/self.value 
    
    @property 
    def absolute_error(self, should_print=False):
        # has unit
        # shouldn't have more decimal places than original value
        if should_print:
            print(r"""\delta y=value\\""".replace("value", str(self.accuracy)))
        return self.accuracy 
    
    @property 
    def max_value(self, should_print=False):
        if should_print:
            print(r"""y_{max}=value""".replace("value", str(self.value+self.accuracy)))
        return self.value+self.accuracy 

    @property 
    def min_value(self, should_print=False):
        if should_print:
            print(r"""y_{min}=value""".replace("value", str(self.value-self.accuracy)))
        return self.value-self.accuracy
    
    def negate(self, should_print=False):
        if should_print:
            print(r"""y*-1""")
        self.value *= -1 
        return self

    def reciprocate(self, should_print=False):
        if should_print:
            print(r"""y=\frac{1}{y}""")
        self.value = 1 / self.value 
        self.unit = f"1/{self.unit}"
        #self.accuracy = 1 / self.accuracy # unsure about this
        return self

    def add(self, other, dependent, should_print=False):
        if isinstance(other, MeasuredValue):
            if dependent:
                if should_print:
                    print(r"(self.value \text{self.unit} \pm self.accuracy \text{self.unit}) + (other.value \text{other.unit} \pm other.accuracy \text{other.unit})=result.value \text{self.unit} \pm result.accuracy \text{self.unit}\\".replace("self.accuracy", str(self.accuracy)).replace("self.value", str(self.value)).replace("self.unit", self.unit).replace("other.accuracy", str(other.accuracy)).replace("other.value", str(other.value)).replace("other.unit", other.unit).replace("result.accuracy", str(self.accuracy+other.accuracy)).replace("result.value", str(self.value+other.value)))
                return MeasuredValue(self.value+other.value, self.unit, self.accuracy+other.accuracy)
            else:
                if should_print:
                    print(r"(self.value \text{self.unit} \pm self.accuracy \text{self.unit}) + (other.value \text{other.unit} \pm other.accuracy \text{other.unit})=result.value \text{self.unit} \pm \sqrt{self.accuracy^2+other.accuracy^2} \text{self.unit}=result.value \text{self.unit} \pm result.accuracy \text{self.unit}\\".replace("self.accuracy", str(self.accuracy)).replace("self.value", str(self.value)).replace("self.unit", self.unit).replace("other.accuracy", str(other.accuracy)).replace("other.value", str(other.value)).replace("other.unit", other.unit).replace("result.accuracy", str(self.accuracy+other.accuracy)).replace("result.value", str(math.sqrt(self.accuracy**2 + other.accuracy**2))))
                return MeasuredValue(
                    self.value+other.value,
                    self.unit,
                    math.sqrt(self.accuracy**2 + other.accuracy**2)
                )
        else:
            if should_print:
                    print(r"(self.value \text{self.unit} \pm self.accuracy \text{self.unit}) + other \text{self.unit} \text{self.unit}=result.value \text{self.unit} \pm result.accuracy \text{self.unit}\\".replace("self.accuracy", str(self.accuracy)).replace("self.value", str(self.value)).replace("self.unit", self.unit).replace("other", str(other)).replace("result.accuracy", str(self.accuracy+other.accuracy)).replace("result.value", str(self.value+other.value)))
            return MeasuredValue(self.value+other, self.unit, self.accuracy)

    def multiply(self, other, dependent):
        if isinstance(other, MeasuredValue):
            if dependent:
                return MeasuredValue(
                    self.value*other.value, 
                    f"{self.unit}*{other.unit}", 
                    (self.value*other.value)*(self.relative_error+other.relative_error)
                )
            else:
                return MeasuredValue(
                    self.value*other.value,
                    f"{self.unit}*{other.unit}", 
                    (self.value*other.value)*math.sqrt(self.relative_error**2+other.relative_error**2)
                ) 
        else:
            return MeasuredValue(self.value*other, self.unit, self.accuracy*other)
    
    def divide(self, other, dependent):
        if isinstance(other, MeasuredValue):
            if dependent:
                return MeasuredValue(
                    self.value/other.value, 
                    f"{self.unit}/{other.unit}", 
                    (self.value/other.value)*(self.relative_error+other.relative_error)
                )
            else:
                return MeasuredValue(
                    self.value/other.value,
                    f"{self.unit}/{other.unit}", 
                    (self.value/other.value)*math.sqrt(self.relative_error**2+other.relative_error**2)
                ) 
        else:
            return MeasuredValue(self.value/other, self.unit, self.accuracy*other)
    

def main():
    pass

if __name__=="__main__":
    main()