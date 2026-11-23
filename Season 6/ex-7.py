import random

list1 = list(set(random.sample(range(1, 101), 20)))
list2 = list(set(random.sample(range(1, 101), 20)))

# Find the difference between two lists using list comprehension
difference = [item for item in list1 if item not in list2]

# Find the symmetric difference between two lists using list comprehension
symmetric_difference = [item for item in list1 if item not in list2] + [item for item in list2 if item not in list1]

# Find the union of two lists using list comprehension
union = list1 + [item for item in list2 if item not in list1]

# Find the intersection of two lists using set() and list()
intersection = list(set(list1) & set(list2))

print("Differential Difference:", difference)
print("Symmetric Difference:", symmetric_difference)
print("Union:", union)
print("Intersection:", intersection)
