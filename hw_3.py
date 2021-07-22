class Worker:
    name = "John"
    surname = "Smith"
    position = "Janitor"
    income = {
        "wage": 10,
        "bonus": 20
    }

    def __init__(self, name, surname, position, wage, bonus):
        self.position = position
        self.surname = surname
        self.name = name
        self.income = {"wage":int(wage),"bonus":int(bonus)}


class Position(Worker):

    def get_full_name(self):
        return f"{self.name} {self.surname}"

    def get_total_income(self):
        return sum(self.income.values())


true_man = Position("Oleg", "Bears", "BigBoss", "10000000000000", "12312321312312321321321")
print(f"{true_man.position} {true_man.get_full_name()} gets {true_man.get_total_income()}$")
