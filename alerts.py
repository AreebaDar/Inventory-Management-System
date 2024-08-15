import sqlite3

# Function to check for low inventory and generate alerts
def check_low_inventory_threshold(threshold):
    conn = sqlite3.connect('inventory.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM products WHERE quantity < ?', (threshold,))
    low_inventory_products = cursor.fetchall()
    conn.close()
    return low_inventory_products
