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
            completed_goal TEXT DEFAULT 'False'
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
            completed_milestone TEXT DEFAULT 'False',
            milestone_number INTEGER
        )
    """)



    # Completed goals and milestones
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS completed (
            id INTEGER  ,
            type TEXT  ,
            completed_at TIMESTAMP
        )
    """)

    conn.commit()
    conn.close()