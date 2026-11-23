import tkinter as tk
from tkinter import messagebox
#------------------------------------------------------------------------------
class Employee:
    def __init__(self, name, e_id , age, salary):
        self.name = name
        self.id = e_id
        self.age = age
        self.salary = salary
#------------------------------------------------------------------------------
class Payroll:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def calculate_payroll(self):
        return sum(employee.salary for employee in self.employees)
#------------------------------------------------------------------------------
class EmployeeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Payroll Management")

        self.payroll = Payroll()

        # Widgets
        self.name_label = tk.Label(root, text="Name:")
        self.name_label.grid(row=0, column=0, padx=10, pady=10)
        self.name_entry = tk.Entry(root)
        self.name_entry.grid(row=0, column=1, padx=10, pady=10)

        self.ID_label = tk.Label(root, text="ID:")
        self.ID_label.grid(row=1, column=0, padx=10, pady=10)
        self.ID_entry = tk.Entry(root)
        self.ID_entry.grid(row=1, column=1, padx=10, pady=10) 

        self.age_label = tk.Label(root, text="Age:")
        self.age_label.grid(row=2, column=0, padx=10, pady=10)
        self.age_entry = tk.Entry(root)
        self.age_entry.grid(row=2, column=1, padx=10, pady=10)

        self.salary_label = tk.Label(root, text="Salary:")
        self.salary_label.grid(row=3, column=0, padx=10, pady=10)
        self.salary_entry = tk.Entry(root)
        self.salary_entry.grid(row=3, column=1, padx=10, pady=10)

        self.add_button = tk.Button(root, text="Add Employee", command=self.add_employee)
        self.add_button.grid(row=4, column=0, columnspan=2, pady=10)

        self.calculate_button = tk.Button(root, text="Calculate Payroll", command=self.calculate_payroll)
        self.calculate_button.grid(row=5, column=0, columnspan=2, pady=10)

        self.result_label = tk.Label(root, text="", font=("Arial", 14))
        self.result_label.grid(row=6, column=0, columnspan=2, pady=10)

    def add_employee(self):
        name = self.name_entry.get()
        e_id = self.ID_entry.get()
        age = self.age_entry.get()
        salary = self.salary_entry.get()

        if name and age and salary:
            try:
                age = int(age)
                salary = float(salary)
                employee = Employee(name,e_id, age, salary)
                self.payroll.add_employee(employee)
                messagebox.showinfo("Success", "Employee added successfully!")
                self.name_entry.delete(0, tk.END)
                self.age_entry.delete(0, tk.END)
                self.salary_entry.delete(0, tk.END)
            except ValueError:
                messagebox.showerror("Error", "Age and Salary must be numbers!")
        else:
            messagebox.showerror("Error", "All fields are required!")

    def calculate_payroll(self):
        total_salary = self.payroll.calculate_payroll()
        self.result_label.config(text=f"Total Payroll: {total_salary}")
#------------------------------------------------------------------------------
if __name__ == "__main__":
    root = tk.Tk()
    app = EmployeeApp(root)
    root.mainloop()
