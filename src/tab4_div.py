from dash import html

# import os, sys
# src_dir_h2 = os.path.abspath(os.path.join(os.path.dirname(__file__),'..','..'))
# sys.path.append(src_dir_h2)

from button import generate_buttons

tab4_layout = html.Div([
    html.Div(*generate_buttons(['Fun Facts HERE']),style={'text-align':'center','margin-top':'120px'}),
    html.Div("Did you know...",style={'text-align': 'center','margin-top':'10px'}),
    html.Div(id="output-tab4"),
    html.Div(id="table-container-tab4"),
    html.Div(id="fact_details") ,
    html.Div(id="press_button-again") ,   
])