numbers = list()
for i in range(10):
    numbers.append(int(input("Enter a number:")))

Divisible_by_four = 0    
for j in numbers:
    if j % 4 == 0:
        Divisible_by_four += 1
    else:
        continue

print("The number of numbers that are divisible by 4:",Divisible_by_four)