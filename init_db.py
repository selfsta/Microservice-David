import sqlite3

# Connect to database (creates database.db if it doesn't exist)
conn = sqlite3.connect("database.db")
cursor = conn.cursor()

# Create posts table with first_name, last_name, and content fields
cursor.execute("""
    CREATE TABLE posts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name TEXT,
        last_name TEXT,
        shifts TEXT,
        days_working TEXT,
        trained_rotations TEXT,
        comments TEXT,
        created TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
""")

# Create schedule table for employee assignments
cursor.execute("""
    CREATE TABLE IF NOT EXISTS schedule (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        employee_id INTEGER,
        day TEXT,
        slot INTEGER,
        FOREIGN KEY (employee_id) REFERENCES posts (id)
    )
""")

conn.commit()
conn.close()

print("Database and tables created successfully!")
