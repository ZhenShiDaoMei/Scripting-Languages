import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar
from datetime import datetime

#add task to task section
def add_task():
    task_name = task_entry.get()
    task_description = desc_entry.get("1.0", tk.END).strip()
    priority = priority_var.get()
    due_date = cal.get_date()
    if task_name and task_description:
        todo_listbox.insert(tk.END, f"{task_name} - {task_description} - Priority: {priority} - Due Date: {due_date}")
        task_entry.delete(0, tk.END)
        desc_entry.delete("1.0", tk.END)

#remove from task section
def mark_complete():
    selected = todo_listbox.curselection()
    if selected:
        completed_listbox.insert(tk.END, todo_listbox.get(selected))
        todo_listbox.delete(selected)

#delete task from removed section
def remove_completed():
    selected = completed_listbox.curselection()
    if selected:
        completed_listbox.delete(selected)

#fonts title
bubbly_font = ("San Francisco", 12)
bubblysmall_font = ("San Francisco", 9, "bold")
bubblybold_font = ("San Francisco", 12, "bold")
root = tk.Tk()
root.title('To-Do List App')

#task
task_entry = tk.Entry(root, width=30)
task_entry.pack()
task_entry.configure(font=bubbly_font)

#description
desc_label = tk.Label(root, text="Task Description:")
desc_label.pack()
desc_label.configure(font=bubblybold_font)
desc_entry = tk.Text(root, height=6, width=45, pady=5)
desc_entry.pack()
desc_entry.configure(font=bubbly_font)

#priority
priority_var = tk.StringVar(value='Medium')
priority_dropdown = ttk.Combobox(root, textvariable=priority_var, values=('Low', 'Medium', 'High'), width = 40)
priority_dropdown.pack()
priority_dropdown.configure(font=bubblysmall_font)

#calendar
cal = Calendar(root, selectmode='day', year=datetime.now().year, month=datetime.now().month, day=datetime.now().day)
cal.pack()
cal.configure(font=bubblysmall_font)

#add task button
add_button = tk.Button(root, text='Add Task', command=add_task)
add_button.pack()
add_button.configure(font=bubblysmall_font)

#task list
todo_listbox = tk.Listbox(root, width=70, height=10)
todo_listbox.pack()
todo_listbox.configure(font=bubbly_font)

#mark complete button
complete_button = tk.Button(root, text='Mark Complete', command=mark_complete)
complete_button.pack()
complete_button.configure(font=bubblysmall_font)

#remove completed button
remove_button = tk.Button(root, text='Remove Completed', command=remove_completed)
remove_button.pack()
remove_button.configure(font=bubblysmall_font)

#completed list
completed_listbox = tk.Listbox(root, width=70, height=10)
completed_listbox.pack()
completed_listbox.configure(font=bubbly_font)

root.mainloop()