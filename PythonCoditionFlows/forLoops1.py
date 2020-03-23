number = "9,223,372,036,854,775,807"
onlyNumber = ''
for char in number:
    if char in '0123456789':
        onlyNumber = onlyNumber + char
newNumber = int(onlyNumber)
print("The number is {}".format(newNumber))

# Iterate array of strings
for state in ["not pinin'","no more","a stiff","bereft of life"]:
    print("This parrot is "+state)
    #print("This parrot is {}".format(state))
# For loop range with 3 parameter. 3rd parameter will jump those values in range
for i in range(0,100,5):
    print("i value is {}".format(i))

# Print math tables using for loops
for i in range(1,13):
    print("======================================")
    for j in range(1,13):
        print("{1:2} times {0:2} is {2:4} ".format(i,j, i*j))