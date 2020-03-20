age = 25
# 'str' is a funtion to convert everything to String
print("My age is " + str(age) + " years")
# Using format function , you can convert int to String. This similar to Java String.format function
print("My age is {0} years".format(age))

#Below values replaces {} in order
print("There are {0} days in {1},{2},{3},{4},{5},{6} and {7}".format(31,
"January","March","May","July","August","October","December"))

# Below example iterate number from 1 to 12
# {0:2} before colon indicates the replacement field number and after code indicates the width
# ** 2 will multiple the integer twice ,** 3 will multiple the integer thrice
#{o:<2} '<' indicate the alignment to be left
for i in range(1,12) :
    print("No. {0:2} squared is {1:4} and cubed is {2:4}".format(i,i ** 2, i ** 3))
for i in range(1,12) :
    print("No. {0:2} squared is {1:<4} and cubed is {2:<4}".format(i,i ** 2, i ** 3))
# Second part of the colon indicates the how many precision have to print
print("Pi is approximately {0:12.50f}".format(22/7))

#If you are not providing any replacement filed number ,it set the value for that
for i in range(1,12) :
    print("No. {:2} squared is {:4} and cubed is {:4}".format(i,i ** 2, i ** 3))

