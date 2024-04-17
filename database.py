import sqlite3

# Connect to the SQLite database file
conn = sqlite3.connect('bank.db')
c = conn.cursor()

# Create table if not exists
c.execute('''CREATE TABLE IF NOT EXISTS accounts
             (account_number INTEGER PRIMARY KEY, name TEXT, balance REAL)''')

c.execute('''CREATE TABLE IF NOT EXISTS transactions
             (transaction_id INTEGER PRIMARY KEY, account_number INTEGER, amount REAL, transaction_type TEXT, transaction_date TEXT)''')
conn.commit()

def close_connection():
    conn.close()
