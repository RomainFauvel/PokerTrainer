
import tkinter
import customtkinter
import os
from PIL import Image

#a basic frame with a label

class Home(customtkinter.CTkFrame):
    def __init__(self, master: any, width: int = 200, height: int = 200):
        super().__init__(master, width, height)
        self.master = master
        self.width = width
        self.height = height        
        

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        
        
        
        #filling the background
        current_path = os.path.dirname(os.path.realpath(__file__))
        self.bg_image = customtkinter.CTkImage(Image.open(current_path + "\\interface.jpg"),
                                               size=(self.width, self.height))
        self.bg_image_label = customtkinter.CTkLabel(self, image=self.bg_image,text="")
        self.bg_image_label.grid(row=0, column=0)
        
        #create button
        self.play_button = customtkinter.CTkButton(self, text="Play", command=self.play_event, width=200)
        self.play_button.grid(row=0, column=0)
        self.play_button.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
        
    def play_event(self):
        self.master.show_frame("Play")
        
    def resize(self,event):
        width=event.width
        height=event.height
        if(width != self.width or height != self.height):
            print("Home resize")
            print("New width: ", width)
            print("New height: ", height)
            self.width = width
            self.height = height
            
            #resize background
            self.bg_image.configure(size=(self.width, self.height))
            self.bg_image_label.configure(image=self.bg_image)
            
            #resize button
            self.play_button.configure(width=self.width/10)
            
            
            

