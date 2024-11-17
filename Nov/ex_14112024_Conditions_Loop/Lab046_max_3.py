# find max of 3 num

num1 = float(input("Enter num1:"))
num2 = float(input("Enter Num2:"))
num3 = float(input("Enter Num3:"))
if num1 > num2 and num1 > num3:
    print("Num1 is maximum")
elif num2 > num3 and num2 > num1:
    print("Num2 is maximum")
else:
    print("Num3 is maximum")