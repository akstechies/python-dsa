import collections

dict1 = {'day1': 'Mon', 'day2': 'Tue'}
dict2 = {'day3': 'Wed', 'day1': 'Thu'}

res = collections.ChainMap(dict1, dict2)

print('\n')
print(res)

# Creating a single dictionary
print(res.maps,'\n')

print('Keys = {}'.format(list(res.keys())))
print('Values = {}'.format(list(res.values())))
print()

# Print all the elements from the result
print('Elements:')
for key, val in res.items():
    print('{} = {}'.format(key, val))
print()

# Find a specific value in the result
print('day2 in res: {}'.format(('day2' in res)))
print('day4 in res: {}'.format(('day4' in res)))

print()

res2 = collections.ChainMap(dict2, dict1)
print(res2.maps,'\n')

# Print all the elements from the result
print('Elements:')
for key, val in res2.items():
    print('{} = {}'.format(key, val))
print()

# Updating 

dict2['day4'] = 'Fri'

print(res.maps,'\n')

dict2['day3'] = 'Sun'
print(res.maps,'\n')