from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


from database.editing import create_goal


@app.route("/sending_goal_details", methods=["POST"])
def sending_goal_details():

    data = request.get_json()

    goal_name = data["goal_name"]
    description = data["description"]
    deadline = data["deadline"]
    why_goal_matters = data["why_it_matters"]

    create_goal(
        goal_name,
        description,
        deadline,
        why_goal_matters
    )

    return "Goal created"


import sqlite3


@app.route("/get_all_stored_goals", methods=["GET"])
def get_all_stored_goals():

    conn = sqlite3.connect("storage/goals.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, name, description, deadline, why_matters, completed_goal
        FROM goals
    """)

    goals = cursor.fetchall()

    string = ""

    for goal_id, goal_name, description, deadline, why_goal_matters, state in goals:

        string += f"""
            <h2>Goal: {goal_name}</h2>

            <p><strong>Name:</strong> {goal_name}</p>

            <p><strong>Description:</strong> {description}</p>

            <p><strong>Deadline:</strong> {deadline}</p>

            <p><strong>Why It Matters:</strong> {why_goal_matters}</p>

            <br>

            <button type="button"
                onclick="delete_goal('{goal_id}')">
                Delete Goal
            </button>

            <br>

            <h3>Milestones</h3>
        """

        # Get milestones belonging to this goal
        cursor.execute("""
            SELECT id, name, description, deadline, completed_milestone, milestone_number
            FROM milestones
            WHERE goal_id = ?
            ORDER BY milestone_number
        """, (goal_id,))

        milestones = cursor.fetchall()

        # Display each milestone
        for milestone_id, milestone_name, milestone_description, milestone_deadline, milestone_state, milestone_number in milestones:

            string += f"""
                <div>
                    <h4>Milestone {milestone_number}: {milestone_name}</h4>

                    <p>
                        <strong>Description:</strong>
                        {milestone_description}
                    </p>

                    <p>
                        <strong>Deadline:</strong>
                        {milestone_deadline}
                    </p>

                    <button type="button" id="milestone_status_{milestone_id}" onclick="toggle_milestone_status('{milestone_id}')">{'Completed' if milestone_state == 'True' else 'Not Completed'}</button>
                </div>
            """

        # Create milestone form for this goal
        string += f"""
            <br>

            <h3>Create Milestone</h3>

            <label for="milestone_title_{goal_id}">
                Milestone Title
            </label>
            <br>

            <input
                type="text"
                id="milestone_title_{goal_id}"
            >

            <br>

            <label for="milestone_description_{goal_id}">
                Milestone Description
            </label>
            <br>

            <input
                type="text"
                id="milestone_description_{goal_id}"
            >

            <br>

            <label for="milestone_schedule_{goal_id}">Milestone Schedule</label>
            <br>

            <input type="date" id="milestone_schedule_{goal_id}">

            <br>

            <button type="button" onclick="send_milestone_info('{goal_id}')">Create Milestone</button>

            <hr>
        """

    conn.close()

    return string


@app.route("/remove_goal", methods=["POST"])
def remove_goal():

    conn = sqlite3.connect("storage/goals.db")
    cursor = conn.cursor()

    data = request.get_json()

    goal_id = data["goal_id"]

    cursor.execute("""
        DELETE FROM goals
        WHERE id = ?
    """, (goal_id,))

    conn.commit()
    conn.close()

    return "Goal deleted"


@app.route("/get_milestone_status", methods=["POST"])
def get_and_switch_milestone_status():

    conn = sqlite3.connect("storage/goals.db")
    cursor = conn.cursor()

    data = request.get_json()

    milestone_id = data["milestone_id"]

    cursor.execute("""
        SELECT completed_milestone
        FROM milestones
        WHERE id = ?
    """, (milestone_id,))

    status = cursor.fetchone()[0]

    if status == "True":
        new_status = "False"
    else:
        new_status = "True"

    cursor.execute("""
        UPDATE milestones
        SET completed_milestone = ?
        WHERE id = ?
    """, (new_status, milestone_id))

    conn.commit()
    conn.close()

    return new_status


@app.route("/create_milestone", methods=["POST"])
def create_milestone():

    conn = sqlite3.connect("storage/goals.db")
    cursor = conn.cursor()

    data = request.get_json()

    goal_id = data["goal_id"]
    milestone_name = data["title_milestone"]
    description = data["description"]

    # Find highest milestone number for this goal
    cursor.execute("""
        SELECT MAX(milestone_number)
        FROM milestones
        WHERE goal_id = ?
    """, (goal_id,))

    current_number = cursor.fetchone()[0]

    if current_number is None:
        milestone_number = 1
    else:
        milestone_number = current_number + 1

    # Create milestone
    cursor.execute("""
        INSERT INTO milestones (
            goal_id,
            name,
            description,
            completed_milestone,
            milestone_number
        )
        VALUES (?, ?, ?, ?, ?)
    """, (
        goal_id,
        milestone_name,
        description,
        "False",
        milestone_number
    ))

    conn.commit()
    conn.close()

    return "Milestone created"


from database.creating_deleting import create_goals_database


if __name__ == "__main__":

    create_goals_database()

    app.run(debug=True)