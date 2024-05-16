
import GameTree
import utils
import random

class GameEngine:



    def __init__(self):
        self.gameTree =GameTree.GameTree()

        self.endOfTheGame=False
        self.endOfTheRound=False

        self.numRound=1
        self.position=0 #0 player IP, 1 computer OOP | (IP -> l'ordi commence, OOP -> le joueur commence)


    # def computerPlay(self,position):#joue la meilleure action possible pour l'ordinateur

    #     if (self.gameTree.isPlayable()==False): # Si il n'y a pas de coup a jouer, retourne 0
    #         return False

    #     actions=self.gameTree.getActions() # Pour récupérer le contenu des actions, renvoie une liste
    #     strategies=self.gameTree.getStrategies() # Pour récupérer le contenu de toutes les paires possibles de l'ordi, renvoie un dico

    #     tab = [0]*len(actions) # tableau de la somme des probas de chaque action

    #     for i in range(len(actions)):
    #         for tabProba in strategies.values():
    #             tab[i] += tabProba[i]  # On fait la somme de toutes les probas de l'action i pour chaque paire de carte

    #     print("<--------------------------------->")
    #     print("Le nombre de combinaisons possibles pour l'ordinateur ")
    #     print(tab)
    #     print("<--------------------------------->\n")

    #     action = utils.getActionAleatoire(actions,tab)
    #     print("<--------------------------------->")
    #     print("l'ordinateur joue : "+action) #affiche l'action que joue l'ordinateur
    #     print("<--------------------------------->\n")

    #     for i in range(len(actions)):
    #         if actions[i]==action:
    #             self.gameTree.updateRange(position,i)

    #     return action
        
    def playerPlay(self,action):

        if(self.endOfTheGame==True or self.endOfTheRound==True):
            return False
        
        if (self.gameTree.isPlayable()==False): # Si il n'y a pas de coup a jouer, retourne 0
            return False
        
        if(self.isEndOfGame(action)==True): # C'est le dernier coup de la partie
            self.endOfTheGame=True
            
        if(self.isEndOfRound(action)==True): # C'est le dernier coup du tour
            self.endOfTheRound=True
        
        self.gameTree.updateStackAndPot(action)
        
        self.GameTree.play(action) #Permet de modifier le chemin selon l'action du joueur

        if(self.endOfTheRound==True):
            self.tree.setActionBeforeToNone() # Il faut remettre à 0 l'actionBefore pour continuer à gérer la fin du tour
            self.numRound+=1

    def computerPlay(self):#joue la meilleure action possible pour l'ordinateur

        if(self.endOfTheGame==True or self.endOfTheRound==True):
                return False

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

        action = utils.getActionAleatoire(actions,tab)
        print("<--------------------------------->")
        print("l'ordinateur joue : "+action) #affiche l'action que joue l'ordinateur
        print("<--------------------------------->\n")

        for i in range(len(actions)):
            if actions[i]==action:
                self.gameTree.updateRange(position,i)

        if(self.isEndOfGame(action)==True):
                self.endOfTheGame=True
                
        if(self.isEndOfRound(action)==True):
            self.endOfTheRound=True
        
        self.gameTree.updateStackAndPot(action)
        
        self.GameTree.play(action) #Permet de modifier le chemin selon l'action du joueur

        if(self.endOfTheRound==True):
            self.tree.setActionBeforeToNone() # Il faut remettre à 0 l'actionBefore pour continuer à gérer la fin du tour
            self.numRound+=1

        
    def isEndOfGame(self,action): #Prend l'action effectuée et regarde si elle est présente dans childrens, si c'est le cas la partie continue sinon elle s'arrête
        if "childrens" in self.gameTree.data:
            actionsInChildrens=list(self.gameTree.data["childrens"].keys())
            print(actionsInChildrens)
            if action in actionsInChildrens:
                action_parts = action.split()
                if self.gameTree.actionBefore!=None:
                    action_before_parts=self.gameTree.actionBefore.split()
                    if len(action_before_parts)>1:
                        if action_parts[0]=="CALL" and self.gameTree.stack==0: 
                            return True
                return False
            return True
        return True
    
    def isEndOfRound(self,action):
        action_parts = action.split()
        print("action before = "+str(self.gameTree.actionBefore))
        if action_parts[0] in ["CHECK","CALL"] and self.gameTree.actionBefore!=None:
            print("action before in if = "+str(self.gameTree.actionBefore))
            return True
        return False
        
    


