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
    import os
    import time
    import PySide6.QtWidgets as QtWidgets
    import sys    

    str1 = r'''
def find_lib():
    dll = None
    plugin_path = os.environ.get('PYTHON_VLC_MODULE_PATH', None)
    if 'PYTHON_VLC_LIB_PATH' in os.environ:
        try:
            dll = ctypes.CDLL(os.environ['PYTHON_VLC_LIB_PATH'])
        except OSError:
            logger.error("Cannot load lib specified by PYTHON_VLC_LIB_PATH env. variable")
            sys.exit(1)
    if plugin_path and not os.path.isdir(plugin_path):
        logger.error("Invalid PYTHON_VLC_MODULE_PATH specified. Please fix.")
        sys.exit(1)
    if dll is not None:
        return dll, plugin_path

    if sys.platform.startswith('win'):
        libname = 'libvlc.dll'
        p = find_library(libname)
        if p is None:
            try:  # some registry settings
                # leaner than win32api, win32con
                if PYTHON3:
                    import winreg as w
                else:
                    import _winreg as w
                for r in w.HKEY_LOCAL_MACHINE, w.HKEY_CURRENT_USER:
                    try:
                        r = w.OpenKey(r, 'Software\\VideoLAN\\VLC')
                        plugin_path, _ = w.QueryValueEx(r, 'InstallDir')
                        w.CloseKey(r)
                        break
                    except w.error:
                        pass
            except ImportError:  # no PyWin32
                pass
            if plugin_path is None:
                # try some standard locations.
                programfiles = os.environ["ProgramFiles"]
                homedir = os.environ["HOMEDRIVE"]
                for p in ('{programfiles}\\VideoLan{libname}', '{homedir}:\\VideoLan{libname}',
                          '{programfiles}{libname}',           '{homedir}:{libname}'):
                    p = p.format(homedir = homedir,
                                 programfiles = programfiles,
                                 libname = '\\VLC\\' + libname)
                    if os.path.exists(p):
                        plugin_path = os.path.dirname(p)
                        break
            if plugin_path is not None:  # try loading
                 # PyInstaller Windows fix
                if 'PyInstallerCDLL' in ctypes.CDLL.__name__:
                    ctypes.windll.kernel32.SetDllDirectoryW(None)
                p = os.getcwd()
                os.chdir(plugin_path)
                 # if chdir failed, this will raise an exception
                dll = ctypes.CDLL('.\\' + libname)
                 # restore cwd after dll has been loaded
                os.chdir(p)
            else:  # may fail
                dll = ctypes.CDLL('.\\' + libname)
        else:
            plugin_path = os.path.dirname(p)
            dll = ctypes.CDLL(p)

    elif sys.platform.startswith('darwin'):
        # FIXME: should find a means to configure path
        d = '/Applications/VLC.app/Contents/MacOS/'
        c = d + 'lib/libvlccore.dylib'
        p = d + 'lib/libvlc.dylib'
        if os.path.exists(p) and os.path.exists(c):
            # pre-load libvlccore VLC 2.2.8+
            ctypes.CDLL(c)
            dll = ctypes.CDLL(p)
            for p in ('modules', 'plugins'):
                p = d + p
                if os.path.isdir(p):
                    plugin_path = p
                    break
        else:  # hope, some [DY]LD_LIBRARY_PATH is set...
            # pre-load libvlccore VLC 2.2.8+
            ctypes.CDLL('libvlccore.dylib')
            dll = ctypes.CDLL('libvlc.dylib')

    else:
        # All other OSes (linux, freebsd...)
        p = find_library('vlc')
        try:
            dll = ctypes.CDLL(p)
        except OSError:  # may fail
            dll = None
        if dll is None:
            try:
                dll = ctypes.CDLL('libvlc.so.5')
            except:
                raise NotImplementedError('Cannot find libvlc lib')

    return (dll, plugin_path)
'''

    str2 = r'''
def find_lib():
    dll = None
    plugin_path = os.environ.get('PYTHON_VLC_MODULE_PATH', None)
    if 'PYTHON_VLC_LIB_PATH' in os.environ:
        try:
            dll = ctypes.CDLL(os.environ['PYTHON_VLC_LIB_PATH'])
        except OSError:
            logger.error("Cannot load lib specified by PYTHON_VLC_LIB_PATH env. variable")
            sys.exit(1)
    if plugin_path and not os.path.isdir(plugin_path):
        logger.error("Invalid PYTHON_VLC_MODULE_PATH specified. Please fix.")
        sys.exit(1)
    if dll is not None:
        return dll, plugin_path

    if sys.platform.startswith('win'):
        libname = 'libvlc.dll'
        p = find_library(libname)
        if p is None:
            try:  # some registry settings
                # leaner than win32api, win32con
                if PYTHON3:
                    import winreg as w
                else:
                    import _winreg as w
                for r in w.HKEY_LOCAL_MACHINE, w.HKEY_CURRENT_USER:
                    try:
                        r = w.OpenKey(r, 'Software\\VideoLAN\\VLC')
                        plugin_path, _ = w.QueryValueEx(r, 'InstallDir')
                        w.CloseKey(r)
                        break
                    except w.error:
                        pass
            except ImportError:  # no PyWin32
                pass
            if plugin_path is None:
                # try some standard locations.
                programfiles = os.environ["ProgramFiles"]
                homedir = os.environ["HOMEDRIVE"]
                for p in ('{programfiles}\\VideoLan{libname}', '{homedir}:\\VideoLan{libname}',
                          '{programfiles}{libname}',           '{homedir}:{libname}'):
                    p = p.format(homedir = homedir,
                                 programfiles = programfiles,
                                 libname = '\\VLC\\' + libname)
                    if os.path.exists(p):
                        plugin_path = os.path.dirname(p)
                        break
            if plugin_path is not None:  # try loading
                 # PyInstaller Windows fix
                if 'PyInstallerCDLL' in ctypes.CDLL.__name__:
                    ctypes.windll.kernel32.SetDllDirectoryW(None)
                p = os.getcwd()
                os.chdir(plugin_path)
                 # if chdir failed, this will raise an exception
                dll = ctypes.CDLL('.\\' + libname)
                 # restore cwd after dll has been loaded
                os.chdir(p)
            else:  # may fail
                dll = ctypes.CDLL('.\\' + libname)
        else:
            plugin_path = os.path.dirname(p)
            dll = ctypes.CDLL(p)

    elif sys.platform.startswith('darwin'):
        d = sys._MEIPASS
        c = os.path.join(d, "libvlccore.dylib")
        p = os.path.join(d, "libvlc.dylib")
        print("paths exists and loaded?", c, p, os.path.exists(p), os.path.exists(c))
        if os.path.exists(p) and os.path.exists(c):
            # pre-load libvlccore VLC 2.2.8+
            ctypes.CDLL(c)
            dll = ctypes.CDLL(p)
            for p in ('modules', 'plugins'):
                p = os.path.join(d, p)
                print("newp?", p)
                if os.path.isdir(p):
                    plugin_path = p
                    print("pluginpath", plugin_path, os.path.exists(plugin_path))
                    break
        else:  # hope, some [DY]LD_LIBRARY_PATH is set...
            # pre-load libvlccore VLC 2.2.8+
            ctypes.CDLL('libvlccore.dylib')
            dll = ctypes.CDLL('libvlc.dylib')

    else:
        # All other OSes (linux, freebsd...)
        p = find_library('vlc')
        try:
            dll = ctypes.CDLL(p)
        except OSError:  # may fail
            dll = None
        if dll is None:
            try:
                dll = ctypes.CDLL('libvlc.so.5')
            except:
                raise NotImplementedError('Cannot find libvlc lib')

    return (dll, plugin_path)
    '''
    import importlib
    import sys

    # https://stackoverflow.com/questions/41858147/how-to-modify-imported-source-code-on-the-fly
    def modify_and_import(module_name, package, modification_func):
        spec = importlib.util.find_spec(module_name, package)
        source = spec.loader.get_source(module_name)
        new_source = modification_func(source)
        print("new source changed?", type(source), new_source)
        print("check str1 in ", str1 in new_source, str2 in new_source)
        module = importlib.util.module_from_spec(spec) #this is always the killer line, because vlc runs shit code it explodes
        og = module.__spec__.origin
        print("origin",type(og), og)
        #delete the file and overwrite, it's so doomed
        os.remove(og)
        f = open(og, "w+")
        f.write(new_source)
        f.close()
        print("INSPECT FILE1")
        import time
        # time.sleep(500)
        codeobj = compile(new_source, og, 'exec')
        exec(codeobj, module.__dict__)
        sys.modules[module_name] = module
        return module

    print("try mod", flush = True)
    #checking to see if pyinstaller module_collection_mode py sends the py file to tmpdir
    my_module = modify_and_import("vlc", None, lambda src: src.replace(str1, str2))
    import vlc

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
