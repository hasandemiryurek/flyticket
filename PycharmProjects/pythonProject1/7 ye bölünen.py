books_file_path = "books.txt"
students_file_path = "students.txt"

def  read_data_from_file(file_path):
    with open(file_path, 'r',) as file:
        list = file.readlines()

    list = [satir.strip() for satir in list]

    return list

def write_data_to_file(file_path, list):
    with open(file_path, "w") as file:
        for item in list:
            file.write("".join(item) + ("\n"))



def list_all_books():
    books = read_data_from_file(books_file_path)
    for book in books:
        print(" ".join(book[:len(book)-2]))

def search_by_name():
    name = input("what is the name of the book")
    books = read_data_from_file(books_file_path)
    for book in books:
        if name in book:
            print(book[11:len(book)-2])


def search_by_isbn():
    isbn_to_search = input("Enter ISBN number of the book: ")
    books = read_data_from_file(books_file_path)
    for book in books:
        if book[0] == isbn_to_search:
            print(book[2:len(book)-4])

def check_out_book():
    student_id = input("Enter student ID: ")
    isbn_to_check_out = input("Enter ISBN of the book to check out: ")

    print(f"Debug: Student ID: {student_id}, ISBN: {isbn_to_check_out}")

    if student_id in students and isbn_to_check_out in books:
        print(f"Debug: Book checked_out value: {books[isbn_to_check_out]['checked_out']}")

        if books[isbn_to_check_out]['checked_out'] == 'F':
            students[student_id]['books_checked_out'].append(isbn_to_check_out)
            books[isbn_to_check_out]['checked_out'] = 'T'
            print("Book checked out successfully.")

            # Dosyayı güncelleme adımları
            with open('books.txt', 'r+', encoding='utf-8') as books_file:
                lines = books_file.readlines()
                books_file.seek(0)
                books_file.truncate()

                for line in lines:
                    if isbn_to_check_out not in line:
                        books_file.write(line)

                # Kitabın ödünç alındığı durumu güncel satırı ekleyin
                books_file.write(f"{isbn_to_check_out},{books[isbn_to_check_out]['title']},{books[isbn_to_check_out]['author']},T\n")
        else:
            print("The book is already checked out.")
    else:
        print("Invalid student ID or ISBN.")


def list_checked_out_books():
    books = read_data_from_file(books_file_path)
    for book in books:
        if book[len(book)-1] == 'T':
         print( "".join(book))



def add_new_book():
    isbn = input("Enter ISBN number: ")
    name = input("Enter book name: ")
    author = input("Enter author name: ")
    checked = 'F'
    new_book =[isbn, name, author, checked]
    books = read_data_from_file(books_file_path)
    books.append(new_book)
    write_data_to_file(books_file_path, books)


def delete_book():
    isbn_to_delete = input("Enter ISBN number of the book to delete: ")
    books = read_data_from_file(books_file_path)
    for book in books:
        if book[:10] == isbn_to_delete and (book[len(book)-1:len(book)]) == 'F':
            books.remove(book)
            write_data_to_file(books_file_path, books)
            print("Book deleted successfully.")
        else:
            print("warning")


# Main menu loop
while True:
    print("\nLibrary Management System Menu:")
    print("1. List all books in the library")
    print("2. List all checked out books")
    print("3. Add a new book")
    print("4. Delete a book")
    print("5. Search by name")
    print("6  Search by isbn")
    print("7  Check out a book")
    print("8  List all the students")
    print("9. Exit")

    choice = input("Enter your choice (1-4, 9): ")

    if choice == '1':
        list_all_books()
    elif choice == '2':
        list_checked_out_books()
    elif choice == '3':
        add_new_book()
    elif choice == '4':
        delete_book()
    elif choice == '5':
        search_by_name()
    elif choice == '6':
        search_by_isbn()
    elif choice == '7':
        checkout_book_to_student()
    elif choice == '8':
        display_students_with_books()

    elif choice == '9':
        books = read_data_from_file(books_file_path)
        write_data_to_file(books_file_path, books)
        students = read_data_from_file(students_file_path)
        write_data_to_file(students_file_path,students)
        print("Exiting the Library Management System. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 4, or 9.")



