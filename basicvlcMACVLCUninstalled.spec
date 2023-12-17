# -*- mode: python ; coding: utf-8 -*-

medianame = "bigbuckbunny x265.mp4"
import inspect
#import vlc

def collect_source_files(modules):
    datas = []
    for module in modules:
        source = inspect.getsourcefile(module)
        dest = f"src.{module.__name__}"  # use "src." prefix
        datas.append((source, dest))
    return datas

#from PyInstaller.utils.hooks import collect_data_files, copy_metadata
#source_files = collect_source_files([vlc])  # return same structure as `collect_data_files()`
#source_files_toc = TOC((name, path, 'DATA') for path, name in source_files)

#vlclocation = vlc.__file__

a = Analysis(
    ['basicpyvlc.py'],
    pathex=["/Users/raidraptorultimatefalcon/CODING/test/BasicPyVLC/dist/VLC.app"], #base VLC.app/Contents path here
    binaries=[
        ("/Users/raidraptorultimatefalcon/CODING/test/BasicPyVLC/dist/VLC.app/Contents/MacOS/plugins/*", "plugins"),
        ],
    datas=[
        (medianame, "."),
        #(vlclocation,"."),
        #("/Users/raidraptorultimatefalcon/CODING/test/BasicPyVLC/.venv/lib/python3.10/site-packages/vlc.py" , "."),
        #*collect_data_files("vlc", include_py_files=True),
        #*copy_metadata("vlc)
        ],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    #https://github.com/pyinstaller/pyinstaller/issues/7851#issuecomment-1677986648
    module_collection_mode={
        'vlc': 'py',
    }
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries + [("libvlc.dylib", "/Users/raidraptorultimatefalcon/CODING/test/BasicPyVLC/dist/VLC.app/Contents/MacOS/lib/libvlc.dylib", "BINARY"),("libvlccore.dylib", "/Users/raidraptorultimatefalcon/CODING/test/BasicPyVLC/dist/VLC.app/Contents/MacOS/lib/libvlccore.dylib", "BINARY")],
    #a.binaries,
    a.datas,
    [],
    name='MACvlcUninstalled',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)

# https://pyinstaller.org/en/stable/spec-files.html#spec-file-options-for-a-macos-bundle
app = BUNDLE(
    exe,
    name='MacpyVLCUninstalled.app',
    #icon="", #put your icon path here
    bundle_identifier=None,
)