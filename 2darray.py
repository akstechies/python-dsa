from array import *

T  = [[20, 1, 5], [30, 20, 6, 5], [1, 2, 5], [40, 26, 58, 32]]

print(T[2])
print(T[2][1])

print('-------------------------')
for x in T:
    for y in x:
        print(y, end=" ")
    print()

print('-------------------------')
# Inserting Values
T.insert(3, [7, 11, 13, 54])
for x in T:
    for y in x:
        print(y, end=" ")
    print()

print('-------------------------')
# Updating Values
T[2] = [3, 7, 100]
T[3][3] = 17
for x in T:
    for y in x:
        print(y, end=" ")
    print()

print('-------------------------')
# Deleting the Values
del T[2]
print(T)
