import pickle
import os
#------------------------------------------------------------------------------
class Employee():
    def __init__(self, name , family_name , ID , position , salary):
        self.name = name
        self.family_name = family_name
        self.ID = ID
        self.position = position
        self.salary = salary  
        
    def display(self):
        print("{0:10s} {1:10s} {2:10d} {3:10s} {4:10d}".format(self.name , self.family_name , self.ID , self.position ,self.salary))
#------------------------------------------------------------------------------
def reportData():
    myfile.seek(0,0)
    print("{0:10s} {1:10s} {2:10s} {3:10s} {4:10s}".format("Name", "Family Name" , "ID" , "Position" ,"Salary"))
    while True:
        try:
            obj = pickle.load(myfile)
            obj.display()
        except (EOFError) as err:
            break
#------------------------------------------------------------------------------
def searchData():
    myfile.seek(0, 0)
    ID = int(input("Enter an ID: "))
    found = False
    while True:
        try:
            obj = pickle.load(myfile)
            if obj.ID == ID:
                found = True
                break
        except (EOFError) as err:
            break
    #end of while
    if found:
        print("{0:10s} {1:10s} {2:10s} {3:10s} {4:10s}".format("Name", "Family Name" , "ID" , "Position" ,"Salary"))
        obj.display()
    else:
        print("Employee not found!")
#------------------------------------------------------------------------------
def deleteData():
    temp_file = open("temp.dat", "wb")
    myfile.seek(0, 0)
    ID = int(input("Enter an ID: "))
    found = False
    while True:
        try:
            obj = pickle.load(myfile)
            if obj.ID == ID:
                found = True
            else:
                pickle.dump(obj, temp_file)
        except (EOFError) as err:
            break
    #end of while    
    if not found:
        print("Employee not found!")
    else:
        myfile.close()
        temp_file.close()
        os.remove("emfile.dat")
        os.rename("temp.dat", "emfile.dat")
#------------------------------------------------------------------------------
def insertData():
    print("Enter name , family name , ID , position , salary: ", end= "")
    name , family_name , ID , position , salary = input().split()
    if len(name) == 0 or len(family_name) == 0 or len(ID) == 0 or len(position) == 0 or len(salary) == 0:
        print("Invalid input. Please enter all fields.")
        return
    obj = Employee(name, family_name, int(ID), position, int(salary))
    pickle.dump(obj , myfile)
#------------------------------------------------------------------------------
def menu():
    print("1. Enter an Employee ")
    print("2. Search an Employee ")
    print("3. Display all Employee ")
    print("4. Delete a Employee ")
    print("5. Exit ")
    choice = int(input("Enter your selection(1-5) : "))
    return choice
#----------------------------Driver program------------------------------------
myfile = open("emfile.dat", "a+b")
c = int()
while True:
    c = menu()
    if c == 1:
        insertData()
    elif c == 2:
        searchData()
    elif c == 3:
        reportData()
    elif c == 4:
        deleteData()
    elif c == 5:
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")
myfile.close()
