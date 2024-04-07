from dash import html

from image import import_image
from colors import green
import os
import base64

tab0_image_folder='src'

tab0_padding='85px'

tab0_image_short_style = {'height': '95px', 'padding': '10px'}
tab0_image_tall_style = {'height': '145px', 'padding': '10px'}
# image1_path = os.path.abspath('hp1.png')

with open("hp1.png", "rb") as image_file:
    encoded_string1 = base64.b64encode(image_file.read()).decode('utf-8')
with open("hp2.png", "rb") as image_file:
    encoded_string2 = base64.b64encode(image_file.read()).decode('utf-8')
with open("hp3.png", "rb") as image_file:
    encoded_string3 = base64.b64encode(image_file.read()).decode('utf-8')
with open("hp4.png", "rb") as image_file:
    encoded_string4 = base64.b64encode(image_file.read()).decode('utf-8')
with open("hp5.png", "rb") as image_file:
    encoded_string5 = base64.b64encode(image_file.read()).decode('utf-8')
with open("hp6.png", "rb") as image_file:
    encoded_string6 = base64.b64encode(image_file.read()).decode('utf-8')

tab0_layout = html.Div([
                html.H3('Welcome!', style={'text-align': 'center','margin-top': '20px','color':green,'font-weight': 'bold'}),
                html.Div([
                    html.Span("You're about to enter "),
                    html.Span("Sara's Super Cool and Epic Spotify Analysis Webapp",style={'background-color':green}),
                    html.Span(".  In short, it's a more comprehensive, interesting, and accurate Wrapped.  If you came from the podcast, you're a real one ☮︎.")
                ],style={'padding-left': tab0_padding,'padding-right': tab0_padding, 'margin-top':'5px'}),
                html.Br(),
                html.Div("Plz explore.  You can find my listening history over the years, my most played artists and songs, and more!  I've even made a Random Song Generator if you're feeling spicy.  Who knows, you may just stumble upon a hidden gem from my past. ¯\_(ツ)_/¯",style={'padding-left': tab0_padding,'padding-right': tab0_padding}),
                html.Br(),
                html.Div([
                    html.Span("Let me know if you want an analysis like this using"),
                    html.Span(" YOUR ",style={'font-weight':'bolder'}),
                    html.Span("Spotify data.  We could make it happen ;).")
                ],style={'padding-left': tab0_padding,'padding-right': tab0_padding}),

                html.Div(['Follow me @sarabarrows18 on Spotify.'
                ],style={'padding-left': tab0_padding,'margin-top':'5px'}),

               
                html.Div([
                    html.Img(src='data:image/png;base64,{}'.format(encoded_string1),style=tab0_image_short_style),
                    html.Img(src='data:image/png;base64,{}'.format(encoded_string2),style=tab0_image_tall_style),
                    html.Img(src='data:image/png;base64,{}'.format(encoded_string3),style=tab0_image_short_style),
                    html.Img(src='data:image/png;base64,{}'.format(encoded_string4),style=tab0_image_short_style),
                    html.Img(src='data:image/png;base64,{}'.format(encoded_string5),style=tab0_image_tall_style),
                    html.Img(src='data:image/png;base64,{}'.format(encoded_string6),style=tab0_image_short_style)
                ],style={'display': 'flex', 'justify-content': 'space-between','padding': '0 60px','margin': '0 -20px','position': 'relative','margin-top':'80px'})
], style={'padding': '0 40px'}) 
