from abstra.forms import display_plotly
import plotly.graph_objects as go

figure = go.Figure(
    data=[go.Bar(x=[1, 2, 3], y=[1, 3, 2])],
    layout=go.Layout(title=go.layout.Title(text="Bar chart example")),
)

display_plotly(figure)
