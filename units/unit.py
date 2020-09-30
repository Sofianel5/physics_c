class Unit:
    def __init__(self, units):
        self.unitdata = units 
     
    def get_units(self):
        return [x["unit"] for x in self.unitdata]
    
    def change_power(self, unit, powerdelta):
        for data in self.unitdata:
            if data["unit"] == unit:
                data["power"] += powerdelta 
                return
    
    def raise_to_power(self, power):
        for data in self.unitdata:
            data["power"] *= power
    
    def multiply(self, other):
        i = 0
        units = self.get_units()
        while i < len(other.unitdata):
            if other.unitdata[i]["unit"] in units:
                self.change_power(other.unitdata[i]["unit"], other.unitdata[i]["power"])
            else:
                self.unitdata.append(other.unitdata[i])
            i += 1
        return self 
    
    def reciprocate(self):
        for data in self.unitdata:
            data["power"] *= -1
    
    def divide(self, other):
        return self.multiply(self, other.reciprocate())

    TIME = "time"
    LENGTH = "length"
    AMOUNT = "amount"
    CURRENT = "current"
    TEMPERATURE = "temperature"
    LUMOSITY = "lumosity"
    MASS = "mass"
    
    SECOND = Unit([{"power": 1, "unit": "s", "multiplier": 1, "type": TIME}])
    METER = Unit([{"power": 1, "unit": "m",  "multiplier": 1, "type": LENGTH}])
    GRAM = Unit([{"power": 1, "unit": "g",  "multiplier": 1, "type": LENGTH}])
