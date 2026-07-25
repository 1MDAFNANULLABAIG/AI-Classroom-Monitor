import sqlite3
from datetime import datetime

DB_NAME = "classroom.db"


def get_connection():
    return sqlite3.connect(DB_NAME)


def create_tables():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS students(
        student_id TEXT PRIMARY KEY,
        student_name TEXT NOT NULL,
        department TEXT,
        semester TEXT,
        section TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS attendance(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        student_id TEXT,
        student_name TEXT,
        date TEXT,
        time TEXT,
        status TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS behaviour(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        student_id TEXT,
        student_name TEXT,
        behaviour TEXT,
        date TEXT,
        time TEXT
    )
    """)

    conn.commit()
    conn.close()


def register_student(student_id, student_name, department, semester, section):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT OR REPLACE INTO students
    (student_id, student_name, department, semester, section)
    VALUES (?, ?, ?, ?, ?)
    """, (
        student_id,
        student_name,
        department,
        semester,
        section
    ))

    conn.commit()
    conn.close()


def mark_attendance(student_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT student_name FROM students WHERE student_id=?",
        (student_id,)
    )

    row = cursor.fetchone()

    if row:

        today = datetime.now().strftime("%Y-%m-%d")
        now = datetime.now().strftime("%H:%M:%S")

        cursor.execute("""
        INSERT INTO attendance
        (student_id, student_name, date, time, status)
        VALUES (?, ?, ?, ?, ?)
        """, (
            student_id,
            row[0],
            today,
            now,
            "Present"
        ))

        conn.commit()

    conn.close()


def save_behaviour(student_id, behaviour):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT student_name FROM students WHERE student_id=?",
        (student_id,)
    )

    row = cursor.fetchone()

    if row:

        cursor.execute("""
        INSERT INTO behaviour
        (student_id, student_name, behaviour, date, time)
        VALUES (?, ?, ?, ?, ?)
        """, (
            student_id,
            row[0],
            behaviour,
            datetime.now().strftime("%Y-%m-%d"),
            datetime.now().strftime("%H:%M:%S")
        ))

        conn.commit()

    conn.close()


create_tables()

if __name__ == "__main__":
    print("Database Ready Successfully")