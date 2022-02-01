# WinFlip
# (C) 2022 ELS

import tkinter, os, sys
import win32gui
from tkinter import *
from PIL import Image, ImageTk, ImageGrab


SEARCH_TEXT = ["Schůzka"]  # set to Teams at first

# get path (for python 3.8+) to be able to compile as one file using PyInstaller
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

tk = Tk()

icon_filename = resource_path("winflip.ico")
tk.iconbitmap(icon_filename)

wintitle = "WinFlip 0.8"
label = tkinter.Label(tk)
label.pack()
tkimg = [None]
# X0, Y0, X1, Y1 = 0, 0, 1920, 1080  # initial grab area

tk.geometry("400x200")  # set initial window size
message = Label(tk, text="Set parameters, then press Go", font=("Calibri", 12))
author_name = Label(tk, text="© 2022 ELS")
framerate_label = Label(tk, text="Framerate")

def set_skype():
    global SEARCH_TEXT
    SEARCH_TEXT = ["Skype"]

def set_teams():
    global SEARCH_TEXT
    SEARCH_TEXT = ["Schůzka"]

def my_callback(hwnd, extra):
    """ callback for EnumWindows function
        to get spicific window coords.
        Can't return values so global var is set."""

    rect = win32gui.GetWindowRect(hwnd)
    x = rect[0]
    y = rect[1]
    w = rect[2] - x
    h = rect[3] - y

    global new_rect
    if SEARCH_TEXT[0] in win32gui.GetWindowText(hwnd):
        new_rect = [x, y, w, h]

def get_all_window_sizes():
    """ Function to get coords from a window name
        specified in my_callback() """

    win32gui.EnumWindows(my_callback, None)
    return new_rect

def get_slider_framerate():
    """ Gets value from slider """
    return slider_framerate.get()

def hide_elements():
    """ hide all window elements """
    skype_button.place_forget()
    teams_button.place_forget()
    go_button.place_forget()
    slider_framerate.place_forget()
    message.place_forget()
    author_name.place_forget()
    framerate_label.place_forget()

def loopcapture():
    """ Main loop
        - hides window elements
        - gets a framerate from slider
        - counts coords not to be <10
        - sets a window size from coords
        - grabs the window size to an image
        - flips it over """

    print(SEARCH_TEXT)
    hide_elements()
    fr = get_slider_framerate()  # get slider fr value
    
    nx0, ny0, nx1, ny1 = get_all_window_sizes()

    rx = nx1 - nx0
    ry = ny1 - ny0
    if rx <= 10:
        rx = 10
    if ry <= 10:
        ry = 10

    # print("real xy: ", rx, "x", ry)

    tk.geometry(str(rx) + "x" + str(ry))  # size it

    flip_method = Image.FLIP_LEFT_RIGHT
    area = (nx0, ny0, nx1, ny1)

    img = ImageGrab.grab(bbox=area)  # grab it
    img = img.transpose(flip_method)  # flip it

    tkimg[0] = ImageTk.PhotoImage(img)
    label.config(image=tkimg[0])
    tk.update_idletasks()
    tk.after(fr, loopcapture)  # loop it

# show texts
message.place(x=10, y=14)
author_name.place(x=330, y=180)
framerate_label.place(x=220, y=50)

# configure slider and button
slider_framerate = Scale(tk, from_=1, to=100)
slider_framerate.set(5)
slider_framerate.place(x=220, y=70)

skype_button = tkinter.Button(tk, text="Skype", command=set_skype)
skype_button.place(x=10, y=130, height=50, width=80)
teams_button = tkinter.Button(tk, text="MS Teams", command=set_teams)
teams_button.place(x=100, y=130, height=50, width=80)
go_button = tkinter.Button(tk, text="Go!", command=loopcapture)  # launch capture window
go_button.place(x=310, y=130, height=50, width=80)


if __name__ == "__main__":
    tk.wm_title(wintitle)
    tk.mainloop()