
try:
    num1= int(input("Enter num1  "))
    num2= int(input("Enter num2  "))
    res = num1/num2
except ValueError as e:
    print(e)

except ZeroDivisionError as e1:
    print(e1)

else:
    print("result is ",res)
