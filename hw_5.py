class Stationery:
    title = ""

    def draw(self):
        print("ЗАПУСК ОТРИСОВКИ")


class Pen(Stationery):
    def draw(self):
        print("ЗАПУСК ШАРИКОВОЙ ОТРИСОВКИ")


class Pencil(Stationery):
    def draw(self):
        print("ЗАПУСК ГРАФИТНОЙ ОТРИСОВКИ")


class Handle(Stationery):
    def draw(self):
        print("ЗАПУСК ЧЕРНИЛЬНОЙ ОТРИСОВКИ")


pen = Pen()
pencil = Pencil()
handle = Handle()

pen.draw()
pencil.draw()
handle.draw()
