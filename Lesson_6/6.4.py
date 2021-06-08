class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        print (self.speed, self.color, self.name, self.is_police)

    def show_speed(self):
        print(self.speed)

    def go(self):
        print('Go')

    def stop(self):
        print('Stop')
    def turn(self, direction):
        print ('direction is', direction)


class TownCar(Car):
    def show_speed(self):
        print('Speed is:',self.speed if self.speed <60 else f'Превышение скорости на {self.speed-60} км/ч')
class SportCar(Car):
    def show_speed(self):
        print('Speed is:',self.speed if self.speed <180 else f'За вами уже выехали')

class WorkCar(Car):
    def show_speed(self):
        print('Speed is:',self.speed if int(self.speed) <40 else f'Превышение скорости на {int(self.speed)-40} км/ч')


class PoliceCar(Car):
    def __init__ (self, speed, color, name, is_police=True):
        super().__init__(speed, color, name, is_police)
    def show_speed(self):
         print('Speed is:',self.speed if self.speed <180 else 'Да-да, это мы, уиу, уиу')

police_car = PoliceCar (280, 'White', 'Ford')
police_car.go()
print(police_car.show_speed())
police_car.turn(0)
police_car.stop
print()
work_car = WorkCar('"Бетономешалка Бабетта"', 'оранжевая', 40)
work_car.go()
work_car.turn(1)
print(work_car.show_speed())
work_car.turn(0)
work_car.stop()

print()
sport_car = SportCar('"Молния McQueen"', 'красный', 190)
sport_car.go()
sport_car.turn(0)
print(sport_car.show_speed())
sport_car.stop()
print()

town_car = TownCar('"Пикап"', 'синий', 50)
town_car.go()
town_car.turn(1)
town_car.turn(0)
print(town_car.show_speed())
town_car.stop()