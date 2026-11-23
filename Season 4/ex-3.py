import numpy as np

Mat = np.matrix(np.zeros((3,5)))
for i in range(np.size(Mat,0)):
    for j in range(np.size(Mat,1)):
        Mat[i,j] = int(input(f"Enter number{i+1},{j+1}:"))

print("The initial matrix:\n",Mat)
Mat = Mat.T
print("\nThe transposed matrix:\n",Mat)