import pandas as pd
import numpy as np

from dash import dash_table
from dash import dcc, html

# import os, sys
# src_dir_h2 = os.path.abspath(os.path.join(os.path.dirname(__file__),'..','..'))
# sys.path.append(src_dir_h2)

from master_df import df_cleaned
from inputs import name


#print(df_cleaned.head())

def top_5_artists():
    by_artist = df_cleaned.groupby('master_metadata_album_artist_name')['ms_played'].sum()/1000/60/60
    top_artists= by_artist.sort_values(ascending=False)
    #print(top_artists)
    df_top_artists=pd.DataFrame(top_artists)
    
    df_top_artists.reset_index(inplace=True)
    df_top_artists.index=df_top_artists.index+1
    df_top_artists=df_top_artists.rename(columns={'master_metadata_album_artist_name':'Artist','ms_played':'Hours Played'})
    df_top_artists['Hours Played']=np.ceil(df_top_artists['Hours Played']).astype(int)
    df_top_5_artists=df_top_artists.head(5)
    top5_artists=df_top_5_artists['Artist'].values

    part1=(', '.join(top5_artists[:-1]))
    part2=top5_artists[-1]

    return (f"{name}'s top 5 artists of all time are {part1}, and {part2}.")


def total_songs():
    total_unique_songs=df_cleaned['master_metadata_track_name'].nunique()
    return f'{name} has played {total_unique_songs} unique songs on Spotify.'

def top10_songs():
    by_song = df_cleaned.groupby(['master_metadata_track_name','master_metadata_album_artist_name'])['ms_played'].sum()/1000/60/60
    top_songs= by_song.sort_values(ascending=False)
    df_top_songs=pd.DataFrame(top_songs)
    
    df_top_songs.reset_index(inplace=True)
    df_top_songs.index=df_top_songs.index+1
    df_top_songs=df_top_songs.rename(columns={'master_metadata_track_name':'Song','master_metadata_album_artist_name':'Artist','ms_played':'Hours Played'})
    df_top_songs['Hours Played']=np.ceil(df_top_songs['Hours Played']).astype(int)
    df_top_10_songs=df_top_songs.head(10)
    #return df_top_10_songs
    return html.Div([
        html.Div(f"{name}'s top 10 songs of all time on Spotify are:", style={'text-align': 'center'}),
        html.Div([
            dash_table.DataTable(
                id='table-tab4-1',
                columns=[{'name': i, 'id': i} for i in df_top_10_songs.columns],
                data=df_top_10_songs.to_dict('records'),
                style_table={'width': '600px', 'margin': 'auto'},  # Center the table using margin: auto
                style_header={'fontWeight': 'bold', 'fontSize': '14px', 'textAlign': 'center', 'verticalAlign': 'middle'},
                style_cell={'textAlign': 'center', 'verticalAlign': 'middle', 'fontSize': '12px'}
            ),
        ], style={'margin-top':'15px','text-align': 'center'})
    ])

                

def total_listening_time():
    total_listening = df_cleaned['ms_played'].sum()/1000/60/60
    total_listening=np.ceil(total_listening).astype(int)
    return f'{name} has spent {total_listening} cumulative hours listening to music on Spotify.'


def first_song():
    first_song=df_cleaned.loc[df_cleaned['ts'] == df_cleaned['ts'].min()]
    return f"The first song {name} played on spotify was {first_song['master_metadata_track_name'].iloc[0]} by {first_song['master_metadata_album_artist_name'].iloc[0]} in {pd.to_datetime(first_song['ts']).dt.year[0]}."

#print(top_5_artists())
def top10_songs_no1975():
    df_cleaned_no1975 = df_cleaned[df_cleaned['master_metadata_album_artist_name'] !='The 1975']
    by_song = df_cleaned_no1975.groupby(['master_metadata_track_name','master_metadata_album_artist_name'])['ms_played'].sum()/1000/60/60
    top_songs= by_song.sort_values(ascending=False)
    df_top_songs=pd.DataFrame(top_songs)
    
    df_top_songs.reset_index(inplace=True)
    df_top_songs.index=df_top_songs.index+1
    df_top_songs=df_top_songs.rename(columns={'master_metadata_track_name':'Song','master_metadata_album_artist_name':'Artist','ms_played':'Hours Played'})
    df_top_songs['Hours Played']=np.ceil(df_top_songs['Hours Played']).astype(int)
    df_top_10_songs=df_top_songs.head(10)
    #return df_top_10_songs
    return html.Div([
        html.Div(f"{name}'s top 10 songs of all time on Spotify minus 1975 songs are:", style={'text-align': 'center'}),
        html.Div([
            dash_table.DataTable(
                id='table-tab4-1',
                columns=[{'name': i, 'id': i} for i in df_top_10_songs.columns],
                data=df_top_10_songs.to_dict('records'),
                style_table={'width': '700px', 'margin': 'auto'},  # Center the table using margin: auto
                style_header={'fontWeight': 'bold', 'fontSize': '14px', 'textAlign': 'center', 'verticalAlign': 'middle'},
                style_cell={'textAlign': 'center', 'verticalAlign': 'middle', 'fontSize': '12px'}
            ),
        ], style={'margin-top':'15px','text-align': 'center'})
    ])

def top5_songs_senior_hs():
    hs_start = '2017-09-01T00:00:00Z'
    hs_end ='2018-05-22T23:59:59Z'
    df_top5_hs= df_cleaned[(df_cleaned['ts'] >= hs_start) & (df_cleaned['ts'] <= hs_end)]
    

    by_song = df_top5_hs.groupby(['master_metadata_track_name','master_metadata_album_artist_name'])['ms_played'].sum()/1000/60/60
    top_songs= by_song.sort_values(ascending=False)
    df_top_songs=pd.DataFrame(top_songs)
    
    df_top_songs.reset_index(inplace=True)
    df_top_songs.index=df_top_songs.index+1
    df_top_10_songs2=df_top_songs.head(3)
    top5_songs2=df_top_10_songs2['master_metadata_track_name'].values
    top5_artists2=df_top_10_songs2['master_metadata_album_artist_name'].values

    part3 = ', '.join([f'{song} by {artist}' for song, artist in zip(top5_songs2[:-1], top5_artists2[:-1])])
    part4 = f'{top5_songs2[-1]} by {top5_artists2[-1]}'

    return f"The songs that ruled {name}'s senior year of high school were {part3}, and {part4}."

    # need to make customizable... TO DO FIX FINISH
def unique_countries():

    countries_list = df_cleaned['conn_country'].unique()
    return f"{name} has played music on Spotify in the US and Canada."


def percent_1975():
    total_songs = len(df_cleaned)
    the1975_songs=df_cleaned[df_cleaned['master_metadata_album_artist_name'] == 'The 1975'].shape[0]
    the1975_percent=(the1975_songs/total_songs)*100
    return f"{the1975_percent:.0f}% of {name}'s entire listening history has been 1975 songs."


#finish this!
def most_skipped():
    skipped_songs = df_cleaned[df_cleaned['skipped']== True]
    skipped_song_counts = skipped_songs['master_metadata_track_name'].value_counts()
    most_skipped_song = skipped_song_counts.idxmax()
    highest_skip_count = skipped_song_counts.max()
    artist = df_cleaned[df_cleaned['master_metadata_track_name'] == most_skipped_song]['master_metadata_album_artist_name'].iloc[0]

    return f"{name}'s most skipped song is {most_skipped_song} by {artist} at {highest_skip_count} skips."



def most_seek_play():
    clicked_songs = df_cleaned[df_cleaned['reason_start'] == 'clickrow']
    clicked_song_count = clicked_songs['master_metadata_track_name'].value_counts()
    most_clicked_song = clicked_song_count.idxmax()
    artist = df_cleaned[df_cleaned['master_metadata_track_name'] == most_clicked_song]['master_metadata_album_artist_name'].iloc[0]

    return f"The song that {name} has chosen to play the most (ie. not played via shuffle or skipped to), is {most_clicked_song} by {artist}."





# def top_repeated_songs():
#     # Initialize variables to store the current song and its repetition count
#     current_song = None
#     current_repetitions = 0

#     # Initialize a dictionary to store the repetition count for each song
#     song_repetitions = {}

#     # Iterate through the DataFrame
#     for index, row in df_cleaned.iterrows():
#         song = row['master_metadata_track_name']
#         artist = row['master_metadata_album_artist_name']

#         # Check if the current song is the same as the previous one
#         if song == current_song:
#             current_repetitions += 1
#         else:
#             # Update repetition count for the previous song
#             if current_song is not None:
#                 song_repetitions[current_song] = current_repetitions

#             # Start counting repetitions for the new song
#             current_song = song
#             current_repetitions = 1

#     # Update repetition count for the last song
#     if current_song is not None:
#         song_repetitions[current_song] = current_repetitions

#     # Sort songs by repetition count in descending order
#     sorted_songs = sorted(song_repetitions.items(), key=lambda x: x[1], reverse=True)

#     # Get the top 3 repeated songs and their repetition counts
#     top_repeated = sorted_songs[:3]

#     result = "Sara's most repeated songs are:\n"
#     # Print the results
#     for song, repetitions in top_repeated:
#         artist = df_cleaned[df_cleaned['master_metadata_track_name'] == song]['master_metadata_album_artist_name'].iloc[0]
#         result += f"- {song} by {artist} ({repetitions} repeats)\n"
#     return result
# # Call the function with your DataFrame df_cleaned
# #print(top_repeated_songs())

def top_3_consecutive_repeated_songs():
    current_song = None
    top_songs = []
    top_repetitions = []

    for index, row in df_cleaned.iterrows():
        song = row['master_metadata_track_name']

        if song == current_song:
            top_repetitions[-1] += 1
        else:
            current_song = song
            top_songs.append(song)
            top_repetitions.append(1)

    sorted_songs_repetitions = sorted(zip(top_songs, top_repetitions), key=lambda x: x[1], reverse=True)
    top_3_songs = []
    top_3_repetitions = []
    for song, repetitions in sorted_songs_repetitions:
        if song not in top_3_songs:
            top_3_songs.append(song)
            top_3_repetitions.append(repetitions)
        if len(top_3_songs) >= 3:
            break

    top_3_artists = []
    for song in top_3_songs:
        artist = df_cleaned[df_cleaned['master_metadata_track_name'] == song]['master_metadata_album_artist_name'].iloc[0]
        top_3_artists.append(artist)


    if len(top_3_songs) < 3 and len(sorted_songs_repetitions) >= 3:
        song, repetitions = sorted_songs_repetitions[3]
        if song not in top_3_songs:
            top_3_songs.append(song)
            top_3_repetitions.append(repetitions)
            artist = df_cleaned[df_cleaned['master_metadata_track_name'] == song]['master_metadata_album_artist_name'].iloc[0]
            top_3_artists.append(artist)

    result=f"{name}'s most repeated songs are:\n"
    for song, artist, repetitions in zip(top_3_songs, top_3_artists, top_3_repetitions):
        result += f"- {song} by {artist} ({repetitions} repeats)\n"
    return result

def most_incognito():

    incognito_songs = df_cleaned[df_cleaned['incognito_mode']== True]
    incognito_songs_counts = incognito_songs['master_metadata_track_name'].value_counts()
    most_incognito_song = incognito_songs_counts.idxmax()
    artist = df_cleaned[df_cleaned['master_metadata_track_name'] == most_incognito_song ]['master_metadata_album_artist_name'].iloc[0]

    return f"{most_incognito_song} by {artist} is the song {name} has played the most on a private listening session."


fun_fact_list=[top_5_artists(),total_songs(), top10_songs(),total_listening_time(),top10_songs_no1975(),top5_songs_senior_hs(),unique_countries(),percent_1975(),most_skipped(),most_seek_play(),top_3_consecutive_repeated_songs(),most_incognito()]


