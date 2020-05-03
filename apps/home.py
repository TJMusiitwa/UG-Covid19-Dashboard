import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

from navbar import Navbar

nav = Navbar()

df_uganda = pd.read_csv('uganda_data.csv')
df_uganda['date'] = pd.to_datetime(df_uganda['date'])

updated = df_uganda['date'].dt.strftime('%B %d, %Y').iloc[-1]

traces = [
    go.Scatter(
        x=df_uganda.groupby('date')['date'].first(),
        y=df_uganda.groupby('date')['Confirmed'].sum(),
        name="Confirmed", stackgroup='one',
        mode='lines', hovertemplate='%{y:,g}'),
    go.Scatter(
        x=df_uganda.groupby('date')['date'].first(),
        y=df_uganda.groupby('date')['Active'].sum(),
        name="Active", stackgroup='one',
        mode='lines', hovertemplate='%{y:,g}'),
    go.Scatter(
        x=df_uganda.groupby('date')['date'].first(),
        y=df_uganda.groupby('date')['Recovered'].sum(),
        name="Recovered", stackgroup='one',
        mode='lines', hovertemplate='%{y:,g}'),
    go.Scatter(
        x=df_uganda.groupby('date')['date'].first(),
        y=df_uganda.groupby('date')['Deaths'].sum(),
        name="Deaths", stackgroup='one',
        mode='lines', hovertemplate='%{y:,g}')
]

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
    # Date updated content
    html.Div(children='Data last updated {}'.format(updated), style={
        'textAlign': 'center',
    }),
    html.Br(),
    # Statitic Cards
    html.Div(dbc.Container(dbc.Row([
        dbc.Col(),
        dbc.Col(),
        dbc.Col(),
        dbc.Col(),

    ]),
    ),
    ),
    # Main Page Content
    html.Div(
        dbc.Container(
            dbc.Row(
                dbc.Col(),
                dbc.Col(),
                dbc.Col(),
            ))
    ),
    # Graph Timeline
    html.Div(
        dbc.Container(
            dcc.Graph(
                figure={
                    'data': traces,
                    'layout': {
                        'title': 'Cases timeline in Africa',
                        'xaxis_title': 'Date',
                        'yaxis_title': 'Number of Cases',
                    }
                })
        ),
    ),
    # Footer
    html.Footer(
        [
            html.Address(html.A(
                html.P('Developed by Jonathan Musiitwa'),
                href='mailto:jonamusiitwa@outlook.com'))
        ]
    )
])
