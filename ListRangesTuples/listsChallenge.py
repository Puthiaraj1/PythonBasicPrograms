# Write a program to create a meal with multiple list of items
# identify the meal without a chicken
# It prints out each of the ingredients of the meal;

menu = list()
menu.append(["veggie","egg","chicken"])
menu.append(["vegan","egg","chicken"])
menu.append(["vegan","veggie","chicken"])
menu.append(["vegan","veggie","egg"])
menu.append(["veggie","egg","veggie","egg","chicken"])
menu.append(["veggie","egg","chicken","vegan","egg","veggie","chicken"])

for meal in menu:
    if not "chicken" in meal:
        for item in meal:
            print(item)
