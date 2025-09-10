# You are building a Library Management System in Python. The system should store books
#  in a dictionary where:

# Key → Book ID
# Value → Book Title
# Write a Python program to perform the following operations using Dictionaries:
# Add a book to the library (Book ID, Title).
# Remove a book using Book ID.
# Search for a book by Book ID and display the title.
# Update the title of a book (e.g., correction in title).
# Display all books in the library.
# Count the total number of books in the library.
# Check if a book title exists in the library (reverse lookup).
# Library Management System

library = {} 

def addbook(bookid, title):
    library[bookid] = title
    print(f"Book ID {bookid} for title '{title}' added.")

def removebook(bookid):
    if bookid in library:
        removed = library.pop(bookid)
        print(f"Book '{removed}' with ID {bookid} removed.")
    else:
        print(f"No book found with ID {bookid} to remove.")

def searchbook(bookid):
    if bookid in library:
        print(f"Book found → ID: {bookid}, Title: {library[bookid]}")
    else:
        print(f"No book found with ID {bookid}.")

def updatebook(bookid, new_title):
    if bookid in library:
        library[bookid] = new_title
        print(f"Book ID {bookid} updated to '{new_title}'.")
    else:
        print(f"No book found with ID {bookid} to update.")

def display():
    if not library:
        print("Library is empty.")
    else:
        print("Books in library:")
        for k, v in library.items():
            print(f"ID: {k} → Title: {v}")

def countbooks():
    print(f"Total number of books: {len(library)}")

def checktitle(title):
    if title in library.values():
        print(f"Book '{title}' exists in the library.")
    else:
        print(f"Book '{title}' does not exist in the library.")

while True:
    print("\nLibrary Operations:")
    print("1. Add Book")
    print("2. Remove Book")
    print("3. Search Book by ID")
    print("4. Update Book Title")
    print("5. Display All Books")
    print("6. Count Total Books")
    print("7. Check Book by Title (reverse lookup)")
    print("8. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        key = input("Enter Book ID: ")
        val = input("Enter Book Title: ")
        addbook(key, val)

    elif choice == 2:
        key = input("Enter Book ID to remove: ")
        removebook(key)

    elif choice == 3:
        key = input("Enter Book ID to search: ")
        searchbook(key)

    elif choice == 4:
        key = input("Enter Book ID to update: ")
        new_title = input("Enter new Book Title: ")
        updatebook(key, new_title)

    elif choice == 5:
        display()

    elif choice == 6:
        countbooks()

    elif choice == 7:
        title = input("Enter Book Title to check: ")
        checktitle(title)

    elif choice == 8:
        print("Exiting... Thank you for using Library Management System.")
        break

    else:
        print("Invalid choice! Try again.")
