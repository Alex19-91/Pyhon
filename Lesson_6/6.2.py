class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width
    def calculus(self):
        return (self._length*self._width*5*5/1000,'т')
m=Road(100,10)
print(m.calculus())
