import dash
from dash import html, dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
from dash import dash_table
import pandas as pd
import random
import base64

# from tabs.tab_blank.tab_blank_div import tab_blank_layout

# import os,sys
# src_dir_h2 = os.path.abspath(os.path.join(os.path.dirname(__file__), '..','..'))
# sys.path.append(src_dir_h2)

from unique_years_list import years_sorted
from inputs import name
from image import import_image
from colors import green, grey
from master_df import df_cleaned

from tab0_div import tab0_layout
from tab1_div import tab1_layout
from tab2_div import tab2_layout
from tab2_top5 import artist_dict, song_dict
from tab3_div import tab3_layout
from tab4_div import tab4_layout
from tab4_fun_facts import fun_fact_list
from tab5_div import tab5_layout


external_stylesheets = [dbc.themes.SKETCHY]
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server #in src/app.py


app.layout = html.Div([
    dcc.Tabs(id="tabs", value='tab-0', children=[
        dcc.Tab(label='Homepage', value='tab-0', children=tab0_layout),
        dcc.Tab(label="And That's a Wrap", value='tab-1', children=tab1_layout),
        dcc.Tab(label="High Five", value='tab-2', children=tab2_layout), 
        dcc.Tab(label="In the Name of New Music", value='tab-3', children=tab3_layout),
        dcc.Tab(label="Fun Facts!", value='tab-4', children=tab4_layout),
        dcc.Tab(label="Under Construction", value='tab-5', children=tab5_layout)
    ]),
])
# with open("hp1.png", "rb") as image_file:
#     encoded_string1 = base64.b64encode(image_file.read()).decode('utf-8')

# html.Div([html.Img(src='data:image/png;base64,{}'.format(encoded_string1),style=tab0_image_short_style)])

# @app.callback(
#     [Output("output-tab2", "children"), Output("image-output-tab2", "src")] + [Output(f"button-{year}", "style") for year in years_sorted],
#     [Input(f"button-{year}", "n_clicks") for year in years_sorted]
# )
# def update_output_tab2(*args):
#     ctx = dash.callback_context
#     if ctx.triggered:
#         button_id = ctx.triggered[0]['prop_id'].split('.')[0]
#         button_name = button_id.split('-')[1]
#         clicked_year = int(button_id.split('-')[1])
        
#         artist_to_table = artist_dict[int(button_name)]
#         song_to_table = song_dict[int(button_name)]
#         clicked_index = years_sorted.index(clicked_year)
        

#         button_styles = [{'font-size': '18px', 'padding': '6px 10px','margin-left':'10px','margin-right':'10px'} for _ in args]
#         button_styles[clicked_index] = {'font-size': '18px', 'padding': '6px 10px','margin-left':'10px','margin-right':'10px','backgroundColor': grey}

#         image_src = 'data:image/png;base64,{}'.format(import_image('src/'+f"pic_button-{clicked_year}.jpg"))
        
#         children = html.Div([
#             html.Div([
#                 html.Div([
#                     dash_table.DataTable(
#                         id='table-tab2-1',
#                         columns=[{'name': i, 'id': i} for i in artist_to_table.columns],
#                         data=artist_to_table.to_dict('records'),
#                         style_table={ 'width': '400px', 'align': 'center'},#'overflowX': 'scroll',
#                         style_header={'fontWeight': 'bold', 'fontSize': '14px', 'textAlign': 'center',
#                                       'verticalAlign': 'middle'},
#                         style_cell={'textAlign': 'center', 'verticalAlign': 'middle', 'fontSize': '12px'},
#                         style_cell_conditional=[{
#                             'if': {'column_id': 'Hours Played'},
#                             'width': '110px',
#                         }],
#                         style_data_conditional=[{
#                             'if': {'filter_query': '{Top Artists} = "The 1975"'},
#                             'backgroundColor': '#F9CFD3',
#                             'color': 'black'}],
#                     )
#                 ], style={'display': 'inline-block', 'margin-right': '20px'}),
#                 html.Div([
#                     dash_table.DataTable(
#                         id='table-tab2-2',
#                         columns=[{'name': i, 'id': i} for i in song_to_table.columns],
#                         data=song_to_table.to_dict('records'),
#                         style_table={ 'width': '800px'},
#                         style_header={'fontWeight': 'bold', 'fontSize': '14px', 'textAlign': 'center',
#                                       'verticalAlign': 'middle'},
#                         style_cell={'textAlign': 'center', 'verticalAlign': 'middle', 'fontSize': '12px'},
#                         style_cell_conditional=[
#                             {'if': {'column_id': 'Artist'},
#                              'width': '200px'},
#                             {'if': {'column_id': 'Hours Played'},
#                              'width': '110px'},
#                         ],
#                         style_data_conditional=[{
#                             'if': {'filter_query': "{Artist} = 'The 1975'"},
#                             'backgroundColor': '#F9CFD3',
#                             'color': 'black'}],
#                     )
#                 ], style={'display': 'inline-block'})
#             ], style={'textAlign': 'center'}),
#             html.Br(),
#         ])

#         return [children, image_src] + button_styles

#     default_button_style = {'font-size': '18px', 'padding': '6px 10px', 'margin-left': '10px', 'margin-right': '10px', 'backgroundColor': 'initial', 'background-image': 'none'}
#     return [html.Div(), ''] + [default_button_style.copy() for _ in years_sorted]

import base64

@app.callback(
    [Output("output-tab2", "children"), Output("image-output-tab2", "src")] + [Output(f"button-{year}", "style") for year in years_sorted],
    [Input(f"button-{year}", "n_clicks") for year in years_sorted]
)
def update_output_tab2(*args):
    ctx = dash.callback_context
    if ctx.triggered:
        button_id = ctx.triggered[0]['prop_id'].split('.')[0]
        button_name = button_id.split('-')[1]
        clicked_year = int(button_id.split('-')[1])
        
        artist_to_table = artist_dict[int(button_name)]
        song_to_table = song_dict[int(button_name)]
        clicked_index = years_sorted.index(clicked_year)
        
        button_styles = [{'font-size': '18px', 'padding': '6px 10px','margin-left':'10px','margin-right':'10px'} for _ in args]
        button_styles[clicked_index] = {'font-size': '18px', 'padding': '6px 10px','margin-left':'10px','margin-right':'10px','backgroundColor': grey}

        # Load image data
        with open(f"pic_button-{clicked_year}.jpg", "rb") as image_file:
            encoded_string1 = base64.b64encode(image_file.read()).decode('utf-8')
        image_src = 'data:image/png;base64,{}'.format(encoded_string1)
        
        children = html.Div([
            html.Div([
                html.Div([
                    dash_table.DataTable(
                        id='table-tab2-1',
                        columns=[{'name': i, 'id': i} for i in artist_to_table.columns],
                        data=artist_to_table.to_dict('records'),
                        style_table={ 'width': '400px', 'align': 'center'},#'overflowX': 'scroll',
                        style_header={'fontWeight': 'bold', 'fontSize': '14px', 'textAlign': 'center',
                                      'verticalAlign': 'middle'},
                        style_cell={'textAlign': 'center', 'verticalAlign': 'middle', 'fontSize': '12px'},
                        style_cell_conditional=[{
                            'if': {'column_id': 'Hours Played'},
                            'width': '110px',
                        }],
                        style_data_conditional=[{
                            'if': {'filter_query': '{Top Artists} = "The 1975"'},
                            'backgroundColor': '#F9CFD3',
                            'color': 'black'}],
                    )
                ], style={'display': 'inline-block', 'margin-right': '20px'}),
                html.Div([
                    dash_table.DataTable(
                        id='table-tab2-2',
                        columns=[{'name': i, 'id': i} for i in song_to_table.columns],
                        data=song_to_table.to_dict('records'),
                        style_table={ 'width': '800px'},
                        style_header={'fontWeight': 'bold', 'fontSize': '14px', 'textAlign': 'center',
                                      'verticalAlign': 'middle'},
                        style_cell={'textAlign': 'center', 'verticalAlign': 'middle', 'fontSize': '12px'},
                        style_cell_conditional=[
                            {'if': {'column_id': 'Artist'},
                             'width': '200px'},
                            {'if': {'column_id': 'Hours Played'},
                             'width': '110px'},
                        ],
                        style_data_conditional=[{
                            'if': {'filter_query': "{Artist} = 'The 1975'"},
                            'backgroundColor': '#F9CFD3',
                            'color': 'black'}],
                    )
                ], style={'display': 'inline-block'})
            ], style={'textAlign': 'center'}),
            html.Br(),
        ])

        return [children, image_src] + button_styles

    default_button_style = {'font-size': '18px', 'padding': '6px 10px', 'margin-left': '10px', 'margin-right': '10px', 'backgroundColor': 'initial', 'background-image': 'none'}
    return [html.Div(), ''] + [default_button_style.copy() for _ in years_sorted]



@app.callback(
    Output("output-tab3", "children"),
    [Input('button-Random Song Generator', "n_clicks")]
)
def update_output_tab3(n_clicks):
    if n_clicks:
        random_selection=df_cleaned.sample(n=1)

        random_selection['ts'] = pd.to_datetime(random_selection['ts'])

        random_song = random_selection['master_metadata_track_name']
        random_artist=random_selection['master_metadata_album_artist_name']
        random_date=random_selection['ts'].dt.strftime('%m/%d/%Y')
        random_time=random_selection['ts'].dt.strftime('%H:%M')

        song_details_1 = f"{name} recommends you listen to "
        song_details_2= f'{random_song.iloc[0]}'
        song_details_3= ' by '
        song_details_4= f'{random_artist.iloc[0]}'
        song_details_5='.'
        song_details_6= f"  Btw, {name} played this song on {random_date.iloc[0]} at {random_time.iloc[0]}!"
        song_details_7=f'Pleaseeee...give {name} new music reccs to replace The 1975 with.'
    
        if random_artist.iloc[0]=='The 1975':
            return html.Div([
                html.Span(song_details_1),
                html.Span(song_details_2,style={'background':green,'font-weight':'boldest'}),
                html.Span(song_details_3),
                html.Span(song_details_4,style={'background':green,'font-weight':'boldest'}),  
                html.Span(song_details_5),  
                html.Span(song_details_6),
                html.Div([song_details_7],style={'margin-top':'5px'}),  
                ],style={'text-align':'center'})
        else:
            return html.Div([
                html.Span(song_details_1),
                html.Span(song_details_2,style={'background':green,'font-weight':'boldest'}),
                html.Span(song_details_3),
                html.Span(song_details_4,style={'background':green,'font-weight':'boldest'}),  
                html.Span(song_details_5),  
                html.Span(song_details_6),  
                ],style={'text-align':'center'})
    return None


@app.callback(
    Output("output-tab4", "children"),
    [Input('button-Fun Facts HERE', "n_clicks")]
)
def update_output_tab4(n_clicks):

    if n_clicks:
        random_fun_fact=random.choice(fun_fact_list)
        return html.Div(random_fun_fact,style={'text-align': 'center','margin-top':'10px'})

    return None


print('ran')

if __name__ == "__main__":
    app.run_server(debug=True) #host='0.0.0.0', port=8050)
    