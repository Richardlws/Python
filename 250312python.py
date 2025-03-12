'''
class Animal:
    alive = True

class Dog(Animal):
    def speak(self):
        print("WOOF!")


class Cat(Animal):
    def speak(self):
        print("MEOW!")

class Car:

    alive = False
    def speak(self):
        print("HONK!")


animals = [Dog(),Cat(),Car()]

for animal in animals:
    animal.speak()
    print(animal.alive)

    #animal.speak
    #animal.speak

class Employee:

    def __init__(self,name,position):
        self.name = name
        self.position = position

    def get_info(self):
        return f"{self.name} = {self.position}"

    @staticmethod
    def is_valid_position(position):
        valid_positions = ["Manager","Cashier","Cook","Janitor","Rocket Scientist"]
        return position in valid_positions


employee1 = Employee("Eugnue","Manager")
employee2 = Employee("Squidward","Cashier")
employee3 = Employee("Spongebob","Cook")

print(Employee.is_valid_position("Rocket Scientist"))

print(employee1.get_info())
print(employee2.get_info())
print(employee3.get_info())





class Student:

    count = 0
    total_gpa = 0

    def __init__(self,name,gpa):
        self.name = name
        self.gpa = gpa
        Student.count += 1
        Student.total_gpa += gpa

    #INSTANCE METHOD
    def get_info(self):
        return f"{self.name}{self.gpa}"

    @classmethod
    def get_count(cls):
        return f"Total # of students:{cls.count}"

    @classmethod
    def get_average_gpa(cls):
        if cls.count == 0:
            return 0
        else:
            return f"The average gpa is {cls.total_gpa/cls.count:.2f}"

student1 = Student("Spongebob",3.2)
student2 = Student("Patrick",2.0)
student3 = Student("Sandy",4.0)

print(Student.get_count())
print(Student.get_average_gpa())

  '''
