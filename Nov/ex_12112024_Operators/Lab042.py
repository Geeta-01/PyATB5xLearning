#if age>=18 allow the voting

age = int(input(" enter user age: "))
if age>=18:
    print("Allow for voting")
else:
    print("Do not allow for voting")

# using ternary
print( "Allow for voting" if age>=18 else "Do not Allow for voting")

# do not use following one liner coding 
#print( "Allow for voting" if int(input(" enter user age: "))>=18 else "Do not Allow for voting")