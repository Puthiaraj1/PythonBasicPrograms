import shelve

books = shelve.open("book")
books["recipes"] = {"dhal_rice": ["dhal", "rice", "tomato", "onion"],
                      "egg_rice": ["egg", "rice", "bell pepper", "onion"],
                      "chicken_briyani": ["chicken", "curd", "masala", "onion", "mint"],
                      "curd_rice": ["rice", "curd", "milk", "fruits"],
                      "rasam": ["pepper", "tomato", "garlic"]}
books["maintenance"] = {"stuck": ["oil"],
                         "loose": ["gaffer tape"]}

print(books["recipes"])
# print(books["recipes"]["dhal_rice"])
#
# print(books["maintenance"]["loose"])

books.close()