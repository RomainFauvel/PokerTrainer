
class GameTree:
    data=None  #contient sous forme de dico les données du fichier json qui va être modifié selon les actions du joueur et de l'ordi
    valeurCarte=None #valeur de la carte du joueur/ordi

    def __init__(self,nomFichier,valeurCarte):
        with open(nomFichier,'r') as json_file:
            self.data=json.load(json_file)
        self.valeurCarte=valeurCarte


    def play(self,actionARealiser): # modifie le chemin pour prendre en compte l'action réalisée par le joueur/Ordi
        self.data=self.data["childrens"][actionARealiser]
        return True

    def isPlayable(self):
        return (self.data.get("strategy", 0) == 0)


    #getters

    def getActions(self):
        return self.data["strategy"]["actions"]

    def getStrategies(self):
        return self.data["strategy"]["strategy"]

    def getPlayerPossiblities(self): # renvoie les proba de chaque actions possibles sous forme de dictionnaire avec les actions pour clés 
        dicoProba={}
        for i in range(len(self.data["strategy"]["actions"])):
            dicoProba.update({self.data["strategy"]["actions"][i]:round(self.data["strategy"]["strategy"][self.valeurCarte][i]*100,3)})
        return dicoProba

    