import plotly.graph_objects as go

def get_goal_graph():
    # Your values
    x = [1, 2, 3, 4, 5]
    y = [10, 15, 13, 20, 25]

    # Create the graph
    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=x,
        y=y,
        mode="markers",
        name="My data"  
    ))

    # Name the axes
    fig.update_layout(
        title="My Graph",
        xaxis_title="Time",
        yaxis_title="Progress"
    )

    graph_html = fig.to_html(full_html=False)
    return graph_html