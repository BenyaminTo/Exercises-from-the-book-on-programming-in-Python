def revers_counter(digit):
    print(digit)
    if digit == 1:
        return 
    return revers_counter(digit-1) 
##############################################
digit = int(input("Enter a number: "))
revers_counter(digit)