fruit = {"orange": "a sweet, orange, citrus fruit",
         "apple": "good for making cider",
         "lemon": "a sour yellow citrus fruit",
         "grape": "a small, sweet fruit growing in bunches",
         "banana": "good for breakfast"}
print(fruit)

veg = {"carrot": "Sweet kids favor",
       "beetroot": "Good for blood",
       "spinach": " Source of protein"}

print(veg)

# Dictionary update
# veg.update(fruit)
# print(veg)

fruit_and_veg = fruit.copy()
fruit_and_veg.update(veg)
print(fruit_and_veg)