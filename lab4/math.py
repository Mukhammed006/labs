#1
import math
n=float(input("Enter a degree: "))
print("Output in radian: ", round(n* math.pi/180, 6))

#2
import math

h=int(input("Enter a height: "))
a=int(input("Base,first value: "))
b=int(input("Base,second value: "))
area=(a+b)*(h/2)

print("Area of trapexoid: ", area)

#3
import math
n=int(input("Number of sides: "))
m=int(input("Length of the sides: "))

area=int((n*m**2)/(4*math.tan(math.pi/n)))
print("The area of the polygon: ", area)

#4
import math
n=int(input("Length of base: "))
h=int(input("Heigth of parallelogram: "))

area=float(n*h)
print("Area of a parallelogram: ", area)