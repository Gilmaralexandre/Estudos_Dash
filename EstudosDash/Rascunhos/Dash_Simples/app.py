import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd

app = dash.Dash(__name__)

df = pd.DataFrame({
    'Fruit': ['Apples', 'Oranges', 'Bananas', 'Apples', 'Oranges', 'Bananas'],
    'Amount': [4, 10, 5, 8, 3, 7],
    'City': ["SF", "SF", "SF", "Montreal", "Montreal", "Belo Horizonte"]
})

fig = px.bar(df, x="Fruit", y="Amount", color="City")

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
