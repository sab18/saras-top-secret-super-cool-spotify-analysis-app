from dash import html

from assets.image import import_image
from assets.colors import green

tab0_image_folder='src/tabs/tab0/tab0_pics'

tab0_padding='85px'

tab0_image_short_style = {'height': '95px', 'padding': '10px'}
tab0_image_tall_style = {'height': '145px', 'padding': '10px'}


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
                    html.Img(src='data:image/png;base64,{}'.format(import_image(tab0_image_folder+'/hp1.png')), style=tab0_image_short_style),
                    html.Img(src='data:image/png;base64,{}'.format(import_image(tab0_image_folder+'/hp2.png')), style=tab0_image_tall_style),
                    html.Img(src='data:image/png;base64,{}'.format(import_image(tab0_image_folder+'/hp3.png')), style=tab0_image_short_style),
                    html.Img(src='data:image/png;base64,{}'.format(import_image(tab0_image_folder+'/hp4.png')), style=tab0_image_short_style),
                    html.Img(src='data:image/png;base64,{}'.format(import_image(tab0_image_folder+'/hp5.png')), style=tab0_image_tall_style),
                    html.Img(src='data:image/png;base64,{}'.format(import_image(tab0_image_folder+'/hp6.png')), style=tab0_image_short_style)
                ],style={'display': 'flex', 'justify-content': 'space-between','padding': '0 60px','margin': '0 -20px','position': 'relative','margin-top':'80px'})
], style={'padding': '0 40px'}) 