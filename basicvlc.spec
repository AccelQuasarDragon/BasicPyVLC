# -*- mode: python ; coding: utf-8 -*-

medianame = "bigbuckbunny x265.mp4"

a = Analysis(
    ['basicpyvlc.py'],
    pathex=[], #insert your base VLC path here, ex: pathex=["D:\KivySchool\VLC"], 
    binaries=[], #insert plugins folder, ex: binaries=[("D:\KivySchool\VLC\plugins\*", "plugins")],
    datas=[(medianame, ".")],
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
    a.binaries, #add libvlc here, ex: a.binaries + [("libVLC.dll", "D:\KivySchool\VLC\libvlc.dll", "BINARY")],
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
