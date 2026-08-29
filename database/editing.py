import sqlite3


def create_goal(name, description, deadline, why_matters):

    conn = sqlite3.connect("storage/goals.db")
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO goals (name, description, deadline, why_matters)
        VALUES (?, ?, ?, ?)
    """, (name, description, deadline, why_matters))

    conn.commit()
    conn.close()


def update_state(goal_id, new_state):

    conn = sqlite3.connect("storage/goals.db")
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE goals
        SET completed_goal = ?
        WHERE id = ?
    """, (new_state, goal_id))

    conn.commit()
    conn.close()