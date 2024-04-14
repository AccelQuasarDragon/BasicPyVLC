# BasicPyVLC
Basic Python script with VLC and Packaging with PyInstaller on Windows and Mac

How to package VLC with PyInstaller. Made for [kivyschool.com/2023/12/14/add-vlc-to-pyinstaller](https://kivyschool.com/blog/2023/12/14/add-vlc-to-pyinstaller/)

# Requirements

Using [python poetry](https://python-poetry.org/).

# Usage

After poetry installation, just cd to the project folder and type: `poetry update` 

Then `poetry shell`

Check the example test py:

`python basicvlc.py`

To compile, add these paths to your specfile: VLC, `libvlc.dll`, `libvlc.dylib`, `libvlccore.dylib`, `plugins` folder, etc)

Then try:

`python -m PyInstaller basicvlcWIN.spec --clean ` OR 

`python -m PyInstaller basicvlcMACBasic.spec --clean ` OR

`python -m PyInstaller basicvlcMACVLCUninstalled.spec --clean ` 

Check out that the `.exe` or `.app` works on your machine.


