# the word is a<n>a<t>o<m>y
import time
import random

alphabets = ['n', 't', 'm']

for i in range(30):
    counter = i+1
    random.shuffle(alphabets)

    word = "a" + alphabets[0] + "a" + alphabets[1] + "o" + alphabets[2] + "y"
    
    print(f"{counter}: {word}")
    # time.sleep(0.5)