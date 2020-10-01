tup1 = ("Anita", "Anand", 1968, 1960)
print(tup1)

tup2 = (1,3,4,6,7)
print(tup2)

tup3 = "a", "b", "c", "d", "e"
print(tup3)

tup4 = ()
print(tup4)

tup5 = (45,)
print(tup5)

print("-----------------------------------")
# Accessing Values
print(tup1)
print(tup1[0])
print(tup1[0:4])
print(tup1[1:7])

print("-----------------------------------")
# Updating Tuples
# Following action is not valid for tuples
# tup1[0] = 100

tup6 = tup1 + tup2
print(tup6)

print("-----------------------------------")
#Delete Tuple Elements -> Removing individual tuple elements is not possible.
del tup6
print(tup6)