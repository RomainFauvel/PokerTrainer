
import GameTree
import utils
import random

class GameEngine:



    def __init__(self):
        self.gameTree =GameTree.GameTree()



    def computerPlay(self,position):#joue la meilleure action possible pour l'ordinateur

        if (self.gameTree.isPlayable()==False): # Si il n'y a pas de coup a jouer, retourne 0
            return False

        actions=self.gameTree.getActions() # Pour récupérer le contenu des actions, renvoie une liste
        strategies=self.gameTree.getStrategies() # Pour récupérer le contenu de toutes les paires possibles de l'ordi, renvoie un dico

        tab = [0]*len(actions) # tableau de la somme des probas de chaque action

        for i in range(len(actions)):
            for tabProba in strategies.values():
                tab[i] += tabProba[i]  # On fait la somme de toutes les probas de l'action i pour chaque paire de carte

        print("<--------------------------------->")
        print("Le nombre de combinaisons possibles pour l'ordinateur ")
        print(tab)
        print("<--------------------------------->\n")

        computerAction = utils.getActionAleatoire(actions,tab)
        print("<--------------------------------->")
        print("l'ordinateur joue : "+computerAction) #affiche l'action que joue l'ordinateur
        print("<--------------------------------->\n")

        for i in range(len(actions)):
            if actions[i]==computerAction:
                self.gameTree.updateRange(position,i)

        if(computerAction=="FOLD"):
            return "Fin de partie"
        
        self.gameTree.play(computerAction)  # on modifie le chemin en passant par children et l'action que doit effectuer l'ordi
        return True
        
    def playerPlay(self):#Affiche les probas de chaque action possible pour le joueur
        if(self.gameTree.isPlayable()==True): 
            return self.gameTree.getPlayerPossiblities()
        else:
            return False # Si il n'y a pas de coup a jouer, retourne False
        
    


