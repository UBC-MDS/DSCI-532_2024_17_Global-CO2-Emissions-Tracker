from dash import html, dcc
import dash_bootstrap_components as dbc

def create_layout(app, melted_df):
    return dbc.Container([
        dbc.Row([
            html.H1('Global CO2 Emission Tracker:', className='text-center', style={'color': '#fff'}),
            html.Br(),
            html.H2('Visualizing Carbon Footprints Worldwide', className='text-center', style={'color': '#fff'}),
            ], style={'backgroundColor': '#002145', 'padding': '10px'}, className='justify-content-center'),

        dbc.Row([
            html.Br(),
        ]),

        dbc.Row([
            dbc.Col([
                dbc.Row([
                    html.Div('Select country and year for emission data:',
                            style={'font-weight': 'bold', 'font-size': '20px', 'color': '#002145'})
                ]),
                dbc.Row([
                    html.Div('Country'),
                    dcc.Dropdown(
                    id='country-dropdown',
                    options=[{'label': i, 'value': i} for i in melted_df['Country Name'].unique()],
                    multi=True,  # Enable multiple selection
                    placeholder="Select Country or Countries",  # Default value
                    ),
                    html.Br(),
                ]),
                dbc.Row([
                    html.Div('Year'),
                    dcc.RangeSlider(
                    id='year-slider',
                    min=melted_df['Year'].min(),
                    max=melted_df['Year'].max(),
                    value=[1990, 2020],  # Default range
                    marks={str(year): str(year) for year in range(melted_df['Year'].min(), melted_df['Year'].max()+1, 5)},  # Mark every 5 years
                    step=1,
                    allowCross=False,
                    className='custom-slider',
                    tooltip={"placement": "bottom", "always_visible": True},
                    updatemode='drag',
                    pushable=1
                    ),
                    html.Br(),
                ]),

            ], md=7, style={'backgroundColor': '#F4F4F4', 'padding': '20px'}),
            dbc.Col([], md=1, style={'backgroundColor': '#F4F4F4'}),
            dbc.Col([
                dbc.Row([
                    html.Div('Select region for top region emitters:',
                            style={'font-weight': 'bold', 'font-size': '20px', 'color': '#002145'})
                ]),
                dbc.Row([
                    html.Div('Region'),
                    dcc.Dropdown(
                    id='region-dropdown',
                    options=[{'label': i, 'value': i} for i in melted_df['Region'].unique()],
                    multi=True,
                    placeholder="Select Region(s)",
                    value=['North America']
                    ),
                    html.Br(),   
                ])
            ], md=4, style={'backgroundColor': '#F4F4F4', 'padding': '20px'}),
        ]),

        dbc.Row([
            dbc.Col([
                dcc.Graph(id='emissions-map-chart')
            ],md=7, style={}),
            dbc.Col([], md=1),
            dbc.Col([
                dcc.Graph(id='emissions-pie-chart')
            ],md=4,style={}),
            html.Br(),
        ]),

        dbc.Row([
            dbc.Col([
                dcc.Graph(id='emissions-time-series')
            ],md=7, style={}),
            dbc.Col([], md=1),
            dbc.Col([
                dcc.Graph(id='emissions-bar-chart')
            ],md=4,style={}),
            html.Br(),
        ]),

        dbc.Row(
            dbc.Col(
                html.Footer([
                    html.P("Global CO2 Emission Tracker - A comprehensive tool to visualize CO2 emissions globally."),
                    html.P("Author: Yili Tang, Jing Wen, Hancheng Qin, Kittipong Wongwipasamitkun"),
                    html.P(["Visit the project repository: ", html.A("GitHub Repo", href="https://github.com/UBC-MDS/DSCI-532_2024_17_Global-CO2-Emissions-Tracker", target="_blank")]),
                    html.P("Last updated: April 20, 2024.")
                ], style={'backgroundColor': '#002145', 'color': 'white', 'textAlign': 'center', 'padding': '20px'}),
                width=12  
            ),
        )
    ], fluid=True)
