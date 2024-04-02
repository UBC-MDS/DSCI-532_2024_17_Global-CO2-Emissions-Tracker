import dash
from dash import dcc, html, Input, Output
import plotly.express as px
import pandas as pd

# Load the dataset and Preprocessing
carbon_df = pd.read_csv('../data/raw/carbon_emission_raw.csv')
carbon_df = carbon_df.drop(['Indicator Name', 'Indicator Code'], axis=1)
non_country_names = [
    'Africa Eastern and Southern', 'Africa Western and Central', 'Arab World', 'Bahamas, The',
    'Central Europe and the Baltics', 'Caribbean small states', 'East Asia & Pacific (excluding high income)',
    'Early-demographic dividend', 'East Asia & Pacific', 'Europe & Central Asia (excluding high income)',
    'Europe & Central Asia', 'Euro area', 'European Union', 'Fragile and conflict affected situations',
    'Heavily indebted poor countries (HIPC)', 'High income', 'IBRD only', 'IDA & IBRD total', 'IDA total',
    'IDA blend', 'IDA only', 'Latin America & Caribbean (excluding high income)', 'Latin America & Caribbean',
    'Least developed countries: UN classification', 'Low income', 'Lower middle income', 'Low & middle income',
    'Late-demographic dividend', 'Middle East & North Africa', 'Middle income', 'Middle East & North Africa (excluding high income)',
    'North America', 'OECD members', 'Other small states', 'Pacific island small states', 'Post-demographic dividend',
    'Pre-demographic dividend', 'Small states', 'Sub-Saharan Africa (excluding high income)', 'Sub-Saharan Africa',
    'East Asia & Pacific (IDA & IBRD countries)', 'Europe & Central Asia (IDA & IBRD countries)',
    'Latin America & the Caribbean (IDA & IBRD countries)', 'Middle East & North Africa (IDA & IBRD countries)',
    'South Asia (IDA & IBRD)', 'Sub-Saharan Africa (IDA & IBRD countries)', 'Upper middle income', 'World'
]

carbon_df_filtered = carbon_df[~carbon_df['Country Name'].isin(non_country_names)]
carbon_df_filtered.head()
carbon_df_new = carbon_df_filtered.copy()

carbon_df_new['Total Emission'] = carbon_df.iloc[:, 2:].sum(axis=1)
carbon_df_new['Yearly Mean'] = carbon_df.iloc[:, 2:].mean(axis=1)
carbon_df_new['Yearly Standard Deviation'] = carbon_df.iloc[:, 2:].std(axis=1)
carbon_df_new['Yearly Minimum'] = carbon_df.iloc[:, 2:].min(axis=1)
carbon_df_new['Yearly Maximum'] = carbon_df.iloc[:, 2:].max(axis=1)


melted_df = carbon_df_filtered.melt(id_vars=["Country Name"], var_name="Year", value_vars=[str(year) for year in range(1990, 2021)], value_name="Emissions")
melted_df['Year'] = melted_df['Year'].astype(int)  # Convert 'Year' to integer for plotting


### app layout
app = dash.Dash(__name__)
server = app.server
app.layout = html.Div([
    html.H1("CO2 Emissions Dashboard"),
    
    dcc.Dropdown(
        id='country-dropdown',
        options=[{'label': i, 'value': i} for i in melted_df['Country Name'].unique()],
        value=['United States'],  # Default value, can now be a list
        multi=True  # Enable multiple selection
    ),
    
    dcc.Graph(id='emissions-time-series')
])


### define function for plot
## line chart
@app.callback(
    Output('emissions-time-series', 'figure'),
    [Input('country-dropdown', 'value')]
)

def update_graph(selected_countries):
    if not selected_countries:
    
        return px.line(title='Select countries to see CO2 Emissions Over Time')
    df_filtered = melted_df[melted_df['Country Name'].isin(selected_countries)]
    fig = px.line(df_filtered, x='Year', y='Emissions', color='Country Name',
                  title='CO2 Emissions Over Time for Selected Countries')
    
    return fig


## Bar Chart
# @app.callback(
#     Output('emissions-time-series', 'figure'),
#     [Input('country-dropdown', 'value')]
# )


## Pie Chart

## Map Chart

if __name__ == '__main__':
    app.run_server(debug=False)