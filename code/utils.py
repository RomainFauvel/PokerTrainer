import customtkinter
import tkinter
import os

def get_display_size():
    root = tkinter.Tk()
    root.update_idletasks()
    root.attributes('-fullscreen', True)
    root.state('iconic')
    height = root.winfo_screenheight()
    width = root.winfo_screenwidth()
    root.destroy()
    return height, width


