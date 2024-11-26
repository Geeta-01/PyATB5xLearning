#Given two integer variables a and b, and a boolean variable flag.
# The task is to check the status and return accordingly.
# Return True for the following cases:
#
# Either a or b (not both) is non-negative and the flag is false.
# Both a and b are negative and the flag is true.
# Otherwise, return false.

a = 0
b = 1
if a >= 0 or b >= 0:
    flag = False
elif a < 0 and b < 0:
    flag = True
print(flag)