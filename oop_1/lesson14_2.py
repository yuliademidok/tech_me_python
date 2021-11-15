class Temperature:
    __CELSIUS_CONSTANT = 273.15

    def __init__(self):
        self.kelvin = 0

    @property
    def celsius(self):
        return self.kelvin - self.__CELSIUS_CONSTANT

    @celsius.setter
    def celsius(self, data):
        self.kelvin = data + self.__CELSIUS_CONSTANT

    @property
    def fahrenheit(self):
        return self.kelvin * 1.8 - 459.67

    @fahrenheit.setter
    def fahrenheit(self, data):
        self.kelvin = (data + 459.67) / 1.8


termo = Temperature()

# print(termo.kelvin)
# print(termo.celsius)
# print(termo.fahrenheit)

termo.fahrenheit = 200
print(termo.kelvin)
print(termo.celsius)
print(termo.fahrenheit)
