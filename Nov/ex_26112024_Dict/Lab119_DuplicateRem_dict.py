# write a function to remove duplicate values from Dict
#from Nov.ex_23112024_Lambda_List_Tuple_Set.Lab082 import result
#from Nov.ex_26112024_Dict.Lab110_dict import value

my_dict = {"a":1,"b":2, "c":1,"d":3}

# unique_value = set(my_dict.values())
unique_value = set()
#print(unique_value)
result = {}
for key,values in my_dict.items():
    if values not in unique_value:
        result[key] = values
        unique_value.add(values)

print(result)
