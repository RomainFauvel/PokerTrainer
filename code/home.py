
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
        self.bg_image = customtkinter.CTkImage(Image.open(current_path + "\\img\\home_fond.png"),
                                               size=(self.width, self.height))
        self.bg_image_label = customtkinter.CTkLabel(self, image=self.bg_image,text="")
        self.bg_image_label.grid(row=0, column=0)
        
        #create buttons
        #play
        self.play_button = customtkinter.CTkButton(self, text="PLAY", command=self.play_event, width=100)
        self.play_button.grid(row=0, column=0, padx=15, pady=(15,15))
        self.play_button.place(relx=0.5,rely=0.58,anchor=tkinter.CENTER)
        #exit
        self.exit_button = customtkinter.CTkButton(self, text="Exit", command=self.exit_event, width=150)
        self.exit_button.grid(row=0, column=0, padx=15, pady=(15,15))
        self.exit_button.place(relx=0.05,rely=0.97,anchor=tkinter.CENTER)
        #home
        self.home_button = customtkinter.CTkButton(self, text="Home", command=self.home_event, width=150)
        self.home_button.grid(row=0, column=0, padx=15, pady=(15,15))
        self.home_button.place(relx=0.05,rely=0.03,anchor=tkinter.CENTER)
        #settings
        self.settings_button = customtkinter.CTkButton(self, text="SETTINGS", width=100)
        self.settings_button.grid(row=0, column=0, padx=15, pady=(15,15))
        self.settings_button.place(relx=0.5,rely=0.63,anchor=tkinter.CENTER)
        #help
        self.help_button = customtkinter.CTkButton(self, text="Help", command=self.help_event, width=150)
        self.help_button.grid(row=0, column=0, padx=15, pady=(15,15))
        self.help_button.place(relx=0.95,rely=0.03,anchor=tkinter.CENTER)
        #Select Configuration
        self.SelectConf_button = customtkinter.CTkButton(self, text="Select\nConfiguration", width=100)
        self.SelectConf_button.grid(row=0, column=0, padx=15, pady=(15,15))
        self.SelectConf_button.place(relx=0.93,rely=0.55,anchor=tkinter.CENTER)

        
    def play_event(self):
        self.master.show_frame("Play")
    
    def home_event(self):
        self.master.show_frame("Home")

    def help_event(self):
        self.master.show_frame("Help")

    def exit_event(self):
        self.master.destroy()
        
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
            
            #resize buttons
            self.play_button.configure(width=self.width/10)
            
            
            
            
            
            
            

