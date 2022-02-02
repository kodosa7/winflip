# WinFlip
# (C) 2022 ELS

import tkinter, os, sys
import win32gui
from tkinter import *
from PIL import Image, ImageTk, ImageGrab


help_text = """
    WinFlip flips the Skype/Teams (Source) screen horizontally. This might be useful
    for situations when presenting on a bigscreen which is taken by a webcam
    and reading texts in video calls locally is needed.\n
    How to use the app:
    1. Have 2 or more displays, one for Source window, other for Output window.
    If you have one display only, both Source and Output windows can't be maximized to the full screen.
    2. Place the original Source window to the top left position of the source display. Do not resize.
    3. Drag the Output window out to other screen (or out of scope of the Source window).
    4. Eventually resize the Source window to a desired size, the Output window will be resized automatically.
    """

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

wintitle = "WinFlip v0.87"
label = tkinter.Label(tk)
label.pack()
tkimg = [None]

tk.geometry("400x200")  # set initial window size
message = Label(tk, text="Adjust app type and framerate, then press Go", font=("Calibri", 12))
author_name = Label(tk, text="© 2022 ELS")
framerate_label = Label(tk, text="Framerate")
buttons_label = Label(tk, text="Set app type")

def set_skype():
    """ set for Skype window """
    global SEARCH_TEXT
    SEARCH_TEXT = ["Skype"]
    skype_button.config(relief=SUNKEN)
    teams_button.config(relief=RAISED)

def set_teams():
    """ set for MS Teams window """
    global SEARCH_TEXT
    SEARCH_TEXT = ["Schůzka"]
    skype_button.config(relief=RAISED)
    teams_button.config(relief=SUNKEN)

def show_help():
    """ show help window """
    help_window = Toplevel(tk)
    help_window.title("Help")
    help_window.geometry("600x220")
    Label(help_window, text=help_text).pack(anchor='w')

    help_button["state"] = "disabled"  # disable button
    help_button.config(relief=SUNKEN)  # make button pushed
    help_window.iconbitmap(icon_filename)  # assign icon

    def win_close_button():
        """ do nothing """
        pass

    def close_help_window():
        """ do this after Close button is pressed """
        help_button["state"] = "normal"
        help_button.config(relief=RAISED)
        help_window.destroy()

    help_window.protocol("WM_DELETE_WINDOW", win_close_button)  # disable [X] button

    quit_button = Button(help_window, text="Close", command=close_help_window)
    quit_button.pack()

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
    try:
        return new_rect
    except NameError:
        print(f"window with string {SEARCH_TEXT[0]} not found")
        tk.destroy()
        quit()

def get_slider_framerate():
    """ Gets value from slider """
    return slider_framerate.get()

def hide_elements():
    """ hide all window elements """
    skype_button.place_forget()
    teams_button.place_forget()
    go_button.place_forget()
    help_button.place_forget()
    slider_framerate.place_forget()
    message.place_forget()
    author_name.place_forget()
    framerate_label.place_forget()
    buttons_label.place_forget()

def loopcapture():
    """ Main loop
        - hides window elements
        - gets a framerate from slider
        - counts coords not to be <10
        - sets a window size from coords
        - grabs the window size to an image
        - flips it over """

    hide_elements()
    fr = get_slider_framerate()  # get slider fr value
    
    nx0, ny0, nx1, ny1 = get_all_window_sizes()

    rx, ry = nx1 - nx0, ny1 - ny0
    if rx <= 10:
        rx = 10
    if ry <= 10:
        ry = 10

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
framerate_label.place(x=142, y=45)
buttons_label.place(x=30, y=45)

# configure slider and button
slider_framerate = Scale(tk, from_=1, to=100)
slider_framerate.set(5)
slider_framerate.place(x=140, y=75)

skype_button = tkinter.Button(tk, text="Skype", command=set_skype)
skype_button.place(x=30, y=70, height=50, width=80)
teams_button = tkinter.Button(tk, text="MS Teams", command=set_teams)
teams_button.place(x=30, y=130, height=50, width=80)
help_button = tkinter.Button(tk, text="Help", command=show_help)
help_button.place(x=300, y=70, height=50, width=80)
go_button = tkinter.Button(tk, text="Go!", command=loopcapture)  # launch capture window
go_button.place(x=300, y=130, height=50, width=80)


if __name__ == "__main__":
    # init settings..
    SEARCH_TEXT = ["Skype"]
    skype_button.config(relief=SUNKEN)
    teams_button.config(relief=RAISED)

    # ..then do things
    tk.wm_title(wintitle)
    tk.mainloop()