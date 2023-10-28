import tkinter as tk
from tkinter import messagebox

def add_task():
    task = entry_task.get()
    if task:
        listbox_tasks.insert(tk.END, task)
        entry_task.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def delete_task():
    try:
        selected_task = listbox_tasks.get(listbox_tasks.curselection())
        listbox_tasks.delete(listbox_tasks.curselection())
    except:
        messagebox.showwarning("Warning", "Please select a task to delete.")

def clear_tasks():
    listbox_tasks.delete(0, tk.END)

root = tk.Tk()
root.title("To-Do List")

frame_tasks = tk.Frame(root)
frame_tasks.pack(pady=10)

listbox_tasks = tk.Listbox(
    frame_tasks, height=10, width=50, selectbackground="lightblue"
)
listbox_tasks.pack(side=tk.LEFT)

scrollbar_tasks = tk.Scrollbar(frame_tasks)
scrollbar_tasks.pack(side=tk.RIGHT, fill=tk.Y)

listbox_tasks.config(yscrollcommand=scrollbar_tasks.set)
scrollbar_tasks.config(command=listbox_tasks.yview)

entry_task = tk.Entry(root, width=50, font=("Helvetica", 12))
entry_task.pack()

button_add_task = tk.Button(
    root,
    text="Add Task",
    width=48,
    command=add_task,
    bg="green",
    fg="white",
    font=("Helvetica", 12),
)
button_add_task.pack()

button_delete_task = tk.Button(
    root,
    text="Delete Task",
    width=48,
    command=delete_task,
    bg="red",
    fg="white",
    font=("Helvetica", 12),
)
button_delete_task.pack()

button_clear_tasks = tk.Button(
    root,
    text="Clear All",
    width=48,
    command=clear_tasks,
    bg="orange",
    fg="white",
    font=("Helvetica", 12),
)
button_clear_tasks.pack()

root.mainloop()
