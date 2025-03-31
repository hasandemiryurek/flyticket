books = {}
students = {}
def read_data_and_load():
    with open('books.txt', 'r') as books_file:
        for line in books_file:
            values = line.strip().split(',')
            if len(values) == 4:
                isbn, book, author, checked_out = values
            books[isbn] = {'book': book, 'author': author, 'checked_out': checked_out}

    with open('students.txt', 'r') as students_file:
        for line in students_file:
            values = line.strip().split()
            if len(values) >= 2:
                student_id, name = values[0], ' '.join(values[1:])
                students[student_id] = {'name': name, 'books_checked_out': []}

def save_data():
    with open('books.txt', 'w') as books_file:
        for isbn, book_info in books.items():
            book = book_info['book']
            author = book_info['author']
            checked_out = book_info['checked_out']
            books_file.write(f"{isbn},{book},{author},{checked_out}\n")

    with open('students.txt', 'w') as students_file:
        for student_id, student_info in students.items():
            name = student_info['name']
            students_file.write(f"{student_id} {name}\n")

def list_all_books():
    for isbn, book_info in books.items():
        print(f"ISBN: {isbn}, Book: {book_info['book']}, Author: {book_info['author']}")

def list_checked_out_books():
    for isbn, book_info in books.items():
        if book_info['checked_out'] == 'T':
            print(f"ISBN: {isbn}, Book: {book_info['book']}, Author: {book_info['author']}")

def add_book():
        isbn = input("Enter ISBN: ")
        book = input("Enter Book name: ")
        author = input("Enter Author: ")
        checked_out = 'F'
        books[isbn] = {'book': book, 'author': author, 'checked_out': checked_out}
        with open('books.txt', 'a',encoding='utf-8') as books_file:
         books_file.write(f"{isbn},{book},{author},{checked_out}\n")
         print("Book added successfully.")

def delete_book():
    isbn_to_delete = input("Enter ISBN of the book to delete: ")
    if isbn_to_delete in books:
        if books[isbn_to_delete]['checked_out'] == 'F':
            del books[isbn_to_delete]
            print("Book deleted successfully.")
            with open('books.txt', 'w', encoding='utf-8') as books_file:
                for isbn, book_info in books.items():
                    book = book_info['book']
                    author = book_info['author']
                    checked_out = book_info['checked_out']
                    books_file.write(f"{isbn},{book},{author},{checked_out}\n")
        else:
            print("Cannot delete the book. It is  checked out.")
    else:
        print("Book not found.")

def search_by_isbn():
    isbn_to_search = input("Enter ISBN to search: ")
    if isbn_to_search in books:
        book_info = books[isbn_to_search]
        print(f"ISBN: {isbn_to_search}, Book: {book_info['book']}, Author: {book_info['author']}")
    else:
        print("Book not found.")

def search_by_name():
    name = input("Enter a keyword to search by name: ")
    for isbn, book_info in books.items():
        if name.lower() in book_info['book'].lower():
            print(f"ISBN: {isbn}, Book: {book_info['book']}, Author: {book_info['author']}")

def check_out_book():
    student_id = input("Enter student ID: ")
    isbn_to_check_out = input("Enter ISBN of the book to check out: ")
    if student_id in students and isbn_to_check_out in books:
        if books[isbn_to_check_out]['checked_out'] == 'F':
            students[student_id]['books_checked_out'].append(isbn_to_check_out)
            books[isbn_to_check_out]['checked_out'] = 'T'
            print("Book checked out successfully.")
            with open('books.txt', 'r') as books_file:
                lines = books_file.readlines()
            with open('books.txt', 'w') as books_file:
                for line in lines:
                    if isbn_to_check_out not in line:
                        books_file.write(line)
                books_file.write(f"{isbn_to_check_out},{books[isbn_to_check_out]['book']},{books[isbn_to_check_out]['author']},T\n")
        else:
            print("The book is already checked out.")
    else:
        print("Invalid student ID or ISBN.")

def list_all_students():
    for student_id, student_info in students.items():
        print(f"Student ID: {student_id}, Name: {student_info['name']}")
        books_checked_out = student_info['books_checked_out']
        if books_checked_out:
            for isbn_checked_out in books_checked_out:
                book_info = books.get(isbn_checked_out)
                if book_info:
                    print(f"   ISBN: {isbn_checked_out}, Book: {book_info['book']}, Author: {book_info['author']}")
        else:
            print("No books checked out")
def run():
    while True:
        print("\n   WELCOME TO THE LIBRARY SYSTEM MENU")
        print("1) List All Books")
        print("2) List Checked Out Books")
        print("3) Add a New Book")
        print("4) Delete a Book")
        print("5) Search by ISBN")
        print("6) Search by Name")
        print("7) Check Out a Book")
        print("8) List All Students")
        print("9) Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            list_all_books()
        elif choice == '2':
            list_checked_out_books()
        elif choice == '3':
            add_book()
        elif choice == '4':
            delete_book()
        elif choice == '5':
            search_by_isbn()
        elif choice == '6':
            search_by_name()
        elif choice == '7':
            check_out_book()
        elif choice == '8':
            list_all_students()
        elif choice == '9':
            print("Exiting the Library System. Saving all data")
            save_data()
            break
        else:
            print("Invalid choice. Please enter a valid option.")

read_data_and_load()
run()

