import sqlite3
from datetime import date

###############################################################################
# Database Setup and Helper Functions
###############################################################################

def create_tables(c, conn):
    """Creates the necessary tables if they don't exist."""
    c.execute("""
    CREATE TABLE IF NOT EXISTS students (
        student_id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL,
        phone TEXT,
        enrollment_date DATE NOT NULL,
        major TEXT,
        gpa REAL
    );
    """)
    
    c.execute(""" 
    CREATE TABLE IF NOT EXISTS departments(
        department_id INTEGER PRIMARY KEY AUTOINCREMENT,
        department_name TEXT NOT NULL UNIQUE,
        description TEXT
    );
    """)
    conn.commit()

#------------------------------------------------------------------------------
def add_student(c, conn, first, last, email, phone, major, gpa):
    """Inserts a single student record into the database."""
    c.execute("""
    INSERT INTO students (first_name, last_name, email, phone, enrollment_date, major, gpa)
    VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (first, last, email, phone, date.today().isoformat(), major, gpa))
    conn.commit()

#------------------------------------------------------------------------------
def insert_student(c, conn):
    """Interactive loop to insert multiple students."""
    while True:
        try:
            first = input("Enter first name: ")
            last = input("Enter last name: ")
            email = input("Enter email: ")
            phone = input("Enter phone: ")
            major = input("Enter major: ")
            gpa = float(input("Enter GPA (0.0 - 4.0): "))
            
            add_student(c, conn, first, last, email, phone, major, gpa)
            print("Student added successfully!")
            
        except ValueError:
            print("Invalid input for GPA. Please enter a number.")
            continue
        except sqlite3.IntegrityError:
            print("Error: Email already exists. Please use a unique email.")
            continue

        control = input("Do you want to add another student? (y/n): ")
        if control.lower() != 'y':
            break

#------------------------------------------------------------------------------
def add_department(c, conn, department_name, description):
    """Inserts a single department record into the database."""
    c.execute("""
    INSERT INTO departments (department_name, description)
    VALUES (?, ?)
    """, (department_name, description))
    conn.commit()

#------------------------------------------------------------------------------
def insert_departments(c, conn):
    """Interactive loop to insert multiple departments."""
    while True:
        department_name = input("Enter department name: ")
        description = input("Enter description for the department: ")
        
        try:
            add_department(c, conn, department_name, description)
            print("Department added successfully!")
        except sqlite3.IntegrityError:
            print("Error: Department name already exists.")

        control = input("Do you want to add another department? (y/n): ")
        if control.lower() != 'y':
            break

#------------------------------------------------------------------------------
def view_top_students(c):
    """Displays students with a GPA greater than 3.5."""
    print("\n--- Top Students (GPA > 3.5) ---")
    c.execute("SELECT * FROM students WHERE gpa > ?", (3.5,))
    rows = c.fetchall()
    if not rows:
        print("No students found with GPA > 3.5.")
    for row in rows:
        print(row)

#------------------------------------------------------------------------------
def update_student_gpa(c, conn):
    """Updates the GPA of a specific student by ID."""
    try:
        student_id = int(input("Enter Student ID to update: "))
        new_gpa = float(input("Enter new GPA: "))
        
        c.execute("UPDATE students SET gpa = ? WHERE student_id = ?", (new_gpa, student_id))
        conn.commit()
        
        if c.rowcount > 0:
            print(f"Successfully updated GPA for Student ID {student_id}.")
        else:
            print(f"No student found with ID {student_id}.")
    except ValueError:
        print("Invalid input. Please enter numeric values.")

###############################################################################
# Main Application Logic
###############################################################################

def main():
    """Main function to run the application menu."""
    conn = None
    try:
        conn = sqlite3.connect('students.db')
        c = conn.cursor()
        
        # Initialize database tables
        create_tables(c, conn)

        # Main menu loop
        while True:
            print("\n========================================")
            print("   University Database Management System")
            print("========================================")
            print("1. Insert Student")
            print("2. Insert Department")
            print("3. View Top Students (GPA > 3.5)")
            print("4. Update Student GPA")
            print("5. Exit")
            
            choice = input("Enter your choice (1-5): ")

            if choice == '1':
                insert_student(c, conn)
            elif choice == '2':
                insert_departments(c, conn)
            elif choice == '3':
                view_top_students(c)
            elif choice == '4':
                update_student_gpa(c, conn)
            elif choice == '5':
                print("Exiting program. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 5.")

    except sqlite3.Error as e:
        print(f"Database error occurred: {e}")
    except KeyboardInterrupt:
        print("\nProgram interrupted by user.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        # Ensure the database connection is always closed
        if conn:
            conn.close()
            print("Database connection closed successfully.")

###############################################################################
# Entry Point
###############################################################################

# This ensures the main() function only runs if the script is executed directly,
# not if it is imported as a module in another script.
if __name__ == "__main__":
    main()