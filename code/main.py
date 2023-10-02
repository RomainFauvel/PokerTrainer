import customtkinter
import tkinter
import os

# Ours imports
import home as home
import play as play
import settings as settings
import utils as utils


class App(customtkinter.CTk):
    def __init__(self,height,width):
        super().__init__()

        # configure window
        self.title("Poker Trainer")
        self.geometry(str(width)+"x"+str(height)+"+0+0")
        


def main():
    print("------------------Main called------------------")
    height, width = utils.get_display_size()
    root = App(height, width)
    root.mainloop()

main()