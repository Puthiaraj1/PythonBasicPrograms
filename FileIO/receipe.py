import shelve

# dhal_rice = ["dhal", "rice", "tomato", "onion"]
# egg_rice = ["egg", "rice", "bell pepper", "onion"]
# chicken_briyani = ["chicken", "curd", "masala", "onion", "mint"]
# curd_rice = ["rice", "curd", "milk", "fruits"]
rasam = ["pepper", "tomato", "garlic"]
with shelve.open("recipes", writeback= True) as recipes:
    # recipes["dhal_rice"] = dhal_rice
    # recipes["egg_rice"] = egg_rice
    # recipes["chicken_briyani"] = chicken_briyani
    # recipes["curd_rice"] = curd_rice
    # recipes["rasam"] = rasam

    # recipes["dhal_rice"].append("garlic")
    # recipes["chicken_briyani"].append("chilli")
    # temp_list = recipes["dhal_rice"]
    # temp_list.append("garlic")
    # recipes["dhal_rice"] = temp_list
    #
    # temp_list = recipes["chicken_briyani"]
    # temp_list.append("chilli")
    # recipes["chicken_briyani"] = temp_list
    # recipes["rasam"].append("tamarind")
    

    for meal in recipes:
        print(meal, recipes[meal])
