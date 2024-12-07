# Two list convert to Dict


keys = ["name", "age", "Role"]
values = ["Geeta","39","SDET"]
my_dict = dict(zip(keys,values))
print(my_dict)

#merge two dicts
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}

merge_dict =dict1|dict2
print(merge_dict)

print(merge_dict.get('a'))