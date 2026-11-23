import numpy as np
####################################################
def sum_matrix(a , b):
    return a + b
####################################################
def getmatrix(matrix):
    print(("\nYou will enter matrix elements:\n"))
    for i in range(np.size(matrix, 0)):
        for j in range(np.size(matrix, 1)):
            matrix[i, j] = int(input(f"Enter number{i + 1},{j + 1}:"))

    return matrix
#####################################################
n = int(input("Enter a number as n:"))
m = int(input("Enter a number as m:"))

a = np.matrix(np.zeros((m,n)))
b = np.matrix(np.zeros((m,n)))

a = getmatrix(a)
b = getmatrix(b)

print("The sum of the elements of the matrix is\n ",sum_matrix(a,b))
