import numpy as np
from Backend import appleMusic, spotify, youtube


"""""input: str from_platform - what platform the playlist is from
            str to_platform - on what platform should the output playlist be
            str playlist_link - link to the playlist (the one that should be copied)
     output: str output_link - link to playlist in the requested platform """""


def convert_playlist(from_platform, to_platform, playlist_link):
    # input check
    if type(from_platform) != type(to_platform) != type(playlist_link) or type(from_platform) != str:
        pass
    else:
        raise "wrong input type, convert_playlist should only get strings"

    # Turn the playlist link into an array of song names to be used later
    song_array = link_to_array(from_platform)

    # Turn the array of songs to a playlist on the required platform
    output_playlist = array_to_link(to_platform, song_array)

    return output_playlist


# Turn the playlist link into an array of song names to be used later
def link_to_array(from_platform):
    song_array = np.ndarray
    if from_platform == 'spotify':
        # song_array = spotify.playlist_to_array(playlist_link)
        pass
    elif from_platform == 'apple_music':
        # song_array = appleMusic.playlist_to_array(playlist_link)
        pass
    elif from_platform == 'youtube':
        # song_array = spotify.playlist_to_array(playlist_link)
        pass
    else:
        raise "unfitting platform"
    return song_array


# Turn the array of songs to a playlist on the required platform
def array_to_link(to_platform, song_array):
    output_playlist = ''
    if to_platform == 'spotify':
        # output_playlist = spotify.array_to_playlist(song_array)
        pass
    elif to_platform == 'apple music':
        # output_playlist = appleMusic.array_to_playlist(song_array)
        pass
    elif to_platform == 'youtube':
        # output_playlist = youtube.array_to_playlist(song_array)
        pass
    else:
        raise "unfitting platform"
    return output_playlist