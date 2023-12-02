import Joueur
import LectureFichierJson


class Partie:

    def __init__(self,position,nomJsonAOuvrir,ValeurCarte):
        self.joueur=Joueur.Joueur(position)  # créer un joueur avec la bonne position
        self.joueur.main=ValeurCarte # donne au joueur la main correspondante à la partie 
        self.fichier=LectureFichierJson.LectureFichierJson(nomJsonAOuvrir,ValeurCarte) #Ouvre le fichier Json après l'appel au solveur
        
    def faireJouerJoueur(self):
        if(self.fichier.data.get("strategy",0)!=0):
            return self.fichier.recupProba()
        else:
            return False
        
    def tour(self):
        if(self.joueur.position==0):
            if(self.faireJouerJoueur()==False): #Permet de tester si on doit ou pas tourner une carte
                return False
            
            self.faireJouerJoueur() #Cela recupère les probas pour chaque actions

            self.fichier.setData() #Permet de modifier le chemin selon l'action du joueur
            
            if(self.fichier.faireJouerOrdi()==False):
                return False
            self.fichier.faireJouerOrdi()

        else:
            if(self.fichier.faireJouerOrdi()==False):
                return False
            self.fichier.faireJouerOrdi()
            if(self.faireJouerJoueur()==False):
                return False
            
            self.faireJouerJoueur()
            self.fichier.setData("Demander à l'interface ce que le joueur choisi de faire")

    def jouerUnePartie(self):
        arret=False
        while(arret!=True): #condition d'arret ligne 50
            boolean=True
            while(boolean==True): #tant qu'on ne doit pas de piocher de carte on continue à jouer dans le même tour
                boolean=self.tour()
            self.fichier.dealcards("3c") #permet de piocher une carte pour la turn ou la river à modifier pour pas avoir tjrs la même carte
            if(self.fichier.data["node_type"]=="chance_node"):
                arret=True
        print("Fin de partie")    


        

partie1=Partie(0,"\\Users\\buche\\OneDrive\\Documents\\GitHub\\PokerTrainer\\code\\Solveur\\resources\\output_result.json","KdJd")

