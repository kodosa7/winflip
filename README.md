# WinFlip
A Win32 tool mirroring the screen content
e.g. for video calls showing the same screen as broadcasted, suitable
for reading texts. For MS Teams or Skype with no screen mirror option.

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
- open ```Skype``` or ```MS Teams``` video call window (that one with camera view)
- launch ```winflip.exe```
- set app type used for streaming (Skype/Teams)
- event. set framerate (5 is default, less than 5 could cause system slowdown)
- press the Go button
- move the source window to position 0,0 on screen 0
- move the output window to a desired location (screen)
- when resizing source window, the WinFlip window is autmatically resized as well
- press [X] to exit WinFlip