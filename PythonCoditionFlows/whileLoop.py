# for i in range(10):
#     print("i value is {}".format(i))
# Equivalent while loop expression below - "for" loop expression
#i = 0
# while i < 10:
#     print("i value is {}".format(i))
#     i+=1
# While loop executes until it fails . You can use break statement to quit from while loop
# you else condition to print "Successful message"
available_exits = ["east","north east","south"]
chosen_exit = ""
while chosen_exit not in available_exits:
    chosen_exit = input("Please choose a diffent exit:")
    if chosen_exit.casefold() == 'quit':
        print("Game over !!!")
        break
else:
    print("Successfully came out of the room !!")


