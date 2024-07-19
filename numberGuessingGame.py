import math
import random

lower = int(input("LOWER BOUND :"))
upper = int(input("UPPER BOUND :"))

x = random.randint(lower,upper)
total_chances = math.ceil(math.log(upper - lower + 1,2))

print("\n\t YOu've only ", total_chances," to guess.");

count = 0
guessed = False;

while count < total_chances:
    count +=1
    guess = int(input("ENTER GUESS: "))

    if (x == guess) :
        print("CONGRATS, YOU WIN")
        guessed = True
        break
    elif x > guess:
        print("TOO SMALL")
    else:
        print("TOO HIGH")

if (guessed == False):
    print("\n The number is %d",x)
    print("GOODBYE")
