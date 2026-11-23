import numpy as np

n = 200

doors_method1 = [False] * (n + 1)
doors_method2 = [False] * (n + 1)

for i in range(1 , n + 1):
    for j in range(i , n + 1 , i):
        for _ in range(i):
            doors_method1[j] = not doors_method1[j]


for i in range(1, n + 1):
    for j in range(i, n + 1 , i):
        doors_method2[j] = not doors_method2[j]


open_doors_1 = [i for i in range(1, n + 1) if doors_method1[i]]
open_doors_2 = [i for i in range(1, n + 1) if doors_method2[i]]
    
print("First approch:" , open_doors_1)
print("Second approch:" , open_doors_2)