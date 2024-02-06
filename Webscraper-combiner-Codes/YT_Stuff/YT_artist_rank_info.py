# artist scraper
from YT_Scraper import  get_dates_until_current, fetch_top_songs
import json
import pandas as pd

start_date = "20170921"
dates = get_dates_until_current(start_date)

data_list = []

for week_start_date in dates[1:]:
    response = fetch_top_songs(week_start_date, "ARTISTS")
    top_artist_data_week = response.json()["contents"]['sectionListRenderer']['contents'][0]['musicAnalyticsSectionRenderer']['content']['artists'][0]['artistViews']

    for artist in top_artist_data_week:
        # Append the aggregated data for the current artist to the main list
        data_list.append({
            'Name': artist['name'],
            'ViewCount': artist['viewCount'],
            'CurrentPosition': artist['chartEntryMetadata']['currentPosition'],
            'WeekStartDate': week_start_date  # Add the week start date
        })


yt_ranks = pd.DataFrame(data_list)
yt_ranks.to_csv("Chart_Data_2/YT_artist_rank.csv", index=False)