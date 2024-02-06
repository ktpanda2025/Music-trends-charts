#music video scraper
from YT_Scraper import  get_dates_until_current, fetch_top_songs
import json
import pandas as pd

#kill terminal and restart it

start_date = "20170921"
dates = get_dates_until_current(start_date)

data_list = []


for week_start_date in dates[1:]:
    response = fetch_top_songs(week_start_date, "VIDEOS")
    top_video_data = response.json()["contents"]['sectionListRenderer']['contents'][0]['musicAnalyticsSectionRenderer']['content']['videos'][0]['videoViews']
    print("hhkhkh")
    for vid_2 in top_video_data:

        try:
            # Try to access 'title' key in vid_2 since some videos have been taken down
            song_vid_title = vid_2['title']
        except KeyError:
            # If 'title' key is not present, skip to the next iteration
            continue

        # Append the aggregated data for the current artist to the main list
        data_list.append({
            'SongVidTitle': song_vid_title,
            'ViewCount': vid_2['viewCount'],
            'CurrentPosition': vid_2['chartEntryMetadata']['currentPosition'],
            'WeekStartDate': week_start_date,  # Add the week start date
            'YtChannel': ",".join(n["name"] for n in vid_2['artists'])
        })

YT_Music_Vid = pd.DataFrame(data_list)
YT_Music_Vid.to_csv("Chart_Data_2/YT_video_rank.csv", index=False)
