'''
def modify_tuple(tuples=()):
    tuples+=(1,)
    return tuples

tuple1=modify_tuple()
tuple2=modify_tuple()

print(tuple1)
print(tuple2)

def modify_list(list=[]):
    list.append(1)
    return list

list1=modify_list()
print(list1)
list2=modify_list()

print(list1)
print(list2)

def happy_birthday():
    print(f"Happy_birthday {name},You are {age} years old ")

def main():

    happy_birthday()


name="Felix"
age="8"
weigth="30kg"
main()



from math import e

def fun1():
    print(e)
e=3
fun1()




def x():
    print(2+3)
print(__name__)
if __name__=="__main__":
    x()
'''


