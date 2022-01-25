#########Assignment 2.2###########

#Answer 1:
#for i in range(0,10,2):
#  print(i)
#Here, 2 acts as the step argument(difference between one number and the next)


#Answer 2:
#Method 1 for infinite for loop
#Iterating the list by increasing the length of the list so that the iteration never ends.
x=[1]
for i in x:
  print(i)
  x.append(i+1)

#Method 2 i.e. using itertools.count()
import itertools
for i in itertools.count(2,2):  #Here, it will print numbers from 2 to infinite numbers with step value of 2
  print(i)

#Method 3 i.e. using itertools.cycle()
import itertools
for i in itertools.cycle('ABCD'):  #Here, it will print A B C D and again print the same....this process will continue to infinite times
  print(i,end='~')                 #The use of ~ shows that the its getting printed letter to letter and not ABCD as a whole at once

#Method 4 i.e. using itertools.repeat()
import itertools
for i in itertools.repeat(100): #We can also add a second argument of no. of times the the value has to be printed...in that case it won't be infinite
  print(i)

#Answer 3:
#Method 1 - To convert tuple to a list, add the item, then convert the list back to tuple
#Eg. Add "mango" to the below tuple

mytuple=("apple","pineapple","orange") #Creating a tuple
print(mytuple)
x=list(mytuple)                       #Convert to a list
x.append("mango")                     #Add the item to the converted list
mytuple=tuple(x)                      #Convert the list back to tuple
print(mytuple)
print()

#Method 2 - To add tuple to a tuple
#Eg. Create a new tuple with the values "yellow","orange","red" and add that tuple

tuple1=("violet", "indigo","blue","green")         #Create a tuple
print(tuple1)
tuple2=("yellow","orange","red")                   #Make another tuple
print(tuple2)
tuple1=tuple1+tuple2                               #Add both the tuples
print(tuple1)

