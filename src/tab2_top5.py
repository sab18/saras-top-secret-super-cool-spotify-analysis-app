import pandas as pd


# import os,sys
# src_dir_h2 = os.path.abspath(os.path.join(os.path.dirname(__file__), '..','..'))
# sys.path.append(src_dir_h2)
from master_df import df_cleaned
from unique_years_list import years_sorted

def artist_by_year(year):
    df_by_year = df_cleaned[pd.to_datetime(df_cleaned['ts']).dt.year == year]
    by_artist = df_by_year.groupby('master_metadata_album_artist_name')['ms_played'].sum()/1000/60/60
    top_artists= by_artist.sort_values(ascending=False)
    df_top_artists=pd.DataFrame(top_artists)
    
    df_top_artists.reset_index(inplace=True)
    df_top_artists.index=df_top_artists.index+1
    df_top_artists=df_top_artists.rename(columns={'master_metadata_album_artist_name':'Top Artists','ms_played':'Hours Played'})
    # df_top_artists['Hours Played']=np.ceil(df_top_artists['Hours Played']).astype(int)
    df_top_artists['Hours Played']=round(df_top_artists['Hours Played'],2)
    return df_top_artists.head(5)

def song_by_year(year):
    df_by_year = df_cleaned[pd.to_datetime(df_cleaned['ts']).dt.year == year]
    by_song = df_by_year.groupby(['master_metadata_track_name','master_metadata_album_artist_name'])['ms_played'].sum()/1000/60/60
    top_songs= by_song.sort_values(ascending=False)
    df_top_songs=pd.DataFrame(top_songs)
    
    df_top_songs.reset_index(inplace=True)
    df_top_songs.index=df_top_songs.index+1
    df_top_songs=df_top_songs.rename(columns={'master_metadata_track_name':'Top Songs','master_metadata_album_artist_name':'Artist','ms_played':'Hours Played'})
    # df_top_songs['Hours Played']=np.ceil(df_top_songs['Hours Played']).astype(int)
    df_top_songs['Hours Played']=round(df_top_songs['Hours Played'],2)
    return df_top_songs.head(5)

artist_dict={}
song_dict={}

for year in years_sorted:
   artist_dict[year]=artist_by_year(year)
   song_dict[year]=song_by_year(year)