# Using continue you can byPass the item to next
shopping_list = ["milk","pasta","eggs","spam","bread","rice"]
for item in shopping_list:
    if item == 'spam':
        continue
    print("Buy "+item)

# If the break statement never executed then it will execute the else statement
meal = ["rice", "egg", "veggie", "chicken"]
nasty_food_item = ""
for item in meal:
    if item == 'sausages':
        nasty_food_item = item
        break
else:
    print("I'll have a plate of that, then, please")
if nasty_food_item:
    print(" Can't I having anything without {} in it".format(nasty_food_item))
