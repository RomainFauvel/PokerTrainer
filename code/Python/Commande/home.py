
import tkinter
import tkinter as tk
from tkinter import filedialog
import customtkinter
import os
from PIL import Image
import re

import Partie


#a basic frame with a label

class Home(customtkinter.CTkFrame):
    def __init__(self, master: any, width: int = 200, height: int = 200):
        super().__init__(master, width, height)
        self.master = master
        self.width = width
        self.height = height   

        self.path = None  
        

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)


        #Variable pour stocker le chemin du fichier choisi
        self.var_fichier = None
        
        #filling the background
        current_path = os.path.dirname(os.path.realpath(__file__))
        #print(current_path)
        parent_path = os.path.abspath(os.path.join(current_path,"..","..",".."))
        #print(parent_path)
        self.bg_image = customtkinter.CTkImage(Image.open(parent_path + "\\Ressources\\img\\home_fond.png"),
                                               size=(self.width, self.height))
        self.bg_image_label = customtkinter.CTkLabel(self, image=self.bg_image,text="")
        self.bg_image_label.grid(row=0, column=0)


        #Etiquette pour afficher le chemin du fichier choisi
        self.file_path = customtkinter.CTkLabel(self.bg_image_label,text="Fichier choisi :\n")   #Texte par défaut
        self.file_path.grid(row=0, column=0, padx=15, pady=(15, 15))

        #Position au-dessus du bouton "Select Configuration"
        self.file_path.place(relx=0.93, rely=0.45, anchor=tkinter.CENTER)


        
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
        self.SelectConf_button = customtkinter.CTkButton(self, text="Select\nConfiguration", command=self.SelectConf_event, width=100)
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

    def SelectConf_event(self):

        #Ouvrir la boîte de dialogue pour choisir un fichier
        fichier = filedialog.askopenfilename()
        #Mettre à jour la variable de classe avec le chemin du fichier choisi
        self.var_fichier = fichier
        #Expression régulière
        #Pour récupérer le premier "/", il faut le mettre dans au tout début des parenthèses mais dans notre cas on le veut pas
        result=re.search(r"/([^/]+\.[^/]+)$",fichier)
        #print(result.group(1))
        if(result!=None):



            #Mettre à jour l'étiquette avec le chemin du fichier choisi
            self.file_path.configure(text=f"Fichier choisi :\n{result.group(1)}")
            self.path = result.group(1)


        
    def resize(self,event):
        width=event.width
        height=event.height
        if((width != self.width or height != self.height) and self.master.frame == self) :
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

    def getPath(self):
        return self.path
            


            
            
            
            
            
            

