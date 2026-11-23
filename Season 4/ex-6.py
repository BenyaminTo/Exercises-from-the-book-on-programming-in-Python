import numpy as np
##################################################################
def get_arr(arr):
    print(("\nYou will enter array elements:\n"))
    for i in range(np.size(arr)):
        temp = int(input(f"Enter number{i + 1}:"))
        arr[i] = temp
    return arr
##################################################################
def Merge_and_sort(arr1, arr2):
    merged_arr = np.concatenate((arr1, arr2))
    merged_arr.sort()
    return merged_arr
###################################################################
arr1 = np.empty(5)
arr2 = np.empty(5)
arr1 = get_arr(arr1)
arr2 = get_arr(arr2)
arr1.sort()
arr2.sort()
print("The sorted array 1 is\n ", arr1)
print("The sorted array 2 is\n ", arr2)
print("The merged and sorted array is\n ", Merge_and_sort(arr1, arr2))