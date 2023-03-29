import tkinter as tk
from tkinter import messagebox

# Scope Binding
# Declaration of a global variable at the module level
amount = 5000

# Object-oriented programming
# A class is a form of an abstraction
# Demonstrate the abstraction component of programming theory
class ATM:
    # Constructor definition
    def __init__(self, master):
        # Demonstrate value binding
        # Python has dynamic typing, therefore types
        # Are determined, and may change at runtime
        self.master = master
        self.master.title("ATM")
        self.master.geometry("300x300")
        self.balance = 5000

        # Create widgets
        self.label1 = tk.Label(master, text="Welcome to the ATM!")
        self.label2 = tk.Label(master, text="Enter amount:")
        self.label3 = tk.Label(master, text="Operation:")
        self.entry = tk.Entry(master)
        self.withdrawButton = tk.Button(master, text="Withdraw", command=self.withdraw)
        self.depositButton = tk.Button(master, text="Deposit", command=self.deposit)
        self.balance_label = tk.Label(master, text="Your balance is: $5000")

        # Display widgets
        self.label1.pack(pady=10)
        self.label2.pack()
        self.entry.pack()
        self.label3.pack(pady=20)
        self.withdrawButton.pack(pady=10)
        self.depositButton.pack(pady=10)
        self.balance_label.pack()

    # Withdrawal method definition
    # Procedural programming
    def withdraw(self):
        # Demonstrate scoping
        # Refer to the global variable
        global amount

        # Exception handling
        # If input is empty or invalid, such as a string
        # Warn the user
        try:
            amount = int(self.entry.get())
        except ValueError:
            tk.messagebox.showerror("Error", "Invalid input")

        # Further operations to demonstrate value binding
        # Mutation operations
        if amount > self.balance:
            tk.messagebox.showerror("Error", "Insufficient funds!")
        else:
            self.balance -= amount
            self.balance_label.config(text="Your balance is: ${}".format(self.balance))
            tk.messagebox.showinfo("Success", "Withdrawal successful!")
            self.entry.delete(0, tk.END)

    # Deposit subroutine
    # Procedural programming paradigm
    def deposit(self):
        # Demonstrate scoping
        # Refer to the global variable
        global amount

        # Exception handling
        # If input is empty or invalid, such as a string
        # Warn the user
        try:
            amount = int(self.entry.get())
        except ValueError:
            tk.messagebox.showerror("Error", "Invalid input")

        # Further operations to demonstrate value binding
        self.balance += amount
        self.balance_label.config(text="Your balance is: ${}".format(self.balance))
        tk.messagebox.showinfo("Success", "Deposit accepted!")
        self.entry.delete(0, tk.END)


# Main subroutine
if __name__ == "__main__":
    root = tk.Tk()
    app = ATM(root)
    root.mainloop()
