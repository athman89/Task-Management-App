# This is a simple Task Management system
# coded in python. This file is for executing the functions defined
# in the two file.

from UI import create_ui
from task_reminder import set_task_reminder
from database import close_database

# Its usage:
create_ui()

# Close database connection when finished
close_database()
