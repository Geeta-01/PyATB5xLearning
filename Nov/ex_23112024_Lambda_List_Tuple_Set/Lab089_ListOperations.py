my_list = [1,2,3]
print("element at index 0 => ", my_list[0])
print("element at index 1 => ", my_list[1])
print("element at index 2 => ", my_list[2])

# append
my_list.append(4)
my_list.append(5)
print(my_list) # append the element at the end of list

# extend- append a new list
my_list.extend([7,8,9]) # add another list at the end of existing list
print(my_list)


#insert - insert at particular index

my_list.insert(10,10)
print(my_list)
my_list.insert(1,11)
print(my_list)

#remove - remove an item from list if item exists in list
my_list.remove(11)
print(my_list)

# my_list.remove("Geeta") #ValueError: list.remove(x): x not in list
# print(my_list)

copied_my_list = my_list.copy()
print(copied_my_list)
print(my_list)

#sort - sorts the elements in a list
# pop- removes the 
