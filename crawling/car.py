class Car:
    count_car = 0

    def __init__(self, name, displacement, year):
        self.__name = name
        self.__displacement = displacement
        self.__year = year
        Car.count_car+=1

    def print_car_name(self):
        print(f"차의 이름은 {self.__name} 입니다.")

    def change_car_name(self, newname):
        self.__name = newname

    def car_count(self):
        print(f"총 차의 개수는 {self.count_car} 입니다.")

    def car_displacement(self):
        if self.__displacement < 1000:
            print(f"이 차는 {self.__displacement} 소형 입니다.")
        elif 1000 <= self.__displacement <= 2000:
            print(f"이 차는 {self.__displacement} 중형 입니다.")
        else:
            print(f"이 차는 {self.__displacement} 대형입니다.")


car1 = Car("A", 900 , 1999)
car2 = Car("B", 2000, 2998)

car1.car_count()

car1.print_car_name()
car2.print_car_name()

car1.change_car_name("Z")
car1.print_car_name()

car3 = Car("C", 2001 , 2001)

car1.car_count()
print("\n")
car1.car_displacement()
car2.car_displacement()
car3.car_displacement()
