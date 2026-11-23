def biggest(*n):
    temp = n[0]
    for i in n:
        if i > temp:
            temp = i
    return temp
############################################################
print("The biggest number is",biggest(54,74,99,158,458,66))