
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
            cls._instance.__initialized = False
        return cls._instance

    def __init__(self,filePath=None,playerHand=None,flop=None,river=None,turn=None): #initialisation de la classe
        if self.__initialized: return

        if(not(filePath==None and playerHand==None)):
            with open(filePath,'r') as json_file:
                self.data=json.load(json_file)
            self.playerHand=playerHand
            self.flop=flop
            self.river=river
            self.turn=turn
            self.__initialized = True
            print("GameTree initialized")
            self.compteur = 0



    def rolloutToInit(self,file,val):
        self.__initialized = False
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
        

    def getPlayerPossiblities(self): # renvoie les proba de chaque actions possibles sous forme de dictionnaire avec les actions pour clés 
        dicoProba={}
        for i in range(len(self.data["strategy"]["actions"])):
            dicoProba.update({self.data["strategy"]["actions"][i]:round(self.data["strategy"]["strategy"][self.playerHand][i]*100,3)})
        return dicoProba

    