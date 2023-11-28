from asyncio.windows_events import NULL
import json

#import pprint

read_jsonOOP='outputOOP.json'
read_jsonIP='outputIP.json'


# faire un chemin de parcours du tableau et dès qu'il y a une action on ajoute pour savoir où on en est dans l'arbre 

"""
with open(read_jsonOOP,'r') as json_file:
    dataOOP=json.load(json_file)
#pprint.pprint(data)

with open(read_jsonIP,'r') as json_fileIP:
    dataIP=json.load(json_fileIP)

#Fonction qui récupère les proba de OOP après le FLOP
def FlopOOP(valeurCarte,donnees):
    dico=donnees["strategy"]
    while(dico["actions"]!=NULL):
        for i in range(len(dico["actions"])):
            print(dico["actions"][i]+" "+str(round(dico["strategy"][valeurCarte][i],3)*100))
            print("\n")
        dico=dico["actions"]   
        
#FlopOOP("QcTd",dataOOP)


def FlopIN(actionOOP,valeurCarte,donnees):
    dico=donnees["childrens"][actionOOP]["strategy"]
    for i in range(len(dico["actions"])):
        print(dico["actions"][i]+" "+str(round(dico["strategy"][valeurCarte][i],3)*100))
    print("\n")


FlopOOP("QcTd", dataOOP)
"""
class JoueurIP():

    dataIP=NULL  #contient sous forme de dico les données du fichier json qui va être modifié selon les actions du joueur et de l'ordi
    valeurCarteIN="" #contient la valeur de la carte du joueur
    
    def __init__(self,nomFichier,valeurCarte):
        with open(nomFichier,'r') as json_file:
            self.dataIP=json.load(json_file)
        self.valeurCarteIP=valeurCarte
        
    def FlopIP(self):
        return self.dataIP["strategy"]["strategy"][self.valeurCarteIN]
    
    def setDataIP(self,actionARealiser):
        if(actionARealiser=="CALL" or actionARealiser=="CHECK"):
            self.dataIP=self.dataIP["childrens"][actionARealiser]["dealcards"]
            return True
        else:
            self.dataIP=self.dataIP["childrens"][actionARealiser]
            return False
    
    