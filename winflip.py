# WinFlip
# (C) 2022 ELS

from tkinter import *
import tkinter
from PIL import Image, ImageTk, ImageGrab


tk = Tk()
tk.iconbitmap(r"winflip.ico")
wintitle = "WinFlip 0.5 © 2022 ELS"
label = tkinter.Label(tk)
label.pack()
tkimg = [None]
X0, Y0, X1, Y1 = 0, 0, 1920, 1080  # initial grab area

tk.geometry("400x200")  # set initial window size
message = Label(tk, text="Set parameters, then press Go", font=("Calibri", 12))
author_name = Label(tk, text="© 2022 ELS")
upper_left_label = Label(tk, text="Upper Left")
bottom_right_label = Label(tk, text="Bottom right")
framerate_label = Label(tk, text="Framerate")

def get_slider_values():
    return slider_upper_x.get(), slider_upper_y.get(), slider_bottom_x.get(), slider_bottom_y.get(), slider_framerate.get()

def hide_elements():
    """ hide all window elements """
    go_button.place_forget()
    slider_upper_x.place_forget()
    slider_upper_y.place_forget()
    slider_bottom_x.place_forget()
    slider_bottom_y.place_forget()
    slider_framerate.place_forget()
    message.place_forget()
    author_name.place_forget()
    upper_left_label.place_forget()
    bottom_right_label.place_forget()
    framerate_label.place_forget()

def loopcapture():
    """ main loop """
    hide_elements()
    nx0, ny0, nx1, ny1, fr = get_slider_values()  # get new slider values
    tk.geometry(str(nx1 - nx0) + "x" + str(ny1 - ny0))  # size it

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
upper_left_label.place(x=42, y=50)
bottom_right_label.place(x=136, y=50)
framerate_label.place(x=220, y=50)

# configure sliders and button
slider_upper_x = Scale(tk, from_=0, to=1920)
slider_upper_x.set(0)
slider_upper_x.place(x=10, y=70)
slider_upper_y = Scale(tk, from_=0, to=1080)
slider_upper_y.set(0)
slider_upper_y.place(x=60, y=70)

slider_bottom_x = Scale(tk, from_=320, to=1920)
slider_bottom_x.set(1920)
slider_bottom_x.place(x=110, y=70)
slider_bottom_y = Scale(tk, from_=200, to=1080)
slider_bottom_y.set(1080)
slider_bottom_y.place(x=160, y=70)

slider_framerate = Scale(tk, from_=1, to=100)
slider_framerate.set(5)
slider_framerate.place(x=220, y=70)

go_button = tkinter.Button(tk, text="Go!", command=loopcapture)  # launch capture window
go_button.place(x=290, y=130, height=50, width=80)


if __name__ == "__main__":
    tk.wm_title(wintitle)
    tk.mainloop()