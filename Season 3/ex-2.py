def dividable(num1 , num2)->bool:
    if num2 % num1 == 0:
        return True
    else:
        return False
################################################
control = True
while control:
    num1 = int(input("Enter a integer:"))
    num2 = int(input("Enter a integer:"))
    if dividable(num1,num2):
        print(f"{num2} is dividable to {num1}")
    else:
        print(f"{num2} is not dividable to {num1}")
    control = bool(int(input("Do you want to continue (1/0)? ")))