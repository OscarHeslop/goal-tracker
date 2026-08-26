import sqlite3


def create_goals_database():
    conn = sqlite3.connect("storage/goals.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS goals (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            description TEXT,
            deadline TEXT,
            why_matters TEXT,
            state TEXT DEFAULT 'Not Started'
        )
    """)

    conn.commit()
    conn.close()

    