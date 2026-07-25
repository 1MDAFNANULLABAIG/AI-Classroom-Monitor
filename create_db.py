import sqlite3

conn = sqlite3.connect("classroom.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS attendance (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_name TEXT,
    date TEXT,
    time TEXT,
    status TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS classroom_logs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_name TEXT,
    attention_status TEXT,
    sleep_status TEXT,
    phone_usage TEXT,
    timestamp TEXT
)
""")

conn.commit()
conn.close()

print("Database and tables created successfully!")