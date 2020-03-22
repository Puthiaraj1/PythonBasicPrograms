age = int(input("How old are you ?"))

# Adding multiple condition check(AND) in if statement. You can use brackets/Parenthesis for more clear
if (age >= 16) and (age <= 65):
    print("Have a good day at work")
# Other way to check age between the limit
if 10 <= age <= 65:
    print("Have a good day at work")

# Adding multiple condition check (OR) in if statement.
if (age < 16 ) or (age > 65):
    print("Enjoy your free time ")
else:
    print("Have a good day at work")

# Since python does not have defined data type like java. It will have boolean data type
x = input("Please enter some text")
if x:
    print("You entered '{}'".format(x))
else:
    print("You did not entered anything")
print(not False) # Returns binary 1 as True
print(not True) # Retruns binary 0 as False

parrot = " Norwegian Blue"
letter = input("Enter a character: ")

# 'in' condition is case sensitive.Similarly you can use 'not in'
if letter in parrot:
    print("Give me an {} , Raj".format(letter))
else:
    print("I don't meed that letter")

if letter not in parrot:
    print("I don't meed that letter")
else:
    print("Give me an {} , Raj".format(letter))

