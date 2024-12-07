# sort the dictionary by the values ascending

dict1 = {"a":3, "b":1, "c": 2}
# for key, values in dict1:

values = set(dict1.values())
keys = set(dict1.keys())
dict2 =dict(zip(keys,values))
print(dict2)
