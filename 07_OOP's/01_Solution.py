# Create a Car Class with attributes like brandes and models. Than create an instance of Class.
class Car:
    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model

    def get_brand(self):
        return self.__brand+ " !"

    def full_name(self):
        return f"{self.__brand} {self.model}"


class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size


my_tesla = ElectricCar("Tesla", "Model S", "1122KWh")
# print(my_tesla.model)
print(my_tesla.get_brand())

# my_car = Car("Toyata","Corolla")
# print(my_car.brand)
# print(my_car.model)
# print(my_car.full_name())

# my_new_car = Car("Ford","Mustang")
# print(my_new_car.model)
