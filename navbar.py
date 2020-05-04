import dash_bootstrap_components as dbc


def Navbar():
    navbar = dbc.NavbarSimple(
        children=[
            dbc.NavItem(dbc.NavLink('Home', href='/apps/home')),

            dbc.NavItem(dbc.NavLink('About', href='/apps/about')),
        ],
        className='navbar navbar-expand-lg navbar-dark bg-dark',
        brand='Uganda Covid-19 Dashboard',
        brand_href="/home",
        dark=True,
        color='primary',
        sticky="top",
    )
    return navbar
