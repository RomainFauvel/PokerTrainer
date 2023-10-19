
import tkinter
import customtkinter
import os

#a basic frame with a label

class Play(customtkinter.CTkFrame):
    def __init__(self, master: any, width: int = 200, height: int = 200):
        super().__init__(master, width, height)
        self.master = master
        self.width = width
        self.height = height  
        
        #create label
        self.label = customtkinter.CTkLabel(self, text="Play", font=("Arial", 20))
        self.label.pack()
        
    def resize(self,event):
        width=event.width
        height=event.height
        if(width != self.width or height != self.height):
            print("Play resize")
            print("New width: ", width)
            print("New height: ", height)
            self.width = width
            self.height = height