import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import dash_auth

VALID_USERNAME_PASSWORD_PAIRS = {
    'hello': 'world'
}

app = dash.Dash(__name__, update_title=None,
    external_stylesheets=[dbc.themes.BOOTSTRAP],
    # these meta_tags ensure content is scaled correctly on different devices
    # see: https://www.w3schools.com/css/css_rwd_viewport.asp for more
    meta_tags=[
        {"name": "viewport", "content": "width=device-width, initial-scale=1"}
    ],
)

# auth = dash_auth.BasicAuth(
#     app,
#     VALID_USERNAME_PASSWORD_PAIRS
# )

app.index_string = '''
<!DOCTYPE html>
<html>
    <head>
        {%metas%}
        <title>{%title%}</title>
        {%favicon%}
        {%css%}
        <!-- Global site tag (gtag.js) - Google Analytics -->
        <script async src="https://www.googletagmanager.com/gtag/js?id=UA-175828599-1"></script>
        <script>
          window.dataLayer = window.dataLayer || [];
          function gtag(){dataLayer.push(arguments);}
          gtag('js', new Date());

          gtag('config', 'UA-175828599-1');
        </script>
    </head>
    <body>
        <div></div>
        {%app_entry%}
        <footer>
            {%config%}
            {%scripts%}
            {%renderer%}
        </footer>
        <div></div>
    </body>
</html>
'''
app.title = 'GeoFlashCards'

server = app.server

# we use the Row and Col components to construct the sidebar header
# it consists of a title, and a toggle, the latter is hidden on large screens
sidebar_header = dbc.Row(
    [
        dbc.Col(dcc.Link(html.H2("GeoFlashCards", className="display-5"),href='/')),
        dbc.Col(
            [
                html.Button(
                    # use the Bootstrap navbar-toggler classes to style
                    html.Span(className="navbar-toggler-icon"),
                    className="navbar-toggler",
                    # the navbar-toggler classes don't set color
                    style={
                        "color": "rgba(0,0,0,.5)",
                        "border-color": "rgba(0,0,0,.1)",
                    },
                    id="navbar-toggle",
                ),
                html.Button(
                    # use the Bootstrap navbar-toggler classes to style
                    html.Span(className="navbar-toggler-icon"),
                    className="navbar-toggler",
                    # the navbar-toggler classes don't set color
                    style={
                        "color": "rgba(0,0,0,.5)",
                        "border-color": "rgba(0,0,0,.1)",
                    },
                    id="sidebar-toggle",
                ),
            ],
            # the column containing the toggle will be only as wide as the
            # toggle, resulting in the toggle being right aligned
            width="auto",
            # vertically align the toggle in the center
            align="center",
        ),
    ]
)

sidebar = html.Div(
    [
        sidebar_header,
        # we wrap the horizontal rule and short blurb in a div that can be
        # hidden on a small screen
        html.Div(
            [
                html.Hr(),
                html.P(
                    "Think you know maps?",
                    className="lead",
                ),
            ],
            id="blurb",
        ),
        # use the Collapse component to animate hiding / revealing links
        dbc.Collapse(
            dbc.Nav(
                [
                    dbc.NavLink("Home", href="/home", id="home-link"),
                    html.Hr(),
                    html.H5("India: Geography", id="india-geography-map-list"),
                    dbc.NavLink("National Parks", href="/nationalparks", id="nationalparks-link"),
                    dbc.NavLink("Wildlife Sanctuaries", href="/wildlifesanctuaries", id="wildlifesanctuaries-link"),
                    dbc.NavLink("Biosphere Reserves [PRO]", href="/biospherereserves", id="biospherereserves-link"),
                    dbc.NavLink("Geological Monuments [PRO]", href="/geologicalmonuments", id="geologicalmonuments-link"),
                    dbc.NavLink("World Heritage Sites [PRO]", href="/worldheritagesites", id="worldheritagesites-link"),
                    dbc.NavLink("Nuclear Power Plants [PRO]", href="/nuclearpowerplants", id="nuclearpowerplants-link"),
                    html.Hr(),
                    html.H5("India: History", id="india-history-map-list"),
                    dbc.NavLink("INC Sessions [PRO]", href="/incsessions", id="incsessions-link"),
                    dbc.NavLink("Major Battles [PRO]", href="/majorbattles", id="majorbattles-link"),
                    dbc.NavLink("EIC Treaties [PRO]", href="/eictreaties", id="eictreaties-link"),
                    dbc.NavLink("Ancient Indian Cities", href="/ancientindiancities", id="ancientindiancities-link"),
                    dbc.NavLink("Indian Freedom Struggle [PRO]", href="/indianfreedomstruggle", id="indianfreedomstruggle-link"),
                    html.Hr(),
                    dbc.NavLink("Get PRO Version", href="/getproversion", id="getproversion-link"),
                    dbc.NavLink("About", href="/about", id="about-link"),
                ],
                vertical=True,
                pills=True,
            ),
            id="collapse",
        ),
    ],
    id="sidebar",
)

content = html.Div(id="page-content")

footer = html.Div(id="page-footer")

app.layout = html.Div([dcc.Location(id="url"), sidebar, content, footer])


# this callback uses the current pathname to set the active state of the
# corresponding nav link to true, allowing users to tell see page they are on
@app.callback(
    [Output("home-link", "active"), Output("about-link", "active"), Output("nationalparks-link", "active"), Output("wildlifesanctuaries-link", "active"), Output("biospherereserves-link", "active"), Output("geologicalmonuments-link", "active"), Output("worldheritagesites-link", "active"), Output("nuclearpowerplants-link", "active"), Output("incsessions-link", "active"), Output("majorbattles-link", "active"), Output("eictreaties-link", "active"), Output("ancientindiancities-link", "active"), Output("indianfreedomstruggle-link", "active"), Output("getproversion-link", "active")],
    [Input("url", "pathname")],
)
def toggle_active_links(pathname):
    if pathname in ["/", "/home"]:
        return True, False, False, False, False, False, False, False, False, False, False, False, False, False
    elif pathname == "/about":
        return False, True, False, False, False, False, False, False, False, False, False, False, False, False
    elif pathname == "/nationalparks":
        return False, False, True, False, False, False, False, False, False, False, False, False, False, False
    elif pathname == "/wildlifesanctuaries":
        return False, False, False, True, False, False, False, False, False, False, False, False, False, False
    elif pathname == "/biospherereserves":
        return False, False, False, False, True, False, False, False, False, False, False, False, False, False
    elif pathname == "/geologicalmonuments":
        return False, False, False, False, False, True, False, False, False, False, False, False, False, False
    elif pathname == "/worldheritagesites":
        return False, False, False, False, False, False, True, False, False, False, False, False, False, False
    elif pathname == "/nuclearpowerplants":
        return False, False, False, False, False, False, False, True, False, False, False, False, False, False
    elif pathname == "/incsessions":
        return False, False, False, False, False, False, False, False, True, False, False, False, False, False
    elif pathname == "/majorbattles":
        return False, False, False, False, False, False, False, False, False, True, False, False, False, False
    elif pathname == "/eictreaties":
        return False, False, False, False, False, False, False, False, False, False, True, False, False, False
    elif pathname == "/ancientindiancities":
        return False, False, False, False, False, False, False, False, False, False, False, True, False, False
    elif pathname == "/indianfreedomstruggle":
        return False, False, False, False, False, False, False, False, False, False, False, False, True, False
    elif pathname == "/getproversion":
        return False, False, False, False, False, False, False, False, False, False, False, False, False, True

@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname in ["/", "/home"]:
        return html.Iframe(id='homepage', srcDoc=open('home.html', 'r').read(), width='100%', height='500', style={'border': 'none'}),
    elif pathname == "/about":
        return dbc.Jumbotron(
        [
            html.Iframe(id='about', srcDoc=open('about_page.html', 'r').read(), width='100%', height='600', style={'border': 'none'}),
        ]
        )
    elif pathname == "/nationalparks":
        return html.Div([html.P('National Parks', className='page-content-title'), dbc.Jumbotron(
        [
            html.Iframe(id='national-parks-map', srcDoc=open('map_national_parks.html', 'r').read(), width='100%', height='600', style={'border': 'none'})
        ]
        )])
    elif pathname == "/wildlifesanctuaries":
        return html.Div([html.P('Wildlife Sanctuaries', className='page-content-title'), dbc.Jumbotron(
        [
            html.Iframe(id='wildlifesanctuaries-map', srcDoc=open('map_wildlife_sanctuaries.html', 'r').read(), width='100%', height='600', style={'border': 'none'})
        ]
        )])
    elif pathname == "/biospherereserves":
        return html.Div([html.P('Biosphere Reserves', className='page-content-title'), dbc.Jumbotron(
        [
            html.Iframe(id='biospherereserves-map', srcDoc=open('map_biosphere_reserves.html', 'r').read(), width='100%', height='600', style={'border': 'none'})
        ]
        )])

    elif pathname == "/geologicalmonuments":
        return html.Div([html.P('National Geological Monuments', className='page-content-title'), dbc.Jumbotron(
        [
            html.Iframe(id='geologicalmonuments-map', srcDoc=open('map_national_geological_monuments.html', 'r').read(), width='100%', height='600', style={'border': 'none'})
        ]
        )])

    elif pathname == "/worldheritagesites":
        return html.Div([html.P('World Heritage Sites', className='page-content-title'), dbc.Jumbotron(
        [
            html.Iframe(id='worldheritagesites-map', srcDoc=open('map_world_heritage_sites_india.html', 'r').read(), width='100%', height='600', style={'border': 'none'})
        ]
        )])

    elif pathname == "/nuclearpowerplants":
        return html.Div([html.P('Nuclear Power Plants', className='page-content-title'), dbc.Jumbotron(
        [
            html.Iframe(id='nuclearpowerplants-map', srcDoc=open('map_india_nuclear_power_plants.html', 'r').read(), width='100%', height='600', style={'border': 'none'})
        ]
        )])

    elif pathname == "/incsessions":
        return html.Div([html.P('Congress Sessions pre \'47', className='page-content-title'), dbc.Jumbotron(
        [
            html.Iframe(id='incsessions-map', srcDoc=open('map_congress_sessions.html', 'r').read(), width='100%', height='600', style={'border': 'none'})
        ]
        )])

    elif pathname == "/majorbattles":
        return html.Div([html.P('Major Battles of pre-modern India', className='page-content-title'), dbc.Jumbotron(
        [
            html.Iframe(id='majorbattles-map', srcDoc=open('map_india_battles.html', 'r').read(), width='100%', height='600', style={'border': 'none'})
        ]
        )])

    elif pathname == "/eictreaties":
        return html.Div([html.P('Treaties of East India Company', className='page-content-title'), dbc.Jumbotron(
        [
            html.Iframe(id='eictreaties-map', srcDoc=open('map_british_india_treaties.html', 'r').read(), width='100%', height='600', style={'border': 'none'})
        ]
        )])

    elif pathname == "/ancientindiancities":
        return html.Div([html.P('Ancient Indian Cities', className='page-content-title'), dbc.Jumbotron(
        [
            html.Iframe(id='ancientindiancities-map', srcDoc=open('map_ancient_indian_cities.html', 'r').read(), width='100%', height='600', style={'border': 'none'})
        ]
        )])

    elif pathname == "/indianfreedomstruggle":
        return html.Div([html.P('Indian Freedom Struggle: Important Places', className='page-content-title'), dbc.Jumbotron(
        [
            html.Iframe(id='indianfreedomstruggle-map', srcDoc=open('map_freedom_struggle.html', 'r').read(), width='100%', height='600', style={'border': 'none'})
        ]
        )])

    elif pathname == "/registrationsuccessful":
        return html.Iframe(id='registrationsuccessful', srcDoc=open('registration_successful_page.html', 'r').read(), width='100%', height='500', style={'border': 'none'})

    elif pathname == "/getproversion":
        return html.Iframe(id='homepage', srcDoc=open('get_pro_version.html', 'r').read(), width='100%', height='500', style={'border': 'none'}),
    # If the user tries to reach a different page, return a 404 message
    return dbc.Jumbotron(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ]
    )


@app.callback(
    Output("sidebar", "className"),
    [Input("sidebar-toggle", "n_clicks")],
    [State("sidebar", "className")],
)
def toggle_classname(n, classname):
    if n and classname == "":
        return "collapsed"
    return ""


@app.callback(
    Output("collapse", "is_open"),
    [Input("navbar-toggle", "n_clicks"),Input("about-link", "active")],
    [State("collapse", "is_open")],
)
def toggle_collapse(n, is_active, is_open):
    if n:
        return not is_open
    elif is_active:
        return not is_open
    return is_open

# @app.callback(Output("page-footer", "children"), [Input("url", "pathname")])
# def render_page_content(pathname):
#     if pathname in ["/", "/home"]:
#         return html.P('Footer goes here')

if __name__ == "__main__":
    app.run_server(debug=True)