import Joueur
import LectureFichierJson


class Partie:

    def __init__(self,nomJsonAOuvrir,ValeurCarte):
        self.position=0
        self.fichier=LectureFichierJson.LectureFichierJson(nomJsonAOuvrir,ValeurCarte) #Ouvre le fichier Json après l'appel au solveur
        
    def faireJouerJoueur(self):
        if(self.fichier.data.get("strategy",0)!=0):  # Si pas de strategy, retourne 0
            return self.fichier.recupProba()
        else:
            return False
        
    def tour(self):
        if(self.position==0):
            if(self.faireJouerJoueur()==False): #Permet de tester si on doit ou pas tourner une carte
                return False
            print(self.faireJouerJoueur()) #Cela recupère les probas pour chaque actions
            actionsjoueur = self.fichier.recupActions()
            for i in range(len(actionsjoueur)):
               print("Pour faire "+actionsjoueur[i]+" tapez "+str(i))
            indiceaction = input("Entrez l'action choisie :")  # Récupérer l'action faite par le joueur (lire sur le clavier)
            self.fichier.setData(actionsjoueur[int(indiceaction)]) #Permet de modifier le chemin selon l'action du joueur
            
            if(self.fichier.faireJouerOrdi()==False):
                return False
            self.fichier.faireJouerOrdi()

        else:
            if(self.fichier.faireJouerOrdi()==False):
                return False
            self.fichier.faireJouerOrdi()
            if(self.faireJouerJoueur()==False):
                return False
            
            print(self.faireJouerJoueur())
            actionsjoueur = self.fichier.recupActions()
            for i in range(len(actionsjoueur)):
                print("Pour faire " + actionsjoueur[i] + " tapez " + str(i))
            indiceaction = input(
                "Entrez l'action choisie :")  # Récupérer l'action faite par le joueur (lire sur le clavier)
            self.fichier.setData(actionsjoueur[int(indiceaction)])  # Permet de modifier le chemin selon l'action du joueur

    def jouerUnePartie(self):
        arret=False
        self.position = input ("Choisissez la position 0 ou 1")  #Faudra checker l'input du joueur qd c'est sur terminal
        while(arret!=True): #condition d'arret ligne 50
            boolean=True
            while(boolean==True): #tant qu'on ne doit pas de piocher de carte on continue à jouer dans le même tour
                boolean=self.tour()
            if (self.fichier.data["node_type"] == "chance_node"):
                arret = True
                print("Fin de partie")
                return 0
            self.fichier.dealcards("3c") #permet de piocher une carte pour la turn ou la river à modifier pour pas avoir tjrs la même carte


        

partie1=Partie("C:\\Users\maths\Documents\Documents INSA\Etude pratique\TexasSolver-v0.2.0-Windows\\resources\outputs\output_strategybon.json","KdJd")
partie1.jouerUnePartie()
