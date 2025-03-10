'''
import random
import string

chars = "" + string.whitespace+string.punctuation + string.digits + string.ascii_letters

chars = list(chars)

key = chars.copy()

random.shuffle(key)

print(f"chars:{chars}")
print(f"key: {key}")

#ENCRYPT
plain_text = input("Enter a message to encrypt: ")
cipher_text = ""

for letter in plain_text:
    index = chars.index(letter)
    cipher_text += key[index]
    #print(f"index: {index}")
    #print(f"cipher_text: {cipher_text}")
print(f"original message: {plain_text}")
print(f"encrypted message: {cipher_text}")

#DECRYPT
plain_text = input("Enter a message to decrypt: ")
cipher_text = ""

for letter in plain_text:
    index = key.index(letter)
    cipher_text += chars[index]
print(f"encrypted message: {plain_text}")
print(f"original message: {cipher_text}")

'''
#Hangman in Python
import random
from Wordlist import words
#import sys



#dictionary of key:()

hangman_art={0:("   ",
               "   ",
               "   "),
            1:(" o ",
               "   ",
               "   "),
            2:(" o ",
               " | ",
               "   "),
            3:(" o ",
               "/| ",
               "   "),
            4:(" o ",
               "/|\\ ",
               "   "),
            5:(" o ",
               "/|\\ ",
               "/   "),
            6:(" o ",
               "/|\\ ",
               "/  \\ ")}




def display_man(wrong_guesses):
    print("*************")
    for line in hangman_art[wrong_guesses]:
        print(line)
    print("*************")

def display_hint(hint):
    print(" ".join(hint))
    #print(hint)
def display_answer(answer):
    print(" ".join(answer))

def main():
    #sys.stdin.reconfigure(encoding="utf-8")
    answer = random.choice(words)
    hint = ["_"] * len(answer)
    wrong_guesses = 0
    guessed_letters = set()
    is_running = True

    while is_running:
        display_man(wrong_guesses)
        display_hint(hint)
        #display_answer(answer)
        print(answer)
        print(type(answer))
        print(type(words))
        guess = input("Enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input")
            continue

        if guess in guessed_letters:
            print(f"{guess} is already guessed")
            continue

        guessed_letters.add(guess)

        if guess in answer:
            for i in range(len(answer)):
                if answer[i] == guess:
                    hint[i] = guess
        else:
            wrong_guesses+=1

        if "_" not in hint:
            display_man(wrong_guesses)
            display_answer(answer)
            print("You win!")
            is_running = False
        elif wrong_guesses >= len(hangman_art) - 1:
            display_man(wrong_guesses)
            display_answer(answer)
            print("You lose!")
            is_running = False
            #print(hint)
            #print(i)
        #print(answer)
        #print(guess)
        #print(wrong_guesses)


if __name__=="__main__":
    main()







#answer = random.choice(words)
#print(answer)
#print(guess)
#pring(wrong_guessesa)