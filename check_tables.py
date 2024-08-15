# To check the already created tables in db
import sqlite3

def check_tables():
    conn = sqlite3.connect('inventory.db')
    cursor = conn.cursor()
    
    # Query to check the existence of tables
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    
    for table in tables:
        print(table[0])
    
    conn.close()

if __name__ == "__main__":
    check_tables()
