import random
import nltk
from nltk.corpus import words
nltk.download('words')
word_list = words.words()

words = [random.choice(word_list) for _ in range(100)]
