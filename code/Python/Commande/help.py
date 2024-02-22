import tkinter
import customtkinter
import os
from PIL import Image
from tkinter import scrolledtext

#a basic frame with a label

class Help(customtkinter.CTkFrame):
    def __init__(self, master: any, width: int = 200, height: int = 200):
        super().__init__(master, width, height)
        self.master = master
        self.width = width
        self.height = height  

        #Lecture du fichier qui permet de prendre le contenu pour écrire dans la page help
        file_path = "help.txt"
        text_content=self.read_text_from_file(file_path)
        
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        
        #filling the background
        current_path = os.path.dirname(os.path.realpath(__file__))
        #print(current_path)
        parent_path = os.path.abspath(os.path.join(current_path,"..","..",".."))
        #print(parent_path)
        self.bg_image = customtkinter.CTkImage(Image.open(parent_path + "\\Ressources\\img\\fond_vierge.png"),
                                               size=(self.width, self.height))
        
        #label
        self.bg_image_label = customtkinter.CTkLabel(self, image=self.bg_image,text="",font=("Arial",25))
        self.bg_image_label.grid(row=0, column=0)  
        self.bg_image_label.configure(text=text_content)


        #create buttons
        #home
        self.home_button = customtkinter.CTkButton(self, text="Home", command=self.home_event, width=150)
        self.home_button.grid(row=0, column=0, padx=15, pady=(15,15))
        self.home_button.place(relx=0.05,rely=0.03,anchor=tkinter.CENTER)
        #exit
        self.exit_button = customtkinter.CTkButton(self, text="Exit", command=self.exit_event, width=150)
        self.exit_button.grid(row=0, column=0, padx=15, pady=(15,15))
        self.exit_button.place(relx=0.05,rely=0.97,anchor=tkinter.CENTER)
        
        """
        #create label
        self.label = customtkinter.CTkLabel(self, text="Play", font=("Arial", 20))
        self.label.place(relx=0.5,rely=0.58,anchor=tkinter.CENTER)
        """



    def home_event(self):
        self.master.show_frame("Home")

    def exit_event(self):
        self.master.destroy()

    def read_text_from_file(self,file_path):
        try:
            with open(file_path,'r',encoding='utf-8') as file:
                text=file.read()
            return text
        except FileNotFoundError:
            return "Fichier introuvable"
        except Exception as e:
            return f"Erreur {str(e)}"
        
    def resize(self,event):
        width=event.width
        height=event.height
        if((width != self.width or height != self.height)and self.master.frame == self):
            print("Play resize")
            print("New width: ", width)
            print("New height: ", height)
            self.width = width
            self.height = height