
# directory = '/Users/sab/Desktop/saras-top-secret-super-cool-spotify-analysis-app/src'

# Define the directory where your JSON files are located


import pandas as pd
import os

# df_cleaned = pd.read_json('src/Streaming_History_Audio_2013-2017_0.json')
# df_cleaned=df_cleaned.head()
# print(df_cleaned)
# print('df created')

file_names = ['Streaming_History_Audio_2013-2017_0.json',
              'Streaming_History_Audio_2017-2018_1.json'
              'Streaming_History_Audio_2018-2019_2.json',
              'Streaming_History_Audio_2019-2020_3.json',
              'Streaming_History_Audio_2020_4.json',
              'Streaming_History_Audio_2020-2021_5.json',
              'Streaming_History_Audio_2021_6.json',
              'Streaming_History_Audio_2021-2022_7.json',
              'Streaming_History_Audio_2022_8.json',
              'Streaming_History_Audio_2022-2023_9.json'
              'Streaming_History_Audio_2023_10.json',
              'Streaming_History_Audio_2023_11.json',
              'Streaming_History_Audio_2023-2024_12.json']

dfs=[]
for file_name in file_names:

    df = pd.read_json(file_name)
    dfs.append(df)
df_master = pd.concat(dfs)
#lengthh=len(df_cleaned)

df_cleaned=df_master.loc[:,['ts','ms_played','master_metadata_track_name','master_metadata_album_artist_name','conn_country','skipped','incognito_mode','reason_start']]
print('clean df successful')
#print(df_cleaned.head())



# # Assuming you have multiple JSON files named music_data1.json, music_data2.json, etc.
# file_names = ['Streaming_History_Audio_2013-2017_0.json',
#               'Streaming_History_Audio_2017-2018_1.json']
#             #   'Streaming_History_Audio_2018-2019_2.json',
#             #   'Streaming_History_Audio_2019-2020_3.json',
#             #   'Streaming_History_Audio_2020_4.json',
#             #   'Streaming_History_Audio_2020-2021_5.json',
#             #   'Streaming_History_Audio_2021_6.json',
#             #   'Streaming_History_Audio_2021-2022_7.json',
#             #   'Streaming_History_Audio_2022_8.json',
#             #   'Streaming_History_Audio_2022-2023_9.json'
#             #   'Streaming_History_Audio_2023_10.json',
#             #   'Streaming_History_Audio_2023_11.json',
#             #   'Streaming_History_Audio_2023-2024_12.json']



# dfs=[]
# # Iterate through each file
# for file_name in file_names:
#     # Construct the full path to the JSON file
    
    
#     # Read the JSON file into a DataFrame and append it to the list
#     df = pd.read_json(file_name)
#     dfs.append(df)

# Concatenate all DataFrames in the list
# df_master = pd.concat(dfs, ignore_index=True)

# df_cleaned=df_master.loc[:,['ts','ms_played','master_metadata_track_name','master_metadata_album_artist_name','conn_country','skipped','incognito_mode','reason_start']]

# print(len(df_cleaned))

# # Example usage:
# directory = directory = '/Users/sab/Desktop/saras-top-secret-super-cool-spotify-analysis-app/src'
# df_cleaned = load_json_files(directory)

# # print(df_cleaned.head())
# print('df cleaned')


# #_______________________________

# import pandas as pd

# # import os, sys
# # src_dir_h2 = os.path.abspath(os.path.join(os.path.dirname(__file__),'..','..'))
# # sys.path.append(src_dir_h2)

# # src_dir_h1 = os.path.abspath(os.path.join(os.path.dirname(__file__),'..'))
# # sys.path.append(src_dir_h1)

# from get_data_funct import get_df

# data='full'  #'subset' or 'full'


# if data=='subset':

#     # folder_name='src/data/raw_mini'
#     # h0=get_df('Streaming_History_Audio_2013-2017_0.json',folder_name)
#     # h1=get_df('Streaming_History_Audio_2017-2018_1.json',folder_name)  
#     # h2=get_df('Streaming_History_Audio_2018-2019_2.json',folder_name)  
#     # h3=get_df('Streaming_History_Video_2016-2024.json',folder_name)
#     # df_master = pd.concat([h0,h1,h2,h3], ignore_index=True)
#     folder_name='src/data/raw_data'
#     h0=get_df('Streaming_History_Audio_2013-2017_0.json',folder_name)
#     df_master = pd.concat([h0], ignore_index=True)

# elif data=='full':

#     folder_name='src'
#     h0=get_df('Streaming_History_Audio_2013-2017_0.json',folder_name)
#     h1=get_df('Streaming_History_Audio_2017-2018_1.json',folder_name)
#     h2=get_df('Streaming_History_Audio_2018-2019_2.json',folder_name)  
#     h3=get_df('Streaming_History_Audio_2019-2020_3.json',folder_name)  
#     h4=get_df('Streaming_History_Audio_2020_4.json',folder_name)  
#     h5=get_df('Streaming_History_Audio_2020-2021_5.json',folder_name)  
#     h6=get_df('Streaming_History_Audio_2021_6.json',folder_name)  
#     h7=get_df('Streaming_History_Audio_2021-2022_7.json',folder_name)  
#     h8=get_df('Streaming_History_Audio_2022_8.json',folder_name)  
#     h9=get_df('Streaming_History_Audio_2022-2023_9.json',folder_name)  
#     h10=get_df('Streaming_History_Audio_2023_10.json',folder_name)  
#     h11=get_df('Streaming_History_Audio_2023_11.json',folder_name)  
#     h12=get_df('Streaming_History_Audio_2023-2024_12.json',folder_name)  
#     df_master = pd.concat([h0,h1,h2,h3,h4,h5,h6,h7,h8,h9,h10,h11,h12], ignore_index=True)


# df_cleaned=df_master.loc[:,['ts','ms_played','master_metadata_track_name','master_metadata_album_artist_name','conn_country','skipped','incognito_mode','reason_start']]
# print('clean df successful')
# #print(df_cleaned.head())






# __________________________


# import os
# import pandas as pd

# directory = '/Users/sab/Desktop/saras-top-secret-super-cool-spotify-analysis-app/src'

# dfs = []

# for filename in os.listdir(directory):
#     if filename.endswith('.json'):
#         filepath = os.path.join(directory, filename)
#         try:
#             df = pd.read_json(filepath)
#             dfs.append(df)
#             print(f"Processed: {filename}")
#         except Exception as e:
#             print(f"Error reading {filename}: {e}")

# if dfs:
#     df_master = pd.concat(dfs, ignore_index=True)
#     print("Concatenation successful")
#     # Further processing if needed
# else:
#     print("No JSON files found in the directory.")
