import sqlite3

# Connection to the SQLite database (or create a new one
# if it does not exist)
conn = sqlite3.connect("task.db")
cursor = conn.cursor()

# Create the table if it doesn't exist

cursor.execute("""
     CREATE TABLE IF NOT EXISTS tasks (
         id INTEGER PRIMARY KEY,
         title TEXT,
         description TEXT,
         deadline TEXT,
         priority INTEGER,
         labels Text)
         """)
conn.commit()


def close_database():
    # Close database connection
    conn.close()
