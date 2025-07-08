import sqlite3
import os

# Define the path to the database file
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, 'database.db')

# Connect to SQLite database (creates the file if it doesn't exist)
connection = sqlite3.connect(db_path)
cursor = connection.cursor()

# Create a table (example)
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    score INTEGER
)
''')

# Commit changes and close the connection
connection.commit()
connection.close()

print(f"Database initialized at {db_path}")