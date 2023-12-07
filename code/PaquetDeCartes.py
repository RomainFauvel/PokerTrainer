import Carte
import random

class PaquetDeCartes:
    def __init__(self):
        couleurs = list(Carte.Couleur)
        hauteurs = list(Carte.Hauteur)
        # Crée le jeu de cartes sans doublons
        self.cartes = [Carte.Carte(couleur, hauteur) for couleur in Carte.Couleur for hauteur in Carte.Hauteur]

    #melange le jeu
    def melanger(self):
        random.shuffle(self.cartes)

    #distribue dans une liste le nombre de cartes demandées en les supprimant du jeu de cartes
    def distribuer(self, nombre_de_cartes):
        if nombre_de_cartes > len(self.cartes):
            print("Il n'y a pas assez de cartes pour distribuer.")
            return None
        cartes = self.cartes[:nombre_de_cartes]
        self.cartes = self.cartes[nombre_de_cartes:]
        return cartes

    def retirerFlop(self,flop):
        for c in self.cartes:
            if c==flop[0] or c==flop[0] or c==flop[0]:
                self.cartes.remove(c)

    # affiche le jeu de cartes
    def afficher_cartes(self, cartes):
        for carte in cartes:
            print(carte)

# créer un jeu et le mélange (utile en début de partie)
def creationJeu():
    jeu = PaquetDeCartes()
    jeu.melanger()
    return jeu