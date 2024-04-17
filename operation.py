from tkinter import messagebox
from database import c, conn
from datetime import datetime
# Function to create a new account

def create_account(name, initial_balance):
    try:
        c.execute("INSERT INTO accounts (name, balance) VALUES (?, ?)", (name, initial_balance))
        conn.commit()
        messagebox.showinfo("Success", "Account created successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to create account: {e}")

# Function to generate a unique account number
def generate_account_number():
    c.execute("SELECT MAX(account_number) FROM accounts")
    result = c.fetchone()[0]
    if result:
        return result + 1
    else:
        return 1001  # Starting account number if no accounts exist

# Function to create a new account
def create_account(name, initial_balance):
    try:
        account_number = generate_account_number()
        c.execute("INSERT INTO accounts (account_number, name, balance) VALUES (?, ?, ?)", (account_number, name, initial_balance))
        conn.commit()
        messagebox.showinfo("Success", f"Account created successfully! Your account number is: {account_number}")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to create account: {e}")

# Function to deposit money
def deposit_money(account_number, amount):
    try:
        c.execute("UPDATE accounts SET balance = balance + ? WHERE account_number = ?", (amount, account_number))
        c.execute("INSERT INTO transactions (account_number, amount, transaction_type, transaction_date) VALUES (?, ?, ?, ?)", (account_number, amount, 'Deposit', datetime.now()))
        conn.commit()
        messagebox.showinfo("Success", "Deposit successful!")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to deposit money: {e}")

# Function to withdraw money
def withdraw_money(account_number, amount):
    try:
        c.execute("SELECT balance FROM accounts WHERE account_number = ?", (account_number,))
        current_balance = c.fetchone()[0]
        if current_balance >= amount:
            c.execute("UPDATE accounts SET balance = balance - ? WHERE account_number = ?", (amount, account_number))
            c.execute("INSERT INTO transactions (account_number, amount, transaction_type, transaction_date) VALUES (?, ?, ?, ?)", (account_number, amount, 'Withdrawal', datetime.now()))
            conn.commit()
            messagebox.showinfo("Success", "Withdrawal successful!")
        else:
            messagebox.showerror("Error", "Insufficient balance!")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to withdraw money: {e}")

# Function to check balance
def check_balance(account_number):
    try:
        c.execute("SELECT balance FROM accounts WHERE account_number = ?", (account_number,))
        balance = c.fetchone()[0]
        messagebox.showinfo("Balance", f"Your current balance is: ${balance}")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to check balance: {e}")

# Function to display transaction history
def show_transaction_history(account_number):
    try:
        c.execute("SELECT * FROM transactions WHERE account_number = ?", (account_number,))
        transactions = c.fetchall()
        if transactions:
            history = "\n".join([f"{row[4]} - {row[3]}: ${row[2]}" for row in transactions])
            messagebox.showinfo("Transaction History", history)
        else:
            messagebox.showinfo("Transaction History", "No transactions found.")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to fetch transaction history: {e}")



