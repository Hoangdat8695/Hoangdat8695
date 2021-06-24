class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("hello " + self.name)

person = Person("Dat", 26)
person.display()
