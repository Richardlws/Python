'''
class Car:
    def __init__(self,model,year,color,for_sale):
        self.model=model
        self.year=year
        self.color=color
        self.for_sale=for_sale

    def driver(self):
        print(f"You drive the {self.color} {self.model}")

    def stop(self):
        print(f"You stop the {self.color} {self.model}")

    def describe(self):
        print(f"{self.year} {self.color} {self.model}")
car1 = Car("Mustang", 2024,"red",True)
car2 = Car("Corvette",2025,"blue",True)
car3 = Car("Charger",2026,"yellow",True)


car1.describe()

car1.driver()

car2.driver()

car3.stop()

class Student:
    years = 2024
    num_students = 0

    def __init__(self,name,age):
        self.name = name
        self.age = age
        Student.num_students += 1

student1 = Student("Spongebob",30)
student2 = Student("patrick",35)
student3 = Student("Squidward",55)
student4 = Student("Sandy",27)

print(f"My graduating class of {Student.years} has {Student.num_students} students")
print(Student.num_students)
print(student1.name)
print(student2.name)
print(student3.name)
print(student4.name)



class Animal:
    def __init__(self,name):
        self.name = name
        self.is_alive = True
    def eat(self):
        print(f"{self.name} is eating")
    def sleep(self):
        print(f"{self.name} is sleeping")

class dog(Animal):
    def speak(self):
        print(f"{dog.name} is woofing")
class cat(Animal):
    def speak(self):
        print("Meow")
class mouse(Animal):
    def speak(self):
        print("squeek")

dog = dog("Scooby")
cat = cat("Garfield")
mouse = mouse("Mickey")

mouse.speak()
mouse.eat()

dog.speak()



class Shape():
    def __init__(self,color,is_filled):
        self.color = color
        self.is_filled = is_filled
    def describe(self):
        print(f"The {self.color} and {'filled' if self.is_filled else 'not filled'}")

class Circle(Shape):
    def __init__(self,color,is_filled,radius):
        super().__init__(color,is_filled)
        self.is_filled = is_filled
        self.radius = radius
    def describe(self):
        super().describe()
        print(f"It's a circle with an area of {3.14*self.radius**2}cm^2")

circle = Circle("red",False,5)

print(circle.color)
circle.describe()

'''

