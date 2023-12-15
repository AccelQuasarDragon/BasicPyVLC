from sys import platform

if platform == "win32": #https://docs.python.org/3/library/sys.html#sys.platform
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
if platform == "darwin":
    #vlc has a problem with mac displaying, see
    #problem description: https://github.com/PySimpleGUI/PySimpleGUI/issues/5581
    #solution: https://stackoverflow.com/a/75022685
    import vlc
    import os
    import time
    import PySide6.QtWidgets as QtWidgets

    vlc_player = vlc.MediaPlayer() 
    medianame = "bigbuckbunny x265.mp4"
    mediapath = os.path.join(os.path.dirname(__file__), medianame)
    media = vlc.Media(mediapath)
    vlc_player.set_media(media)

    vlcApp = QtWidgets.QApplication([])
    vlcWidget = QtWidgets.QFrame()
    vlcWidget.resize(700,700)
    vlcWidget.show()

    vlc_player.set_nsobject(vlcWidget.winId())
    vlc_player.play() #you need to play vlc first else the qtapp will just open and hold forever
    vlcApp.exec()
