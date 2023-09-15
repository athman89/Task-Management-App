# This is a simple Task Management system
# coded in python. This file is for executing the functions defined
# in the two file.
import tkinter as tk
from UI import create_ui
from database import close_database

# Its usage:
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Task Management Application")

    # Call the create_ui function from 'ui.py' to create the UI
    create_ui()

    # Start the Tkinter main loop
    root.mainloop()

# Close database connection when finished
close_database()
