# Program- find the area of circle
# step 1: Input/ output identification
# radius-> float
# pi -> 3.142 float
# area=> float

#Step2: rough logic
# area= pi *(r**2)
#pi = 3.140198
import math
pi = math.pi
radius = float(input("Enter the radius:"))
area = pi * (radius ** 2)
print(f"Area of circle is {area:.2f} with radius {radius}")