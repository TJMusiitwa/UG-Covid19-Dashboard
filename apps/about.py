import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

from navbar import Navbar

nav = Navbar()

about_layout = html.Div([
    nav,
    html.Div(
        dbc.Container(
            dbc.Row(
                dcc.Markdown('''
# Uganda Covid-19 Dashboard
### Foreword
Hello and welcome, this is my second dashboard so far and I am borrowing implementations from my first dashboard to help speed things along which you can check out [here](https://african-covid19-dashboard.herokuapp.com/). The prime focus of this dashboard is as stated in the title to mainly visualize an overview of the 2019 Novel Coronavirus COVID-19 (2019-nCoV) epidemic as it relates to the Ugandan context.

This dashboard was built with Python using [Dash](https://dash.plotly.com/), with charts made in [Plotly](https://plotly.com/) and the Darkly theme of the app provided by [Bootswatch](https://bootswatch.com/darkly/).
 The code behind the dashboard  is available [here](https://github.com/TJMusiitwa/UG-Covid19-Dashboard).  I welcome any suggestions and pull requests to help add more features or improve upon the dashboard.

### Data
The data used in this dashboard is provided by the [Johns Hopkins Center for Systems Science and Engineering](https://github.com/CSSEGISandData/COVID-19) Coronavirus repository.

Further information was provided by the   [Ministry of Health](https://health.go.ug) & [Covid-19 Information Portal](https://covid19.gou.go.ug/)

### Inspiration
I would not have been able to create my this dashboard without some inspiration from the following sources, and I am highly grateful to them.

 - [COVID-19 Tracker](https://github.com/ncov19-us/front-end) 

### Contact
If you wish to contact me, I am available at this [email](mailto:jonamusiitwa@outlook.com)          
            '''),
                justify="center",
            ),

        )
    )

])
