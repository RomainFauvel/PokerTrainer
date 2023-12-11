import os
import customtkinter
from PIL import Image


class card():
    def __init__(self, suit, rank,flop):
        self.suit = suit
        self.rank = rank
        self.flop = flop
        self.image = self.get_image()

    def get_image(self):

        # a faire

        # la c est juste pour tester
        current_path = os.path.dirname(os.path.realpath(__file__))

        if (not self.flop):
            return customtkinter.CTkImage(Image.open(current_path + "/img/back_card.png")
                                          , size=(100, 150))
        else:
            # la ca serait complexe
            return customtkinter.CTkImage(Image.open(current_path + "/img/back_card.png")
                                          , size=(100, 150))