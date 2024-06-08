import tkinter as tk
from tkinter import messagebox

# Function to evaluate the expression in the entry widget
def evaluate_expression():
    try:
        # Get the expression from the entry widget
        expression = entry.get()
        # Evaluate the expression
        result = eval(expression)
        # Set the result in the entry widget
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        messagebox.showerror("Error", "Invalid Expression")

# Function to add text to the entry widget
def add_to_expression(char):
    entry.insert(tk.END, char)

# Function to clear the entry widget
def clear_expression():
    entry.delete(0, tk.END)

# Initialize the main window
root = tk.Tk()
root.title("Basic Calculator")

# Entry widget for the expression
entry = tk.Entry(root, width=16, font=('Arial', 24), borderwidth=2, relief="solid")
entry.grid(row=0, column=0, columnspan=4)

# Buttons for the calculator
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
]

# Create and place buttons in the window
for (text, row, col) in buttons:
    if text == '=':
        button = tk.Button(root, text=text, width=4, height=2, font=('Arial', 18), command=evaluate_expression)
    else:
        button = tk.Button(root, text=text, width=4, height=2, font=('Arial', 18), command=lambda t=text: add_to_expression(t))
    button.grid(row=row, column=col, padx=5, pady=5)

# Clear button
clear_button = tk.Button(root, text='C', width=4, height=2, font=('Arial', 18), command=clear_expression)
clear_button.grid(row=4, column=0, padx=5, pady=5)

# Run the application
root.mainloop()
