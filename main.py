import user_management
import product_management
import order_management
import reporting
import alerts

def main_menu():
    print("Welcome to Inventory Management System")
    while True:
        print("1. Login")
        print("2. Register")
        print("3. Launch GUI")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            username = input("Enter username: ")
            password = input("Enter password: ")
            user = user_management.authenticate_user(username, password)
            if user:
                print(f"Welcome {user[1]} ({user[3]})!")
                if user[3] == 'admin':
                    admin_menu()
                elif user[3] == 'storeman':
                    storeman_menu()
            else:
                print("Invalid username or password.")
        
        elif choice == '2':
            username = input("Enter new username: ")
            password = input("Enter new password: ")
            role = input("Enter role (admin/storeman): ")
            user_management.register_user(username, password, role)
            print("User registered successfully.")
        
        elif choice == '3':
            import gui
            gui.run_gui()
        
        elif choice == '3':
            print("Exiting...")
            break
        
        else:
            print("Invalid choice. Please enter a valid option.")

def admin_menu():
    while True:
        print("\nAdmin Menu:")
        print("1. Add Product")
        print("2. Add Category")
        print("3. Generate Inventory Report")
        print("4. Logout")
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter product name: ")
            category = input("Enter product category: ")
            quantity = int(input("Enter product quantity: "))
            price = float(input("Enter product price: "))
            product_management.add_product(name, category, quantity, price)
            print("Product added successfully.")
        
        elif choice == '2':
            name = input("Enter category name: ")
            product_management.add_category(name)
            print("Category added successfully.")
        
        elif choice == '3':
            products = reporting.generate_inventory_report()
            print("\nInventory Report:")
            for product in products:
                print(f"ID: {product[0]}, Name: {product[1]}, Category: {product[2]}, Quantity: {product[3]}, Price: {product[4]}")
        
        elif choice == '4':
            print("Logging out...")
            break
        
        else:
            print("Invalid choice. Please enter a valid option.")

def storeman_menu():
    while True:
        print("\nStore Manager Menu:")
        print("1. Update Product Quantity")
        print("2. Place Order")
        print("3. Return Product(s)")
        print("4. Check Low Inventory")
        print("5. Search Products")
        print("6. Logout")
        choice = input("Enter your choice: ")

        if choice == '1':
            product_id = int(input("Enter product ID: "))
            new_quantity = int(input("Enter new quantity: "))
            product_management.update_product_quantity(product_id, new_quantity)
            print("Product quantity updated successfully.")
        
        elif choice == '2':
            user_id = 1  
            product_id = int(input("Enter product ID: "))
            quantity = int(input("Enter quantity: "))
            order_management.place_order(user_id, product_id, quantity)
            
        elif choice == '3':
            user_id = 1  
            product_id = int(input("Enter product ID: "))
            quantity = int(input("Enter quantity: "))
            order_management.return_product(user_id, product_id, quantity)
        
        elif choice == '4':
            threshold = int(input("Enter low inventory threshold: "))
            low_inventory_products = alerts.check_low_inventory_threshold(threshold)
            print("\nLow Inventory Products:")
            for product in low_inventory_products:
                print(f"ID: {product[0]}, Name: {product[1]}, Category: {product[2]}, Quantity: {product[3]}")
        
        elif choice == '5':
            search_term = input("Enter product name or category to search: ")
            results = product_management.search_products(search_term)
            print("\nSearch Results:")
            for product in results:
                print(f"ID: {product[0]}, Name: {product[1]}, Category: {product[2]}, Quantity: {product[3]}, Price: {product[4]}")
        
        elif choice == '6':
            print("Logging out...")
            break
        
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main_menu()
