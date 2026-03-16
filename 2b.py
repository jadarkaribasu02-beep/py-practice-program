#program to create a list and perform  the foloowing operations
#inserting an element
#removing an element
#appending an element
#displaying length of the list
#popping an element
#clearing the list

#1 creating
my_list=[15,25,35,45,55]
print(f'initial list:{my_list}')

#2 inserting 60 at index 5
my_list.insert(5,60)
print(f'list after inserting number:{my_list}')

#3 removing
my_list.remove(25)
print(f'list after removing:{my_list}')

# 4 appending
my_list.append(78)
print(f'list after adding 78 to end of lit:{my_list}')

# 5 length 
list_length=len(my_list)
print(f'length of the list:{list_length}')

# 6 poping
popped_element=my_list.pop()
print(f'popped element(last element):{popped_element}')
print(f'list after popping an element:{my_list}')

#7 clearing
my_list.clear()
print(f' list after clearing:{my_list}')
