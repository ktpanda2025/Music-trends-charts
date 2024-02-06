from YT_Scraper import  get_dates_until_current, fetch_top_songs
import json
import pandas as pd

#kill terminal and restart it

start_date = "20170921"
dates = get_dates_until_current(start_date)

print(dates)


data_list = []


for week_start_date in dates[1:]:
    response = fetch_top_songs(week_start_date, "TRACKS")
    top_song_data = response.json()["contents"]['sectionListRenderer']['contents'][0]['musicAnalyticsSectionRenderer']['content']['trackTypes'][0]['trackViews']
    print("fdfdfdfdfdf")
    for song in  top_song_data:
      
        try:
            # Try to access 'title' key in vid_2 since some videos have been taken down
            song_vid_title = song['name']
        except KeyError:
            # If 'title' key is not present, skip to the next iteration
            continue

        # Append the aggregated data for the current artist to the main list
        data_list.append({
            'SongTitle': song_vid_title,
            'ViewCount': song['viewCount'],
            'CurrentPosition': song['chartEntryMetadata']['currentPosition'],
            'WeekStartDate': week_start_date,  # Add the week start date
            'YtChannel': ",".join(n["name"] for n in song['artists'])
        })

YT_song_rank = pd.DataFrame(data_list)
YT_song_rank.to_csv("Chart_Data_2/YT_song_rank.csv", index=False)

