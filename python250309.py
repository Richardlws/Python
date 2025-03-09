
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

words=("apple","orange","banana","coconut","pineapple")

#dictionary of key:()

hanman_art={0:("   ",
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
'''