import os
import random
import Carte


class Scenario:

    def __init__(self):

        #recuperation d'un fichier Json aléatoirement
        repertoire_Json = "./fichiersJson"
        noms_fichiers = [f for f in os.listdir(repertoire_Json) if os.path.isfile(os.path.join(repertoire_Json, f))]
        #self.nomFichierJson = random.choice(noms_fichiers)
        self.nomFichierJson="sQhJh2.json"

        #creation du flop a partir du titre du fichier json
        carte1=CarteDepuisString(self.nomFichierJson[:2])
        carte2=CarteDepuisString(self.nomFichierJson[2:4])
        carte3=CarteDepuisString(self.nomFichierJson[4:6])
        self.flop=[carte1,carte2,carte3]

#methode utile pour obtenir les 3 cartes du flop a partir du nom du fichier Json
def CarteDepuisString(nom):
    valeur_couleur=nom[0]
    couleur_correspondante = next(c for c in Carte.Couleur if c.value == valeur_couleur)
    valeur_hauteur=nom[1]
    hauteur_correspondante = next(h for h in Carte.Hauteur if h.value == valeur_hauteur)
    return Carte.Carte(couleur_correspondante,hauteur_correspondante)