
import GameTree
import utils
import random
import Solveur as Solveur

class GameEngine:



    def __init__(self):
        self.gameTree =GameTree.GameTree()

        self.endOfTheGame=False
        self.endOfTheRound=False

        self.computerLastAction="Computer Action"

        self.numRound=1
        self.position=0 #0 player OOP, 1 player IP | (IP -> l'ordi commence, OOP -> le joueur commence)

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
        
    def playerPlay(self,action):


        if(action=="FOLD"):
            self.endOfTheGame=True
            self.endOfTheRound=True
            return False
        if(self.endOfTheGame==True or self.endOfTheRound==True):
            return False
        
        # if (self.gameTree.isPlayable()==False): # Si il n'y a pas de coup a jouer, retourne 0
        #     return False
        
        if(self.isEndOfGame(action)==True): # C'est le dernier coup de la partie
            self.endOfTheGame=True
            return True
            
        if(self.isEndOfRound(action)==True): # C'est le dernier coup du tour
            self.endOfTheRound=True

        idAction = self.gameTree.getActions().index(action)
        self.gameTree.updateRange(self.position,idAction)
        
        self.gameTree.updateStackAndPot(action)
        
        self.gameTree.play(action) #Permet de modifier le chemin selon l'action du joueur

        if(self.numRound==2 and self.getEndOfTheRound()==True):
            Solveur.solveurRiver()
            GameTree.GameTree(filePath="output_result.json")

        if(self.endOfTheRound==True):
            self.gameTree.setActionBeforeToNone() # Il faut remettre à 0 l'actionBefore pour continuer à gérer la fin du tour
            self.numRound+=1

        if(self.endOfTheGame==False and self.endOfTheRound==False): # Si la partie n'est pas finie et que le tour n'est pas fini L'ordinateur joue
            self.computerPlay()

        if(self.endOfTheRound==True and self.endOfTheGame==False and self.position==1): # Si le tour est fini mais pas la partie et qu'on est en IP l'ordinateur commence le nouveau tour
            self.endOfTheRound=False
            self.computerPlay()
        elif(self.endOfTheRound==True and self.endOfTheGame==False and self.position==0): # Si le tour est fini mais pas la partie et qu'on est en OOP le joueur commence le nouveau tour
            self.endOfTheRound=False

        

        return True

    def computerPlay(self):#joue la meilleure action possible pour l'ordinateur

        if(self.endOfTheGame==True or self.endOfTheRound==True):
                return False

        # if (self.gameTree.isPlayable()==False): # Si il n'y a pas de coup a jouer, retourne 0
        #         return False

        actions,tab=self.gameTree.getComputerActionProba()

        print("<--------------------------------->")
        print("Le nombre de combinaisons possibles pour l'ordinateur ")
        print(tab)
        print("<--------------------------------->\n")

        action = utils.getActionAleatoire(actions,tab)
        print("<--------------------------------->")
        print("l'ordinateur joue : "+action) #affiche l'action que joue l'ordinateur
        print("<--------------------------------->\n")

        if(action=="FOLD"):
            self.endOfTheGame=True
            self.endOfTheRound=True
            return action

        for i in range(len(actions)):
            if actions[i]==action:
                self.gameTree.updateRange(not self.position,i)

        if(self.isEndOfGame(action)==True):
                self.endOfTheGame=True
                return action
                
        if(self.isEndOfRound(action)==True):
            self.endOfTheRound=True
        
        self.gameTree.updateStackAndPot(action)
        
        self.gameTree.play(action) #Permet de modifier le chemin selon l'action

        if(self.numRound==2 and self.getEndOfTheRound()==True):
            Solveur.solveurRiver()
            GameTree.GameTree(filePath="output_result.json")

        if(self.endOfTheRound==True):
            self.gameTree.setActionBeforeToNone() # Il faut remettre à 0 l'actionBefore pour continuer à gérer la fin du tour
            self.numRound+=1

        if(self.endOfTheRound==True and self.endOfTheGame==False and self.position==1): # Si le tour est fini mais pas la partie et qu'on est en IP l'ordinateur commence le nouveau tour
            self.endOfTheRound=False
            self.computerPlay()
        elif(self.endOfTheRound==True and self.endOfTheGame==False and self.position==0): # Si le tour est fini mais pas la partie et qu'on est en OOP le joueur commence le nouveau tour
            self.endOfTheRound=False
        
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
                        action_before_value=action_before_parts[1].split(',')
                        action_before_valueBis=action_before_value[0].split('.')
                        if action_parts[0]=="CALL" and self.gameTree.stack<int(action_before_valueBis[0]): 
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
        
    


