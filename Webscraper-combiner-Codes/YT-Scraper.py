
from datetime import datetime, timedelta
from lxml import html
import requests
import re




def fetch_top_songs(end_date, chart_type, country_code="us"):
    """This is the return the html of the youtubechart
        chart types are : VIDEOS, ARTIST, TRACKS"""

    response = requests.get("https://charts.youtube.com")

    # Extracting API key using regex
    key_regex = re.compile(r"\"INNERTUBE_API_KEY\"\s*:\s*\"(.*?)\"", re.MULTILINE)
    api_key_match = key_regex.search(response.text)

    if not api_key_match:
        print("Error: Unable to find API key.")
        return None

    api_key = api_key_match.group(1)

    post_url = f"https://charts.youtube.com/youtubei/v1/browse?alt=json&key={api_key}"

    headers = {
        "referer": "https://charts.youtube.com",
    }

    data = {
        "context": {
            "client": {
                "clientName": "WEB_MUSIC_ANALYTICS",
                "clientVersion": "0.2",
                "hl": "en",
                "gl": "en",
                "experimentIds": [],
                "experimentsToken": "",
                "theme": "MUSIC",
            },
            "capabilities": {},
            "request": {
                "internalExperimentFlags": [],
            },
        },
        "browseId": "FEmusic_analytics_charts_home",
        "query": f"perspective=CHART_DETAILS&chart_params_country_code={country_code}&chart_params_chart_type={chart_type}&chart_params_period_type=WEEKLY&chart_params_end_date={end_date}"
    }

    response = requests.post(post_url, json=data, headers=headers)
    return response




#code to find the dates for the url
#although give me the last date of the segment week.
#so the url needs 9/10 that means it is the week 9/4 - 9/10

def get_dates_until_current(start_date):
    date_format = "%Y%m%d"
    current_date = datetime.strptime(start_date, date_format)
    current_date_str = datetime.now().strftime(date_format)

    dates_list = [current_date_str]

    while current_date < datetime.now():
        current_date += timedelta(days=7)
        if current_date <= datetime.now():
            current_date_str = current_date.strftime(date_format)
            dates_list.append(current_date_str)

    return dates_list
