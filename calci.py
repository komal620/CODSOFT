import tkinter as tk

def calculate():
    num1 = float(entry_num1.get())
    num2 = float(entry_num2.get())
    operation = operation_var.get()

    if operation == "Add":
        result.set(num1 + num2)
    elif operation == "Subtract":
        result.set(num1 - num2)
    elif operation == "Multiply":
        result.set(num1 * num2)
    elif operation == "Divide":
        if num2 == 0:
            result.set("Cannot divide by zero")
        else:
            result.set(num1 / num2)

root = tk.Tk()
root.title("Simple Calculator")

entry_num1 = tk.Entry(root)
entry_num2 = tk.Entry(root)
operation_var = tk.StringVar()
operation_var.set("Add")
operation_menu = tk.OptionMenu(root, operation_var, "Add", "Subtract", "Multiply", "Divide")

calculate_button = tk.Button(root, text="Calculate", command=calculate)
result = tk.StringVar()
result_label = tk.Label(root, textvariable=result)

entry_num1.pack()
entry_num2.pack()
operation_menu.pack()
calculate_button.pack()
result_label.pack()

root.mainloop()