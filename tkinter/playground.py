# # input tuple
# def add(*n):
#     sum = 0
#     for i in n:
#         sum += i
#     print(sum)
#
# add(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)


# input dictionary
def calculate(n, **kwargs):
    # print(kwargs)
    # for key, value in kwargs.items():
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(2, add=3, multiply=5)


class Car:

    def __init__(self, **kw):
        self.make = kw["make"]
        self.model = kw["model"]


my_car = Car(make="Nissan", model="GT-R")
print(my_car.model)