import pandas as pd
import os
dfs = []
directory = "Chart_Data_2/Spotify_Weekly_Csv"
# Iterate through files in the directory
for filename in os.listdir(directory):
    if filename.endswith('.csv'):
        df = pd.read_csv(os.path.join(directory, filename))

        date_components = filename.split('.')[0].split('-')[-3:]
        year, month, day = date_components

        df['WeekDate'] = pd.to_datetime(f'{year}-{month}-{day}', format='%Y-%m-%d')

        dfs.append(df)

result_df = pd.concat(dfs, ignore_index=True)
result_df.to_csv('Chart_Data_2/Spotify_chart_song_ranks.csv',index = False)
