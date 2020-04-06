# farm_animals = {"sheep","cow","hen"}
# print(farm_animals)
#
# for animal in farm_animals:
#     print(animal)
#
# print("-" * 30)
# wild_animal = set(["lion", "tiger", "panther", "wolf"])
# print(wild_animal)
#
# for animal in wild_animal:
#     print(animal)
#
# farm_animals.add("horse")
# wild_animal.add("horse")
# print(farm_animals)
# print(wild_animal)

even =  set(range(0, 40, 2))
print(sorted(even))

squares_tuples = (4, 6, 9, 16, 25)
squares = set(squares_tuples)
# # Union
# print(even.union(squares))
# print(squares.union(even))
#
# # Intersection
# print(even.intersection(squares))
# print(even & squares)

# Difference between two sets
print(" even minus squares")
print(sorted(even.difference(squares)))
print(sorted(even - squares))

print(" squares minus even")
print(squares.difference(even))
print(squares - even)

# # Symmentric difference is opposite to intersection.
# print("Symmetric even minus squares")
# print(sorted(even.symmetric_difference(squares)))
#
# print("Symmetric squares minus even")
# print(sorted(squares.symmetric_difference(even)))

# # Remove/ discard element from set
# squares.discard(4)
# squares.discard(16)
# squares.discard(8)
# print(squares)
# try:
#     squares.remove(8)
# except KeyError:
#     print("The item 8 is not a member of the set")

# Superset & subset
# even =  set(range(0, 40, 2))
# print(sorted(even))
#
# squares_tuples = (4, 6, 16)
# squares = set(squares_tuples)
# if squares.issubset(even):
#     print("squares is a subset of even")
# if even.issuperset(squares):
#     print("even is superset of squares")

# # frozen set
# even = frozenset(range(0, 40, 2))
# print(even)
