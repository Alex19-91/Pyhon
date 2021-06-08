
class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage":wage, "bonus": bonus}

class Position(Worker):
    def get_full_name(self):
        return self.name, self.surname

    def get_full_profit(self):
        return sum(self._income.values())

p=Position("Joseph", "Wilkin", "Engineer", 4000, 500)
print(p.position)
print(p.get_full_name())
print(p.get_full_profit())



