class Student:
    school = "GuangRongXiang"
    count = 0
    def __init__(self, name, sid, grade):
        self.name = name
        self.sid = sid
        self.grade = grade
        Student.count += 1

    def info(self):
        return(f"Name:{self.name}, Sid:{self.sid}, Grade:{self.grade}")

s1 = Student("zhangsan", "202301", "3rd")
s2 = Student("lisi","202302","4th")

print(s1.info())
print(s2.info())
print(f"Name of the School:{Student.school}\nNumber of students:{Student.count}")

