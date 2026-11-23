import math
import cmath

print("Solving the quadratic equation ax^2 + bx + c = 0")

a = float(input("Enter a:"))
b = float(input("Enter b:"))
c = float(input("Enter c:"))

if a == 0:
    print("This is not a quadratic equation!")
else:
    delta = b**2 - 4*a*c
    print(f"Delta = {delta}")
    
    if delta > 0:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        print(f"Roots: x1 = {x1}, x2 = {x2}")
    elif delta == 0:
        x = -b / (2*a)
        print(f"Double root: x = {x}")
    else:
        x1 = (-b + cmath.sqrt(delta)) / (2*a)
        x2 = (-b - cmath.sqrt(delta)) / (2*a)
        print(f"Mixed roots: x1 = {x1}, x2 = {x2}")