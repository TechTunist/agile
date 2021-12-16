import dash
import dash_core_components as dcc
import dash_html_components as html

from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px

# load the dataset
# avocado = pd.read_csv('data/avocado-updated-2020.csv')
imr = pd.read_csv('data/InfantMortalityRate.csv', encoding='cp1252')
imr.dropna(inplace=True)
# create the Dash app
app = dash.Dash()

# set up the app layout
app.layout = html.Div(children=[
    html.H1(children='Excess mortality Dashboard'),
    dcc.Dropdown(id='geo-dropdown',
                 options=[{'label': i, 'value': i}
                          for i in imr['Country'].unique()],
                 value='United Kingdom'),
    dcc.Graph(id='imr-graph')
])


# set up the callback function
@app.callback(
    Output(component_id='imr-graph', component_property='figure'),
    Input(component_id='geo-dropdown', component_property='value')
)
def update_graph(selected_country):
    filtered_imr = imr[imr['Country'] == selected_country]
    line_fig = px.line(filtered_imr,
                       x='Year', y='Infant Mortality Rate',
                       color='Gender',
                       title=f'Infant Mortality in {selected_country}')
    return line_fig


if __name__ == '__main__':
    app.run_server(debug=True)

"""
type "python dash_plotly_visualisation.py" in terminal to run script

I got a "colorama ModuleNotFound" error and had to "pip install colorama" in terminal  
"""
