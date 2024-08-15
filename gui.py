import tkinter as tk
from tkinter import messagebox
import user_management
import product_management
import order_management
import reporting
import alerts

class InventoryApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Inventory Management System")
        self.geometry("600x400")
        self.create_login_screen()

    def clear_frame(self):
        """Clear the current frame."""
        for widget in self.winfo_children():
            widget.destroy()

    def create_login_screen(self):
        """Create the login screen."""
        self.clear_frame()
        tk.Label(self, text="Login", font=("Arial", 18)).pack(pady=20)

        tk.Label(self, text="Username").pack()
        self.username_entry = tk.Entry(self)
        self.username_entry.pack()

        tk.Label(self, text="Password").pack()
        self.password_entry = tk.Entry(self, show="*")
        self.password_entry.pack()

        tk.Button(self, text="Login", command=self.handle_login).pack(pady=10)
        tk.Button(self, text="Sign Up", command=self.create_signup_screen).pack(pady=10)

    def handle_login(self):
        """Handle the login process."""
        username = self.username_entry.get()
        password = self.password_entry.get()
        user = user_management.authenticate_user(username, password)
        if user:
            if user[3] == 'admin':
                self.create_admin_menu()
            elif user[3] == 'storeman':
                self.create_storeman_menu()
        else:
            messagebox.showerror("Login Error", "Invalid username or password.")

    def create_signup_screen(self):
        """Create the signup screen."""
        self.clear_frame()
        tk.Label(self, text="Sign Up", font=("Arial", 18)).pack(pady=20)

        tk.Label(self, text="Username").pack()
        self.signup_username_entry = tk.Entry(self)
        self.signup_username_entry.pack()

        tk.Label(self, text="Password").pack()
        self.signup_password_entry = tk.Entry(self, show="*")
        self.signup_password_entry.pack()

        tk.Label(self, text="Role (admin/storeman)").pack()
        self.signup_role_entry = tk.Entry(self)
        self.signup_role_entry.pack()

        tk.Button(self, text="Sign Up", command=self.handle_signup).pack(pady=10)
        tk.Button(self, text="Back to Login", command=self.create_login_screen).pack(pady=10)

    def handle_signup(self):
        """Handle the signup process."""
        username = self.signup_username_entry.get()
        password = self.signup_password_entry.get()
        role = self.signup_role_entry.get()
        user_management.register_user(username, password, role)
        messagebox.showinfo("Sign Up", "User registered successfully.")
        self.create_login_screen()

    def create_admin_menu(self):
        """Create the admin menu in the GUI."""
        self.clear_frame()
        tk.Label(self, text="Admin Menu", font=("Arial", 18)).pack(pady=20)

        tk.Button(self, text="Add Product", command=self.add_product).pack(pady=10)
        tk.Button(self, text="Add Category", command=self.add_category).pack(pady=10)
        tk.Button(self, text="Generate Inventory Report", command=self.generate_report).pack(pady=10)
        tk.Button(self, text="Logout", command=self.create_login_screen).pack(pady=10)

    def add_product(self):
        """Create a form to add a product."""
        self.clear_frame()
        tk.Label(self, text="Add Product", font=("Arial", 18)).pack(pady=20)
        
        tk.Label(self, text="Name").pack()
        name_entry = tk.Entry(self)
        name_entry.pack()

        tk.Label(self, text="Category").pack()
        category_entry = tk.Entry(self)
        category_entry.pack()

        tk.Label(self, text="Quantity").pack()
        quantity_entry = tk.Entry(self)
        quantity_entry.pack()

        tk.Label(self, text="Price").pack()
        price_entry = tk.Entry(self)
        price_entry.pack()

        def submit_product():
            """Submit the new product."""
            name = name_entry.get()
            category = category_entry.get()
            quantity = int(quantity_entry.get())
            price = float(price_entry.get())
            product_management.add_product(name, category, quantity, price)
            messagebox.showinfo("Success", "Product added successfully.")
        
        tk.Button(self, text="Submit", command=submit_product).pack(pady=10)
        tk.Button(self, text="Back to Menu", command=self.create_admin_menu).pack(pady=10)

    def add_category(self):
        """Create a form to add a category."""
        self.clear_frame()
        tk.Label(self, text="Add Category", font=("Arial", 18)).pack(pady=20)

        tk.Label(self, text="Category Name").pack()
        category_entry = tk.Entry(self)
        category_entry.pack()

        def submit_category():
            """Submit the new category."""
            name = category_entry.get()
            product_management.add_category(name)
            messagebox.showinfo("Success", "Category added successfully.")
        
        tk.Button(self, text="Submit", command=submit_category).pack(pady=10)
        tk.Button(self, text="Back to Menu", command=self.create_admin_menu).pack(pady=10)

    def generate_report(self):
        """Generate and display the inventory report."""
        self.clear_frame()
        tk.Label(self, text="Inventory Report", font=("Arial", 18)).pack(pady=20)
        
        products = reporting.generate_inventory_report()
        for product in products:
            tk.Label(self, text=f"ID: {product[0]}, Name: {product[1]}, Category: {product[2]}, Quantity: {product[3]}, Price: {product[4]}").pack()
        
        tk.Button(self, text="Back to Menu", command=self.create_admin_menu).pack(pady=10)

    def create_storeman_menu(self):
        """Create the store manager menu in the GUI."""
        self.clear_frame()
        tk.Label(self, text="Store Manager Menu", font=("Arial", 18)).pack(pady=20)
        
        tk.Button(self, text="Update Product Quantity", command=self.update_quantity).pack(pady=10)
        tk.Button(self, text="Place Order", command=self.place_order).pack(pady=10)
        tk.Button(self, text="Return Product(s)", command=self.return_product).pack(pady=10)
        tk.Button(self, text="Check Low Inventory", command=self.check_low_inventory).pack(pady=10)
        tk.Button(self, text="Search Products", command=self.search_products).pack(pady=10)
        tk.Button(self, text="Logout", command=self.create_login_screen).pack(pady=10)

    def update_quantity(self):
        """Create a form to update product quantity."""
        self.clear_frame()
        tk.Label(self, text="Update Product Quantity", font=("Arial", 18)).pack(pady=20)
        
        tk.Label(self, text="Product ID").pack()
        product_id_entry = tk.Entry(self)
        product_id_entry.pack()

        tk.Label(self, text="New Quantity").pack()
        quantity_entry = tk.Entry(self)
        quantity_entry.pack()

        def submit_update():
            """Submit the updated quantity."""
            product_id = int(product_id_entry.get())
            new_quantity = int(quantity_entry.get())
            product_management.update_product_quantity(product_id, new_quantity)
            messagebox.showinfo("Success", "Product quantity updated successfully.")
        
        tk.Button(self, text="Submit", command=submit_update).pack(pady=10)
        tk.Button(self, text="Back to Menu", command=self.create_storeman_menu).pack(pady=10)

    def place_order(self):
        """Create a form to place an order."""
        self.clear_frame()
        tk.Label(self, text="Place Order", font=("Arial", 18)).pack(pady=20)
        
        tk.Label(self, text="Product ID").pack()
        product_id_entry = tk.Entry(self)
        product_id_entry.pack()

        tk.Label(self, text="Quantity").pack()
        quantity_entry = tk.Entry(self)
        quantity_entry.pack()

        def submit_order():
            """Submit the new order."""
            product_id = int(product_id_entry.get())
            quantity = int(quantity_entry.get())
            user_id = 1  # Assuming the store manager is logged in, adjust accordingly
            order_management.place_order(user_id, product_id, quantity)
            messagebox.showinfo("Success", "Order placed successfully.")
        
        tk.Button(self, text="Submit", command=submit_order).pack(pady=10)
        tk.Button(self, text="Back to Menu", command=self.create_storeman_menu).pack(pady=10)

    def return_product(self):
        """Create a form to return products."""
        self.clear_frame()
        tk.Label(self, text="Return Product(s)", font=("Arial", 18)).pack(pady=20)
        
        tk.Label(self, text="Product ID").pack()
        product_id_entry = tk.Entry(self)
        product_id_entry.pack()

        tk.Label(self, text="Quantity").pack()
        quantity_entry = tk.Entry(self)
        quantity_entry.pack()

        def submit_return():
            """Submit the return."""
            product_id = int(product_id_entry.get())
            quantity = int(quantity_entry.get())
            user_id = 1  # Assuming the store manager is logged in, adjust accordingly
            order_management.return_product(user_id, product_id, quantity)
            messagebox.showinfo("Success", "Product returned successfully.")
        
        tk.Button(self, text="Submit", command=submit_return).pack(pady=10)
        tk.Button(self, text="Back to Menu", command=self.create_storeman_menu).pack(pady=10)

    def check_low_inventory(self):
        """Create a form to check low inventory levels."""
        self.clear_frame()
        tk.Label(self, text="Check Low Inventory", font=("Arial", 18)).pack(pady=20)
        
        tk.Label(self, text="Enter Threshold").pack()
        threshold_entry = tk.Entry(self)
        threshold_entry.pack()

        def submit_threshold():
            """Submit the low inventory check."""
            threshold = int(threshold_entry.get())
            low_inventory_products = alerts.check_low_inventory_threshold(threshold)
            tk.Label(self, text="Low Inventory Products:", font=("Arial", 16)).pack(pady=10)
            for product in low_inventory_products:
                tk.Label(self, text=f"ID: {product[0]}, Name: {product[1]}, Category: {product[2]}, Quantity: {product[3]}").pack()

        tk.Button(self, text="Submit", command=submit_threshold).pack(pady=10)
        tk.Button(self, text="Back to Menu", command=self.create_storeman_menu).pack(pady=10)

    def search_products(self):
        """Create a form to search for products."""
        self.clear_frame()
        tk.Label(self, text="Search Products", font=("Arial", 18)).pack(pady=20)
        
        tk.Label(self, text="Enter Product Name or Category").pack()
        search_entry = tk.Entry(self)
        search_entry.pack()

        def submit_search():
            """Submit the search query."""
            search_term = search_entry.get()
            results = product_management.search_products(search_term)
            tk.Label(self, text="Search Results:", font=("Arial", 16)).pack(pady=10)
            for product in results:
                tk.Label(self, text=f"ID: {product[0]}, Name: {product[1]}, Category: {product[2]}, Quantity: {product[3]}, Price: {product[4]}").pack()

        tk.Button(self, text="Search", command=submit_search).pack(pady=10)
        tk.Button(self, text="Back to Menu", command=self.create_storeman_menu).pack(pady=10)

def run_gui():
    """Runs the Tkinter main loop to display the GUI."""
    app = InventoryApp()
    app.mainloop()

if __name__ == "__main__":
    run_gui()  # Start the GUI application
