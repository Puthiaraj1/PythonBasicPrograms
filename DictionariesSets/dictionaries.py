# Dictionaries can access only through key - value pair
# These are all immutable. Dictionaries are un-ordered value
fruit = {"orange": "a sweet, orange, citrus fruit",
         "apple": "good for making cider",
         "lemon": "a sour yellow citrus fruit",
         "grape": "a small, sweet fruit growing in bunches",
         "banana": "good for breakfast"}
# If you have duplicate key in Dictionary. It will take the last value

car = {"make": "mazda",
       "model": "Mazda 6",
       "capacity": 4,
       "color": "Red"}

print(car)
print(car["capacity"])
# To Add a value to an existing dictionary. If you're using an existing key it will replace the old value
fruit["melon"] = "Good fruit with more water"
print(fruit)
fruit["melon"] = "Great fruit for summer season"
print(fruit)
# del command to remove a key - value pair from dictionary
del fruit["melon"]
print(fruit)

# To get the value you can use .get()
print(fruit.get("banana"))

# To clear a dictionary use .clear() method
fruit.clear()
print(fruit)



