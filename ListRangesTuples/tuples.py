# Tuples are immutable(unchangeable)

kural = "thriukural","thrivalluvar",1330
aathi = "aathi soodi", "paati", 12
mahaKavi = "Mahakavi","Paatu", 18

print(kural)
# Since Tuples are immutable you cannot change the value
# kural[1] = "valluvan" # this line throw an error
# To change the value use below
kural = kural[0],"Valluvar",kural[2] # Right hand side first evaluated so it will use krual old value to create new
print(kural)