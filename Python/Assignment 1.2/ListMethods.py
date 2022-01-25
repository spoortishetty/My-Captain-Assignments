l1=[1,2,3,4,5,34,22,44]

#Adds an element at the end of the list
l1.append(3)
print(l1)

#Sorts the list
l1.sort()
print(l1)

#Reverses the order of the list
l1.reverse()
print(l1)

#Removes the item with the specified value
l1.remove(34)
print(l1)

#Removes the element at the specified position
l1.pop(3)
print(l1)

#Adds an element at the specified position
l1.insert(2,11)
print(l1)

#Returns the index of the first element with the specified value
z = l1.index(22)
print(z)

l2=['These','are','numbers']
#Add the elements of a list (or any iterable), to the end of the current list
l1.extend(l2)
print(l1)

#Returns the number of elements with the specified value
x = l1.count(3)
print(x)

#Returns a copy of the list
y = l1.copy()
print(y)

#Removes all the elements from the list
l1.clear()
print(l1)
