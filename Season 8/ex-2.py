import csv
#------------------------------------------------------------------------------
class Student:
    def __init__(self, name, stno, ave):
        self.name = name
        self.stno = stno
        self.ave = ave

    def display(self):
        print("{0:10s} {1:5d} {2:8.2f}".format(self.name, self.stno, self.ave))
#------------------------------------------------------------------------------
def menu():
    print("1. Enter a student ")
    print("2. Search a student ")
    print("3. Delete a student ")
    print("4. Update the ave of student ")
    print("5. Display all students")
    print("6. Exit ")
    choice = int(input("Enter your selection(1-6) : "))
    return choice
#------------------------------------------------------------------------------
def insertData():
    print("Enter name, stno, ave :", end="")
    name, stno, ave = input().split()
    ob = Student(name, int(stno), float(ave))
    with open("students.csv", "a", newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([name, stno, ave])
#------------------------------------------------------------------------------
def reportData():
    with open("students.csv", "r") as csvfile:
        reader = csv.reader(csvfile)
        print("{0:10s} {1:10s} {2:10s}".format("Name", "Stno", "Ave"))
        for row in reader:
            name, stno, ave = row
            student = Student(name, int(stno), float(ave))
            student.display()
#------------------------------------------------------------------------------
def searchData():
    stno = int(input("Enter a stno to search : "))
    found = False
    with open("students.csv", "r") as csvfile:
        reader = csv.reader(csvfile)
        print("{0:10s} {1:10s} {2:10s}".format("Name", "Stno", "Ave"))
        for row in reader:
            name, stno_csv, ave = row
            if int(stno_csv) == stno:
                found = True
                student = Student(name, int(stno_csv), float(ave))
                student.display()
                break
    if not found:
        print("Student not found : ")
#------------------------------------------------------------------------------
def updateData():
    stno = int(input("Enter stno and ave to change "))
    ave = float(input("Enter new average : "))
    with open("students.csv", "r") as csvfile:
        reader = csv.reader(csvfile)
        temp_data = []
        found = False
        for row in reader:
            name, stno_csv, ave_csv = row
            if int(stno_csv) == stno:
                found = True
                temp_data.append([name, stno_csv, str(ave)])
            else:
                temp_data.append(row)

    if not found:
        print("Student not found : ")
    else:
        with open("students.csv", "w", newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(temp_data)
#------------------------------------------------------------------------------
def deleteData():
    stno = int(input("Enter stno to delete :"))
    with open("students.csv", "r") as csvfile:
        reader = csv.reader(csvfile)
        temp_data = []
        found = False
        for row in reader:
            name, stno_csv, ave = row
            if int(stno_csv) != stno:
                temp_data.append(row)
            else:
                found = True

    if not found:
        print("Student not found : ")
    else:
        with open("students.csv", "w", newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(temp_data)

#----------------------------Driver program------------------------------------
while True:
    c = menu()
    if c == 1:
        insertData()
    elif c == 2:
        searchData()
    elif c == 3:
        deleteData()
    elif c == 4:
        updateData()
    elif c == 5:
        reportData()
    else:
        break
