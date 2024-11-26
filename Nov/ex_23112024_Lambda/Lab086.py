#write a program to find given num is even/odd

is_even =lambda num: num%2 ==0
#print(is_even(10))
if is_even(11):
    print("num is even")
else:
    print("num is odd")

check_even_odd= lambda num: "even" if num%2 ==0 else "odd"
print(check_even_odd(100))
