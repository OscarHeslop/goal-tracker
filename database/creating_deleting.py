import sqlite3


def create_goals_database():
    conn = sqlite3.connect("storage/goals.db")
    cursor = conn.cursor()

    # Goals table
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

    # Milestones table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS milestones (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            goal_id INTEGER,
            name TEXT,
            description TEXT,
            deadline TEXT,
            state TEXT DEFAULT 'Not Started',
            milestone_number INTEGER,
            FOREIGN KEY (goal_id) REFERENCES goals(id)
        )
    """)

    conn.commit()
    conn.close()