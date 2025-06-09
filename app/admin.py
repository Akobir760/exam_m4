from core.db_settings import execute_query



def add_new_book():
    try:
        b_title = input("Enter book title: ")
        author_id = int(input("Enter author's id: "))

        check_query = "SELECT title, author_id FROM books;"
        books_list = execute_query(query=check_query, fetch="all")

        for book in books_list:
            if book[0] == b_title and book[1] == author_id:
                print("This book is exists!")
                return

        published = input("Enter book's published date: ")
        count = input("Enter book's total count: ")

        add_book_query = "INSERT INTO books (title, author_id, published_at, total_count, available_count) VALUES (%s, %s, %s, %s, %s);"
        execute_query(query=add_book_query, params=(b_title,author_id, published, count, count ))
        print("New book added!")
    
    except BaseException as e:
        print(e)


def new_author():
    try:
        full_name = input("Enter author's full name: ")

        author_check = "SELECT * FROM authors;"
        authors_list = execute_query(query=author_check, fetch="all")

        for author in authors_list:
            if author[1] == full_name:
                print(f"This author is exists! \n Author id: {author[0]}")
                return

        add_author_query = "INSERT INTO authors (full_name) VALUES (%s);"
        execute_query(query=add_author_query, params=(full_name,))
        print("New author added!")

    except BaseException as e:
        print(e)


def change_books(choice_number):
    books = "SELECT id, title, author_id FROM books;"
    books_list = execute_query(query=books, fetch="all")
    for book in books_list:
        print(f"book id: {book[0]}, title: {book[1]}, author id: {book[2]}")

    book_id = int(input("Enter book's id: "))

    if choice_number == 1:
        new_title = input("Enter new title: ")
        query = "UPDATE books SET title = %s WHERE id = %s;"
        execute_query(query=query, params=(new_title, book_id))
        print("Title is update!")

    
    elif choice_number == 2:
        authors = "SELECT * FROM authors;"
        authors_list = execute_query(query=authors, fetch="all")

        for author in authors_list:
            print(f"id: {author[0]}, full name: {author[1]}")

        author_id = int(input("Enter new author's id: "))

        update_author = "UPDATE books SET author_id = %s WHERE id = %s;"
        execute_query(query=update_author, params=(author_id, book_id))
        print("Author is update!")


    elif choice_number == 3:
        new_date = input("Enter new date (YYYY-MM-DD): ")
        update_date = "UPDATE books SET published_at = %s WHERE id = %s;"

        execute_query(query=update_date, params=(new_date, book_id))
        print("Date is update!")


    elif choice_number == 4:
        new_tcount = int(input("Enter new total count: "))
        update_tcount = "UPDATE books SET total_count = %s WHERE id = %s;"        

        execute_query(query=update_tcount, params=(new_tcount, book_id))
        print("Total count is update!")

    elif choice_number == 5:
        new_acount = int(input("Enter new available count: "))
        update_acount = "UPDATE books SET available_count = %s WHERE id = %s;"        

        execute_query(query=update_acount, params=(new_acount, book_id))
        print("Available count is update!")




def delete_book():
    books = "SELECT id, title, author_id FROM books;"
    books_list = execute_query(query=books, fetch="all")
    for book in books_list:
        print(f"book id: {book[0]}, title: {book[1]}, author id: {book[2]}")


    book_id = int(input("Enter deleting book's id: "))
    delete_query = "DELETE FROM books WHERE id = %s;"
    execute_query(query=delete_query, params=(book_id,))

    print("Book is delete!")   


def show_all_users():
    show_query = "SELECT * FROM users;"
    users_list = execute_query(query=show_query, fetch="all")
    
    print('-' *15, "USERS", '-' * 15)
    for user in users_list:
        print(f"id: {user[0]}, name: {user[1]}, emal: {user[2]}")
    print('-' *15, "USERS", '-' * 15)


def statistics():
    all_debts_number = 0

    books = "SELECT * FROM books;"
    books_list = execute_query(query=books, fetch="all")

    print('-' *15, "BOOKS   ", '-' * 15) 
    for book in books_list:
        print(f"book id: {book[0]}, title: {book[1]}, author id: {book[2]}, published date: {book[3]}, total count: {book[4]}, available count: {book[5]}")
        debt_book = book[4] - book[5]
        all_debts_number += debt_book

    print(f"All debts count: {all_debts_number}")
    print('-' *15, "BOOKS ", '-' * 15) 