import os
import customtkinter as tk
import customtkinter
from PIL import Image


class card(tk.CTkCanvas):
    def __init__(self, suit, rank, flip):
        self.suit = suit #Couleur de la carte (carreau,pique....)
        self.rank = rank #Hauteur de la carte (1,2,...)
        self.flip = flip #Carte face cachée si false et retournée si true
        #self.show = show #Afficher ou cache la carte (True->affiche,False->cache)      <-------------- Tentative de faire un attribut pour afficher et caché la carte mais c'est assez galère donc on verra si on en a vraiment besoin
        self.image = self.get_image()
        #self.setShow(self.show)
        

    def get_image(self):

        #Chemin vers le bon dossier, ici, on revient en arrière vers le dossier PokerTrainer (la racine)
        current_path = os.path.dirname(os.path.realpath(__file__))
        print(current_path)
        parent_path = os.path.abspath(os.path.join(current_path,"..","..",".."))
        print(parent_path)

        if (self.flip):
            if(self.suit == "c"):
                return customtkinter.CTkImage(Image.open(parent_path + "\/Ressources\/Flat Playing Cards Set\/Clubs\/" + self.rank + ".png"), size=(100, 150))
            elif(self.suit == "d"):
                return customtkinter.CTkImage(Image.open(parent_path + "\/Ressources\/Flat Playing Cards Set\/Diamonds\/" + self.rank + ".png"), size=(100, 150))
            elif(self.suit == "s"):
                return customtkinter.CTkImage(Image.open(parent_path + "\/Ressources\/Flat Playing Cards Set\/Spades\/" + self.rank + ".png"), size=(100, 150))
            elif(self.suit == "h"):
                return customtkinter.CTkImage(Image.open(parent_path + "\/Ressources\/Flat Playing Cards Set\/Hearts\/" + self.rank + ".png"), size=(100, 150))
            else:
                return "ERREUR"

        else:
            #Dans le cas où flip est false, on laisse la carte face cachée
            return customtkinter.CTkImage(Image.open(parent_path + "\/Ressources\/img\/back_card.png"), size=(100, 150))    #carte face cachée
        
    #Setter de flip
    def setFlip(self,bool):
        self.flip = bool
        self.get_image()

"""""
    def setShow(self,bool):
        self.show = bool
        if(self.show):
            customtkinter.CTkImage(self.image,state=tk.NORMAL)
        else:
            customtkinter.CTkImage(self.image,state=tk.HIDDEN)
"""
