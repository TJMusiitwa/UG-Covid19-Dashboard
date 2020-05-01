import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from apps import about, home

dash_stylesheets = [
    dbc.themes.GRID,
    dbc.themes.DARKLY,
]

app = dash.Dash(__name__, external_stylesheets=dash_stylesheets, meta_tags=[
    {
        'name': 'viewport',
        'content': 'width=device-width, initial-scale=1.0'
    },
    {
        'name': 'description',
        'content': 'A dashboard built to visualise the effect of the Coronavirus in Uganda with information on the active, confirmed, recovered and death cases.',

    },
    {
        'name': 'author',
        'content': 'Jonathan Thomas Musiitwa'
    },
])

server = app.server

app.config.suppress_callback_exceptions = True
app.title = 'Uganda COVID-19 Dashboard'
app._favicon = 'assets/favicon.ico'

app.layout = html.Div(
    [
        dcc.Location(id='url', refresh=False),
        html.Div(id='page-content')
    ]
)

# Navigation Callback
@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/apps/home':
        return home.home_layout
    elif pathname == '/apps/about':
        return about.about_layout
    else:
        return home.home_layout


if __name__ == '__main__':
    app.run_server(debug=True)
