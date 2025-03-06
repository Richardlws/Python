#quiz game

questions=("How many elements are in the periodic table?: ",
           "Which animal lays the largest eggs?: ",
           "What is the most abundant gas in Earth's atmosphere?: ",
           "How many bones are in the human body?: ",
           "Which planet in the solar system is the hottest?: ")

options=(("A.116","B.117","C.118","D.119"),
         ("A.220","B.221","C.223","D.224"),
         ("A.311","B.312","C.313","D.314"),
         ("A.411","B.412","C.413","D.414"),
         ("A.511","B.512","C.513","D.514"))

answers=("A","C","D","B","C")
guesses=[]
score = 0
question_num = 0


for question in questions:
    print("----------------")
    print(question)
    for option in options[question_num]:
        print(option)
    guess=input("Please input your choice(A B C D): ").upper()
    guesses.append(guess)
    for answer in answers[question_num]:
        print(f"The answer is {answer}")
    question_num+=1
    if guess == answer:
        print("It's corrcet")
        score+=1
    else:
        print(f"It's incorrect,{answer} is the correct")
print("-----------------------------")
print("---------RESULT--------------")
print("-----------------------------")
print("Your guess is :",end=" ")
for guess in guesses:
    print(guess,end="")
print()
print("Your answer is :",end=" ")
for answer in answers:
    print(answer,end="")
print()
#print(f"Your guess is {guesses}")
#print(f"The answer is {answers}")
print(f"Your socore is {int( (score/question_num)*100)}")
#print(guesses)
#print(type(questions))
#print(type(options))
