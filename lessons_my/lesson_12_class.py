class Person:
    name = "null"
    age = 0
    def __init__(self, name = "null", age = 0):
        self.name = name
        self.age = age
    def set1(self, name, age):
        self.name = name
        self.age = age
    def _set2(self, name, age):
        self.name = name
        self.age = age
    def __set3(self, name, age):
        self.name = name
        self.age = age


class Student(Person):
    course = 1
    def set1(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

ivan = Person

petr = Person()
petr.name = "Петя"
petr.age = "20"

katya = Person()
katya.set1("Катя",31)

olya = Student()
olya._set2("Катя",31)
olya._Person__set3("Оля",55)

oleg = Student("Олег", 38)


print(ivan.name + " " + str(ivan.age))
print(petr.name + " " + str(petr.age))
print(katya.name + " " + str(katya.age))
print(olya.name + " " + str(olya.age) + " курс " + str(olya.course))
print(oleg.name + " " + str(oleg.age) + " курс " + str(oleg.course))
oleg.set1("Олег",39,4)
print(oleg.name + " " + str(oleg.age) + " курс " + str(oleg.course))

