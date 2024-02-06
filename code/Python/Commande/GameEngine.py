
import GameTree
import json

class GameEngine:

    gameTree=None #contient l'arbre de jeu provenant du fichier json de sortie du solveur

    def __init__(self,nomFichier,valeurCarte):
        self.gameTree=gameTree.GameTree(nomFichier,valeurCarte)

    def computerPlay(self):

        if (gameTree.isPlayable()==True): # Si il n'y a pas de coup a jouer, retourne 0
            return False

        actions=self.gameTree.getActions() # Pour récupérer le contenu des actions, renvoie une liste
        strategies=self.gameTree.getStrategies() # Pour récupérer le contenu de toutes les paires possibles de l'ordi, renvoie un dico

        tab = [0]*len(actions) # tableau de la somme des probas de chaque action

        for i in range(len(actions)):
            for tabProba in strategies.values():
                tab[i] += tabProba[i]  # On fait la somme de toutes les probas de l'action i pour chaque paire de carte

        """print("<--------------------------------->")
        print("Le nombre de combinaisons possibles pour l'ordinateur ")
        print(tab)
        print("<--------------------------------->\n")"""
        actionordi = self.recupmax(tab)  # On récupère l'indice de l'action à jouer
        print("<--------------------------------->")
        print("l'ordinateur joue : "+actions[actionordi]) #affiche l'action que joue l'ordinateur
        print("<--------------------------------->\n")

        if(actions[actionordi]=="FOLD"):
            return "Fin de partie"
        
        self.gameTree.play(actions[actionordi])  # on modifie le chemin en passant par children et l'action que doit effectuer l'ordi
        return True
        else:
            return False
        
    def playerPlay(self):
        if(self.gameTree.isPlayable()==True): 
            return self.gameTree.getPlayerPossiblities()
        else:
            return False # Si il n'y a pas de coup a jouer, retourne False

    def recupmax(self,tab):  # Fonction pour récupérer l'indice de la valeur max dans un tableau
        res=0
        max=tab[0]
        for i in range(len(tab)):
            if(tab[i]>max):
                res=i
                max=tab[i]
        return res

    # def dealcards(self,cartepiochee):
    #     self.data=self.data["dealcards"][cartepiochee]
