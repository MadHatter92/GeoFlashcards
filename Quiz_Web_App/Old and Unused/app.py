import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP],
    meta_tags=[
        {"name": "viewport", "content": "width=device-width, initial-scale=1"}
    ]
    )

server = app.server

# the style arguments for the sidebar. We use position:fixed and a fixed width
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "padding": "2rem 1rem",
    "background-color": "#f8f9fa",
}

# the styles for the main content position it to the right of the sidebar and
# add some padding.
CONTENT_STYLE = {
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}

sidebar = html.Div(
    [
        html.H2("GeoMate", className="display-4"),
        html.Hr(),
        html.P(
            "Think you know India?", className="lead"
        ),
        dbc.Nav(
            [
                dbc.NavLink("Home", href="/home", id="home"),
                html.Hr(),
                dbc.NavLink("National Parks", href="/national-parks", id="national-parks"),
                dbc.NavLink("Wildlife Sanctuaries", href="/wildlife-sanctuaries", id="wildlife-sanctuaries"),
                html.Hr(),
                dbc.NavLink("About", href="/about", id="about"),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    style=SIDEBAR_STYLE,
)

content = html.Div(id="page-content", style=CONTENT_STYLE)

app.layout = html.Div([dcc.Location(id="url"), sidebar, content])


# this callback uses the current pathname to set the active state of the
# corresponding nav link to true, allowing users to tell see page they are on
@app.callback(
    [Output("home", "active"), Output("national-parks", "active"), Output("wildlife-sanctuaries", "active"), Output("about", "active")],
    [Input("url", "pathname")],
)

def toggle_active_links(pathname):
    if pathname == "/":
        return True, False, False, False

    if pathname == "/home":
        return True, False, False, False

    elif pathname == "/national-parks":
        return False, True, False, False

    elif pathname == "/wildlife-sanctuaries":
        return False, False, True, False

    elif pathname == "/about":
        return False, False, False, True

@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname in ["/", "/home"]:
        return html.P("Home Page Goes Here")
    elif pathname == "/national-parks":
        return html.Iframe(id='national-parks-map', srcDoc=open('map_national_parks.html', 'r').read(), width='100%', height='860', style={'border': 'none'}),

    elif pathname == "/wildlife-sanctuaries":
        return html.Iframe(id='wildlife-sanctuaries-map', srcDoc=open('map_wildlife_sanctuaries.html', 'r').read(), width='100%', height='860', style={'border': 'none'}),

    elif pathname == "/about":
        return html.P("About Page Goes Here")
    # If the user tries to reach a different page, return a 404 message
    return dbc.Jumbotron(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ]
    )


if __name__ == "__main__":
    app.run_server()
