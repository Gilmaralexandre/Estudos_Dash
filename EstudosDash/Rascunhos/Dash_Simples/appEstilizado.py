import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd

app = dash.Dash(__name__, style.css)


# ========================
# Layout
app.layout = html.Div(id="div1",
                      children=[
                          html.H1("Hello Dash", id="h1"),

                          html.Div("Um framework para python"),

                          dcc.Graph(figure=fig, id='graph')
                      ]
                      )

if __name__ == '__main__':
    app.run_server(debug=True)
