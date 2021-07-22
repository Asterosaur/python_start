class Car:
    speed = 100
    color = "white"
    name = "TACHKA"
    is_police = True

    def go(self):
        print(f"{self.name} поехала")

    def stop(self):
        print(f"{self.name} остановилась")

    def turn(self,direction = "в никуда"):
        print(f"{self.name} повернула {direction}")

    def show_speed(self, current_speed):
        print(f"{self.name} едет со скоростью {current_speed}")


class TownCar(Car):
    name = "LADA"

    def show_speed(self, current_speed):
        Car.show_speed(self,current_speed)
        if current_speed>60:
            print(f"ПРЕВЫШЕНА СКОРОСТЬ")


class SportsCar(Car):
    speed = 1000
    name = "LADA SPORT"


class PoliceCar(Car):
    is_police = True
    name = "UAZ"


class WorkCar(Car):
    name = "BOOHANKA"

    def show_speed(self, current_speed):
        Car.show_speed(self, current_speed)
        if current_speed > 40:
            print(f"ПРЕВЫШЕНА СКОРОСТЬ")


car_1 = TownCar()
car_2 = SportsCar()
car_3 = PoliceCar()
car_4 = WorkCar()

print(car_1.name,car_2.color,car_3.is_police,car_4.name)
car_4.show_speed(1000)
car_3.turn("по-полицейски")
car_2.go()
car_1.stop()
