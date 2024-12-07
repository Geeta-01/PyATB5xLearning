#dict-  is a key value pair
# It is unordered, mutable and indexed collection of key and value pair
# syntax --> { }

my_dict = {"name" :"Geeta",
            "age": 30,
            "Role" : "SDET",
            "Experience":5}

# access the item from the dict
print(my_dict["name"])

# update the key value
my_dict["Role"] = "Manual Tester"
print(my_dict)

# Delete a key from the dict
del my_dict["age"]
print(my_dict)

#iterting over a dict
for key,value in my_dict.items():
    print(key,"\t :",value)


# empty dict
student = dict()
print(type(student))
print(student)

