'''
Generally, libraries are bits of code written by you or others that you can use in your program.
Python allows you to share functions or features with others as “modules”.
'''

"""Random Module"""
import random
from random import choice
from random import randint

coin = "head", "tail"
print(random.choice(coin))

#calling the choice function directly from random module
print(choice(["head","tail"]))
print("tuhin")

# randint picks a value from a range
print(randint(1,10))

shuffle = ["apple","Mango","Orange","Coconut"]
print_shuffle = random.shuffle(shuffle)
for card in shuffle:
    print(card)



""" Statistics library """
import statistics

avarage = statistics.mean([10,20])
print(avarage)



"""Command line arguments"""

import sys
# sys is a module that allows us to take arguments at the command line.
# argv is a list inside the sys module. sys store the arguments in the argv varriabe
'''
print("Hello my name is",sys.argv[2])
print("Hello my name is",sys.argv[1])

try:
    print("Your name is", sys.argv[1])
except IndexError:
    print("Type an input in terminal")

if len(sys.argv) > 2:
    print("Too many arguments")
elif len(sys.argv) < 2:
    print("Too few arguments")
else:
    print("The fruit name is", sys.argv[1])

if len(sys.argv) > 2:
    sys.exit("Many arguments")
elif len(sys.argv) < 2:
    sys.exit("Few arguments")
else:
    print("Fruit name is", sys.argv[1])

'''


"""slice"""
# : represents everything in the list and 1 means start from 1 and after colon the -1 means reverse the list
'''
if len(sys.argv) < 2:
    sys.exit("Too few arguments")
for argv in sys.argv[1:-1]:
    print(argv)
'''


''' Packages'''
# packages are third party libraries. which is stored in a folder.
# to install packages use pip. pip install cowsay
import cowsay
cowsay.trex("Hello, Tomal")
cowsay.cow("Hello, Tuhin")



""" APIs """

'''
APIs or “application program interfaces” allow you to connect to the code of others.
requests is a package that allows your program to behave as a web browser would.
JSON is a text-based format that is used to exchange text-based data between applications.
'''
import requests
from sys import argv
import json

if len(argv) > 2:
    sys.exit()

responce = requests.get("https://itunes.apple.com/search?entity=song&limit=1&term=" + argv[1] )
#json.dumps returns a string object and indent give spaces before a line
print(json.dumps(responce.json(), indent = 2))

o = responce.json()
# change the limit value in the link to get more tracks

for result in o["results"]:
    print(result["trackName"])



"""Making your own libraries"""
# In the sayings.py
import sys

def main():
    hello(sys.argv[1])
    goodbye(sys.argv[1])
    
def hello(nam):
    print("Hello", nam)
def goodbye(nam):
    print("Goodbye", nam)

if __name__ == "__main__":
    main()

# In the say.py
# Using sayings.py as a library
'''
import sys
import sayings

sayings.hello(sys.argv[1])
sayings.main()
'''




