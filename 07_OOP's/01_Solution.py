# Create a Car Class with attributes like brandes and models. Than create an instance of Class.
class Car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

    def full_name (self):
        return f"{self.brand} {self.model}"

my_car = Car("Toyata","Corolla")
print(my_car.brand)
print(my_car.model)
print(my_car.full_name())

my_new_car = Car("Ford","Mustang")
print(my_new_car.model)