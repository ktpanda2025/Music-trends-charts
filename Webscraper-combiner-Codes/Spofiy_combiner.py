

# i need help making a program that accesses Chart_Data_2/Spotify_Weekly_Csv and go through each csv file and add a column called "WeekDate" and add the date of the csv file to the column
# weekdata would be taken from the title of the csv file you can do that by doing this date_components = filename.split('.')[0].split('-')[-3:] then this:  ear, month, day = date_components
# then you can add the date to the dataframe by doing this df['WeekDate'] = pd.to_datetime(f'{year}-{month}-{day}', format='%Y-%m-%d')
# it should combine all the files in one big dataframe

import pandas as pd
import os
directory = "/Users/kevintorres/Desktop/GitHub/Music-trends-charts/Chart_Data_2/Spotify_Weekly_Csv" 

os.listdir(directory)