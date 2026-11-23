input_string1 = input("Enter elements of the list1 separated by spaces: ")
input_string2 = input("Enter elements of the list2 separated by spaces: ")

vector1 = input_string1.split()
vector2 = input_string2.split()

vector1 = [int(elem) for elem in vector1]
vector2 = [int(elem) for elem in vector2]

if len(vector1) != len(vector2):
    print("Error: The two lists must have the same length.")
else:
    pro_vector = list()
    for vec in range(len(vector1)):
        pro_vector.append(vector1[vec] * vector2[vec])
    print("Product of vectors:", pro_vector)
