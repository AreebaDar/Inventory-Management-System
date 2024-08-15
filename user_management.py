import sqlite3

# Function to register a new user
def register_user(username, password, role):
    conn = sqlite3.connect('inventory.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO users (username, password, role) VALUES (?, ?, ?)', (username, password, role))
    conn.commit()
    conn.close()

# Function to authenticate user login
def authenticate_user(username, password):
    conn = sqlite3.connect('inventory.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, password))
    user = cursor.fetchone()
    conn.close()
    return user
