#set is collection of Unique items
# Dupliates were not allowed
# Syntax -{ }
# order of items are different

my_set ={1,2,3,2,5,5,5}
print(my_set) # output-- {1, 2, 3, 5}



#convert list to set
my_list = [34,45.2,41,8,100]
mt_set1 = set(my_list)
print(mt_set1) # out put {34, 100, 8, 41, 45.2} -> order is not maintained

t = ("TheTestingAcademy", "Pramod", "Pramod","By Pramod sir")
print(t)
print(set(t))

# Out put
# ('TheTestingAcademy', 'Pramod', 'Pramod', 'By Pramod sir')
# {'Pramod', 'By Pramod sir', 'TheTestingAcademy'}


