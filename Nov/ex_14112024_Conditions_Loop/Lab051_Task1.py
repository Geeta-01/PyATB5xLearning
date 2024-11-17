#Leap day occurs in each year that is a multiple of 4,
# except for years evenly divisible by 100 but not by 400.
year = int(input(" enter year to check whether its a leap year: "))
if year % 4 == 0 :
    print("It's leap year!!")
elif year % 100 == 0:
    print("It's leap year!!")
elif year % 400 == 0:
    print("It's leap year!!")

else:
    print("It's not a leap year!!")