from core.db_settings import execute_query
from datetime import datetime


def show_all_books():
    books = "SELECT * FROM books;"
    books_list = execute_query(query=books, fetch="all")
    for book in books_list:
        if int(book[5]) > 0:
            print(f"book id: {book[0]}, title: {book[1]}, author id: {book[2]}, published year: {book[3]}")


def rent_book():
    try:
        login_userr = "SELECT id FROM users WHERE is_login = TRUE;"
        user = execute_query(query=login_userr, fetch="all")
        user_id = int(user[0][0])

        show_all_books()

        book_id = input("Enter book id: ")
        borrowed_at = datetime.now().strftime('%Y-%m-%d')

        query = "SELECT * FROM borrows WHERE user_id = %s and returned_at is NULL;"
        unreturned_b_list = execute_query(query=query, params=(user_id,), fetch="all")

        if unreturned_b_list:
            for books_list in unreturned_b_list:
                if books_list[1] == user_id and books_list[2] ==  book_id and books_list[4] is None:
                    print("You already rent this book!")
                    return

        borrow_query = "INSERT INTO borrows (user_id, book_id, borrowed_at) VALUES (%s, %s, %s)"
        execute_query(query=borrow_query, params=(user_id, book_id, borrowed_at))
        print("The book was rented!")

        update_query = "UPDATE books SET available_count = available_count - 1 WHERE id = %s;"
        execute_query(query=update_query, params=(book_id,))

    except BaseException as e:
        print(e)


def return_book():
    try:
        login_userr = "SELECT id FROM users WHERE is_login = TRUE;"
        user = execute_query(query=login_userr, fetch="all")
        user_id = int(user[0][0])


        book_query = "SELECT * FROM books;"
        books_list = execute_query(query=book_query, fetch="all")

        print("-" * 15, "Your unreturned books list:", "-" * 15)

        query = "SELECT * FROM borrows WHERE user_id = %s and returned_at is NULL;"
        unreturned_b_list = execute_query(query=query, params=(user_id,), fetch="all")
        for book in books_list:
            for b_list in unreturned_b_list:
                if book[0] == b_list[2]:
                    print(f"book id: {b_list[2]}, book name: {book[1]} ,borrowed_at: {b_list[3]}")

        print("-" * 15, "Your unreturned books list:", "-" * 15)

        
        book_id = int(input("Enter the id of the book you want to return: "))
        returned_at = datetime.now().strftime('%Y-%m-%d')

        for list in unreturned_b_list:
            if int(book_id) == int(list[2]):
                update_borrow = "UPDATE borrows SET returned_at = %s WHERE user_id = %s and book_id = %s;"
                execute_query(query=update_borrow, params=(returned_at, user_id, book_id))
                print("The book was returned!")

                update_query_return = "UPDATE books SET available_count = available_count + 1 WHERE id = %s;"
                execute_query(query=update_query_return, params=(book_id,))

                return
                
        
        print("You did not rent this book!")
        

    
    except BaseException as e:
            print(e)

def show_my_rents():
    try:
        login_userr = "SELECT id FROM users WHERE is_login = TRUE;"
        user = execute_query(query=login_userr, fetch="all")
        user_id = int(user[0][0])

        print("-" * 15, "Your unreturned books list:", "-" * 15)

        query = "SELECT * FROM borrows WHERE user_id = %s and returned_at is NULL;"
        unreturned_b_list = execute_query(query=query, params=(user_id,), fetch="all")
        for b_list in unreturned_b_list:
            print(f"book id: {b_list[2]}, borrowed_at: {b_list[3]}")

        print("\n","-" * 15, "Your unreturned books list:", "-" * 15)

        print("*" * 91)

        print("-" * 15, "Your returned books list:", "-" * 15)

        query = "SELECT * FROM borrows WHERE user_id = %s and returned_at is NOT NULL;"
        returned_b_list = execute_query(query=query, params=(user_id,), fetch="all")
        for r_list in returned_b_list:
            print(f"book id: {r_list[2]}, borrowed_at: {r_list[3]}, returned_at: {r_list[4]}")

        print("-" * 15, "Your returned books list:", "-" * 15)       


    except BaseException as e:
        print(e)
    
