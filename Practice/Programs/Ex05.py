#Given a positive integer x,
# the task is to print the numbers from 1 to x in the order as 1^2, 2^2, 3^2, 4^2, 5^2, ...
# (in increasing order).
#ex: input -> x = 10, O/p ->  1, 4, 9
# Using While loop
#     x = 10
#     i = 1
#     while i <= x:
#         square = i * i
#         if square <= x :
#             print(square)
#         i += 1

#Using for loop
N = 100
for i in range(1, N+1):
    square = i * i
    if square <= N:
        print(square)

