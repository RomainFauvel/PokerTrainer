
import json
import os
import Cards
import random


class GameTree:
    data=None  #contient sous forme de dico les données du fichier json qui va être modifié selon les actions du joueur et de l'ordi
    playerHand=None #valeur de la carte du joueur/ordi
    flop=None
    river=None
    turn=None

    #attributs pour gérer l'effective stack pour l'appel au solveur et la fin d'une partie
    initialStack=200 # Paramètre par défaut dans le solveur, amélioration possible 
    stack=200
    actionBefore=None

    #attributs pour gérer le pot
    initialPot=50 # Paramètre par défaut dans le solveur, amélioration possible 
    pot=50

    rangeOOP={}
    rangeIP={}

    _instance = None

    def __new__(cls, *args, **kwargs): #Creation d'un singleton pour avoir une seule sdd partagee entre les classes
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    #Initialisation de la classe avec les valeurs si elles sont donnees sinon, on donne juste la reference de la classe
    def __init__(self,filePath=None,playerHand=None,flop=None,river=None,turn=None,rangeOOP=None,rangeIP=None,stack=200): #initialisation de la classe
        if(filePath!=None):
            self.filePath=filePath
        if(playerHand!=None):
            self.playerHand=playerHand
        if(flop!=None):
            self.flop=flop
        if(river!=None):
            self.river=river
        if(turn!=None):
            self.turn=turn
        if(stack!=200):
            self.stack=stack
        if(not(filePath==None and playerHand==None and flop==None and river==None and turn==None)):
            self.initialise(self.filePath,self.playerHand,self.flop,self.river,self.turn) 
    
    #Peux etre acceder depuis l exterieur sans initialiser un objet (exemple: GameTree.initialise(filePath,playerHand,flop,river,turn))
    @classmethod
    def initialise(cls,filePath,playerHand,flop,river,turn):
        if(cls._instance is None):
            cls._instance = cls()

        
        current_path = os.path.dirname(os.path.realpath(__file__))
        parent_path = os.path.abspath(os.path.join(current_path,"..","..",".."))
        filePath=os.path.join(parent_path,filePath)
        with open(filePath) as f:
            cls._instance.setData(json.load(f))
        cls._instance.setPlayerHand(playerHand)
        cls._instance.setFlop(flop)
        cls._instance.setRiver(river)
        cls._instance.setTurn(turn)
        cls._instance.compteur=0
        cls._instance.setRandomPlayerHandFromRange()

    def __str__(self):
        return "GameTree: playerHand: " + str(self.playerHand) + " flop: " + str(self.flop) + " river: " + str(self.river) + " turn: " + str(self.turn)

    #getters

    def getActions(self):
        return self.data["strategy"]["actions"]

    def getStrategies(self):
        return self.data["strategy"]["strategy"]
    
    #return round (i.e pre-flop,flop,turn,river)
    def getRound(self):
        return self.compteur
    
    def getData(self):
        return self.data

    def getPlayerHand(self):
        return self.playerHand

    def getFlop(self):
        return self.flop

    def getRiver(self):
        return self.river

    def getTurn(self):
        return self.turn
    
    def getRange(self):
        return list(self.data["strategy"]["strategy"])
    
    # setters

    def setData(self,data):
        self.data=data

    def setPlayerHand(self, playerHand):
        self.playerHand = playerHand

    def setFlop(self, flop):
        self.flop = flop

    def setRiver(self, river):
        self.river = river

    def setTurn(self, turn):
        self.turn = turn

    def setActionBeforeToNone(self):
        self.actionBefore=None

    #fonctions utiles

    # def play(self,todo): # se deplace dans l arbre en prenant en compte l'action réalisée par le joueur/Ordi
    #     if(self.isPlayable()==False):
    #         #print("Il n'y a pas d'action possible à jouer")
    #         return False
    #     self.data=self.data["childrens"][todo]
    #     self.compteur += 1
    #     self.playerTurn = not self.playerTurn
    #     if(self.playerTurn):
    #         #print("C'est au tour du joueur")
    #     else:
    #         #print("C'est au tour de l'ordinateur")

    #     #On remet les actions à None car on doit les recalculer
    #     self.bestAction=None
    #     self.worstAction=None
    #     return True

    def play(self,action):
        if(self.isPlayable()==False):
            #print("Il n'y a pas d'action possible à jouer")
            return False
        self.data=self.data["childrens"][action]

    def isPlayable(self): #verifie s'il y a des actions possibles à jouer
        return (self.data.get("strategy", 0) != 0)
    
    def dealcards(self,card):
        self.data=self.data["dealcards"][card]

    def setRandomPlayerHandFromRange(self):
        range=self.getRange()
        randomNomber=random.randint(0,len(range))
        hand = range[randomNomber]

        string_card1 = hand[:2]
        string_card2 = hand[2:]
        card1 = Cards.Card(Cards.get_suit_from_value(string_card1[1]),Cards.get_height_from_value(string_card1[0]),True)
        card2 = Cards.Card(Cards.get_suit_from_value(string_card2[1]),Cards.get_height_from_value(string_card2[0]),True)
        playerhand = [card1,card2]
        self.setPlayerHand(playerhand)

    def getPlayerPossiblities(self): # renvoie les proba de chaque actions possibles sous forme de dictionnaire avec les actions pour clés, utile pour la classe Partie
        dicoProba={}
        for i in range(len(self.data["strategy"]["actions"])):
            dicoProba.update({self.data["strategy"]["actions"][i]:round(self.data["strategy"]["strategy"][str(self.playerHand[0])+str(self.playerHand[1])][i]*100,3)})
        return dicoProba

    def getPlayerBestAction(self):
        '''Renvoie la meilleure action possible pour le joueur Check/Bet...'''    
        return max(self.getPlayerPossiblities(), key=self.getPlayerPossiblities().get)
    
    def getPlayerWorstAction(self):
        '''Renvoie la pire action possible pour le joueur Check/Bet...'''
        return min(self.getPlayerPossiblities(), key=self.getPlayerPossiblities().get)

    def getComputerActionProba(self):
        actions=self.getActions() # Pour récupérer le contenu des actions, renvoie une liste
        strategies=self.getStrategies() # Pour récupérer le contenu de toutes les paires possibles de l'ordi, renvoie un dico

        tab = [0]*len(actions) # tableau de la somme des probas de chaque action

        for i in range(len(actions)):
            for tabProba in strategies.values():
                tab[i] += tabProba[i]  # On fait la somme de toutes les probas de l'action i pour chaque paire de carte
                
                
        return actions,tab
        

    def categorize_pair(self,pair):
        card1, card2 = pair[0:2], pair[2:4]  # Extrait les deux cartes du format "2d3c"
        if card1[1] == card2[1]:  # Vérifie si les cartes ont la même forme (suites)
            return card1[0] + card2[0] + 's'
        else:  # Sinon, les cartes sont de formes différentes (offsuites)
            height1,heigth2=card1[0:1],card2[0:1]
            if(height1[0]==heigth2[0]):
                return card1[0]+card2[0]
            else:
                return card1[0] + card2[0] + 'o'

    def categorize_rangeIP(self):
        rangeIP_number={}
        rangeIP_final={}

        #la boucle suivante va permettre de mettre sous la bonne forme la rangeIP en faisant une moyenne sur les valeurs des pairs de même forme
        for pairCards in self.rangeIP.keys():
            pairCategorized=self.categorize_pair(pairCards)
            if(pairCategorized in rangeIP_number):
                rangeIP_number[pairCategorized]+=1
            else:
                rangeIP_number[pairCategorized]=1
            
            if(pairCategorized in rangeIP_final):
                rangeIP_final[pairCategorized]+=self.rangeIP[pairCards]
            else:
                rangeIP_final[pairCategorized]=self.rangeIP[pairCards]

        #calcule la moyenne
        for pairCardsCategorized in rangeIP_final.keys():
            rangeIP_final[pairCardsCategorized]/=rangeIP_number[pairCardsCategorized]

        return rangeIP_final
    
    def categorize_rangeOOP(self):
        rangeOOP_number={}
        rangeOOP_final={}
        #print("rangeOOP")
        #print(self.rangeOOP)
        #la boucle suivante va permettre de mettre sous la bonne forme la rangeOOP en faisant une moyenne sur les valeurs des pairs de même forme
        for pairCards in self.rangeOOP.keys():
            pairCategorized=self.categorize_pair(pairCards)
            if(pairCategorized in rangeOOP_number):
                rangeOOP_number[pairCategorized]+=1
            else:
                rangeOOP_number[pairCategorized]=1
            
            if(pairCategorized in rangeOOP_final):
                rangeOOP_final[pairCategorized]+=self.rangeOOP[pairCards]
            else:
                rangeOOP_final[pairCategorized]=self.rangeOOP[pairCards]

        #calcule la moyenne
        for pairCardsCategorized in rangeOOP_final.keys():
            rangeOOP_final[pairCardsCategorized]/=rangeOOP_number[pairCardsCategorized]

        return rangeOOP_final
        
    def updateRange(self,position,action):
        strategies=self.getStrategies()
        if(position==1):
            for pairCards in strategies.keys():
                if(pairCards in self.rangeIP):
                    self.rangeIP[pairCards]*=strategies[pairCards][action]
                else:
                    self.rangeIP[pairCards]=strategies[pairCards][action]
            #print("range IP")
            #print(self.rangeIP)
        else:
            for pairCards in strategies.keys():
                if(pairCards in self.rangeOOP):
                    self.rangeOOP[pairCards]*=strategies[pairCards][action]
                else:
                    self.rangeOOP[pairCards]=strategies[pairCards][action]
            #print("range OOP")
            #print(self.rangeOOP)

    def formattedRange(self,position):
        
        formatted_string = ""
        if(position==1):
            self.rangeIP=self.categorize_rangeIP()
            for index, (key, value) in enumerate(self.rangeIP.items()):
                pair = ''.join(key)
                formatted_string += f"{pair}:{value}"
                if index != len(self.rangeIP) - 1:
                    formatted_string += ","
        else:
            self.rangeOOP=self.categorize_rangeOOP()
            for index, (key, value) in enumerate(self.rangeOOP.items()):
                pair = ''.join(key)
                formatted_string += f"{pair}:{value}"
                if index != len(self.rangeOOP) - 1:
                    formatted_string += ","
        return formatted_string   
    
    def updateStackAndPot(self,action):#prend l'action sous forme de string et met à jour l'effective stack pour ensuite appeler le solveur avec la bonne valeur
        # Décodage de l'action
        action_parts = action.split()
        if len(action_parts) > 1: # On vérifie si l'action est bien un BET ou RAISE, et on diminue le montant de la stack
            if action_parts[0]=="BET":
                amount_str = action_parts[1].split(',')[0]  # Récupérer la partie avant la virgule.
                amount_str_without_point=amount_str.split('.')[0] # Permet de gérer le cas si c'est un point et non une virgule dans le montant.
                amount = int(amount_str_without_point)
                self.stack -= amount

                #On multiplie directement par 2 car :
                #Le joueur suivant: fold => fin de partie
                #Le joueur suivant: call => 2 fois la mise du BET dans le pot
                #Le joueur suivant: raise => scénario géré par la condition suivante
                self.pot +=2*amount 

            if action_parts[0]=="RAISE": #dans le cas d'un raise faut diminuer la stack que du montant du RAISE et augmenter le pot que 2 fois le montant du RAISE
                amount_str_current_action=action_parts[1].split(',')[0]
                amount_str_current_action_without_point=amount_str_current_action.split('.')[0]
                amount_str_action_before=self.actionBefore.split()[1].split(',')[0]
                amount_str_action_before_without_point=amount_str_action_before.split('.')[0]
                amount_stack=int(amount_str_current_action_without_point)-int(amount_str_action_before_without_point)
                self.stack-=amount_stack

                amount_bet=2*int(amount_str_current_action_without_point)-2*int(amount_str_action_before_without_point)
                self.pot+=amount_bet

        self.actionBefore=action
        #print("Stack ="+str(self.stack))
        #print("Pot ="+str(self.pot))

    
if(__name__=="__main__"):
    
    gt0=GameTree()
    gt1=GameTree(filePath="fichiersJson/sQhJh2.json",playerHand="playerHand",flop="Theo",river="river",turn="turn")
    #print(gt0)
    #print(gt1)
    GameTree.initialise("fichiersJson/sQhJh2.json","","","Corentin","")
    #print(gt0)
    #print(gt1)
    gt2=GameTree(filePath="fichiersJson/sQhJh2.json",playerHand="playerHand",flop="Theo",river="river",turn="turn")
    gt3=GameTree()
    #print(gt0)
    #print(gt1)
    #print(gt2)
    #print(gt3)
    filepath="fichiersJson/sQhJh2.json"
    # filepath2="PokerTrainer/Ressources/output_strategyTest.json"
    GameTree.initialise(filepath,"playerHand","flop","river","turn")
    #print(gt3)
    #print(gt3.getFlop())
    
