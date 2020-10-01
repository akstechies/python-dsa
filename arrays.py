from array import *

# arrayName = array(typecode, [Initializers])

#Create and Print an array

array1 = array('i', [22, 35, 44, 52, 60])
# i => Represents signed integer of size 2 bytes

for x in array1:
    print(x)

print('-----------------')
# accessing array elemnets - using index
print(array1[1])
print(array1[3])

print('-----------------')
# Insertion
array1.insert(0, 13)
for y in array1:
    print(y)

print('-----------------')
# Deletion
array1.remove(44)
for z in array1:
    print(z)

print('-----------------')
# Search 
print(array1.index(52))

print('-----------------')
# Update
array1[4] = 66
print(array1[4])

print('-----------------')
for a in array1:
    print(a)
