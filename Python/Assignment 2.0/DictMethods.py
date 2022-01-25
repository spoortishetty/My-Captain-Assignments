birthday = {
  "name": "Ray",
  "month": "August",
  "age": 14
}

#Returns a copy of the dictionary
print(birthday.copy())

#Returns a dictionary with the specified keys and value
x=('a','b','c')
y=1
thisdict=dict.fromkeys(x,y)
print(thisdict)

#Returns the value of the specified key
print(birthday.get("month"))

#Returns a list containing a tuple for each key value pair
print(birthday.items())

#Returns a list containing the dictionary's keys
print(birthday.keys())

#Removes the element with the specified key
birthday.pop("month")
print(birthday)

#Updates the dictionary with the specified key-value pairs
birthday.update({"year":2007})
print(birthday)

#Removes the last inserted key-value pair
birthday.popitem()
print(birthday)

#Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
print(birthday.setdefault("name","Sara"))
print(birthday.setdefault("color","purple"))

#Returns a list of all the values in the dictionary
print(birthday.values())

#Removes all the elements from the dictionary
print(birthday.clear())

