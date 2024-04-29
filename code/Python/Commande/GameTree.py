
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

    rangeOOP={}
    rangeIP={}

    _instance = None

    def __new__(cls, *args, **kwargs): #Creation d'un singleton pour avoir une seule sdd partagee entre les classes
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    #Initialisation de la classe avec les valeurs si elles sont donnees sinon, on donne juste la reference de la classe
    def __init__(self,filePath=None,playerHand=None,flop=None,river=None,turn=None,rangeOOP=None,rangeIP=None): #initialisation de la classe
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
        print(filePath)
        with open(filePath) as f:
            cls._instance.setData(json.load(f))
        cls._instance.setPlayerHand(playerHand)
        cls._instance.setFlop(flop)
        cls._instance.setRiver(river)
        cls._instance.setTurn(turn)
        cls._instance.compteur=0
        cls._instance.setRandomPlayerHandFromRange()



    def rolloutToInit(self,file,val):
        self.__init__(file,val)

        

    def play(self,todo): # se deplace dans l arbre en prenant en compte l'action réalisée par le joueur/Ordi
        self.data=self.data["childrens"][todo]
        self.compteur += 1
        return True

    def isPlayable(self): #verifie si il y a des actions possibles à jouer
        return (self.data.get("strategy", 0) != 0)
    
    def dealcards(self,card):
        self.data=self.data["dealcards"][card]

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

    def to_string(self):
        return "GameTree: playerHand: " + str(self.playerHand) + " flop: " + str(self.flop) + " river: " + str(self.river) + " turn: " + str(self.turn)

    def getPlayerPossiblities(self): # renvoie les proba de chaque actions possibles sous forme de dictionnaire avec les actions pour clés, utile pour la classe Partie
        dicoProba={}
        for i in range(len(self.data["strategy"]["actions"])):
            dicoProba.update({self.data["strategy"]["actions"][i]:round(self.data["strategy"]["strategy"][str(self.playerHand[0])+str(self.playerHand[1])][i]*100,3)})
        return dicoProba
    
    def categorize_pair(self,pair):
        card1, card2 = pair[0:2], pair[2:4]  # Extrait les deux cartes du format "2d3c"
        if card1[1] == card2[1]:  # Vérifie si les cartes ont la même forme (suites)
            return card1[0] + card2[0] + 's'
        else:  # Sinon, les cartes sont de formes différentes (offsuites)
            return card1[0] + card2[0] + 'o'

    
    def updateRange(self,position,action):
        strategies=self.getStrategies()
        if(position==1):
            self.rangeIP={} #faut la remettre à 0 pour éviter d'avoir des cartes inutiles qu'on aurait déjà mis dans les tours d'avant 
            for pairCards in strategies.keys():
                pairCategorized=self.categorize_pair(pairCards)
                self.rangeIP[pairCategorized]=strategies[pairCards][action]
        else:
            self.rangeOOP={}
            for pairCards in strategies.keys():
                pairCategorized=self.categorize_pair(pairCards)
                self.rangeOOP[pairCategorized]=strategies[pairCards][action]

    def formattedRange(self,position):
        formatted_string = ""
        if(position==0):
            for index, (key, value) in enumerate(self.rangeIP.items()):
                pair = ''.join(key)
                rounded_value = round(value, 10)
                formatted_string += f"{pair}:{rounded_value}"
                if index != len(self.rangeIP) - 1:
                    formatted_string += ","
        else:
            for index, (key, value) in enumerate(self.rangeOOP.items()):
                pair = ''.join(key)
                rounded_value = round(value, 10)
                formatted_string += f"{pair}:{rounded_value}"
                if index != len(self.rangeOOP) - 1:
                    formatted_string += ","
        return formatted_string
    
    
if(__name__=="__main__"):
    
    gt0=GameTree()
    gt1=GameTree(filePath="fichiersJson/sQhJh2.json",playerHand="playerHand",flop="Theo",river="river",turn="turn")
    print(gt0.to_string())
    print(gt1.to_string())
    GameTree.initialise("fichiersJson/sQhJh2.json","","","Corentin","")
    print(gt0.to_string())
    print(gt1.to_string())
    gt2=GameTree(filePath="fichiersJson/sQhJh2.json",playerHand="playerHand",flop="Theo",river="river",turn="turn")
    gt3=GameTree()
    print(gt0.to_string())
    print(gt1.to_string())
    print(gt2.to_string())
    print(gt3.to_string())
    filepath="fichiersJson/sQhJh2.json"
    # filepath2="PokerTrainer/Ressources/output_strategyTest.json"
    GameTree.initialise(filepath,"playerHand","flop","river","turn")
    print(gt3.to_string())
    print(gt3.getFlop())
    
