from PIL import Image
import tkinter
import customtkinter
import os


class Play(customtkinter.CTkFrame):
    def __init__(self, master: any, width: int = 200, height: int = 200):
        super().__init__(master, width, height)
        self.master = master
        self.width = width
        self.height = height
        
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)
        
        #Import images
        current_path = os.path.dirname(os.path.realpath(__file__))
        self.bg_image = customtkinter.CTkImage(Image.open(current_path + "\\img\\fond_vierge.png"),
                                               size=(self.width, self.height))
        self.button_image = customtkinter.CTkImage(Image.open(current_path + "\\img\\bouton.png"),
                                                   size=(128, 128))
        
        #label
        self.bg_image_label = customtkinter.CTkLabel(self, image=self.bg_image,text="Play\nà compléter")
        self.bg_image_label.grid(row=0, column=0)   


        #create buttons frame
        self.buttons_frame = customtkinter.CTkFrame(self)
        self.buttons_frame.grid(row=0, column=0, sticky="nsew")
        
        #create buttons
        #bet 'x'
        self.button_bet_x = customtkinter.CTkButton(self.buttons_frame, image=self.button_image, text="Bet\n 'x'")
        self.button_bet_x.grid(row=0, column=0, padx=15, pady=(15,15))
        
        #bet 'y'
        self.button_bet_y = customtkinter.CTkButton(self.buttons_frame, image=self.button_image, text="Bet\n 'y'")
        self.button_bet_y.grid(row=1, column=0, padx=15, pady=(15,15))
        
        #check
        self.button_check = customtkinter.CTkButton(self.buttons_frame, image=self.button_image, text="Check")
        self.button_check.grid(row=2, column=0, padx=15, pady=(15,15))
        
        #fold
        self.button_fold = customtkinter.CTkButton(self.buttons_frame, image=self.button_image, text="Fold")
        self.button_fold.grid(row=3, column=0, padx=15, pady=(15,15))
        
        
        
        
        #home
        self.home_button = customtkinter.CTkButton(self, text="Home", command=self.home_event, width=150)
        # self.home_button.grid(row=0, column=0, padx=15, pady=(15,15))
        self.home_button.place(relx=0.05,rely=0.03,anchor=tkinter.CENTER)
        #exit
        self.exit_button = customtkinter.CTkButton(self, text="Exit", command=self.exit_event, width=150)
        # self.exit_button.grid(row=0, column=0, padx=15, pady=(15,15))
        self.exit_button.place(relx=0.05,rely=0.97,anchor=tkinter.CENTER)
        


    def home_event(self):
        self.master.show_frame("Home")

    def exit_event(self):
        self.master.destroy()
        
    def resize(self,event):
        width=event.width
        height=event.height
        if(width != self.width or height != self.height):
            print("Play resize")
            print("New width: ", width)
            print("New height: ", height)
            self.width = width
            self.height = height