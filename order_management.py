import sqlite3

def place_order(user_id, product_id, quantity):
    conn = sqlite3.connect('inventory.db')
    cursor = conn.cursor()

    # Check the current quantity of the product
    cursor.execute('SELECT quantity FROM products WHERE id = ?', (product_id,))
    result = cursor.fetchone()
    if result is None:
        print("Product not found.")
        conn.close
        return

    current_quantity = result[0]    
    print(f"Current quantity of product ID {product_id}: {current_quantity}")
   
    if current_quantity < quantity:
        print("Insufficient stock to fulfill the order.")
        conn.close
        return

    # Insert the order into the orders table
    cursor.execute('INSERT INTO orders (user_id, product_id, quantity) VALUES (?, ?, ?)', (user_id, product_id, quantity))
    
    # Update the product quantity in the inventory
    new_quantity = current_quantity - quantity
    cursor.execute('UPDATE products SET quantity = ? WHERE id = ?', (new_quantity, product_id))

    conn.commit()
    print(f"New quantity of product ID {product_id}: {new_quantity}")
    
    conn.close()
    print("Order placed successfully.")

def return_product(user_id, product_id, quantity):
    conn = sqlite3.connect('inventory.db')
    cursor = conn.cursor()

    # Check the current quantity of the product
    cursor.execute('SELECT quantity FROM products WHERE id = ?', (product_id,))
    result = cursor.fetchone()
    if result is None:
        print("Product not found.")
        conn.close()
        return

    current_quantity = result[0]
    print(f"Current quantity of product ID {product_id}: {current_quantity}")

    # Update the product quantity in the inventory
    new_quantity = current_quantity + quantity
    cursor.execute('UPDATE products SET quantity = ? WHERE id = ?', (new_quantity, product_id))

    # Record the return in a returns table 
    cursor.execute('INSERT INTO returns (user_id, product_id, quantity) VALUES (?, ?, ?)', (user_id, product_id, quantity))

    conn.commit()
    print(f"New quantity of product ID {product_id}: {new_quantity}")
    
    conn.close()
    print("Product returned successfully.")