from dash.dependencies import Input, Output, State
import plotly.express as px
import pandas as pd
import dash
from dash.exceptions import PreventUpdate


def register_callbacks(app, cache, melted_df):
    @cache.memoize(timeout=300) 
    def get_filtered_data(melted_df, selected_countries, selected_years):
        return melted_df[
            (melted_df['Country Name'].isin(selected_countries)) &
            (melted_df['Year'] >= selected_years[0]) &
            (melted_df['Year'] <= selected_years[1])
        ]
    @app.callback(
        [Output('country-dropdown', 'value'),
         Output('emissions-time-series', 'figure')],
        [Input('emissions-map-chart', 'clickData'),
         Input('country-dropdown', 'value'),
         Input('year-slider', 'value')]
    )
    def line_from_map_click(clickData, selected_countries, selected_years):
        ctx = dash.callback_context
        if not ctx.triggered:
            placeholder_figure = {
                'data': [],
                'layout': {
                    'xaxis': {'visible': False},
                    'yaxis': {'visible': False},
                    'annotations': [{
                        'text': 'Please select a country to visualize the carbon emission line chart',
                        'xref': 'paper',
                        'yref': 'paper',
                        'showarrow': False,
                        'font': {
                            'size': 16
                        },
                        'align': 'center'
                    }]
                }
            }
            return [selected_countries, placeholder_figure]
        
        input_id = ctx.triggered[0]['prop_id'].split('.')[0]

        if selected_countries is None:
            selected_countries = []

        if input_id == 'emissions-map-chart' and clickData:
            country_name = clickData['points'][0]['location']
            if country_name not in selected_countries:
                selected_countries.append(country_name)
            else:
                selected_countries.remove(country_name)

        # Proceed with filtering data and creating the line chart
        df_filtered = get_filtered_data(melted_df, selected_countries, selected_years)

        line_fig = px.line(df_filtered, x='Year', y='Emissions', color='Country Name',
                           title='CO2 Emissions Over Time for Selected Countries')
        line_fig.update_yaxes(title_text='Emissions (kt CO2)')
        return [selected_countries, line_fig]


    ## Bar Chart @ Jing
    colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']

    def generate_color_map(df_top_countries):
        color_discrete_map = {country: colors[i] for i, country in enumerate(df_top_countries['Country Name'])}
        return color_discrete_map
    
    @app.callback(
        Output('emissions-bar-chart', 'figure'),
        [Input('region-dropdown', 'value')]
    )
    
    def update_bar_chart(selected_regions):
        if not selected_regions:
            return px.bar(title='Choose any Region(s): <br>For CO2 Emissions Bar Chart')

        df_filtered_by_region = melted_df[melted_df['Region'].isin(selected_regions)]
        df_countries = df_filtered_by_region.groupby('Country Name', as_index=False).agg({'Emissions':'sum'})
        df_top_countries = df_countries.sort_values('Emissions', ascending=False).head(5)
        color_discrete_map = generate_color_map(df_top_countries)

        max_emissions_value = df_top_countries['Emissions'].max()
        y_axis_max = max_emissions_value * 1.2

        fig = px.bar(df_top_countries, x='Country Name', y='Emissions', text='Emissions',
                 title='Top 5 Countries\' Cumulative CO2 Emissions<br>in Selected Region(s)',
                 color='Country Name',
                 color_discrete_map=color_discrete_map)
        
        fig.update_traces(texttemplate='%{text:.2s}', textposition='outside')
        fig.update_xaxes(title_text='')
        fig.update_yaxes(title_text='Emissions (kt CO2)', range=[0, y_axis_max])

        return fig


    # Pie Chart @ Jo
    def generate_color_sequence(df_top_countries):
        colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#7f7f7f']  
        color_sequence = [colors[i] for i in range(len(df_top_countries) + (1 if 'Others' in df_top_countries['Country Name'].values else 0))]
        return color_sequence

    @app.callback(
        Output('emissions-pie-chart', 'figure'),
        [Input('region-dropdown', 'value')]
    )
    def update_pie_chart(selected_regions):
        if not selected_regions:
            return px.pie(title='Choose any Region(s): <br>For CO2 Emissions Pie Chart')

        df_filtered_by_region = melted_df[melted_df['Region'].isin(selected_regions)]
        df_countries = df_filtered_by_region.groupby('Country Name', as_index=False).agg({'Emissions':'sum'})
        
        df_top_countries = df_countries.sort_values('Emissions', ascending=False).head(5)
        if len(df_countries) > 5: 
            other_emissions = df_countries.sort_values('Emissions', ascending=False)[5:]['Emissions'].sum()
            other_row = pd.DataFrame(data={'Country Name': ['Others'], 'Emissions': [other_emissions]})
            df_display = pd.concat([df_top_countries, other_row], ignore_index=True)
        else:
            df_display = df_top_countries
        
        color_sequence = generate_color_sequence(df_top_countries)
        fig = px.pie(data_frame=df_display,
                    names='Country Name', 
                    values='Emissions',
                    hover_data={'Country Name': True, 'Emissions': ':.2f'}, 
                    hole=.2,
                    title='Cumulative CO2 Emission: <br>Top 5 Countries and Others of Selected Region(s)')
        
        fig.update_traces(hovertemplate='%{label}: <br>Percentage: %{percent} <br>CO2 Emission: %{value} MT/capita<br>', textposition='outside',
                      marker=dict(colors=color_sequence))
        return fig

    # Map Chart @ Yili
    @app.callback(
        Output('emissions-map-chart', 'figure'),
        [Input('country-dropdown', 'value'), Input('year-slider', 'value')]
    )

    def update_map(selected_countries, selected_years):
        if selected_countries:
            df_filtered = melted_df[
                (melted_df['Country Name'].isin(selected_countries)) &
                (melted_df['Year'] >= selected_years[0]) &
                (melted_df['Year'] <= selected_years[1])
            ]
        else:
            df_filtered = melted_df[
                (melted_df['Year'] >= selected_years[0]) &
                (melted_df['Year'] <= selected_years[1])
            ]
        
        # Calculate summary statistics for each country
        stats_by_country = df_filtered.groupby('Country Name').agg(
            Total_Emissions=pd.NamedAgg(column='Emissions', aggfunc='sum'),
            Average_Emissions=pd.NamedAgg(column='Emissions', aggfunc='mean'),
            Std_Emissions=pd.NamedAgg(column='Emissions', aggfunc='std'), 
            Max_Emissions=pd.NamedAgg(column='Emissions', aggfunc='max'),
            Min_Emissions=pd.NamedAgg(column='Emissions', aggfunc='min')
        ).reset_index()

        # Create the choropleth map
        fig = px.choropleth(
            stats_by_country,
            locations="Country Name",
            locationmode="country names",
            color="Total_Emissions",
            hover_name="Country Name",
            hover_data={
                'Total_Emissions': True,
                'Average_Emissions': ':.2f',
                'Std_Emissions': ':.2f',
                'Max_Emissions': ':.2f',
                'Min_Emissions': ':.2f'
            },
            color_continuous_scale=px.colors.sequential.Teal,
            title="CO2 Emissions by Country",
            labels={'Total_Emissions': 'Total Emissions (kt CO2)'}
        )

        fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0}, clickmode='event+select' )
        fig.update_geos(projection_type="natural earth")

        return fig

    