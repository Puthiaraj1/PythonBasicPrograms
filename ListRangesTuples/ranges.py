decimals = range(0, 100)
my_range = decimals[3:40:3]
print(my_range == range(3, 40, 3))
print(range(0, 5, 2) == range(0, 6, 2))  # This will return True as long as the output of the range is similar

o = range(0, 100, 4)
print(o)
p = o[::5]
print(p)
for i in p:
    print(i)