# Range in python is a sequance operator . It can be used for 'For Loop ' and If condition
age = input("How old are you? ")

if age in range(16, 66):
    print("Have a good day at work")
else:
    print("Enjoy your free time")

for i in range(10): # range without a start
    print("i is now {}".format(i))
