# -*- mode: python ; coding: utf-8 -*-

medianame = "bigbuckbunny x265.mp4"

a = Analysis(
    ['basicpyvlc.py'],
    pathex=["/Applications/VLC.app"], #base VLC.app/Contents path here
    binaries=[
        ("/Applications/VLC.app/Contents/MacOS/plugins/*", "plugins"),
        ],
    datas=[
        (medianame, "."),
        ],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='basicvlc',
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
    name='basicpyVLC.app',
    #icon="", #put your icon path here
    bundle_identifier=None,
)