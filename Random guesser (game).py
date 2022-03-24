list=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50]
import random
import time
from colorama import init
from termcolor import colored
from colorama import Fore, Back, Style
x=random.choice(list)
print("Welcome to the random guesser game by Adhrit.")
print(".")
time.sleep(1)
print("How to play:")
time.sleep(1)
print("1. There are 4 levels in this game. ")
time.sleep(1)
print("2. Each next level gets harder.")
time.sleep(1)

print(".")
print(".")
print(".")
while True:
    time.sleep(1)
    print("Welcome to the 1st level.")
    print(".")
    time.sleep(1)
    print("Rules:")
    time.sleep(1)
    print("1. Python will choose any number between 1-50. ")
    time.sleep(1)
    print("2. You should first try to guess it.")
    time.sleep(1)
    print("3. If you do not get it correct, python will give you clues about it.Using these clues,you must find the number.")
    print(".")
    print(".")
    time.sleep(1)
    break

while True:
    time.sleep(.5)
    try:
        guess=input("Try to guess the number: ")
        print(".")
        guess=str(guess)
        guess=int(guess)
    except ValueError:
        guess=0
        print("Wrong.")

    if (guess==x):
        print(".")
        time.sleep(1)
        break
    elif (guess>x):
        print("Your guess is higher than the number, try decreasing your number and trying again.")
        print(".")
        time.sleep(1)
    elif (guess<x):
        print("Your guess is lower than the number, try increasing your number and trying again.")
        print(".")
        time.sleep(1)
    else:
        print("Error :( please retry")
        print(".")
        time.sleep(1)
init()
print(colored('Congratulations,you have passed the first level :) !', 'blue', 'on_white'))
print(".")
print(".")
time.sleep(1)
list=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100]
while True:
    x=random.choice(list)
    time.sleep(1)
    print("Welcome to the 2nd level.")
    print(".")
    time.sleep(1)
    print("Rules:")
    time.sleep(1)
    print("1. Python will choose any number between 1-100. ")
    time.sleep(1)
    print("2. You should first try to guess it.")
    time.sleep(1)
    print("3. If you do not get it correct, python will give you clues about it.Using these clues,you must find the number.")
    time.sleep(1)
    print(".")
    print(".")
    break

while True:
    time.sleep(.5)
    try:
        guess=input("Try to guess the number: ")
        print(".")
        guess=str(guess)
        guess=int(guess)
    except ValueError:
        guess=0
        print("Wrong.")
        print(".")

    if (guess==x):

        time.sleep(1)
        break
    elif (guess>x):
        print("Your guess is higher than the number, try decreasing your number and trying again.")
        print(".")
        time.sleep(1)
    elif (guess<x):
        print("Your guess is lower than the number, try increasing your number and trying again.")
        print(".")
        time.sleep(1)
    else:
        print("Error :( please retry")
        print(".")
        time.sleep(1)
init()
print(colored('Congratulations,you have passed the second level :) !', 'red', 'on_white'))
print(".")
print(".")
print(".")
time.sleep(1)
list= [i for i in range(1000)]
while True:
    x=random.choice(list)
    time.sleep(1)
    print("Welcome to the 3rd level.")
    print(".")
    time.sleep(1)
    print("Rules:")
    time.sleep(1)
    print("1. Python will choose any number between 1-1000. ")
    time.sleep(1)
    print("2. You should first try to guess it.")
    time.sleep(1)
    print("3. If you do not get it correct, python will give you clues about it.Using these clues,you must find the number.")
    print(".")
    print(".")
    time.sleep(1)
    break
while True:
    time.sleep(.5)
    try:
        guess=input("Try to guess the number: ")
        print(".")
        guess=str(guess)
        guess=int(guess)
    except ValueError:
        guess=0
        print("Wrong.")

    if (guess==x):

        time.sleep(1)
        break
    elif (guess>x):
        print("Your guess is higher than the number, try decreasing your number and trying again.")
        print(".")
        time.sleep(1)
    elif (guess<x):
        print("Your guess is lower than the number, try increasing your number and trying again.")
        print(".")
        time.sleep(1)
    else:
        print("Error :( please retry")
        time.sleep(1)

init()
print(colored('Congratulations,you have passed the third level :) !', 'green', 'on_white'))
print(".")
print(".")
print(".")
time.sleep(1)
list= [i for i in range(7500)]
while True:
    x=random.choice(list)
    time.sleep(1)
    print("Welcome to the 4th level.")
    print(".")
    time.sleep(1)
    print("Rules:")


    time.sleep(1)

    print("1. Python will choose any number between 1-7500. ")
    time.sleep(1)
    print("2. You should first try to guess it.")
    time.sleep(1)
    print("3. If you do not get it correct, python will give you clues about it.Using these clues,you must find the number.")
    time.sleep(1)
    print("4. This level has usage limit(You must find the number in 15 attemts.)")

    time.sleep(1)
    print(".")
    print(".")
    time.sleep(1)
    break
kkooll=16
while True:

    time.sleep(.5)
    try:
        guess=input("Try to guess the number: ")
        kkooll=kkooll-1
        print(".")
        guess=str(guess)
        guess=int(guess)
    except ValueError:
        guess=0
        kkooll=kkooll-1
        print("Wrong.")

    if (guess==x) and (kkooll!=0) :
        time.sleep(1)
        break
    elif (guess>x) and (kkooll!=0):
        print("Your guess is higher than the number, try decreasing your number and trying again.(",kkooll,"chances left)")
        print(".")
        time.sleep(1)
    elif (guess<x) and (kkooll!=0):
        print("Your guess is lower than the number, try increasing your number and trying again.(",kkooll,"chances left)")
        print(".")
        time.sleep(1)
    elif (kkooll==0) and (guess!=x):
        print("Chances up(no chances left)")
        time.sleep(1)
        time.sleep(9)
        time.sleep(9)
        time.sleep(9)
        time.sleep(9)
        time.sleep(9)
        time.sleep(9)
        time.sleep(9)
        time.sleep(9)
        time.sleep(9)
        time.sleep(9)
        time.sleep(9)
        time.sleep(9)
        time.sleep(9)
        time.sleep(9)
        time.sleep(9)
        time.sleep(9)
        time.sleep(9)
        time.sleep(9)
        time.sleep(9)
        time.sleep(9)
        time.sleep(9)
        time.sleep(9)
        time.sleep(9)
        time.sleep(9)
        time.sleep(9)
        time.sleep(9)
        time.sleep(9)
        time.sleep(9)
        time.sleep(9)
        time.sleep(9)
x=25
while x>0:
    lom=["white","blue","magenta","green","cyan","red","yellow"]
    mom=["red","cyan","blue","yellow","white","green","magenta"]
    z=random.choice(mom)
    m=random.choice(lom)
    z=str(z)
    m=str(m)
    time.sleep(1)

    message='''


____________________________________
|                                  |
|  |   |                           |
|  |___|  ____                     |
|    |   |    |  |    |            |
|    |   |____|  |____|            |
|                                  |
|                                  |
|  |     |                         |
|  |_____|  ____         ___       |
|  |     | |    |  \  / | __|      |
|  |     | |____|\  \/  |____      |
|                                  |
|                                  |
|  |           |                   |
|  |           |  _____  \ _____   |
|  |     |     | |     |  |     |  |
|  |_____|_____| |_____|  |     |  |
|__________________________________|






    '''
    ftty="on_"+z
    init()
    print(colored(message,m,ftty))

    x=x-1
time.sleep(2)
print("BYE :)")
