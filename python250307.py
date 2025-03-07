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

'''

