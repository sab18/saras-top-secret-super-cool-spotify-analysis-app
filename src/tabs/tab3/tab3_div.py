from dash import html

import os, sys
src_dir_h2 = os.path.abspath(os.path.join(os.path.dirname(__file__),'..','..'))
sys.path.append(src_dir_h2)

from assets.button import generate_buttons
from assets.inputs import name

tab3_layout = html.Div([
    html.Div(f"Click to receive a randomly selected song from {name}'s entire listening history.",style={'text-align':'center','margin-top':'120px'}),
    html.Div(*generate_buttons(['Random Song Generator']),style={'text-align':'center','margin-top':'15px'}),
    html.Div(id="output-tab3",style={'margin-top':'15px'}),
    html.Div(id="table-container-tab3"),
    html.Div(id="song-details"),
    
])