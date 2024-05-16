
import GameTree
import utils
import random

class GameEngine:



    def __init__(self):
        self.gameTree =GameTree.GameTree()

        self.endOfTheGame=False
        self.endOfTheRound=False

        self.computerLastAction="Computer Action"

        self.numRound=1
        self.position=1 #0 player IP, 1 computer OOP | (IP -> l'ordi commence, OOP -> le joueur commence)

    def getNumRound(self):
        return self.numRound
    
    def getPosition(self):
        return self.position
    
    def getComputerLastAction(self):
        return self.computerLastAction
    
    def getEndOfTheGame(self):
        return self.endOfTheGame
    
    def getEndOfTheRound(self):
        return self.endOfTheRound
    
    def setPosition(self,position):
        self.position=position


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
        
        self.gameTree.play(action) #Permet de modifier le chemin selon l'action du joueur

        if(self.endOfTheRound==True):
            self.gameTree.setActionBeforeToNone() # Il faut remettre à 0 l'actionBefore pour continuer à gérer la fin du tour
            self.numRound+=1

        if(self.endOfTheGame==False and self.endOfTheRound==False): # Si la partie n'est pas finie et que le tour n'est pas fini L'ordinateur joue
            self.computerPlay()

        if(self.endOfTheRound==True and self.endOfTheGame==False and self.position==0): # Si le tour est fini mais pas la partie et qu'on est en IP l'ordinateur commence le nouveau tour
            self.endOfTheRound=False
            self.computerPlay()
        return True

    def computerPlay(self):#joue la meilleure action possible pour l'ordinateur

        if(self.endOfTheGame==True or self.endOfTheRound==True):
                return False

        if (self.gameTree.isPlayable()==False): # Si il n'y a pas de coup a jouer, retourne 0
                return False

        actions,tab=self.gameTree.getComputerActionProba()

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
                self.gameTree.updateRange(self.position,i)

        if(self.isEndOfGame(action)==True):
                self.endOfTheGame=True
                
        if(self.isEndOfRound(action)==True):
            self.endOfTheRound=True
        
        self.gameTree.updateStackAndPot(action)
        
        self.gameTree.play(action) #Permet de modifier le chemin selon l'action

        if(self.endOfTheRound==True):
            self.gameTree.setActionBeforeToNone() # Il faut remettre à 0 l'actionBefore pour continuer à gérer la fin du tour
            self.numRound+=1

        if(self.endOfTheRound==True and self.endOfTheGame==False and self.position==0): # Si le tour est fini mais pas la partie et qu'on est en IP l'ordinateur commence le nouveau tour
            self.endOfTheRound=False
            self.computerPlay()
        
        self.computerLastAction=action
        return action

        
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
        
    


