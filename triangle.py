#14.WAP that will accept the sides of a triangle, check whether the sides makes a triangle and compute the area.
import math
print("\nSides of Triangle")
a=int(input("Enter length of 1st side:"))
b=int(input("Enter length of 2nd side:"))
c=int(input("Enter length of 3rd side:"))
if a+b>c and b+c>a and a+c>b :
    s=(a+b+c)/2
    area=math.sqrt(s*(s-a)*(s-b)*(s-c))
    print("Area of triangle:",area)
else:
    print("These sides does not form a triangle")