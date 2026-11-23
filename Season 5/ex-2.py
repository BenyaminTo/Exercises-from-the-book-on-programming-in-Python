def getName(names):
    while True:
        string = input("Enter a name:")
        if string.strip() != "":
            names.append(string)
        else:
            break
        #end of while
    return names
###############################################################################
def getAvg(avgs):
    while True:
        try:
            string = input("Enter a number for avgs or space to finish:")
            if string.strip() == "":
                break
            else:
                avgs.append(float(string))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    return avgs
###############################################################################
def getstnos(stnos):
    while True:
        try:
            string = input("Enter a number for stnos or space to finish:")
            if string.strip() == "":
                break
            else:
                stnos.append(int(string))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    return stnos
###############################################################################
def highestAverage(avgs):
    if len(avgs) == 0:
        return None

    highest_avg = avgs[0]
    highest_index = 0

    for i, avg in enumerate(avgs):
        if avg > highest_avg:
            highest_avg = avg
            highest_index = i

    return highest_index
###############################################################################
def lowestAverage(avgs):
    if len(avgs) == 0:
        return None

    lowest_avg = avgs[0]
    lowest_index = 0

    for i, avg in enumerate(avgs):
        if avg < lowest_avg:
            lowest_avg = avg
            lowest_index = i

    return lowest_index
###############################################################################
def deleteStudent(stnos, stno):
    try:
        return stnos.index(stno)
    except ValueError:
        print(f"The student number {stno} does not exist.")
        return None
###############################################################################
def sortStudents(names, avgs, stnos):
    avg_index_pairs = list(enumerate(avgs))
    
    avg_index_pairs.sort(key=lambda pair: pair[1], reverse=True)
    
    sorted_names = [names[i] for i, _ in avg_index_pairs]
    sorted_avgs = [avgs[i] for i, _ in avg_index_pairs]
    sorted_stnos = [stnos[i] for i, _ in avg_index_pairs]
    
    return sorted_names, sorted_avgs, sorted_stnos
###############################################################################
def menu():
    print("1. Enter data")
    print("2. Remove data")
    print("3. Sort data")
    print("4. Highest data")
    print("5. Lowest data")
    choice = int(input("Enter your select(1-5): "))
    return choice
###############################################################################
names = []
avgs = []
stnos = []

while True:
    c = menu()
    if c == 1:
        names = getName(names)
        avgs = getAvg(avgs)
        stnos = getstnos(stnos)
    elif c == 2:
        control = input("Do you want delete any one?(y/n)")
        stno = None
        if control == "y":
            stno = int(input("Enter a stno:"))
            indexForDel = deleteStudent(stnos, stno)
            names.pop(indexForDel)
            avgs.pop(indexForDel)
            stnos.pop(indexForDel)
        else:
            print("OK!")
    elif c == 3:
        names, avgs, stnos = sortStudents(names, avgs, stnos)
        print("Sorted students:")
        for i in range(len(names)):
            print(f"Name: {names[i]}, Average: {avgs[i]}, Student Number: {stnos[i]}")
    elif c == 4:
        highest_index = highestAverage(avgs)
        print(f"The highest average is : {avgs[highest_index]} name is: {names[highest_index]} stnos is: {stnos[highest_index]}")
    elif c == 5:
        lowest_index = lowestAverage(avgs)
        print(f"The highest average is : {avgs[lowest_index]} name is: {names[lowest_index]} stnos is: {stnos[lowest_index]}")
    else:
        break
#The End-----------------------------------------------------------------------
        
        
        
        

