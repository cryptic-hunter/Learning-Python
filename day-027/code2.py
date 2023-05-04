#define function that can take any number of arguments

# def add(*args):
#     sum=0
#     for n in args:
#         sum += num
#     return sum

# add(3,5,6)


class Car:
    def __init__(self, **kwargs):
        self.make = kwargs.get("make")
        self.model = kwargs.get("model")

my_car = Car(make="Nissan", model="GT-R")
print(my_car.model)
print(my_car.make)