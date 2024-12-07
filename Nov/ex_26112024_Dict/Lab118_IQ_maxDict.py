#write a function to return the max/min value in dict
myDict = {"a":10,"b":1,"c":45}
def max_value_dict(dictionary):
    return max(dictionary.values())

print(max_value_dict(myDict))

def min_value_dict(dict):
    return min(dict.values())

print(min_value_dict(myDict))