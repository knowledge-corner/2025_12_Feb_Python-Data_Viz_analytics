from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px

from mpg import df

app = Dash()

app.layout = [
    html.H1("MPG Dashboard", style={'text-align': 'center', 'color': 'darkslategray'}),
    html.Label("Select Origin", style={'font-size': '16px', 'margin-left': '20px'}),
    dcc.Dropdown(id='dropdown-selection',
                 value = "All",
                 options = [{"label" : "All", "value" : "All"}] + 
                 [{"label" : val, "value" : val} for val in df.origin.unique()],
                 clearable = False,
                 style={'width': '50%', 'margin-bottom': '20px', 'margin-left': '10px'}),
    dcc.Graph(id='bar'),
    dcc.Graph(id='scatter'),
    dcc.Graph(id='box')
]

@callback(
    Output('bar', 'figure'),
    Output('scatter', 'figure'),
    Output('box', 'figure'),
    Input('dropdown-selection', 'value')
)
def update_graph(value):
    if value == "All" :
        dff = df
    else:
        dff = df[df.origin == value]

    fig_scatter = px.scatter(dff, x = "horsepower", y = "mpg", color="cylinders",
           title= "Correlation between MPG Horsepower",
                   labels={"cylinders" : "Cylinders", "mpg" : "MPG"}, 
                   template="simple_white")
    
    fig_bar = px.histogram(dff, x = "cylinders", y = "mpg", 
                   title= "Average MPG by Cylinders",
                   labels={"cylinders" : "Cylinders", "mpg" : "Average MPG"}, 
                   template="simple_white", color_discrete_sequence=["teal"]
                   )
    
    fig_box = px.box(dff, y = "mpg", color="cylinders",
           title= "IQR Distribution for MGP across Cylinders",
                   labels={"cylinders" : "Cylinders", "mpg" : "MPG"}, 
                   template="simple_white")

    return fig_bar, fig_scatter, fig_box

if __name__ == '__main__':
    app.run(debug=True)
