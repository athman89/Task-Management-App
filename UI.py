# This file contains the code for creating the user interface
# the user is going to use. It uses the built-in python library
# Tkinter to create the user interface.
import tkinter as tk

from task_operator import create_task, read_tasks, delete_task, update_task_progress, filter_tasks_by_priority, \
    sort_tasks_by_priority

from task_reminder import set_task_remainder

task_categories = {
    "Work": "Work",
    "Personal": "Personal",
    "Study": "Study",
}

root = tk.Tk()
root.title("Task management Application")

task_list = tk.Listbox(root)
task_list.pack()

filter_priority = tk.Entry(root)
filter_priority.pack()

progress_var = tk.StringVar(root)
category_var = tk.StringVar(root)

entry_title = tk.Entry(root)
entry_description = tk.Entry(root)
entry_deadline = tk.Entry(root)
entry_priority = tk.Entry(root)


def update_task_list():
    task_list.delete(0, tk.END)
    tasks = read_tasks()
    for task in tasks:
        # Create a user-friendly display format
        task_id, title, description, deadline, priority, category, progress = task[:7]
        display_text = f"Task {task_id}: {title}\n"
        display_text += f"Description: {description}\n"
        display_text += f"Deadline: {deadline}\n"
        display_text += f"Priority: {priority}\n"
        display_text += f"Category: {category}\n"
        display_text += f"Progress: {progress}\n"

        # Insert the formatted display text into the task list
        task_list.insert(tk.END, display_text)


def mark_task_completed():
    selected_task_index = task_list.curselection()
    if selected_task_index:
        task_id = selected_task_index[0] + 1  # SQLite use 1-based indexing
        update_task_progress(task_id, 100)
        update_task_list()


def add_task():
    title = entry_title.get()
    description = entry_description.get()
    deadline = entry_deadline.get()
    priority = int(entry_priority.get())
    category = category_var.get()
    create_task(title, description, deadline, priority, category)
    update_task_list()
    entry_title.delete(0, tk.END)
    entry_description.delete(0, tk.END)
    entry_deadline.delete(0, tk.END)
    entry_priority.delete(0, tk.END)
    progress_var.set("")


def delete_selected_task():
    selected_task_index = task_list.curselection()
    if selected_task_index:
        task_id = selected_task_index[0] + 1  # Added 1 because SQLite uses 1-based indexing
        delete_task(task_id)
        update_task_list()


def filter_tasks_priority():
    # Clear the task list
    task_list.delete(0, tk.END)

    # Get the priority value entered by the user
    priority = int(filter_priority.get())

    # Call the filter_tasks_by_priority function with the user-provided priority
    tasks = filter_tasks_by_priority(priority)
    for task in tasks:
        if len(task) >= 2:
            task_title = task[1]
        else:
            task_title = "Title N/A"

        if len(task) >= 5 and isinstance(task[4], int):
            task_priority = task[4]
        else:
            task_priority = "Priority N/A"

        task_list.insert(tk.END, f"{task_title} - Priority: {task_priority}")


# Create a function to sort tasks by priority
def sort_tasks_priority():
    task_list.delete(0, tk.END)
    tasks = sort_tasks_by_priority()
    for task in tasks:
        if len(task) >= 2:
            task_title = task[1]
        else:
            task_title = "Title N/A"

        if len(task) >= 5 and isinstance(task[4], int):
            task_priority = task[4]
        else:
            task_priority = "Priority N/A"

        task_list.insert(tk.END, f"{task_title} - Priority: {task_priority}")


def set_reminder(task_id, title, deadline, reminder_minutes):
    # Get the remainder time in minutes from the user input
    reminder_seconds = reminder_minutes * 60

    set_task_remainder(task_id, title, deadline, reminder_seconds)


def create_ui():
    # The main Tkinter window is defined
    # create UI elements
    global entry_title, entry_description, entry_deadline, entry_priority
    label_title = tk.Label(root, text="Title:")
    # entry_title = tk.Entry(root)
    label_description = tk.Label(root, text="Description:")
    # entry_description = tk.Entry(root)
    label_deadline = tk.Label(root, text="Deadline:")
    # entry_deadline = tk.Entry(root)
    label_priority = tk.Label(root, text="Priority:")
    # entry_priority = tk.Entry(root)
    label_reminder = tk.Label(root, text="Set Reminder (minutes from now):")
    entry_reminder = tk.Entry(root)
    label_category = tk.Label(root, text="Category:")
    category_dropdown = tk.OptionMenu(root, category_var, *task_categories.keys())

    btn_add_task = tk.Button(root, text="Add Task", command=add_task)
    btn_delete_task = tk.Button(root, text="Delete Selected Task", command=delete_selected_task)
    btn_set_reminder = tk.Button(root, text="Set Remainder", command=set_reminder)
    btn_mark_completed = tk.Button(root, text="Mark Completed", command=mark_task_completed)
    btn_sort_by_priority = tk.Button(root, text="Sort by Priority", command=sort_tasks_priority)
    btn_filter_by_priority = tk.Button(root, text="Filter by Priority", command=filter_tasks_priority)

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
    category_dropdown.pack()
    label_category.pack()
    btn_delete_task.pack()
    label_reminder.pack()
    entry_reminder.pack()
    btn_set_reminder.pack()
    btn_sort_by_priority.pack()
    btn_filter_by_priority.pack()
    btn_mark_completed.pack()

    # Start the Tkinter main loop
    if __name__ == "__main__":
        create_ui()
    root.mainloop()
