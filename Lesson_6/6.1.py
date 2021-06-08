from time import sleep
class TrafficLight:
    __color = 'white'
    def running(self):
        while True:
            print("\33[31mLight is red")
            sleep(0.2)
            print("\33[31m\33[43mLight is red and yellow")
            sleep(0.2)
            print("\33[32m\33[48mLight is green")
            sleep(0.2)
            print("\33[33m\33[48mLight is yellow")
            sleep(0.2)

light = TrafficLight()
light.running()