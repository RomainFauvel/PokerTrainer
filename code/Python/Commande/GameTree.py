
import json

class GameTree:
    data=None  #contient sous forme de dico les données du fichier json qui va être modifié selon les actions du joueur et de l'ordi
    playerHand=None #valeur de la carte du joueur/ordi
    flop=None
    river=None
    turn=None

    _instance = None

    def __new__(cls, *args, **kwargs): #Creation d'un singleton pour avoir une seule sdd partagee entre les classes
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    #Initialisation de la classe avec les valeurs si elles sont donnees sinon, on donne juste la reference de la classe
    def __init__(self,filePath=None,playerHand=None,flop=None,river=None,turn=None): #initialisation de la classe

        if(not(filePath==None and playerHand==None and flop==None and river==None and turn==None)):
            self.initialise(filePath,playerHand,flop,river,turn) 
    
    #Peux etre acceder depuis l exterieur sans initialiser un objet (exemple: GameTree.initialise(filePath,playerHand,flop,river,turn))
    @classmethod
    def initialise(cls,filePath,playerHand,flop,river,turn):
        if(cls._instance is None):
            cls._instance = cls()
        with open(filePath) as f:
            cls._instance.data = json.load(f)
        cls._instance.setPlayerHand(playerHand)
        cls._instance.setFlop(flop)
        cls._instance.setRiver(river)
        cls._instance.setTurn(turn)
        cls._instance.compteur=0



    def rolloutToInit(self,file,val):
        self.__init__(file,val)

        

    def play(self,todo): # se deplace dans l arbre en prenant en compte l'action réalisée par le joueur/Ordi
        self.data=self.data["childrens"][todo]
        self.compteur += 1
        return True

    def isPlayable(self): #verifie si il y a des actions possibles à jouer
        return (self.data.get("strategy", 0) != 0)
    
    def dealcards(self,cartepiochee):
        self.data=self.data["dealcards"][cartepiochee]


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
    
    # setters

    def setPlayerHand(self, playerHand):
        self.playerHand = playerHand

    def setFlop(self, flop):
        self.flop = flop

    def setRiver(self, river):
        self.river = river

    def setTurn(self, turn):
        self.turn = turn

    def to_string(self):
        return "GameTree: playerHand: " + str(self.playerHand) + " flop: " + str(self.flop) + " river: " + str(self.river) + " turn: " + str(self.turn)


if(__name__=="__main__"):
    gt0=GameTree()
    gt1=GameTree(filePath="Ressources/output_strategyTest.json",playerHand="playerHand",flop="Theo",river="river",turn="turn")
    print(gt0.to_string())
    print(gt1.to_string())
    GameTree.initialise("Ressources/output_strategyTest.json","","","Corentin","")
    print(gt0.to_string())
    print(gt1.to_string())
    gt2=GameTree(filePath="Ressources/output_strategyTest.json",playerHand="playerHand",flop="Theo",river="river",turn="turn")
    gt3=GameTree()
    print(gt0.to_string())
    print(gt1.to_string())
    print(gt2.to_string())
    print(gt3.to_string())
