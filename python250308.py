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

def show_balance():
    print("***************************")
    print(f"Your balance is $ {balance:.2f}")
def deposit():
    amount=float(input("Enter your deposit: "))
    if amount < 0:
        print("Invalid input")
        return 0
    else:
        return amount
        #return balance
def withdraw():
    amount=float(input("Enter your withdraw: "))
    if amount > balance:
        print("insufficiency")
        return 0
    elif amount < 0:
        print("The amount should be more than 0")
        return 0
    else:
        return amount
        #return balance


#main()
#show_banlance(200)
#deposit(50)
#withdraw(250)

def main():
    balance=0
    is_running=True
    while is_running:
        print("-------------Bank Programme-------------")
        print("1.Show your banlance")
        print("2.Enter your deposit")
        print("3.Enter your withdraw")
        print("4.Exit")
        num=int(input("Please input your choice(1-4): "))
        if num==1:
            show_balance()
        elif num==2:
            balance+=deposit()
        elif num==3:
            balance-=withdraw()
        elif num==4:
            is_running=False
        else:
            print("Invalid input")
    print("Thanks for using")

if __name__=="__main__":
    main()



