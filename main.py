def Auth():
    print("""
1. Register
2. Login
3. Exit""")
    
    choice = input("Enter your choice number: ")
    
    if choice == '1':
        pass
    elif choice == '2':
        pass
    elif choice == '3':
        pass
    
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
        pass
    elif choice == '2':
        pass
    elif choice == '3':
        pass
    elif choice == '4':
        pass
    elif choice == '5':
        pass
    elif choice == '6':
        pass
    elif choice == '7':
        print("Good bye! \n Exiting...")
        return Auth()

    
def user_menu():
    print("""
1. Show all books
2. Rent book 
3. Return book
4. Show my rents
5. Exit""")
    
    choice = input("Enter your choice number: ")
    
    if choice == '1':
        pass
    elif choice == '2':
        pass
    elif choice == '3':
        pass
    elif choice == '4':
        pass
    elif choice == '5':
        print("Good bye! \n Exiting...")
        return Auth()

    

if __name__ == "__main__":
    Auth()