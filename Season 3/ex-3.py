def gcd(num1:int,num2:int)->int: 
    div1 = divs(num1)
    div2 = divs(num2)
    div = list()
    for i in div1:
        for j in div2:
            if i == j:
                div.append(j)
                
    big = div.pop()
    return big

def divs(num:int)->list:
    temp = num 
    list_divs = list()
    for i in range(1,temp+1,1):
        if temp % i == 0:
            list_divs.append(i)
        else:
            continue
    return list_divs       
################################################  
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))    
print("The biggest divis:" , gcd(num1,num2))