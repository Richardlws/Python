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


class Book():
    def __init__(self,title,author,num_pages):
        self.title = title
        self.author = author
        self.num_pages = num_pages
    def __str__(self):
        return f"'{self.title}' by {self.author}"
    def __eq__(self,other):
        return (self.title == other.title and self.author == other.author)
    def __lt__(self,other):
        return (self.num_pages < other.num_pages)
    def __add__(self,other):
        return (self.num_pages + other.num_pages)
    def __contains__(self, keyword):
        return keyword in self.title or keyword in self.author
    def __getitem__(self,key):
        if key == "title":
            return self.title
        if key == "author":
            return self.author
        elif key == "num_pages":
            return self.num_pages
        else:
            return f"key {key} was not found"
book1 = Book("The Hobbit","J.R.R Tolkien",310)
book2 = Book("Harry Potter and The Philosopher's Stone","J.K. Rowling",223)
book3 = Book("The Lion,the Witch and the Wardrobe","C.S. Lewis",172)

#print(book1)
#print(book2)
#print(book3)
#print(book1 == book2)
#print(book1 > book2)
#print(book1 + book2)
#print("Rowling" in book2)
print(book2['audio'])




def add_sprinkles(fun):
    def wrapper():
        print("*You add sprinkles 🍓*")
        fun()
    return wrapper

@add_sprinkles
def get_ice_cream():
    print("Here is your ice cream 🍨")

get_ice_cream()



import os
file_path = "test.txt"
if os.path.exists((file_path)):
    print(f"The location '{file_path}' exists.")
else:
    print(f"The location '{file_path}' doesn't exist.")'





txt_data = "I like pizza!"
file_path="output.txt"

with open(file_path,"x") as file:
    file.write(txt_data)
    print(f"txt file '{file_path}' was created")




from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from bs4 import BeautifulSoup

# 1. 启动 Chrome 浏览器（确保安装 `chromedriver`）
driver = webdriver.Edge()

# 2. 访问百度首页
driver.get("https://www.baidu.com")

# 3. 等待页面加载
time.sleep(2)

# 4. 获取完整的 HTML
html = driver.page_source
soup = BeautifulSoup(html, "html.parser")

# 5. 提取标题
if soup.title:
    print("百度首页标题:", soup.title.text)
else:
    print("未找到 <title> 标签")

# 6. 关闭浏览器
driver.quit()
'''
























