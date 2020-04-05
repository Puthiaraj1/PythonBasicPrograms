item_list = ["Exit","Learn Python", "Learn Java", "Practice coding", "Go for a walk", "Take some rest"]
print("Please choose your option from the list:")
for item_index in range(len(item_list)):
    print("{}. {}".format(item_index,item_list[item_index]))

your_option = int(input("Please select your option :"))
while your_option != 0:
    if your_option < len(item_list):
        print("You selected {} and you're going to do {} ".format(your_option, item_list[your_option]))
        your_option = int(input("Please choose different option :"))
    else:
        print("Your selection {} not in the option.Please choose from the above list ".format(your_option))
        your_option = int(input("Please choose different option :"))
else:
    print("Your out of game now")
