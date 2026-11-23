import tkinter as tk
from tkinter import Listbox, Scrollbar

def print_selections_color():
    selected_colors = listbox1.curselection()
    label1.config(text="Selected Colors: " + ", ".join([listbox1.get(i) for i in selected_colors]))
    
def print_selections_sports():
    selected_sports = listbox2.curselection()
    label2.config(text="Selected Sports: " + ", ".join([listbox2.get(i) for i in selected_sports]))

root = tk.Tk()
root.title('Sports & Color')

# Create the first listbox for colors (single selection)
listbox1 = Listbox(root, width=50, height=6, selectmode=tk.SINGLE)
listbox1.grid(row=0, column=0, padx=10, pady=10)

# Create the vertical scrollbar for the first listbox
yscroll1 = Scrollbar(root, command=listbox1.yview, orient=tk.VERTICAL)
yscroll1.grid(row=0, column=1, sticky=tk.N+tk.S)
listbox1.configure(yscrollcommand=yscroll1.set)

# Create the horizontal scrollbar for the first listbox
xscroll1 = Scrollbar(root, command=listbox1.xview, orient=tk.HORIZONTAL)
xscroll1.grid(row=1, column=0, columnspan=2, sticky=tk.W+tk.E)
listbox1.configure(xscrollcommand=xscroll1.set)

# Load data into the first listbox
colors = ["red", "yellow", "green", "blue", "purple", "black", "orange", "pink"]
for item in colors:
    listbox1.insert(tk.END, item)

# Create the second listbox for sports (multiple selection)
listbox2 = Listbox(root, width=50, height=6, selectmode=tk.MULTIPLE)
listbox2.grid(row=2, column=0, padx=10, pady=10)

# Create the vertical scrollbar for the second listbox
yscroll2 = Scrollbar(root, command=listbox2.yview, orient=tk.VERTICAL)
yscroll2.grid(row=2, column=1, sticky=tk.N+tk.S)
listbox2.configure(yscrollcommand=yscroll2.set)

# Create the horizontal scrollbar for the second listbox
xscroll2 = Scrollbar(root, command=listbox2.xview, orient=tk.HORIZONTAL)
xscroll2.grid(row=3, column=0, columnspan=2, sticky=tk.W+tk.E)
listbox2.configure(xscrollcommand=xscroll2.set)

# Load data into the second listbox
sports = ["Football", "Basketball", "Tennis", "Swimming", "Golf", "Running", "Cycling", "Volleyball"]
for item in sports:
    listbox2.insert(tk.END, item)

# Labels to display selected items
label1 = tk.Label(root, text="Selected Colors: ")
label1.grid(row=4, column=0, padx=10, pady=10)

label2 = tk.Label(root, text="Selected Sports: ")
label2.grid(row=5, column=0, padx=10, pady=10)

# Button to print selection
print_color_button = tk.Button(root, text="Print Color Selections", command=print_selections_color)
print_color_button.grid(row=6, column=0, columnspan=2, pady=10)

print_sport_button = tk.Button(root, text="Print Sports Selections", command=print_selections_sports)
print_sport_button.grid(row=7, column=0, columnspan=2, pady=10)

root.mainloop()
