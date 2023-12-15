from sys import platform

if "win" in platform: #check if it's windows, ex: it could be win32 or win64
    import vlc
    import os
    import time

    vlc_player = vlc.MediaPlayer() 
    medianame = "bigbuckbunny x265.mp4"
    mediapath = os.path.join(os.path.dirname(__file__), medianame)
    media = vlc.Media(mediapath)
    vlc_player.set_media(media)
    vlc_player.play()
    offset = 5
    time.sleep(offset)
    length = vlc_player.get_length() #time in ms (divide by 1000 to get in seconds)
    newoffset = length/1000 - offset
    time.sleep(newoffset)
if "darwin" in platform:
    #vlc has a problem with mac displaying, see
    #problem description: https://github.com/PySimpleGUI/PySimpleGUI/issues/5581
    #solution: https://stackoverflow.com/a/75022685
    import vlc
    import os
    import time

    vlc_player = vlc.MediaPlayer() 
    medianame = "bigbuckbunny x265.mp4"
    mediapath = os.path.join(os.path.dirname(__file__), medianame)
    media = vlc.Media(mediapath)
    vlc_player.set_media(media)
    vlc_player.play()
    offset = 5
    time.sleep(offset)
    length = vlc_player.get_length() #time in ms (divide by 1000 to get in seconds)
    newoffset = length/1000 - offset
    time.sleep(newoffset)

