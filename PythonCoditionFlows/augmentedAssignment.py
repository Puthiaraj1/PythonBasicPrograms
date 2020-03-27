number = "9,223,372,036,854,775,807"
cleanedNumber = ''

for i in range(0, len(number)):
    if number[i] in '0123456789':
        # cleanedNumber = cleanedNumber + number[i] -- This binary assignment
        # This can be replaced with below augmented assignment
        cleanedNumber += number[i]
newNumber = int(cleanedNumber)
print("The number is {}".format(newNumber))
