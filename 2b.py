
my_list=[15,25,35,45,55]
print(f'initial list:{my_list}')


my_list.insert(5,60)
print(f'list after inserting number:{my_list}')


my_list.remove(25)
print(f'list after removing:{my_list}')


my_list.append(78)
print(f'list after adding 78 to end of lit:{my_list}')


list_length=len(my_list)
print(f'length of the list:{list_length}')


popped_element=my_list.pop()
print(f'popped element(last element):{popped_element}')
print(f'list after popping an element:{my_list}')

my_list.clear()
print(f' list after clearing:{my_list}')
