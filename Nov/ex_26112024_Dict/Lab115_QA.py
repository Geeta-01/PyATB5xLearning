#frequecy of a char in a string

string= "geeta"

char_count ={}
for char in string:
    char_count[char] =char_count.get(char, 0) +1

print(char_count)

