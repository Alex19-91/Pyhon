class Stationery:
    def __init__(self, title="Чем ты умеешь рисовать?"):
        self.title = title

    def draw(self):
        print(f"Любишь рисовать?! {self.title}")


class Pen(Stationery):
    def draw(self):
        print(f"Рисуй {self.title} ручкой, если другого нет под рукой!")


class Pencil(Stationery):
    def draw(self):
        print(f"Но лучше {self.title} карандашом!")


class Marker(Stationery):
    def draw(self):
        print(f"А можно и {self.title} маркером!")


stat = Stationery()
stat.draw()
pen = Pen("шариковой")
pen.draw()
pencil = Pencil("простым")
pencil.draw()
marker = Marker("перманентным")
marker.draw()