# GUI

import tkinter as tk
from tkinter import messagebox
from operation import *

def create_account_window():
    window = tk.Tk()
    window.title("Create Account")
    window.geometry("300x170")
    window.configure(bg="#7AD7E0")

    tk.Label(window, text="Name:", bg="#7AD7E0").grid(row=0, column=0, padx=10, pady=10)
    name_entry = tk.Entry(window)
    name_entry.grid(row=0, column=1, padx=10, pady=10)

    tk.Label(window, text="Initial Balance:", bg="#7AD7E0").grid(row=1, column=0, padx=10, pady=10)
    initial_balance_entry = tk.Entry(window)
    initial_balance_entry.grid(row=1, column=1, padx=10, pady=10)

    def submit():
        name = name_entry.get()
        initial_balance = float(initial_balance_entry.get())
        create_account(name, initial_balance)
        window.destroy()

    tk.Button(window, text="Create Account", command=submit, bg="#FFACAC",height=2, width=15).grid(row=2, column=0, columnspan=2, padx=10, pady=10)

    window.mainloop()
def deposit_window():
    window = tk.Tk()
    window.title("Deposit Money")
    window.geometry("300x200")
    window.configure(bg="#FFD966")

    tk.Label(window, text="Account Number:", bg="#FFD966").grid(row=0, column=0, padx=10, pady=10)
    account_number_entry = tk.Entry(window)
    account_number_entry.grid(row=0, column=1, padx=10, pady=10)

    tk.Label(window, text="Amount:", bg="#FFD966").grid(row=1, column=0, padx=10, pady=10)
    amount_entry = tk.Entry(window)
    amount_entry.grid(row=1, column=1, padx=10, pady=10)

    def submit():
        account_number = int(account_number_entry.get())
        amount = float(amount_entry.get())
        deposit_money(account_number, amount)
        window.destroy()

    tk.Button(window, text="Deposit", command=submit, bg="#ACE7FF").grid(row=2, column=0, columnspan=2, padx=10, pady=10)

    window.mainloop()

def withdraw_window():
    window = tk.Tk()
    window.title("Withdraw Money")
    window.geometry("300x200")
    window.configure(bg="#B6D7A8")

    tk.Label(window, text="Account Number:", bg="#B6D7A8").grid(row=0, column=0, padx=10, pady=10)
    account_number_entry = tk.Entry(window)
    account_number_entry.grid(row=0, column=1, padx=10, pady=10)

    tk.Label(window, text="Amount:", bg="#B6D7A8").grid(row=1, column=0, padx=10, pady=10)
    amount_entry = tk.Entry(window)
    amount_entry.grid(row=1, column=1, padx=10, pady=10)

    def submit():
        account_number = int(account_number_entry.get())
        amount = float(amount_entry.get())
        withdraw_money(account_number, amount)
        window.destroy()

    tk.Button(window, text="Withdraw", command=submit, bg="#C2F0C2").grid(row=2, column=0, columnspan=2, padx=10, pady=10)

    window.mainloop()

def balance_inquiry_window():
    window = tk.Tk()
    window.title("Balance Inquiry")
    window.geometry("300x150")
    window.configure(bg="#F4A261")

    tk.Label(window, text="Account Number:", bg="#F4A261").grid(row=0, column=0, padx=10, pady=10)
    account_number_entry = tk.Entry(window)
    account_number_entry.grid(row=0, column=1, padx=10, pady=10)

    def submit():
        account_number = int(account_number_entry.get())
        check_balance(account_number)
        window.destroy()

    tk.Button(window, text="Check Balance", command=submit, bg="#FFD166").grid(row=1, column=0, columnspan=2, padx=10, pady=10)

    window.mainloop()

def transaction_history_window():
    window = tk.Tk()
    window.title("Transaction History")
    window.geometry("400x300")
    window.configure(bg="#F76F8E")

    tk.Label(window, text="Account Number:", bg="#F76F8E").grid(row=0, column=0, padx=10, pady=10)
    account_number_entry = tk.Entry(window)
    account_number_entry.grid(row=0, column=1, padx=10, pady=10)

    def submit():
        account_number = int(account_number_entry.get())
        show_transaction_history(account_number)
        window.destroy()

    tk.Button(window, text="Show History", command=submit, bg="#FF9671").grid(row=1, column=0, columnspan=2, padx=10, pady=10)

    window.mainloop()

    # Main application window
root = tk.Tk()
root.title("Banking System")
root.geometry("500x300")
root.configure(bg="#82C0CC")

## Buttons for different operations with improved size and minimized gap
tk.Button(root, text="Create Account", command=create_account_window, bg="#FF6B6B",height=4, width=17).grid(row=0, column=0, padx=(20, 5), pady=10)
tk.Button(root, text="Deposit Money", command=deposit_window, bg="#FFD966", height=4, width=17).grid(row=0, column=1, padx=5, pady=10)
tk.Button(root, text="Withdraw Money", command=withdraw_window, bg="#B6D7A8", height=4, width=17).grid(row=0, column=2, padx=5, pady=10)
tk.Button(root, text="Balance Inquiry", command=balance_inquiry_window, bg="#F4A261", height=4, width=17).grid(row=1, column=0, padx=(20, 5), pady=10)
tk.Button(root, text="Transaction History", command=transaction_history_window, bg="#F76F8E", height=4, width=17).grid(row=1, column=1, padx=5, pady=10)


root.mainloop()