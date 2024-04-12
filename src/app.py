import dash
import dash_bootstrap_components as dbc

from src.data import load_data
from src.components import create_layout
from src.callbacks import register_callbacks

### app layout
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
#### USE IT WHEN DEPLOYMENT
server = app.server

melted_df = load_data()
app.layout = create_layout(app, melted_df)  
register_callbacks(app, melted_df)  



if __name__ == '__main__':
    # app.run_server(debug=True, host='127.0.0.1', port=8050)
    #### CHANGE IT WHEN DEPLOYMENT
    app.run_server(debug=False)