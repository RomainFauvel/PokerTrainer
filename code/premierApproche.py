import random
from enum import Enum
from itertools import product


class Couleur(Enum):
    SPADES="s"
    HEARTS="h"
    DIAMONDS="d"
    CLUBS="c"

class Hauteur(Enum):
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

    def melanger(self):
        random.shuffle(self.cartes)

    def distribuer(self, nombre_de_cartes):
        if nombre_de_cartes > len(self.cartes):
            print("Il n'y a pas assez de cartes pour distribuer.")
            return None

        main = self.cartes[:nombre_de_cartes]
        self.cartes = self.cartes[nombre_de_cartes:]

        return main

    def afficher_cartes(self, cartes):
        for carte in cartes:
            print(carte)



# Exemple d'utilisation
jeu = JeuDeCartes()


main1=JeuDeCartes.distribuer(jeu,2)

JeuDeCartes.afficher_cartes(jeu, jeu.cartes)
print(f"\n\n{main1[0]}\n{main1[1]}")


