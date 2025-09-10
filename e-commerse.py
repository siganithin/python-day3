'''You are building a simple E-commerce application in Python. 
  The system should maintain a list of products available in the cart.
 Write a Python program to perform the following operations using Lists:
1.Add a product to the cart.
2.Remove a product from the cart 
3.Search for a product in the cart 
4.Display all products in the cart
5.Show the total number of products in the cart
 
Cart Operations:
1. Add Product
2. Remove Product
3. Search Product
4. Display Cart
5. Count Products
6. Exit
 
Enter choice: 1
Enter product to add: Laptop
Product 'Laptop' added to cart.
 
Enter choice: 1
Enter product to add: Phone
Product 'Phone' added to cart.
 
Enter choice: 4
Cart: ['Laptop', 'Phone']
 
Enter choice: 3
Enter product to search: Phone
Yes, 'Phone' is in the cart.
 
Enter choice: 5
Total products in cart: 2  '''


def addprod(lst, prod):
    lst.append(prod)
    print(f"Product '{prod}' added to cart.")

def removeprod(lst, prod):
    if prod in lst:
        lst.remove(prod)
        print(f"Product '{prod}' removed from cart.")
    else:
        print(f"Product '{prod}' not found in cart.")

def searchprod(lst, prod):
    if prod in lst:
        print(f"Yes, '{prod}' is in the cart.")
    else:
        print(f"No, '{prod}' is not in the cart.")

def display(lst):
    print("Cart:", lst)

def countprods(lst):
    print(f"Total products in cart: {len(lst)}")

products = []
while True:
    print("\nCart Operations:")
    print("1. Add Product")
    print("2. Remove Product")
    print("3. Search Product")
    print("4. Display Cart")
    print("5. Count Products")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        prod = input("Enter product to add: ")
        addprod(products, prod)

    elif choice == 2:
        prod = input("Enter product to remove: ")
        removeprod(products, prod)

    elif choice == 3:
        prod = input("Enter product to search: ")
        searchprod(products, prod)

    elif choice == 4:
        display(products)

    elif choice == 5:
        countprods(products)

    elif choice == 6:
        print("Exiting... Thank you for shopping")
        break

    else:
        print("Invalid choice! Please try again.")
