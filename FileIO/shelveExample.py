# Pickle uses memory to store values while reading/ writing. It will be drawback
# Shelve will use file instead of memory
# All shelve files created with an extension '.db'
# Data will be stored ina database
# Shelve are similar to a dictionary. It will store as a key - value pair
# Shelve key must be a String but Dictionary can accept int value as well
import shelve

with shelve.open('ShelfTest') as fruit:
    fruit['orange'] = "a sweet, orange, citrus fruit"
    fruit['banana'] = "a sweet, good for breakfast"
    fruit['apple'] = "good for making cider"
    fruit['grape'] = "a small sweet fruit growing in bunches"
    fruit['melon'] = "a sweet, color full fruit"

    print(fruit["grape"])
    print(fruit["melon"])
