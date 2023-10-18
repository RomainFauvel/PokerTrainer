import random
from enum import Enum
from itertools import product



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
    
    def carteAleatoire(self):
        self.couleur=random.choice(list(Couleur))
        self.hauteur=random.choice(list(Hauteur))

    def __str__(self):
        return f"{self.hauteur.value}{self.couleur.value}"



class JeuDeCartes:
    def __init__(self):
        couleurs = list(Couleur)
        hauteurs = list(Hauteur)
        # Crée le jeu de cartes sans doublons
        self.cartes = [Carte(couleur, hauteur) for couleur in Couleur for hauteur in Hauteur]

    #melange le jeu
    def melanger(self):
        random.shuffle(self.cartes)

    #distribue dans une liste le nombre de cartes demandées en les supprimant du jeu de cartes
    def distribuer(self, nombre_de_cartes):
        if nombre_de_cartes > len(self.cartes):
            print("Il n'y a pas assez de cartes pour distribuer.")
            return None
        main = self.cartes[:nombre_de_cartes]
        self.cartes = self.cartes[nombre_de_cartes:]
        return main

    #affiche le jeu de cartes
    def afficher_cartes(self, cartes):
        for carte in cartes:
            print(carte)

    # revoie un String correspondant à ceux utilisés par le solveur en prenant une liste de 2 cartes en entrée (une main)
    def toStringPaire(Paire):
        carte1=Paire[0]
        carte2=Paire[1]
        res=f"{carte1.hauteur.value}{carte2.hauteur.value}"
        if(carte1.hauteur==carte2.hauteur):
            return res
        else: 
            if(carte1.couleur==carte2.couleur):
                return f"{res}s"
            else:
                return f"{res}o"
    

# créer un jeu et le mélange (utile en début de partie)
def creationJeu():
    jeu = JeuDeCartes()
    jeu.melanger()
    return jeu
    



