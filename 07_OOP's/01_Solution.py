class Car:
    total_car = 0

    def __init__(self, brand, model):
        self.__brand = brand
        self.__model = model
        Car.total_car += 1

    def get_brand(self):
        return self.__brand + " !"

    def full_name(self):
        return f"{self.__brand} {self.__model}"

    def fuel_type(self):
        return "Petrol or Diesel"

    @staticmethod
    def general_description():
        return "Cars are means of transport"

    @property
    def model(self):
        return self.__model


class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def fuel_type():
        return "Electric charge"






# blue_box = Car("Ford","Mustang")
# print(blue_box.fuel_type())

# # my_car = Car("Toyata","Corolla")
# # print(my_car.brand)
# # print(my_car.model)
# # print(my_car.full_name())

# # my_new_car = Car("Ford","Mustang")
# # print(my_new_car.model)
