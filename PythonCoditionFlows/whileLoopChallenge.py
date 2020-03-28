# This guessing number challenge using python import
# You can write a logic in different method. Please feel free to change it for your convenient
import random

highest = 10
answer = random.randint(1, highest)
#
# print("Please guess a number between 1 and {}:".format(highest))
# guess = int(input())
# if guess != answer:
#     if guess < answer:
#         print("Please guess higher ")
#     else:
#         print("Please guess lower")
#     guess = int(input())
#     if guess == answer:
#         print(" Well done, you guessed it")
#     else:
#         print("Sorry, you have not guessed correctly")
# else:
#     print("You nailed it")

no_of_guess = 0
print("Please guess a number between 1 and {}:".format(highest))
guess = int(input())
while no_of_guess < 2:

    if guess == 0:
        print("You'r out of game !!")
        break
    elif guess != answer:
        if guess < answer:
            print("Please guess higher or enter 0 to quit ")
        else:
            print("Please guess lower or enter 0 to quit")
        guess = int(input())
        no_of_guess += 1
    else:
        print("You nailed it")
        break
else:
    print("Sorry, you have not guessed correctly")
