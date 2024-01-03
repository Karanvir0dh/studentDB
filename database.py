import sqlite3

def connect():
    """Create a connection to the SQLite database and create the table if it doesn't exist."""
    conn = sqlite3.connect('students.db')
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS student (id INTEGER PRIMARY KEY, name TEXT, age INTEGER, grade TEXT)")
    conn.commit()
    conn.close()

def add_student(name, age, grade):
    """Add a new student record to the database."""
    conn = sqlite3.connect('students.db')
    cur = conn.cursor()
    cur.execute("INSERT INTO student VALUES (NULL, ?, ?, ?)", (name, age, grade))
    conn.commit()
    conn.close()

def view_students():
    """Retrieve all student records from the database."""
    conn = sqlite3.connect('students.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM student")
    rows = cur.fetchall()
    conn.close()
    return rows

def delete_student(student_id):
    """Delete a student record from the database based on its ID."""
    conn = sqlite3.connect('students.db')
    cur = conn.cursor()
    cur.execute("DELETE FROM student WHERE id=?", (student_id,))
    conn.commit()
    conn.close()

connect()  # Initialize the database when the module is imported
