numbers = [1, 45, 31, 16, 60]

for number in numbers:
    if number % 8 == 0:
        # reject the list
        print("The number are unacceptabl")
        break
else: # Else for a loop will check all the elements are processed successfully
    print("All those numbers are fine")