from dash import html
from dash import dcc


# import os, sys
# src_dir_h2 = os.path.abspath(os.path.join(os.path.dirname(__file__),'..','..'))
# sys.path.append(src_dir_h2)

from button import generate_buttons
from unique_years_list import years_sorted
from inputs import name

tab2_layout=html.Div([
    html.Div(generate_buttons(years_sorted), style={'text-align': 'center', 'margin-top': '10px'}),

])

tab2_layout = html.Div([
    html.Div([
        html.Div([
            html.Div(f"Click a button to learn more about {name}'s top artists and songs each year.",
                     style={'text-align': 'center','margin-top':'15px'}),
            html.Div("Shocker there's one band that takes the cake.", style={'text-align': 'center'}),
            html.Div(generate_buttons(years_sorted), style={'text-align': 'center', 'margin-top': '10px'}),
        ]),
    ], style={'text-align': 'center', 'margin-bottom': '20px'}),
    html.Div([
        html.Div([
            html.Img(id="image-output-tab2", style={'height': '200px', 'display': 'block', 'margin': '0 auto'}),
        ]),
    ], style={'text-align': 'center'}),
    html.Div(id="output-tab2", style={'text-align': 'center', 'margin-top': '15px'}),
    html.Div(id="table-container-tab2", style={'text-align': 'center'}),
])