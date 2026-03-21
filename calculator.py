import tkinter as tk
from tkinter import messagebox

# Functions
def calculate():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        operator = operator_var.get()

        if operator == "+":
            result = num1 + num2
        elif operator == "-":
            result = num1 - num2
        elif operator == "*":
            result = num1 * num2
        elif operator == "/":
            if num2 == 0:
                messagebox.showerror("Error", "Cannot divide by zero")
                return
            result = num1 / num2
        else:
            messagebox.showwarning("Warning", "Select an operator")
            return

        result_label.config(text="Result: " + str(result))

    except ValueError:
        messagebox.showerror("Error", "Enter valid numbers")


# Main window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("350x300")

# Widgets
tk.Label(root, text="Enter First Number").pack()
entry1 = tk.Entry(root)
entry1.pack()

tk.Label(root, text="Enter Second Number").pack()
entry2 = tk.Entry(root)
entry2.pack()

operator_var = tk.StringVar()

tk.Radiobutton(root, text="Add (+)", variable=operator_var, value="+").pack()
tk.Radiobutton(root, text="Subtract (-)", variable=operator_var, value="-").pack()
tk.Radiobutton(root, text="Multiply (*)", variable=operator_var, value="*").pack()
tk.Radiobutton(root, text="Divide (/)", variable=operator_var, value="/").pack()

tk.Button(root, text="Calculate", command=calculate).pack(pady=10)

result_label = tk.Label(root, text="Result: ")
result_label.pack()

root.mainloop()