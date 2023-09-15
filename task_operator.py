# This file contains functions for creating,reading,updating,
# and deleting tasks.
import sqlite3

from database import cursor, conn


def create_task(title, description, deadline, priority, category):
    try:
        cursor.execute("""
            INSERT INTO tasks (title, description, deadline, priority, category)
            VALUES (?, ?, ?, ?, ?)
        """, (title, description, deadline, priority, category))
        conn.commit()
    except sqlite3.Error as e:
        print(f"SQLite error: {e}")


def read_tasks():
    # Retrieve all tasks from the database
    cursor.execute("SELECT * FROM tasks")
    tasks = cursor.fetchall()
    return tasks


def update_task_progress(task_id, progress):
    # Query to update_task_progress function
    try:
        sql_query = "UPDATE tasks SET progress = ? WHERE id = ?"
        cursor.execute(sql_query, (progress, task_id))
        conn.commit()

    except sqlite3.Error as e:
        print("Error updating task progress:", e)
        conn.rollback()


def update_task(task_id, title, description, deadline, priority):
    # Update an existing task in the database

    cursor.execute("""
     UPDATE tasks
     SET title = ?, description = ?, deadline = ?, priority = ?
     WHERE ID = ?
     """, (title, description, deadline, priority, task_id))
    conn.commit()


def add_labels_to_task(task_id, labels):
    # Add labels to a specific task
    cursor.execute("UPDATE tasks SET labels = ? WHERE id = ?", (labels, task_id))
    conn.commit()


def get_tasks_by_label(label):
    # Retrieve tasks with a specific label
    cursor.execute("SELECT * FROM tasks WHERE labels LIKE ?", ('%' + label + '%'))
    tasks = cursor.fetchall()
    return tasks


def sort_tasks_by_priority():
    # retrieve tasks sorted by priority
    cursor.execute("SELECT * FROM tasks ORDER BY priority")
    tasks = cursor.fetchall()
    return tasks


def filter_tasks_by_priority(priority):
    # filter by priority
    cursor.execute("SELECT * FROM tasks WHERE priority= ?", (priority,))
    tasks = cursor.fetchall()
    return tasks


def delete_task(task_id):
    # Delete a task from the database
    cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    conn.commit()
