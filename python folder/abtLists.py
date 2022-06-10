#Susie Fagelman
#We are going to learn about lists, fucntions to lists
#We are going to learn about forloop
import random
import os
os. system ('cls')
thislist = ["apple", "bannana","kiwi","cherry","orange", "melon"]
#               0       1         2       3        4         5
#                                -4       -3      -2         -1
print(thislist[1]) #print from a specific index
print(thislist[-1]) #print from the end
print(thislist[2:5]) #print from the two value the first one is included in the set the second is excluded
print(thislist[:3]) #print up to a value but not including a value
print(thislist[2:]) #prints everything after a value including the original element
print(thislist[-4:-1])
if "apple" in thislist:
    print("yes the apple is in the list")

for num in range(10): #loops a specific number of times
    print(num,end="")
print()

for element in thislist: #element = thislist[ time run through the loop]
    print(element, end="")
print()

thislist.append("pinnaple") #add an element to the end of a list
print(thislist[0:])

# for num in range(10):
#     thislist.append(input("input a food"))
# print(thislist[0:])
#for num in range(2):
# thislist.append(input(:"input a food"))
#print(thislist[0:])

thislist.insert(1,"pinapple") #adding an element to a specific index insert(indez, element you want to add)
print(thislist[0:])

for i in range(len(thislist)): #loops for the lenght of the list
    print(thislist[i], end = " / ")
print()

list_num = [1,2,3,4]
list_num.extend(thislist) #add the elements from one list to another
print(list_num)

list_num=[1,2,3,4]
list_num.append(thislist) #add the whole list to the last index
print(list_num)
print(list_num[-1])
print(list_num[-1[0]])

word = random.choice(thislist) #picks a random element in the list
print(word)


guess=input("input a food: \t")
if guess in word.lower:
    print("congrats you guessed the food ")