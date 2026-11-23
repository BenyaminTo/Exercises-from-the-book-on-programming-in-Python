import numpy as np
from collections import Counter
##############################################################################
def most_iter(arr):
    counter = Counter(arr)
    duplicates = [item for item, count in counter.items() if count > 1]

    if len(duplicates) == 0:
        return np.array(["No iteration"])

    return np.array(duplicates)
##############################################################################
def most_frequent(arr):
    if len(arr) == 0:
        return np.array([])

    counter = Counter(arr)
    max_count = max(counter.values())
    most_freq = [item for item, count in counter.items() if count == max_count]

    return np.array(most_freq), max_count
##############################################################################
number = int(input("Enter length of array: "))
arr = np.empty(number, dtype=object)

print("Enter numbers:")
for i in range(number):
    arr[i] = input(f"Enter number {i + 1}: ")

print("\n" + "=" * 40)
print(f"Original array: {arr}")
print(f"Duplicates: {most_iter(arr)}")

most_freq_items, freq_count = most_frequent(arr)
print(f"Most frequent item(s): {most_freq_items} (occurring {freq_count} times)")