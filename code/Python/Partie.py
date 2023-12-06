
import Joueur
import Cartes
import LectureFichierJson
import Solveur
import Scenario
import random

tableauDeScenarios=[]

class Partie:

    def __init__(self,position):
        self.paquetDeCartes=Cartes.creationJeu()
        self.joueur=Joueur.Joueur(position)
        self.scenario=tableauDeScenarios[random.randint(0,len(tableauDeScenarios))]
        self.joueur.pioche(self.paquetDeCartes)

        
    
    


    def tourFlop(self):
        # doit demander à l'interface ce que joue le joueur
        # il faut rester dans le flop tant que qqun mise plus que l'autre d'avant
        # après avoir récupéré l'action du joueur, 
        # je modifie le chemin actuel dans l'arbre pour pouvoir récupérer proba ordi puis du prochain tour 
        self.fichier.setData(actionARealiser="")  # renvoie vrai si la modif a bien été effectuée
        return self.fichier.recupProba() # renvoie les proba pour le flop

        
    #meme principe que le tourFLOP
    def tourTurnCard(self,turnCard):
        self.fichier.data=self.fichier.data["dealcards"][turnCard] # remplacer turnCard ! au début du tour on modifie le chemin pour se placer au prochain tour
        # self.joueur.faireJouerOrdi() si c'est à l'ordi de jouer mais pas faite pour l'instant cette fonction
        self.fichier.setData(actionARealiser="")
        return self.fichier.recupProba()
    
    def tourRiver(self,river):
        self.fichier.data=self.fichier.data["dealcards"][river]
        # self.joueur.faireJouerOrdi() si c'est à l'ordi de jouer mais pas faite pour l'instant cette fonction
        self.fichier.setData(actionARealiser="")
        return self.fichier.recupProba()

        # faudra faire différents cas quand un joueur peut encore jouer ou pas selon s'il a fait tapis au tour d'avant extc


        

partie1=Partie(1)

