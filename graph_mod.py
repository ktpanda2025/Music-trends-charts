
import pandas as pd
import plotly.express as px
import plotly.offline as pyo


def Spotify_Chart_Maker(artist_name):


    #how to make the function know only to take in strings
    assert isinstance(artist_name, str), 'Strings only!'

    Spotify_chart = pd.read_csv("Chart_Data_2/Spotify_chart_song_ranks.csv").sort_values(by='WeekDate', ascending=False)
    Spotify_chart ['WeekStartDate'] = pd.to_datetime(Spotify_chart['WeekDate'], format='%Y-%m-%d')
    Spotify_chart = Spotify_chart[['rank', 'artist_names', 'track_name', 'streams', 'WeekDate']]
    Spotify_chart = Spotify_chart [Spotify_chart['rank']<=100 ]
    spotify_chart = Spotify_chart.rename(columns={'artist_names':'artist'})

  
    type_stream = "streams"


    data = spotify_chart[spotify_chart['artist'].str.contains(artist_name, case=False)]


    spotify_groupbysong = data.groupby('track_name').agg(        # this part is for seeing many times song pop up on the charts and it min and max date on it, not on graphs
        Appearances=pd.NamedAgg(column='rank', aggfunc='size'),
        FirstAppearance=pd.NamedAgg(column='WeekDate', aggfunc='min'),
        LastAppearance=pd.NamedAgg(column='WeekDate', aggfunc='max'),
    )

    spotify_groupbysong = spotify_groupbysong.reset_index().sort_values(by='FirstAppearance', ascending=True)


    fig_spot = px.line(data, x='WeekDate', y= "streams", color='track_name',
                title=f'Weekly Streams of Artist songs in the Top 100 for {artist_name} on {"Spotify"}',
                markers=True)  # Add markers to data points


    fig_spot.update_xaxes(title_text='Week')
    fig_spot.update_yaxes(title_text='Streams per Week')

    fig_spot.update_xaxes(rangeslider_visible=True)

    # Show the plot
    return fig_spot.show()

def YT_Chart_Maker(artist_name):
    assert isinstance(artist_name, str), 'Strings only!'
    Song_rank =pd.read_csv("Chart_Data_2/YT_song_rank.csv").sort_values(by='WeekStartDate', ascending=False)
    Song_rank['WeekStartDate'] = pd.to_datetime(Song_rank['WeekStartDate'], format='%Y%m%d')
    Song_rank= Song_rank[Song_rank['WeekStartDate'] >='2020']
    YT_Song_rank = Song_rank.rename(columns={'WeekStartDate':'WeekDate',"SongTitle": 'track_name'})

    data = YT_Song_rank[YT_Song_rank['track_name'].str.contains(artist_name, case=False) | YT_Song_rank['YtChannel'].str.contains(artist_name, case=False)]


    youtube_groupbysong = data.groupby('track_name').agg(  # this part is for seeing many times song pop up on the charts and it min and max date on it, not on graphs
        Appearances=pd.NamedAgg(column='CurrentPosition', aggfunc='size'),
        FirstAppearance=pd.NamedAgg(column='WeekDate', aggfunc='min'),
        LastAppearance=pd.NamedAgg(column='WeekDate', aggfunc='max')
        #DateSpan=pd.NamedAgg(column='WeekDate', aggfunc=lambda x: (x.max() - x.min()).days + 1)
    )


    youtube_groupbysong = youtube_groupbysong.reset_index().sort_values(by='FirstAppearance', ascending=True)



    data['WeekDate'] = pd.to_datetime(YT_Song_rank['WeekDate'], format='Y-m-d')

    fig_YT = px.line(data, x='WeekDate', y= "ViewCount", color='track_name',
                title=f'Weekly Streams of Artist songs in the Top 100 for {artist_name} on {"Youtube"}',
                markers=True)  # Add markers to data points


    fig_YT.update_xaxes(title_text='Week')
    fig_YT.update_yaxes(title_text='Streams per Week')

    fig_YT.update_xaxes(rangeslider_visible=True)
    return fig_YT.show()

# can you help me with my error data['WeekDate'] = pd.to_datetime(Song_rank['WeekDate'], format='Y-m-d')