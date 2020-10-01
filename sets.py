Days = set(["Mon", "Tue", "Wed", "Thu", "Fri"])
Months = {4, 6, 5, 11, 23}
Test = {1, 1, 3}

print(Days)
print(Months)
print(Test)

print('-----------------------')
# Accessing

for x in Days:
    print(x)

print('-----------------------')
# Adding Items to a Set
Days.add('Saturday')
print(Days)

print('-----------------------')
# Remove
Days.discard('Fri')
print(Days)

print('-----------------------')
# Union
Days2 = {'Mon', 'Sat', 'Fri', 'Thu'}
allDays = Days|Days2
print(allDays)

print('-----------------------')
# Inserction
interDay = Days & Days2
print(interDay)

print('-----------------------')
# Difference
diffDay = Days - Days2
print(Days)
print(Days2)
print(diffDay)

print('-----------------------')
# Compare
DaysA = set(["Mon","Tue","Wed"])
DaysB = set(["Mon","Tue","Wed","Thu","Fri","Sat","Sun"])
SubsetRes = DaysA <= DaysB
SupersetRes = DaysB >= DaysA
SubsetRes2 = DaysA >= DaysB
SupersetRes2 = DaysB <= DaysA
print(SubsetRes)
print(SupersetRes)
print(SubsetRes2)
print(SupersetRes2)