from numpy import *

a = array([['Mon',18,20,22,17],['Tue',11,18,21,18],
		   ['Wed',15,21,20,19],['Thu',11,20,22,21],
		   ['Fri',18,17,23,22],['Sat',12,22,20,18],
		   ['Sun',13,15,19,16]])
    
m = reshape(a,(7,5))
print(m)

print("-----------------------")
# Accessing values
# Print data for Friday
print(m[4])

# Print data for Sunday Afternoon
print(m[6][2])

print("-----------------------")
# Adding a row
m_r = append(m,[['Avg',12,15,13,11]],0)
print(m_r)

print("-----------------------")
# Adding a column
m_c = insert(m,[2],[[1],[2],[3],[4],[5],[6],[7]],1)

print(m_c)

print("-----------------------")
# Delete a row

m = delete(m,[6],0)
print(m)

print("-----------------------")
# Delete a column
m = delete(m,[2],1)
print(m)

print("-----------------------")
# Update a row
m[4] = ['Fri',0,0,0]
print(m)