from abc import ABC, abstractmethod
class Clothes(ABC):
    def __init__(self, param):
        self.param= param
    @property
    @abstractmethod
    def consumption (self):
        pass

    def __add__(self, other):
        return self.consumption+other.consumption
class Coat(Clothes):
    @property
    def consumption(self):
        print('Расход на производство пальто - ',  round(self.param(6.5))+ 0.5, "м ткани")
        return round (self.param(6.5)+ 0.5)
class Costume(Clothes):
    @property
    def consumption(self):
        print ('Расход на производство костюма', (2*self.param+0.3)/100, 'м ткани')

coat = Coat(48)
costume = Costume(176)
print(coat + costume)
