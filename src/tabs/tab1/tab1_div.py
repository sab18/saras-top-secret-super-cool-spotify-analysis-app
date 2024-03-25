from dash import html
from dash import dcc


import os, sys
tab1_dir_h1 = os.path.abspath(os.path.join(os.path.dirname(__file__),'..'))
sys.path.append(tab1_dir_h1)
from tab1.tab1_plot import fig_mins_vs_year, year_total_music

src_dir_h2 = os.path.abspath(os.path.join(os.path.dirname(__file__),'..','..'))
sys.path.append(src_dir_h2)
from assets.inputs import name
#tab1_layout=html.Div(['Tab1'])


tab1_layout = html.Div([
    html.H3(f"{name}'s Spotify Minutes Listened Over the Years", style={'text-align': 'center', 'font-weight': 'bold','marginBottom': '15px'}),
    html.Div(f'At this rate, {name} will be listening to music 24/7 in {year_total_music}!', style={'margin-left':'50px','marginBottom': '15px'}),
    dcc.Graph(figure=fig_mins_vs_year, style={'marginLeft':'15px','marginRight':'15px','marginBottom':'20px'}),
], style={'margin-top': '25px'})