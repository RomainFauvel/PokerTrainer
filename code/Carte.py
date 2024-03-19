from enum import Enum


class Couleur(Enum):
    SPADES="s"
    HEARTS="h"
    DIAMONDS="d"
    CLUBS="c"

class Hauteur(Enum):
    Deux="2"
    TROIS="3"
    Quatre="4"
    CINQ="5"
    SIX="6"
    SEPT="7"
    HUIT="8"
    NEUF="9"
    DIX="T"
    VALET="J"
    DAME="Q"
    KING="K"
    AS="A"




class Carte:
    #attributs de la classe
    def __init__(self, couleur, hauteur):
        self.couleur = couleur
        self.hauteur = hauteur

    def __str__(self):
        return f"{self.couleur.value}{self.hauteur.value}"

