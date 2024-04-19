import pandas as pd

def load_data(cache):
    @cache.memoize(timeout=3600)  # Cache for 1 hour
    def _load_and_process_data(file_path):
        carbon_df = pd.read_parquet(file_path)
        melted_df = carbon_df.drop(columns=['Country Code']).melt(id_vars=["Country Name", "Region"], var_name="Year", value_name="Emissions")
        melted_df['Year'] = melted_df['Year'].astype(int)
        return melted_df

    file_path = '../data/proceed/carbon_emission_proceed.parquet'
    #### Adjust the file path as needed, especially when deploying
    # file_path = 'data/proceed/carbon_emission_proceed.parquet'

    return _load_and_process_data(file_path)