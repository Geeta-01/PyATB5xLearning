#Given a natural number n,
# the task is to write a Python program to first find the sum of first n natural numbers
# and then print each step as a pattern.
# Input: 5
# Output:
# 1 = 1
# 1 + 2 = 3
# 1 + 2 + 3 = 6
# 1 + 2 + 3 + 4 = 10
# 1 + 2 + 3 + 4 + 5 = 15

N = 5
for j in range(1, N+1):
    for i in range(1,j+1):
        print(f"{i} ", end = ' ')
        if (i < j):
            print(" + ", end = ' ')
        print( f"{j} ", end = ' ')
        sum = i + j
        print(" = ",sum )



