# In 'for' loop range will not take last value. Here it will run till 19
for i in range(1,20):
    print(" Value of i is now {}".format(i))

# Print each character of the String. len() will give you length of the String
# Here you no need to set length -1 unlike java
number = "9,223,372,036,854,775,807"
for i in range(0,len(number)):
    print(number[i])

# Print only the number from the input string
# you can use special funtion to print in one line
number = "9,223,372,036,854,775,807"
for i in range(0,len(number)):
    if number[i] in '0123456789':
        print(number[i],end='')

# Set only the number to a variable
number = "9,223,372,036,854,775,807"
onlyNumber = ''
for i in range(0,len(number)):
    if number[i] in '0123456789':
        onlyNumber += number[i]
newNumber = int(onlyNumber)
print("The number is {}".format(newNumber))