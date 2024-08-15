import sqlite3

# Function to generate inventory report
def generate_inventory_report():
    conn = sqlite3.connect('inventory.db')
    cursor = conn.cursor()
    cursor.execute('SELECT id, name, category, quantity, price FROM products')
    products = cursor.fetchall()
    conn.close()
    return products
