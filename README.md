# WinFlip
A Win32 tool mirroring the screen content
e.g. for video calls showing the same screen as broadcasted, suitable
for reading texts. Useful for apps like MS Teams or Skype with no screen mirror option.

## requirements
- Python 3
- see requirements.txt
or
- just a Win32 environment when running binary
- Windows default scale 100%, two displays recommended (1st for source screen, other for WinFlip output)
- powerful CPU :)

## run
```python winflip.py```
or
```winflip.exe```
- open Skype or MS Teams video call window (that one with camera view)
- launch WinFlip
- set framerate (5 is default, less than 5 could cause system slowdown)
- choose Go Skype or Go MS Teams
- move the output window to a desired location (not the source screen if possible)
- when resizing source window, the WinFlip window is autmatically resized as well
- press [X] to exit WinFlip
