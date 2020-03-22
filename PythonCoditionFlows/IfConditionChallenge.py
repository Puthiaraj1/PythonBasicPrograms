# Write a small program to check the user is eligible for 18-30 holiday club
name = input("Please enter your name :")
age = int(input("Please enter your age :"))
if 18 <= age <= 30:
    print(" Welcome to the holiday {}".format(name))
else:
    print("Sorry to inform {}, your not eligible for this holiday".format(name))