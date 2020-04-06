fruit = {"orange": "a sweet, orange, citrus fruit",
         "apple": "good for making cider",
         "lemon": "a sour yellow citrus fruit",
         "grape": "a small, sweet fruit growing in bunches",
         "banana": "good for breakfast"}

print(fruit)
# while True:
#     dict_key = input("Please select a fruit :")
#     if dict_key.casefold() == "quit":
#         break
#     description = fruit.get(dict_key,"We don't have a "+dict_key) # You can set default value to a dictionaries
#     print(description)
#
# # To iterate the fruit
# for snack in fruit:
#     print(fruit[snack])

# Print dictionaries in order
# for key in sorted(fruit.keys()):
#     print(key+ " - "+ fruit[key])
print(fruit.items()) # '.items()' will print dictionary as a list of tuples
f_tuples = tuple(fruit.items())
print(f_tuples)
print(dict(f_tuples)) # dict() will convert tuples into dictionary

