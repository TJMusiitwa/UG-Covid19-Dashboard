from navbar import Navbar
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.io as pio
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import requests

pio.templates.default = "plotly_dark"


nav = Navbar()

df_uganda = pd.read_csv('uganda_data.csv')
df_uganda['date'] = pd.to_datetime(df_uganda['date'])

updated = df_uganda['date'].dt.strftime('%B %d, %Y').iloc[-1]

# Statistic Indicators
recovered = df_uganda[df_uganda['date'] ==
                      df_uganda['date'].iloc[-1]]['Recovered'].sum()
confirmed = df_uganda[df_uganda['date'] ==
                      df_uganda['date'].iloc[-1]]['Confirmed'].sum()
deaths = df_uganda[df_uganda['date'] ==
                   df_uganda['date'].iloc[-1]]['Deaths'].sum()
active = df_uganda[df_uganda['date'] ==
                   df_uganda['date'].iloc[-1]]['Active'].sum()

fig = go.Figure(go.Indicator(
    mode="gauge+number",
    value=450,
    title={'text': "Speed"},
    domain={'x': [0, 1], 'y': [0, 1]}
))

# Get Information from REST API
r = requests.get(
    'https://corona.lmao.ninja/v2/countries/Uganda?yesterday=false&strict&query%20')

data = r.json()

num_tests = data['tests']
cases_per_mill = data['casesPerOneMillion']
test_coverage = data['testsPerOneMillion']

# Graph Timeline Data
timeline_fig = go.Figure()
timeline_fig.add_trace(go.Scatter(
    x=df_uganda.groupby('date')['date'].first(),
    y=df_uganda.groupby('date')['Confirmed'].sum(),
    name="Confirmed", stackgroup='one',
    mode='lines', hovertemplate='%{y:,g}'))


timeline_fig.add_trace(go.Scatter(
    x=df_uganda.groupby('date')['date'].first(),
    y=df_uganda.groupby('date')['Active'].sum(),
    name="Active", stackgroup='one',
    mode='lines', hovertemplate='%{y:,g}'))

timeline_fig.add_trace(go.Scatter(
    x=df_uganda.groupby('date')['date'].first(),
    y=df_uganda.groupby('date')['Recovered'].sum(),
    name="Recovered", stackgroup='one',
    mode='lines', hovertemplate='%{y:,g}'))

timeline_fig.add_trace(go.Scatter(
    x=df_uganda.groupby('date')['date'].first(),
    y=df_uganda.groupby('date')['Deaths'].sum(),
    name="Deaths", stackgroup='one',
    mode='lines', hovertemplate='%{y:,g}'))

timeline_fig.update_xaxes(rangeslider_visible=True)

timeline_fig.update_layout(title="COVID-19 infections in Uganda",
                           xaxis_title="Date",
                           yaxis_title="Number of Individuals")

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
    # Date updated content`
    html.Div(children='Data last updated {}'.format(updated), style={
        'textAlign': 'center',
    }),
    html.Br(),
    # Statitic Cards
    html.Div(
        dbc.Container(
            dbc.Row(
                [
                    dbc.Col(dcc.Graph(
                        figure=go.Figure(
                            go.Indicator(mode='number',
                                         value=confirmed, title='Confirmed Cases'),
                            layout=go.Layout(
                                paper_bgcolor='rgba(0,0,0,0)',
                                plot_bgcolor='rgba(0,0,0,0)'
                            )
                        ),
                        style={'height': 250}
                    ),
                    ),
                    dbc.Col(
                        dcc.Graph(figure=go.Figure(go.Indicator(mode='number',
                                                                value=active, title='Active Cases'),
                                                   layout=go.Layout(
                            paper_bgcolor='rgba(0,0,0,0)',
                            plot_bgcolor='rgba(0,0,0,0)'
                        )
                        ), style={'height': 250}),
                    ),
                    dbc.Col(
                        dcc.Graph(figure=go.Figure(
                            data=go.Indicator(mode='number',                                         value=recovered,
                                              title='Recovered Cases'), layout=go.Layout(
                                paper_bgcolor='rgba(0,0,0,0)',
                                plot_bgcolor='rgba(0,0,0,0)'
                            )), style={'height': 250}),
                    ),

                    dbc.Col(
                        dcc.Graph(figure=go.Figure(go.Indicator(mode='number',
                                                                value=deaths, title='Death Cases'), layout=go.Layout(
                            paper_bgcolor='rgba(0,0,0,0)',
                            plot_bgcolor='rgba(0,0,0,0)'
                        )), style={'height': 250}),
                    ),

                ],
            ),

        ),

    ),
    html.Br(),
    # Main Page Content
    html.Div(
        dbc.Container(
            dbc.Row(
                [
                    dbc.Col(dbc.ListGroup(
                        [
                            dbc.ListGroupItem(["Cases per million", dbc.Badge(
                                cases_per_mill)], className='list-group-item d-flex justify-content-between align-items-center'),
                            dbc.ListGroupItem(["Test Carried out", dbc.Badge(
                                num_tests)], className='list-group-item d-flex justify-content-between align-items-center'),
                            dbc.ListGroupItem(["Test Coverage per million", dbc.Badge(
                                test_coverage)], className='list-group-item d-flex justify-content-between align-items-center'),
                        ],
                        className='list-group',
                    ), width=3),
                    dbc.Col(dcc.Graph(figure=timeline_fig)),
                    dbc.Col(
                        dbc.Card(
                            className='card border-primary mb-3',
                            outline=True,
                            children=[
                                dbc.CardHeader(
                                    'Twitter Feed', className='card-header'),
                                dbc.CardBody(
                                    className='card-body',
                                    children=dbc.ListGroup(

                                        [
                                            dbc.ListGroupItem(
                                                [
                                                    dbc.ListGroupItemHeading(
                                                        "This item has a heading"),
                                                    dbc.ListGroupItemText(
                                                        "And some text underneath"),
                                                ]
                                            ),
                                            dbc.ListGroupItem(
                                                [
                                                    dbc.ListGroupItemHeading(
                                                        "This item also has a heading"),
                                                    dbc.ListGroupItemText(
                                                        "And some more text underneath too"),
                                                ]
                                            ),
                                            dbc.ListGroupItem(
                                                [
                                                    dbc.ListGroupItemHeading(
                                                        "This item has a heading"),
                                                    dbc.ListGroupItemText(
                                                        "And some text underneath"),
                                                ]
                                            ),
                                            dbc.ListGroupItem(
                                                [
                                                    dbc.ListGroupItemHeading(
                                                        "This item also has a heading"),
                                                    dbc.ListGroupItemText(
                                                        "And some more text underneath too"),
                                                ]
                                            ),
                                        ],
                                        className='list-group',
                                        flush=True,
                                    ),),
                            ],

                        ),
                        width=3),
                ]
            )),
    ),
    # Footer
    html.Footer(
        html.Center([
            html.Address(
                html.A(
                    html.P('Developed by Jonathan Musiitwa'),
                    href='mailto:jonamusiitwa@outlook.com'))
        ])
    )
])
