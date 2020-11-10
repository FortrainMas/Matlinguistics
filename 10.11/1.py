class Person:
    def __init__(self, name, surname, age):
        self.name=name
        self.surname=surname
        self.age=age
    def getFullName(self):
        return self.name + ' ' + self.surname

person1 = Person('Ivan', 'Shebanov', 15)
person2 = Person('Nikola', 'Lees', 12)

print(person1.getFullName())
print(person2.getFullName())