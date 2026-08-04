class Car:
    def __init__(self):
        print("this is car")

car = Car()

class Intro:
    def __init__(self,name):
        self.name = name

n1= Intro("tehmina")
print(n1.name)


class Student:
    def __init__(self , name , age):
        self.name = name
        self.age = age

    def print_intro(self):
        print(f"my name is {self.name} and my age is {self.age}" )

s1 = Student('Tehmina' , 22)
s1.print_intro()