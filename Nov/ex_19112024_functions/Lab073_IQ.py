#sum of 3 num, user does not use any argument then use default arg as 100,200,300

def sum_three(num1=100,num2 =200, num3 = 300):
    return num1+num2+num3

sum1= sum_three(20,10,30)
sum2 = sum_three()
sum3 = sum_three(10)

print(sum1,sum2,sum3)