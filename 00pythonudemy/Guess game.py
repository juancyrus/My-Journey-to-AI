# Generate a random number between 1 and 9 (including 1 and 9).
# Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right. 
import random
Number = int(input("Guess a number between 1 and 9 including 1 and 9: "))
random_num = random.randint(1, 10)

for i in range(1):
    if Number == random_num:
        print("exactly right")
    elif Number < random_num:
        print("too low")
    else:
        print("too high")





