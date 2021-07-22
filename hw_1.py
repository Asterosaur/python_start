from time import sleep


class TrafficLight:
    __states = ["red","yellow","green"]
    __delays = ["7000","2000","5000"]
    __color = "red"

    def running(self, state=0, auto=False):
        print(f"{self.__color}")
        self.__color = self.__states[state]
        sleep(float(self.__delays[state]))
        if auto:
            self.running(state)

    def try_next_state(self, next_state):
        if next_state == self.__states.index(self.__color) + 1:
            self.running(next_state)
        else:
            print(f"Поломатушки")
            exit()

my_light = TrafficLight();
my_light.try_next_state(2);