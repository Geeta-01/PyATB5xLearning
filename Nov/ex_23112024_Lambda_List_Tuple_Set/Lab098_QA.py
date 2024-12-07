# Find the first non-repeating char in a string using sets.

def first_non_repeating_char(string):
    for char in string:
        if string.count(char)== 1:
            return char
    return None

print(first_non_repeating_char("swiss"))
print(first_non_repeating_char("Geeta"))
print(first_non_repeating_char("Vihan"))
print(first_non_repeating_char("mamma"))

