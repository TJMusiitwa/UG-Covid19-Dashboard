import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

#from app import app
from navbar import Navbar

nav = Navbar()

home_layout = html.Div([
    # Disclaimer Alert
    dbc.Alert(
        [
            html.H4("Disclaimer!", className="alert-heading"),
            html.P(
                "The information provided from this dashboard is in no way endorsed by the Ministry of Health. The contents of this website are for information purposes only and are not guaranteed to be accurate. Reliance on this website for medical guidance is strictly prohibited.",
                className="mb-0"
            ),
        ],
        id="disclaimer-alert",
        dismissable=True,
        is_open=True,
        duration=10000,
        className='alert alert-dismissible alert-warning'
    ),
    nav,
    html.Br(),
    html.Div(dbc.Container(dbc.Row([
        dbc.Col(),
        dbc.Col(),
        dbc.Col(),
        dbc.Col(),

    ]),),),
    html.Footer(
        [
            html.Address(html.A(
                html.P('Developed by Jonathan Musiitwa'),
                href='mailto:jonamusiitwa@outlook.com'))
        ]
    )

])
