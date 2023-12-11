import Joueur
import LectureFichierJson


class Partie:

    def __init__(self,nomJsonAOuvrir,ValeurCarte):
        self.position = int(input ("Choisissez la position 0 ou 1 \n"))
        self.fichier=LectureFichierJson.LectureFichierJson(nomJsonAOuvrir,ValeurCarte) #Ouvre le fichier Json après l'appel au solveur

    def demanderActionJoueur(self,actionsjoueur): #prend en paramètre les différentes actions que le joueur peut faire
        
        for i in range(len(actionsjoueur)):
            print("Pour faire "+actionsjoueur[i]+" tapez "+str(i))
        
        return input("Entrez l'action choisie : \n")  # Récupérer l'action faite par le joueur (lire sur le clavier)
        
        
    def tour(self):
        if(self.position==0):
            print("cas 1")
            if(self.fichier.faireJouerJoueur()==False): #Permet de tester si on doit ou pas tourner une carte
                return "Piocher une carte"
            
            actionsjoueur=self.fichier.recupActions() #récupère les différentes actions que le joueur peut faire

            indiceaction = self.demanderActionJoueur(actionsjoueur) #demande au joueur quelle action il veut faire

            print(self.fichier.faireJouerJoueur()) #Cela recupère les probas pour chaque actions et les affiche

            if(actionsjoueur[int(indiceaction)]=="FOLD"): #car fin de partie quand fold
                return "Fin de partie"
            
            self.fichier.setData(actionsjoueur[int(indiceaction)]) #Permet de modifier le chemin selon l'action du joueur

            actionOrdi=self.fichier.faireJouerOrdi()

            if(actionOrdi==False):
                return "Piocher une carte"
            if(actionOrdi=="Fin de partie"):
                return "Fin de partie"

            return "Fin du tour"

        elif(self.position==1):
            print("cas 2")

            actionOrdi=self.fichier.faireJouerOrdi()
            
            if(actionOrdi==False): 
                return "Piocher une carte"
            if(actionOrdi=="Fin de partie"):
                return "Fin de partie"
        
            
            if(self.fichier.faireJouerJoueur()==False):
                return "Piocher une carte"
            
            actionsjoueur=self.fichier.recupActions() #récupère les différentes actions que le joueur peut faire

            indiceaction = self.demanderActionJoueur(actionsjoueur) #demande au joueur quelle action il veut faire

            print(self.fichier.faireJouerJoueur()) #Cela recupère les probas pour chaque actions et les affiche

            if(actionsjoueur[int(indiceaction)]=="FOLD"):
                return "Fin de partie"
            
            self.fichier.setData(actionsjoueur[int(indiceaction)]) #Permet de modifier le chemin selon l'action du joueur
            
            return "Fin du tour"
    
        print("erreur")

    def jouerUnePartie(self):
        arret=False
        nbCarte=1
        while(arret!=True): #condition d'arret ligne 50
            Etat="Fin du tour"
            while(Etat=="Fin du tour"): #tant qu'on ne doit pas de piocher de carte on continue à jouer dans le même tour
                Etat=self.tour()
                if(Etat=="Fin de partie"):
                    print("Fin de partie")
                    return 0       
            if(nbCarte==1):
                self.fichier.dealcards("2c") #permet de piocher une carte pour la turn ou la river à modifier pour pas avoir tjrs la même carte
                nbCarte+=1
            else:
                self.fichier.dealcards("2s") #permet de piocher une carte pour la turn ou la river à modifier pour pas avoir tjrs la même carte

        

partie1=Partie("Ressources/output_strategyTest.json","KsKh")
partie1.jouerUnePartie()
