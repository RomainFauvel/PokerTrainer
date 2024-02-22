import os
import customtkinter
from PIL import Image


class card():
    def __init__(self, suit, rank, show):
        self.suit = suit
        self.rank = rank
        self.show = show #Carte face cachée si false et retournée si true
        self.image = self.get_image()

    def get_image(self):

        # a faire

        # la c est juste pour tester
        current_path = os.path.dirname(os.path.realpath(__file__))
        print(current_path)
        parent_path = os.path.abspath(os.path.join(current_path,"..","..",".."))
        print(parent_path)

        if (self.show):
            #return customtkinter.CTkImage(Image.open(parent_path + "\\Ressources\\img\\back_card.png"), size=(100, 150))
            return 0

        else:
            # la ca serait complexe
            return customtkinter.CTkImage(Image.open(parent_path + "\\Ressources\\img\\back_card.png"), size=(100, 150))    #carte face cachée