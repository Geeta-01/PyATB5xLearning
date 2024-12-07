# count the number od vowels in the string
input = "Hello world!!"
# vowels = a, e,i,o u

vowels = "aeiou"
vowel_count =0
for char in input:
    if char in vowels:
        vowel_count = vowel_count + 1


print(vowel_count)