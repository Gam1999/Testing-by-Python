class Employee:
    def __init__(self, salary):
        self.salary = salary

    def get_bonus(self):
        print("get bonus in Employee")
        return 0.1 * self.salary

    def get_tax(self):
        total = self.salary + self.get_bonus()

        return 0.07 * total