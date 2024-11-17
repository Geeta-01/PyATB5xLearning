#Write a program that classifies a triangle based on its side lengths.
# Given three input values representing the lengths of the sides,
# determine if the triangle is equilateral (all sides are equal),
# isosceles (exactly two sides are equal), or scalene (no sides are equal).
# Use an if-else statement to classify the triangle

#s1, s2, s3 → int

#o/p →. iso, eq, scelene

s1 = int(input(" Enter length of side 1 of triangle s1:"))
s2 = int(input(" Enter length of side 2 of triangle s2:"))
s3 = int(input(" Enter length of side 3 of triangle s3:"))
if s1 == s2 == s3:
    print("It's an equilateral triangle")
elif s1== s2 or s2==s3 or s3 == s1:
    print("It's an isosceles triangle")
else:
    print("It's a scalene triangle")
# edge cases


