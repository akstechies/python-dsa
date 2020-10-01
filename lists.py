list1 = ['Ayush', 'Abhinav', 1995, 2000]

for x in list1:
    print(x)

print('-----------------------')
# Accessing Values

print(list1[1])
print(list1[2])

print(list1[1:3])
print(list1[1:10])

print('-----------------------')
# Updating Lists
print(list1[3])
list1[3] = 1999
print(list1[3])
print(list1[0:5])

print('-----------------------')
# Delete List Elements
print(list1)
del list1[2]
print(list1)