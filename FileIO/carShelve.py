import shelve

with shelve.open("car") as car:
    # car["make"] = "Mazda"
    # car["model"] = "Mazda 6"
    # car["colour"] = "Red"
    # car["year"] = 2016
    for key in car:
        print(key)
    #del car['color']
   # print(car["color"])
    print(car["colour"])
    print(car["model"])


