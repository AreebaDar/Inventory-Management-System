import sqlite3

# Function to add a new product
def add_product(name, category, quantity=0, price=0.0):
    conn = sqlite3.connect('inventory.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO products (name, category, quantity, price) VALUES (?, ?, ?, ?)', (name, category, quantity, price))
    conn.commit()
    conn.close()

# Function to add a new category
def add_category(name):
    conn = sqlite3.connect('inventory.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO categories (name) VALUES (?)', (name,))
    conn.commit()
    conn.close()

# Function to update product quantity
def update_product_quantity(product_id, new_quantity):
    conn = sqlite3.connect('inventory.db')
    cursor = conn.cursor()
    cursor.execute('UPDATE products SET quantity = ? WHERE id = ?', (new_quantity, product_id))
    conn.commit()
    conn.close()

# Function to search for products
def search_products(search_term):
    conn = sqlite3.connect('inventory.db')
    cursor = conn.cursor()
    
    query = '''
    SELECT * FROM products 
    WHERE name LIKE ? OR category LIKE ?
    '''
    search_term_wildcard = f'%{search_term}%'
    cursor.execute(query, (search_term_wildcard, search_term_wildcard))
    
    results = cursor.fetchall()
    conn.close()
    
    return results