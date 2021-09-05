class Employee:
    company = "Google"
    eCode = 120


class Freelancer:
    company = "Fiver"
    level = 0

    def upgradeLevel(self):
        self.level = self.level + 1


class Programmer(Employee, Freelancer):
    name = "Mahadi Rahman"


p = Programmer()
print(p.company)
print(p.eCode)
print(p.name)
print(p.level)
p.upgradeLevel()
print(p.level)
