from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")



from database.editing import add_record
@app.route("/sending_goal_details", methods=["POST"])
def sending_goal_details():

    # Get JSON sent from JavaScript
    data = request.get_json()

    # Get each individual part
    goal_name = data["goal_name"]
    description = data["description"]
    deadline = data["deadline"]
    why_goal_matters = data["why_it_matters"]

    # Create HTML
    goal_html = ""

    goal_html += f"""
        <h2>Goal: {goal_name}</h2>

        <p><strong>Name:</strong> {goal_name}</p>

        <p><strong>Description:</strong> {description}</p>

        <p><strong>Deadline:</strong> {deadline}</p>

        <p><strong>Why It Matters:</strong> {why_goal_matters}</p>

        <hr>
    """

    add_record(goal_name, description, deadline, why_goal_matters)

    return goal_html

import sqlite3
@app.route("/get_all_stored_goals", methods=["GET"])
def get_all_stored_goals():
    conn = sqlite3.connect("storage/goals.db")
    cursor = conn.cursor()
    cursor.execute("""
        SELECT *
        FROM goals 
                   
""")
    list = cursor.fetchall()
    string = ""
    for id,goal_name,description,deadline,why_goal_matters,state in list:


        string += f"""
            <h2>Goal: {goal_name}</h2>

            <p><strong>Name:</strong> {goal_name}</p>

            <p><strong>Description:</strong> {description}</p>

            <p><strong>Deadline:</strong> {deadline}</p>

            <p><strong>Why It Matters:</strong> {why_goal_matters}</p>

            <hr>
        """

    return string

from database.creating_deleting import create_goals_database
if __name__ == "__main__":
    
    create_goals_database()
    app.run(debug=True)