from master_df import df_cleaned
print(df_cleaned.head())


import pandas as pd


# Define name variable
name = "User"

# Define first_song function
# def first_song():
#     first_song = df_cleaned.loc[df_cleaned['ts'] == df_cleaned['ts'].min()]
#     return f"The first song {name} played on Spotify was {first_song['master_metadata_track_name'].iloc[0]} by {first_song['master_metadata_album_artist_name'].iloc[0]} in {pd.to_datetime(first_song['ts']).dt.year[0]}."
# def first_song():
#     first_song=df_cleaned.loc[df_cleaned['ts'] == df_cleaned['ts'].min()]
#     return f"The first song {name} played on spotify was {first_song['master_metadata_track_name'].iloc[0]} by {first_song['master_metadata_album_artist_name'].iloc[0]} in {pd.to_datetime(first_song['ts']).dt.year[0]}."
def first_song():
    print(df_cleaned.loc[df_cleaned['ts'] == df_cleaned['ts'].min()])  # Debug print
    first_song = df_cleaned.loc[df_cleaned['ts'] == df_cleaned['ts'].min()]
    return f"The first song {name} played on Spotify was {first_song['master_metadata_track_name'].iloc[0]} by {first_song['master_metadata_album_artist_name'].iloc[0]} in {pd.to_datetime(first_song['ts']).dt.year[0]}."

# Call first_song function
print(first_song())



# print(df_cleaned.head())  # Print the first few rows of the DataFrame
# print(df_cleaned['ts'].min())  # Print the minimum timestamp to verify if it's correctly extracted

# Call first_song function
# print(first_song())
