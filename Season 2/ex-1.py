numbers = list()
y = True
while True:
    numbers.append(int(input("Enter a number:")))
    if y == int(input("Do you want to continue(1,0):")):
        continue
    else:
        break

sumofpower = 0
for i in numbers:
    sumofpower += i
    
print("Sum of Digits:",sumofpower)  