import dash
import dash_bootstrap_components as dbc
from dash import html
#from spm import pipelinejob
import dash_leaflet as dl


app = dash.Dash(__name__,
                external_stylesheets=[dbc.themes.BOOTSTRAP,dbc.icons.BOOTSTRAP,
                                      'https://use.fontawesome.com/releases/v5.11.2/css/all.css',
                                      {'href': 'https://fonts.googleapis.com/icon?family=Material+Icons',
                                       'rel': 'stylesheet'}],
                meta_tags=[{"name": "viewport", "content": "width=device-width, initial-scale=1"},
                           {'name': 'description', 'content': 'SPM ANALTICAL APP'},
                           {'property': 'og:title', 'content': 'SPM'},
                           {'property': 'og:type', 'content': 'website'},
                           {'property': 'og:url:', 'content': ''},
                           {'property': 'og:image',
                            'content': ''},
                           {'property': 'og:image:secure_url',
                            'content': ''},
                           {'property': 'og:image:type', 'content': 'image/png'},
                           {'http-equiv': 'X-UA-Compatible', 'content': 'IE=edge'},
                           {'name': "author", 'content': "Yogananda Muthaiha"},
                           {'charset': "UTF-8"},
                           ],

                )

app.title = 'SPM Event'
server = app.server
app.config.suppress_callback_exceptions = True

#############################################################

shortmonths = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun','Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

years = ['2018','2019','2020','2021','2022','2023']


#################################################################

header1 = html.H4(children='Dashboard Page')


#########################################################################################################
navbar_layout = dbc.Navbar([
    html.A(
        # Use row and col to control vertical alignment of logo / brand
        dbc.Row([
            dbc.Col(html.Img(src=app.get_asset_url("SAPLogo.svg"),height="40px", style={'stroke': '#508caf'})),
            dbc.Col(dbc.NavbarBrand("Incentive Management", className="ml-2",style={'fontSize': '1.3em', 'fontWeight': '600', 'color': '#ffff'})),
        ]), href='#'),

    dbc.NavbarToggler(id="navbar-toggler", className="ml-auto"),

    dbc.Collapse(
        dbc.Row([
            dbc.NavLink("MAP", href='#'),
            dbc.NavLink("TAB1", href='#timeline', external_link=True),
            dbc.NavLink("TAB2", href='#progression', external_link=True),
            dbc.NavLink("TAB3", href='#projection', external_link=True),
            dbc.NavLink("ABOUT", href='#about', external_link=True),
        ], className="ml-auto flex-nowrap mt-3 mt-md-0 align-items-center", align="right",style={'width': '9%', 'margin-left': '50%','color': '#ffff'}),
        id="navbar-collapse", navbar=True),

], sticky="top", className='mb-4 bg-white', style={'WebkitBoxShadow': '0px 5px 5px 0px rgba(100, 100, 100, 0.1)', })

################################


cards = [dbc.Card([
        html.H2("€ 2000", className="card-title"),
        html.P("Target", className="card-text"), ],
        body=True, color="light",
            ),
        dbc.Card([
        html.H2("€ 1505", className="card-title"),
        html.P("Achievement", className="card-text"), ],
        body=True, color="dark",inverse=True,
            ),
        dbc.Card([
        html.H2("75%", className="card-title"),
        html.P("Achievement %", className="card-text"), ],
        body=True, color="primary",inverse=True,
            ),
        dbc.Card([
        html.H2("€ 495", className="card-title"),
        html.P("Required", className="card-text"), ],
        body=True, color="light",
            )
         
         ]
        
Card1 = dbc.Container(
    [
        dbc.Row([dbc.Col(card) for card in cards]),
    ],
    fluid=False,
)

###############################################################################################

card_sales = dbc.Card(
    dbc.CardBody(
        [
            html.H2([html.I(className="bi bi-currency-exchange me-2"), "Sales"], className="text-nowrap"),
            html.H4("$106.7M"),
            html.Div(
                [
                    html.I("5.8%", className="bi bi-caret-up-fill text-success"),
                    " vs LY",
                ]
            ),
        ], className="border-start border-success border-5"
    ),
    className="text-center m-4"
)


card_profit = dbc.Card(
    dbc.CardBody(
        [
            html.H2([html.I(className="bi bi-bank me-2"), "Profit"], className="text-nowrap"),
            html.H4("$8.3M",),
            html.Div(
                [
                    html.I("12.3%", className="bi bi-caret-down-fill text-danger"),
                    " vs LY",
                ]
            ),
        ], className="border-start border-danger border-5"
    ),
    className="text-center m-4",
)


card_orders = dbc.Card(
    dbc.CardBody(
        [
            html.H2([html.I(className="bi bi-cart me-2"), "Orders"], className="text-nowrap"),
            html.H4("91.4K"),
            html.Div(
                [
                    html.I("10.3%", className="bi bi-caret-up-fill text-success"),
                    " vs LY",
                ]
            ),
        ], className="border-start border-success border-5"
    ),
    className="text-center m-4",
)




#######################################
# A few cities in Germany.
cities = [dict(title="Berlin", position=[52.5200, 13.405000]),
          dict(title="Walldorf", position=[49.30642, 8.642800]),
          dict(title="Munich", position=[48.1351, 11.582000])]
# Create example app.
center = [48, 11]
map_component = html.Div(
    [html.Br(),
    dl.Map([
    dl.TileLayer(),
    dl.CircleMarker(center=center, radius=30)
], center=center, zoom=6, style={'height': '50vh'}),
])

###############################

summary = {"Sales": "$100K", "Profit": "$5K", "Orders": "6K", "Customers": "300"}


def make_card(title, amount):
    return dbc.Card(
        [
            dbc.CardHeader(html.H2(title)),
            dbc.CardBody(html.H3(amount, id=title)),
        ],
        className="text-center shadow",
    )

##########################################################################




footer_section = html.H4('Data Source', className='mb-4', id='about')






app.layout = html.Div([
    navbar_layout,
    header1,
    Card1,
    dbc.Container(dbc.Row([dbc.Col(card_sales), dbc.Col(card_profit), dbc.Col(card_orders)],),fluid=True,),
    dbc.Container(dbc.Row([dbc.Col(make_card(k, v)) for k, v in summary.items()], className="my-4"),fluid=True,),
    map_component,
    #timeline_section,
    #progression_section,
    #projection_section,
    footer_section
]
)

if __name__ == '__main__':
    app.run_server(debug=True, host='127.0.0.1', port=8050)
