from app.table_execute import executes
from app.auth  import Register, logout, login
from app.admin import add_new_book, new_author, change_books, delete_book, show_all_users, statistics
from app.user import show_all_books, rent_book, return_book, show_my_rents




def Auth():
    print("""
1. Register
2. Login
3. Exit""")
    
    choice = input("Enter your choice number: ")
    
    if choice == '1':
        Register()
    elif choice == '2':
        res = login()
        if res == "admin":
            return Admin_menu()
        elif res == "user":
            return user_menu()
        else:
            print("You need to register!")
    elif choice == '3':
        return
    return Auth()

    
def Admin_menu():
    print("""
1. Add new  book
2. Add new author
3. Change book
4. Delete book
5. Show all users
6. Statistics
7. Exit
""")
    
    choice = input("Enter your choice number: ")
    
    if choice == '1':
        add_new_book()
    elif choice == '2':
        new_author()
    elif choice == '3':
        change_book()
    elif choice == '4':
        delete_book()
    elif choice == '5':
        show_all_users()
    elif choice == '6':
        statistics()
    elif choice == '7':
        print("Good bye! \n Exiting...")
        Auth()
    return Admin_menu()


def change_book():
    print("""
1. Change title
2. Change author
3. Change published date
4. Change total count
5. Change available count
6. Exit""")
    
    ch_choice = input("Enter your choice number: ")

    if ch_choice == '1':
        change_books(1)
    elif ch_choice == '2':
        change_books(2)
    elif ch_choice == '3':
        change_books(3)
    elif ch_choice == '4':
        change_books(4)
    elif ch_choice == '5':
        change_books(5)
    elif ch_choice == '6':
        print("Exiting...")
        return Admin_menu()
    return(change_book())

def user_menu():
    print("""
1. Show all books
2. Rent book 
3. Return book
4. Show my rents
5. Exit""")
    
    choice = input("Enter your choice number: ")
    
    if choice == '1':
        show_all_books()
    elif choice == '2':
        rent_book()
    elif choice == '3':
        return_book()
    elif choice == '4':
        show_my_rents()
    elif choice == '5':
        print("Good bye! \n Exiting...")
        logout()
        return Auth()
    return user_menu()

    

if __name__ == "__main__":
    executes()
    logout()
    Auth()