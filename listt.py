# take inputs from user
numbers=5
list = []
for i in range(numbers):
    n=int(input('Enter list numbers: '))
    list.append(n)
print('Initial List',list)

# sum of all elements
print('Sum of elements in list: ',sum(list))

# largest element in list
print('Largest element in list: ',max(list))

# smallest element in list
print('Smallest element in list: ',min(list))

# sorting in ascending order
list.sort()
print('Ascending order: ',list)


# sorting in descending order
list.reverse()
print('Descending order: ',list)

# converting into tuple
t1=tuple(list)
print('Converted list: ',t1)

# delete list
del list
print('List is deleted successfully')
