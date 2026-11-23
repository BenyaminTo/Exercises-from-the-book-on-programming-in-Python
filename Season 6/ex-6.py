import random

set1 = set(random.sample(range(1, 101), 10))
set2 = set(random.sample(range(1, 101), 10))

print("Differential Difference:", set1 - set2)
print("Subtraction:" , set1 & set2)
print("Union:" , set1 | set2)