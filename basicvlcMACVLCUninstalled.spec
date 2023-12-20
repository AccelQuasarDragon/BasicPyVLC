# -*- mode: python ; coding: utf-8 -*-

medianame = "bigbuckbunny x265.mp4"

a = Analysis(
    ['basicpyvlc.py'],
    pathex=["/Users/kivyschool/CODING/test/BasicPyVLC/dist/VLC.app/Contents"], #base VLC.app/Contents path here
    binaries=[("/Users/kivyschool/CODING/test/BasicPyVLC/dist/VLC.app/Contents/MacOS/plugins/*", "plugins")],
    datas=[(medianame, ".")],
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
    a.binaries + [
        ("libvlc.dylib", "/Users/kivyschool/CODING/test/BasicPyVLC/dist/VLC.app/Contents/MacOS/lib/libvlc.dylib", "BINARY"),
        ("libvlccore.dylib", "/Users/kivyschool/CODING/test/BasicPyVLC/dist/VLC.app/Contents/MacOS/lib/libvlccore.dylib", "BINARY")
        ],
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