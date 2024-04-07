# import os
# import pandas as pd

# # Define the directory where your JSON files are located
# directory = '/Users/sab/Desktop/saras-top-secret-super-cool-spotify-analysis-app/src'

# # Initialize an empty list to store DataFrames
# dfs = []

# # Iterate through all files in the directory
# for filename in os.listdir(directory):
#     if filename.endswith('.json'):
#         # Construct the full file path
#         filepath = os.path.join(directory, filename)
        
#         # Read the JSON file into a DataFrame and append to the list
#         df= pd.read_json(filepath)
#         dfs.append(df)

# # Concatenate all DataFrames in the list into one large DataFrame
# df_master = pd.concat(dfs, ignore_index=True)
# df_cleaned=df_master.loc[:,['ts','ms_played','master_metadata_track_name','master_metadata_album_artist_name','conn_country','skipped','incognito_mode','reason_start']]

# print('df cleaned')
# print(df_cleaned.head(10))
# Now you have one large DataFrame containing data from all JSON files
#print(df_master.head())



import pandas as pd

# import os, sys
# src_dir_h2 = os.path.abspath(os.path.join(os.path.dirname(__file__),'..','..'))
# sys.path.append(src_dir_h2)

# src_dir_h1 = os.path.abspath(os.path.join(os.path.dirname(__file__),'..'))
# sys.path.append(src_dir_h1)

from get_data_funct import get_df

data='full'  #'subset' or 'full'


if data=='subset':

    # folder_name='src/data/raw_mini'
    # h0=get_df('Streaming_History_Audio_2013-2017_0.json',folder_name)
    # h1=get_df('Streaming_History_Audio_2017-2018_1.json',folder_name)  
    # h2=get_df('Streaming_History_Audio_2018-2019_2.json',folder_name)  
    # h3=get_df('Streaming_History_Video_2016-2024.json',folder_name)
    # df_master = pd.concat([h0,h1,h2,h3], ignore_index=True)
    folder_name='src/data/raw_data'
    h0=get_df('Streaming_History_Audio_2013-2017_0.json',folder_name)
    df_master = pd.concat([h0], ignore_index=True)

elif data=='full':

    folder_name='src'
    h0=get_df('Streaming_History_Audio_2013-2017_0.json',folder_name)
    h1=get_df('Streaming_History_Audio_2017-2018_1.json',folder_name)
    h2=get_df('Streaming_History_Audio_2018-2019_2.json',folder_name)  
    h3=get_df('Streaming_History_Audio_2019-2020_3.json',folder_name)  
    h4=get_df('Streaming_History_Audio_2020_4.json',folder_name)  
    h5=get_df('Streaming_History_Audio_2020-2021_5.json',folder_name)  
    h6=get_df('Streaming_History_Audio_2021_6.json',folder_name)  
    h7=get_df('Streaming_History_Audio_2021-2022_7.json',folder_name)  
    h8=get_df('Streaming_History_Audio_2022_8.json',folder_name)  
    h9=get_df('Streaming_History_Audio_2022-2023_9.json',folder_name)  
    h10=get_df('Streaming_History_Audio_2023_10.json',folder_name)  
    h11=get_df('Streaming_History_Audio_2023_11.json',folder_name)  
    h12=get_df('Streaming_History_Audio_2023-2024_12.json',folder_name)  
    df_master = pd.concat([h0,h1,h2,h3,h4,h5,h6,h7,h8,h9,h10,h11,h12], ignore_index=True)


df_cleaned=df_master.loc[:,['ts','ms_played','master_metadata_track_name','master_metadata_album_artist_name','conn_country','skipped','incognito_mode','reason_start']]
print('clean df successful')
#print(df_cleaned.head())


