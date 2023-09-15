# This file contains the code for creating the user interface
# the user is going to use. It uses the built-in python library
# Tkinter to create the user interface.
import time
import tkinter as tk
from tkinter import messagebox
from database import close_database
from task_operator import create_task, read_tasks, delete_task, sort_tasks_by_priority, filter_tasks_by_priority


def create_ui():
    # The main Tkinter window is defined
    root = tk.Tk()
    root.title("Task management Application")

    # create UI elements
    label_title = tk.Label(root, text="Title:")
    entry_title = tk.Entry(root)
    label_description = tk.Label(root, text="Description:")
    entry_description = tk.Entry(root)
    label_deadline = tk.Label(root, text="Deadline:")
    entry_deadline = tk.Entry(root)
    label_priority = tk.Label(root, text="Priority:")
    entry_priority = tk.Entry(root)
    label_reminder = tk.Label(root, text="Set Reminder (minutes from now):")
    entry_reminder = tk.Entry(root)

    btn_add_task = tk.Button(root, text="Add Task", command=add_task)
    btn_delete_task = tk.Button(root, text="Delete Selected Task", command=delete_selected_task)
    btn_set_reminder = tk.Button(root, text="Set Remainder", command=set_reminder)

    task_list = tk.Listbox(root)
    task_list.pack()

    # Place UI elements in the window
    label_title.pack()
    entry_title.pack()
    label_description.pack()
    entry_description.pack()
    label_deadline.pack()
    entry_deadline.pack()
    label_priority.pack()
    entry_priority.pack()
    btn_add_task.pack()
    btn_delete_task.pack()
    label_reminder.pack()
    entry_reminder.pack()
    btn_set_reminder.pack()

    def update_task_list():
        task_list.delete(0, tk.END)
        tasks = read_tasks()
        for task in tasks:
            task_list.insert(tk.END, task[1])

    def add_task():
        title = entry_title.get()
        description = entry_description.get()
        deadline = entry_deadline.get()
        priority = int(entry_priority.get())
        create_task(title, description, deadline, priority)
        update_task_list()
        entry_title.delete(0, tk.END)
        entry_description.delete(0, tk.END)
        entry_deadline.delete(0, tk.END)
        entry_priority.delete(0, tk.END)

    def delete_selected_task():
        selected_task_index = task_list.curselection()
        if selected_task_index:
            task_id = selected_task_index[0] + 1  # Add 1 because SQLite uses 1-based indexing
            delete_task(task_id)
            update_task_list()

    def set_reminder():
        try:
            # Get the remainder time in minutes from the user input
            reminder_minutes = int(entry_reminder.get())

            # Convert minutes to seconds for the sleep function
            reminder_seconds = reminder_minutes * 60

            # Wait for the specified time
            time.sleep(reminder_seconds)

            # When time is uo, show a remainder
            messagebox.showinfo("This is a reminder,its time for your task!")

        except ValueError:
            # handle invalid input
            messagebox.showerror("Invalid input", "Please enter a valid number of minutes.")

    # Start the Tkinter main loop
    root.mainloop()
