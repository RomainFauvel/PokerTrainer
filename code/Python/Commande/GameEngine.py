
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

        return computerAction
        
    def playerPlay(self):#Affiche les probas de chaque action possible pour le joueur
        if(self.gameTree.isPlayable()==True): 
            return self.gameTree.getPlayerPossiblities()
        else:
            return False # S'il n'y a pas de coup à jouer, retourne False
        
    def isEndOfGame(self,action): #Prend l'action effectuée et regarde si elle est présente dans childrens, si c'est le cas la partie continue sinon elle s'arrête
        if "childrens" in self.gameTree.data:
            actionsInChildrens=list(self.gameTree.data["childrens"].keys())
            print(actionsInChildrens)
            if action in actionsInChildrens:
                action_parts = action.split()
                if self.gameTree.actionBefore!=None:
                    action_before_parts=self.gameTree.actionBefore.split()
                    if len(action_before_parts)>1:
                        amountCalled=int(action_before_parts[1].split(',')[0])
                        if action_parts[0]=="CALL" and self.gameTree.stack==0: 
                            return True
                return False
            return True
        return True
    
    def isEndOfRound(self,action):
        action_parts = action.split()
        if action_parts[0] in ["CHECK","CALL"] and self.gameTree.actionBefore!=None:
            return True
        return False
        
    


