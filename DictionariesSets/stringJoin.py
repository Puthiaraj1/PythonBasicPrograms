myList = ["a","b","c","d"]
newString = ",".join(myList)
print(newString)

locations = { 0: " Learning Python",
              1: "In fornt of the building",
              2: "In Hill",
              3: "In a house",
              4: "In the valley",
              5: "In the forest"
              }
exits = [{"Q": 0},
         {"W": 2, "E": 3, "N": 5, "S": 4, "Q": 0},
         {"N": 5, "Q": 0},
         {"W": 1, "Q": 0},
         {"N": 1, "W": 2, "Q": 0},
         {"W": 2, "S": 1, "Q": 0}]
loc = 1
while True:
    availableExits = ", ".join(exits[loc].keys())
    print(locations[loc])
    if loc == 0:
        break
    direction = input("Available exits are "+ availableExits).upper()
    print()
    if direction in exits[loc]:
        loc = exits[loc][direction]
    else:
        print("You cannot go in the direction")