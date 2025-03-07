capitals = {"USA": "Washington D.C.",
            "India": "New Delhi",
            "China": "Beijing",
            "Russia": "Moscow"}
#print(dir(capitals))
#print(help(capitals))

#print(capitals.get("China"))

#country=(input("Enter the country: ")).capitalize()
#print(country)
#if capitals.get(country):
#    print(f"The country's capital is {capitals.get(country)}")
#else:
#    print('This capital does not exists')

#capitals.update({"Germany":"Berlin"})
#capitals.update({"USA":"Detroit"})

#capitals.pop("China")
#capitals.popitem()
#capitals.clear()

#keys=capitals.keys()

#print(keys)


#for key in capitals.keys():
 #   print(f"{capitals.get(key )}",end=' ')

#items=capitals.items()
#print(items)

#for key,value in capitals.items():
#    print(f"{key}:{value}")

'''
#menu list

menu = {"pizza":3.00,
        "nachos":4.50,
        "popcorn":6.00,
        "fries":2.50,
        "chips":1.00,
        "pretzel":3.50,
        "soda":3.00,
        "lemonade":4.25}
cart=[]
total=0
print('--------Menu---------')
for key,value in menu.items():
    print(f"{key:10}:${value:.2f}")
print('---------------------')
while True:
    food=input("Enter your food(q to quit): ").lower()
    #print(food)
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)
    
#print(cart)
print('--------Your order-------')
for food in cart:
    
    total+=menu.get(food)
    print(food,end=' ')
print()
print(f"Your bill is ${total:.2f}")


import random

#print(dir(random))
#print(help(random))

lowest_num=1
highest_num=100
answer=random.randint(lowest_num,highest_num)
guesses=0
is_running=True

while is_running:
    guess=(input(f"Please input a number between {lowest_num} and {highest_num}: "))
    #print (guess.isdigit())
    if guess.isdigit():
        guess=int(guess)
        guesses += 1
        if guess > highest_num or guess < lowest_num:
            print("The guess number is invalid")
            print(f"The number must between {lowest_num} and {highest_num}")
        elif guess > answer:
            print("Low")
            #print(answer,guesses)
        elif guess < answer:
            print("High")
            print(answer,guesses)
        else:
            print(f"correct! The answer was: {answer}")
            print(f"Number of guesses: {guesses}")
            is_running=False  
            
    else:
        print("The input is invalid")
        print(f"The number must between {lowest_num} and {highest_num}")
        
#print(guess)
#print(answer)
'''
import random

options=("paper","rock","scissors")
computer=random.choice(options)
#print(computer)
running=True
#while running:
#    player=None
#    computer=random.choice(options)

while player not in options:
    player=input(f"Your choice{options}(q to quit): ").lower()
    while True:
        if player == "q":
            break
        elif player == computer:
            print("Tie")
        elif player=="paper" and computer=="rock":
            print("You win")
        elif player=="rock" and computer=="scissors":
            print("You win")
        elif player=="scissors" and computer=="paper":
            print("You win")
        else:
            print("You lose")
        print(f"computer is :{computer}")
        print(f"player is :{player}")
        player_again=input("Would you like playing again(y or n): ").lower()
        if not player_again == "y":
            running=False
print("Thanks for playing")


    
    

