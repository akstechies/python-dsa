dict1 = {'mother': 'Anita', 'father': "dad", 'sons': 2, "daughter": 0, 4: 'total', '4': 'members', 'father': 'Anand'}

print(dict1)
print(dict1['father'])
print(dict1['sons'])
print(dict1['4'])
print(dict1[4])

print("-----------------------")
# Updating Dictionary
dict1[4] = 'family member'
print(dict1)
print(dict1[4])

dict1['location'] = 'Lucknow'
print(dict1)
print(dict1['location'])

print("-----------------------")
# Delete Dictionary Elements
del dict1['4']
print(dict1)

dict1.clear()
print(dict1)

del dict1
#print(dict1)

# dict = {['Name']: 'Zara', 'Age': 7} -> not allowed