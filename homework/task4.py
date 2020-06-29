class Car:

    def __init__(self, speed, color, name):
        self.speed = int(speed)
        self.color = color
        self.name = name
        self.is_police = False

    def go(self):
        if self.speed != 0:
            print(f'{self.color} {self.name} проехала со скоростью {self.speed}')

    def stop(self):
        if self.speed == 0:
            print(f'{self.color} {self.name} остановилась')

    def turn(self, direction):
        print(f'{self.color} {self.name} повернула {direction}')

    def police(self):
        if self.is_police:
            print('Полицейская машина')
        else:
            print('Не полицейская машина')

    def show_speed(self):
        print(f'Текущая скорость: {self.speed}')


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f'{self.color} {self.name} привысил скорость на: {self.speed - 40}')
        else:
            print('Скорость нормальная')


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f'{self.color} {self.name} привысили скорость на: {self.speed - 40}')
        else:
            print('Скорость нормальная')


class SportCar(Car):
    pass


class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)
        self.is_police = True


bmw = Car(60, 'red', 'bmw')
bmw.go()
bmw.stop()
bmw.turn('прямо')
bmw.turn('назад')
bmw.turn('влево')
bmw.turn('вправо')
bmw.show_speed()

opel = TownCar(75, 'Зеленый', 'Opel')
opel.go()
opel.stop()
opel.show_speed()

truck = WorkCar(50, 'Жёлтый', 'Зил')
truck.go()
truck.show_speed()

mercedes = SportCar(150, 'blue', 'Mercedes')
mercedes.go()
mercedes.turn('влево')

oka = PoliceCar(90, 'yellow', 'Oka')
oka.go()
oka.police()

