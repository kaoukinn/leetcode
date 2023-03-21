class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        anslist = []
        Fahrenheit = celsius * 1.80 + 32.00
        Kelvin = celsius + 273.15
        anslist.append(Kelvin)
        anslist.append(Fahrenheit)
        return anslist