day = int()
while True:
    day = int(input("Enter a number (0,6):"))
    if day == 0 :
        print("Saturday")
    elif day == 1:
        print("Sunday")
    elif day == 2:
        print("Monday")
    elif day == 3:
        print("Tuesday")
    elif day == 4:
        print("Wednesday")
    elif day == 5:
        print("Thursday")
    elif day == 6:
        print("Friday")
    else:
        print("Error!")
        break