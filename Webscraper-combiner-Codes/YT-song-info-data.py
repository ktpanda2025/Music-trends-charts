from YT-Scraper import get_dates_until_current, fetch_top_songs
import json
import pandas as pd


# Example: Starting date is 20170921
start_date = "20170921"
dates = get_dates_until_current(start_date)




data_list = []


for week_start_date in dates[1:]:
    response = fetch_top_songs(week_start_date, "TRACKS")
    top_song_data = response.json()["contents"]['sectionListRenderer']['contents'][0]['musicAnalyticsSectionRenderer']['content']['trackTypes'][0]['trackViews']

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
