# WinFlip
A Win32 tool mirroring the screen content
e.g. for video calls showing the same screen as broadcasted.
Useful for apps like MS Teams or Skype with no screen mirror option.

## requirements
- Python 3
- see requirements.txt
or
- just a Win32 environment when running binary
- minimum resolution 1920x1080, Windows default scale 100%, two displays recommended (1st for source screen, 2nd for WinFlip output)
- powerful CPU :)

## run
```python winflip.py```
or
```winflip.exe```
- set grab area (top left and bottom right pixel on the source screen)
- set framerate (5 is default, less than 5 could cause system slowdown)
- press Go and move the output window to a desired location
- press [X] to exit the program