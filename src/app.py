import dash
from dash import dcc, html, Input, Output
import plotly.express as px
import pandas as pd

# Load the dataset and Preprocessing
carbon_df = pd.read_csv('../data/proceed/carbon_emission_proceed.csv')
#### CHANGE IT WHEN DEPLOYMENT
# carbon_df = pd.read_csv('data/proceed/carbon_emission_raw.csv')

melted_df = carbon_df.drop(columns=['Country Code']).melt(id_vars=["Country Name", "Region"], var_name="Year", value_name="Emissions")
melted_df['Year'] = melted_df['Year'].astype(int)  # Ensure 'Year' is an integer for plotting


### app layout
app = dash.Dash(__name__)
#### USE IT WHEN DEPLOYMENT
# server = app.server

## @ Hanchen  Change the Layout
app.layout = html.Div([
    html.H1("CO2 Emissions Dashboard"),
    
    dcc.Dropdown(
        id='country-dropdown',
        options=[{'label': i, 'value': i} for i in melted_df['Country Name'].unique()],
        multi=True,  # Enable multiple selection
        value=['United States']  # Default value
    ),
    
    dcc.Dropdown(
        id='region-dropdown',
        options=[{'label': i, 'value': i} for i in melted_df['Region'].unique()],
        multi=True,
        placeholder="Select Region(s)"
    ),
    
    dcc.RangeSlider(
        id='year-slider',
        min=melted_df['Year'].min(),
        max=melted_df['Year'].max(),
        value=[1990, 2020],  # Default range
        marks={str(year): str(year) for year in range(melted_df['Year'].min(), melted_df['Year'].max()+1, 5)},  # Mark every 5 years
        step=1,
        allowCross=False
    ),
    
    dcc.Graph(id='emissions-time-series'),

    dcc.Graph(id='emissions-bar-chart')
])


### define function for plot 
## line chart @ Yili Change required
@app.callback(
    Output('emissions-time-series', 'figure'),
    [Input('country-dropdown', 'value'), Input('year-slider', 'value')]
)

def update_graph(selected_countries, selected_years):
    if not selected_countries or not selected_years:
        return px.line(title='Select countries and year range to see CO2 Emissions Over Time')
    
    df_filtered = melted_df[(melted_df['Country Name'].isin(selected_countries)) & 
                            (melted_df['Year'] >= selected_years[0]) & 
                            (melted_df['Year'] <= selected_years[1])]
    
    fig = px.line(df_filtered, x='Year', y='Emissions', color='Country Name',
                  title='CO2 Emissions Over Time for Selected Countries')
    
    return fig


## Bar Chart @ Jing
@app.callback(
    Output('emissions-bar-chart', 'figure'),
    [Input('region-dropdown', 'value')]
)

def update_bar_chart(selected_regions):
    if not selected_regions:
        return px.bar(title='Select a region to see the Top 5 Countries\' CO2 Emissions')

    df_filtered_by_region = melted_df[melted_df['Region'].isin(selected_regions)]
    df_top_countries = df_filtered_by_region.groupby('Country Name').agg({'Emissions':'sum'}).nlargest(5, 'Emissions').reset_index()

    fig = px.bar(df_top_countries, x='Country Name', y='Emissions', text='Emissions',
                 title='Top 5 Countries\' Total CO2 Emissions in Selected Region(s)')

    fig.update_traces(texttemplate='%{text:.2s}', textposition='outside')

    return fig


## Pie Chart @ J0
# @app.callback(
#     Output(, ),
#     [Input(, )]
# )

## Map Chart @ Yili
# @app.callback(
#     Output(, ),
#     [Input(, )]
# )

if __name__ == '__main__':
    app.run_server(debug=True, host='127.0.0.1', port=8050)
    
    #### CHANGE IT WHEN DEPLOYMENT
    # app.run_server(debug=False)