from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/sending_goal_details", methods=["POST"])
def sending_goal_details():

    # Get JSON sent from JavaScript
    data = request.get_json()

    # Get each individual part
    goal_name = data["goal_name"]
    description = data["description"]
    deadline = data["deadline"]
    why_it_matters = data["why_it_matters"]

    # Create HTML
    goal_html = ""

    goal_html += f"""
        <h2>Goal: {goal_name}</h2>

        <p><strong>Name:</strong> {goal_name}</p>

        <p><strong>Description:</strong> {description}</p>

        <p><strong>Deadline:</strong> {deadline}</p>

        <p><strong>Why It Matters:</strong> {why_it_matters}</p>

        <hr>
    """

    return goal_html


if __name__ == "__main__":
    app.run(debug=True)