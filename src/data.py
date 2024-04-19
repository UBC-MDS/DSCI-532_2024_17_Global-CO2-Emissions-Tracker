import pandas as pd


def load_data():
    carbon_df = pd.read_parquet('../data/proceed/carbon_emission_proceed.parquet')
    #### CHANGE IT WHEN DEPLOYMENT
    # carbon_df = pd.read_parquet('data/proceed/carbon_emission_proceed.parquet')
    melted_df = carbon_df.drop(columns=['Country Code']).melt(id_vars=["Country Name", "Region"], var_name="Year", value_name="Emissions")
    melted_df['Year'] = melted_df['Year'].astype(int)
    return melted_df