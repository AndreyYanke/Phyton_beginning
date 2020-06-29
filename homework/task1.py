
from time import sleep


class TrafficLight:
    color = ['red', 'yellow', 'green']
    def running(self):
        self.res = print(light.color[0])
        sleep(7)
        self.res = print(light.color[1])
        sleep(2)
        self.res = print(light.color[2])
        sleep(6)



light = TrafficLight()
light.running()
