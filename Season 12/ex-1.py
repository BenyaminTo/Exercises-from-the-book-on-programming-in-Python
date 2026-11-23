import pandas as pd
###############################################################################
class Library:
    def __init__(self, file_path):
        self.df = pd.read_excel(file_path)
    
    def find_book(self, book_code):
        return self.df.loc[self.df['Book Code'] == book_code]
    
    def insert_book(self, book_code, book_title, author, publisher, year_of_publication, isbn, shelf_number, status, position='end'):
        new_book = {
            'Book Code': [book_code],
            'Book title': [book_title],
            'Author': [author],
            'Publisher': [publisher],
            'Year of publication': [year_of_publication],
            'ISBN': [isbn],
            'Shelf number': [shelf_number],
            'Status': [status]
        }
     
        new_row = pd.DataFrame(new_book)
        if position.lower() == 'end':
            self.df = pd.concat([self.df, new_row], ignore_index=True)
        elif position.lower() == 'beginning':
            self.df = pd.concat([new_row, self.df], ignore_index=True)
        else:
            raise ValueError("Invalid position. Use 'end' or 'beginning'.")
     
        self.df.to_excel(file_path, index=False)
    
    def display_books(self):
        print(self.df)
    
    def run(self):
        while True:
            print("\nLibrary Management System")
            print("1. Find a book")
            print("2. Add a book")
            print("3. Display all books")
            print("4. Exit")
            choice = input("Enter your choice (1-4): ")

            if choice == '1':
                book_code = input("Enter book code: ")
                book_info = self.find_book(book_code)
                if not book_info.empty:
                    print(book_info)
                else:
                    print("Book not found.")
            elif choice == '2':
                new_book_code = input("Enter new book code: ")
                new_book_title = input("Enter new book title: ")
                new_author = input("Enter author: ")
                new_publisher = input("Enter publisher: ")
                new_year_of_publication = input("Enter year of publication: ")
                new_isbn = input("Enter ISBN: ")
                new_shelf_number = input("Enter shelf number: ")
                new_status = input("Enter status: ")
                position = input("Enter position (end/beginning): ")
                self.insert_book(new_book_code, new_book_title, new_author, new_publisher, new_year_of_publication, new_isbn, new_shelf_number, new_status, position)
                print("Book added successfully.")
            elif choice == '3':
                self.display_books()
            elif choice == '4':
                print("Exiting the system. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

###############################################################################
file_path = r"C:\Project\تمرین های کتاب برنامه نویسی با زبان پایتون\Season 12\Library.xlsx"
library = Library(file_path)

library.run()
