import plotly.graph_objects as go
import sqlite3


def get_goal_graph(date, num_milestones):

    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=date,
        y=num_milestones,
        mode="markers",
        name="Milestones completed"
    ))

    fig.update_layout(
        title="My Graph",
        xaxis_title="Time",
        yaxis_title="Number of milestones completed"
    )

    graph_html = fig.to_html(full_html=False)
    return graph_html

#update / display graph
def display_graph():

    conn = sqlite3.connect("storage/goals.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Completed")

    completed = cursor.fetchall()

    conn.close()

    graph_dict = {}

    for row in completed:

        completed_datetime = row[2]

        # Get just the date
        date = completed_datetime.split(" ")[0]

        # If this date already exists, increase its count
        if date in graph_dict:
            graph_dict[date] += 1

        # Otherwise start it at 1
        else:
            graph_dict[date] = 1

    dates = list(graph_dict.keys())
    num_milestones = list(graph_dict.values())

    return get_goal_graph(dates, num_milestones)