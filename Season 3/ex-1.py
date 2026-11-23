def Maximum(num1:int = 0 , num2:int = 0, num3:int = 0)-> int:
    max = num1
    if max < num2:
        max = num2
        if max < num3:
            max = num3
    return max
############################################################
num1 = int(input("Enter first integer:"))
num2 = int(input("Enter second integer:"))
num3 = int(input("Enter third integer:"))

print("The Maximum is :", Maximum(num1 , num2 , num3 ))