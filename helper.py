import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from cleaner import *

#################
### helper.py ###
#################

# setup global variables
# TODO - get his and unskipped

#################

#
# plots top (numtracks) songs by a given artist
#
plt.rcParams['figure.figsize'] = [20, 8]
def plotArtist(artistname, numtracks):
    artistdata = unskipped[unskipped['artistName'] == artistname]
    artistdata = artistdata['trackName'].value_counts()
    plt.plot(artistdata.head(numtracks), 'o')
    plt.xticks(rotation = 90)
    plt.title('Most played songs by ' + artistname)
    plt.ylabel('Plays')
    plt.show()

#################

#
# List top n songs
#
# TODO - change to output in the form of 'songPlayCount' function 
def topSongPlays(numsongs):
    int(numsongs)
    print('Your top', numsongs, 'songs: ')
    print('Song                       Plays')
    print(tracks.head(numsongs))
    return(tracks)

#################

#
# Get total playtime (dropping skipped songs)
#
def playtime(his):
    playtime = his['msPlayed'].sum()
    playtime /=  60000
    playtime = int(playtime)
    print("Total minutes listened:", playtime)
    print("Total hours listened:", playtime / 60)
    return(playtime)

#################

# TODO

#
# Get total play count for a given artist
#
def artistPlayCount(artistname):
    plays = unskipped[unskipped['artistName'] == artistname]
    plays = plays.apply(lambda x: x.nunique())
    return plays[0]
    
#
# Get total play count for a given song 
#
def songPlayCount(trackname):
    plays = unskipped[unskipped['trackName'] == trackname]
    plays = plays.apply(lambda x: x.nunique())
    return plays[0]

#################

#
# Get top songs since a date
#
def topSongsTimeframe(timestamp):
    plt.rcParams['figure.figsize'] = [20, 8]
    # convert input into timestamp format
    element = datetime.datetime.strptime(timestamp, "%Y-%m-%d")
    times = unskipped[unskipped['endTime'] >= element]
    temp = times['trackName'].value_counts() 
    plt.plot(temp.head(100), 'o')
    plt.xticks(rotation = 90)
    plt.title('Top Tracks Since ' + timestamp)
    plt.ylabel('Plays')
    plt.show()
    return(temp.head(10))
    
#
# Get top songs between two dates
#
def topSongsTimeframeBounded(lower, upper):
    plt.rcParams['figure.figsize'] = [20, 8]
    element_l = datetime.datetime.strptime(lower, "%Y-%m-%d")
    element_u = datetime.datetime.strptime(upper, "%Y-%m-%d")
    times = unskipped[unskipped['endTime'] >= element_l] 
    times = times[times['endTime'] <= element_u]
    temp = times['trackName'].value_counts() 
    plt.plot(temp.head(100), 'o')
    plt.xticks(rotation = 90)
    plt.title('Top tracks between ' + lower + ' and ' + upper)
    plt.ylabel('Plays')
    plt.show()
    return (temp.head(25))

#
# Get top artists since a data
#
def topArtistsTimeframe(timestamp):
    plt.rcParams['figure.figsize'] = [20, 8]
    element = datetime.datetime.strptime(timestamp, "%Y-%m-%d")
    times = unskipped[unskipped['endTime'] >= element]
    temp = times['artistName'].value_counts()
    plt.plot(temp.head(100), 'o')
    plt.xticks(rotation = 90)
    plt.title('Top Artists Since ' + timestamp)
    plt.ylabel('Plays')
    plt.show()
    return(temp.head(10))

#
# Get top artists between two dates
#
def topArtistsTimeframeBounded(lower, upper):
    plt.rcParams['figure.figsize'] = [20, 8]
    element_l = datetime.datetime.strptime(lower, "%Y-%m-%d")
    element_u = datetime.datetime.strptime(upper, "%Y-%m-%d")
    times = unskipped[unskipped['endTime'] >= element_l]
    times = times[times['endTime'] <= element_u]
    temp = times['artistName'].value_counts()
    plt.plot(temp.head(100), 'o')
    plt.xticks(rotation = 90)
    plt.title('Top Artists Between ' + lower + ' and ' + upper)
    plt.ylabel('Plays')
    plt.show()
    return(temp.head(10))

#################

# TODO - fix end of month bounds

#
# find listening time for a given month
#
def listeningTimeMonth(month_num, year):
    # define bounds for month
    lower = str(year) + "-" + str(month_num) + "-01"
    element_l = datetime.datetime.strptime(lower, "%Y-%m-%d")
    upper = str(year) + "-" + str(month_num) + "-31"
    element_u = datetime.datetime.strptime(upper, "%Y-%m-%d")
    
    # narrow data to fit parameters
    df_params = unskipped[unskipped['endTime'] >= element_l]
    df_params = df_params[df_params['endTime'] <= element_u]
    total = df_params['msPlayed'].sum()
    #calculate hours listened
    total = total / 1000 / 60 / 60
    
    return(total)

#################

#
# Get the listening time for an individual artist
#
def listeningTimeArtist(artist):
    df_params = unskipped[unskipped['artistName'] == artist]
    return(df_params['msPlayed'].sum() / 1000 / 60 / 60)