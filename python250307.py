'''
def net_price(price,discount=0,tax=0.05):
    return price*(1-discount)*(1+tax)


print (f"Your total price is :{net_price(100,0,0.01)}")

import time
def count(end,start=1):
    for x in range (start,end+1):
        print(x)
        time.sleep(1)
    print("Done")
n=int(input("please input the count #: "))
count(n)


def shipping_label(*args,**kwargs):
    for arg in args:
        print(f"{arg} ",end="")
    print()

    #for kwarg in kwargs:
    print(f"{kwargs.get("street")}",end='')
    if "apt" in kwargs:
        print(f"{kwargs.get("apt")}")
    else:
        print()
    print(f"{kwargs.get("city")} {kwargs.get("state")} {kwargs.get("zip")}",end="")

   
shipping_label("Dr.","Spongebob","Squarepants",
               street="123 Fake St.",
               apt="#100",
               city="Detroit",
               state="MI",
               zip="54321")

mydict={"A":1,"B":2,"C":3}
#for key in mydict:
#    print(f"{key} = ",end='')
#    print(mydict.get(key))
#    for value in mydict.values():
#        print(value)

for key,value in mydict.items():
    print(f"{key} = {value}")



word="apple"

letter=input("Please input a letter: ")

if letter in word:
    print(f"The {letter} is in the {word}")
else:
    print(f"The {letter} isn't in the {word}")


students={"Spongebob","Patrick","Sandy"}

student=input("Please input name: ")
if student not in students:
    print(f"{student} not found")
else:
    print(f"{student} is a student")


grades={"Sandy":"A","Squidward":"B","Spondgebob":"C","Patrick":"D"}

student=input("Please input the name: ")

if student in grades:
    print(f"{student}'s grade is {grades[student]}")
else:
    print(f"{student} not found")

email="BroCode@gmail.com"

if "@" in email and "." in email:
    print("valid")
else:
    print("invalid")

from tokenize import triple_quoted

doubles=[x*2 for x in range(1,11)]
triples=[y*3 for y in range(1,11)]
squares=[z**2 for z in range(1,11)]
print(squares)


numbers=[1,-1,-4,3,7,8,9,10,-16]

positive_num=[num for num in numbers if num>0]
negative_num=[num for num in numbers if num<0]
even_num=[num for num in numbers if num%2==0]
odd_num=[num for num in numbers if num%2==1]

print(positive_num)
print(negative_num)
print(even_num)
print(odd_num)

grades=[85,42,79,90,56,61,30]
letter=[]
for grade in grades:
    if grade >= 90:
        letter.append('A')
    elif grade>=80:
        letter.append('B')
    elif grade>=70:
        letter.append('C')
    elif grade>=60:
        letter.append('D')
    else:
        letter.append('Not pass')
print(letter)


def day_of_week(day):
    match day:
        case 1:
            return "It is Sunday"
        case 2:
            return "It is Monday"
        case 3:
            return "It is Tuesday"
        case 4:
            return "It is Wednesday"
        case 5:
            return "It is Thursday"
        case 6:
            return "It is Friday"
        case 7:
            return "It is Saturday"
        case _:
            return "Not a valid day"

print(day_of_week(3))

  '''
import example

print(example.zhouchang(3))


