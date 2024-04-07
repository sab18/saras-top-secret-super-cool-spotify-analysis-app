from dash import html

card_style = {
    'border': '1px solid #ccc',
    'border-radius': '5px',
    'padding': '10px',
    'margin': '10px',
    'width': '320px',  
    'box-shadow': '0 4px 8px 0 rgba(0,0,0,0.2)',
    #'margin-top':'200px',  # Add a shadow effect
}

tab5_layout = html.Div([
    html.Div([
        html.H4('Coming to screen near you!',style={'font-weight':'bold'}),
        html.Div('A way for you to recommend songs to me, a suggestions box for the webapp, a search engine to see if I listened to a specific song, most played song given selected dates, and anything else you think would be cool.  Send me what else would be cool to see and I will incorporate it into the webapp!!'),
        #html.Div('Send me what else would be cool to see!!'),
        html.Div(id="output-tab5")
        ],style=card_style),   
],style={"display": "flex", "justifyContent": "center", "alignItems": "center"})