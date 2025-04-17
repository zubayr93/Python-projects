import sqlite3
def create_table():
    conn = sqlite3.connect("customers.db")
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS customers (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        email TEXT,
        phone TEXT
        )
    ''')
    conn.commit()
    conn.close()
    
def add_customer(customer):
    conn = sqlite3.connect("customers.db")
    cursor = conn.cursor()
    cursor.execute('INSERT INTO customers (name,email,phone) VALUES (?,?,?)',(customer.name,customer.email,customer.phone))
    conn.commit()
    conn.close()

def get_all_customers():
    conn = sqlite3.connect('customers.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM customers')
    rows = cursor.fetchall()
    conn.close()
    return rows    