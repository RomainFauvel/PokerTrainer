import Joueur
import GameEngine
import GameTree
import Solveur
import Scenario


class Partie:

    def __init__(self):
        self.scenario=Scenario.Scenario()
        self.position = int(input ("\nChoisissez la position 0 ou 1 \n"))
        self.tree=GameTree.GameTree()
        self.fichier=GameEngine.GameEngine()
        self.numTour=0

        self.arretTour=False
        self.arretPartie=False

    def demanderActionJoueur(self): #prend en paramètre les différentes actions que le joueur peut faire
        
        actionsjoueur = self.tree.getActions()
        for i in range(len(actionsjoueur)):
            print("Pour faire "+actionsjoueur[i]+" tapez "+str(i))
        
        return input("\nEntrez l'action choisie :\n")  # Récupérer l'action faite par le joueur (lire sur le clavier)
        
        
    def tour(self):
        if(self.position==0):

            if(self.numTour==0):
                self.tree.setRandomPlayerHandFromRange()
                self.numTour+=1

                print("main du joueur\n")
                print(str(self.tree.playerHand[0])+str(self.tree.playerHand[1])+"\n")
            
            actionsjoueur=self.tree.getActions() #récupère les différentes actions que le joueur peut faire

            indiceaction = self.demanderActionJoueur() #demande au joueur quelle action il veut faire

            self.tree.updateRange(0,int(indiceaction)) 

            print("<--------------------------------->")
            print(self.tree.getPlayerPossiblities()) #Cela recupère les probas pour chaque actions et les affiche
            print("<--------------------------------->\n")

            if(self.fichier.isEndOfGame(actionsjoueur[int(indiceaction)])==True):
                self.arretPartie=True
                return 0
            
            if(self.fichier.isEndOfRound(actionsjoueur[int(indiceaction)])==True):
                self.arretTour=True
            
            self.tree.updateStack(actionsjoueur[int(indiceaction)])
            
            self.tree.play(actionsjoueur[int(indiceaction)]) #Permet de modifier le chemin selon l'action du joueur

            if(self.arretTour==True):
                return 0
            
            ##############################################################

            actionOrdi=self.fichier.computerPlay(1)

            if(self.fichier.isEndOfGame(actionOrdi)==True):
                self.arretPartie=True
                return 0
            
            if(self.fichier.isEndOfRound(actionOrdi)==True):
                self.arretTour=True

            self.tree.updateStack(actionOrdi)

            self.tree.play(actionOrdi)  # on modifie le chemin en passant par children et l'action que doit effectuer l'ordi

            if(self.arretTour==True):
                return 0

        elif(self.position==1):

            actionOrdi=self.fichier.computerPlay(0)
            
            if(actionOrdi==False): 
                return "Piocher une carte"
            if(actionOrdi=="Fin de partie"):
                return "Fin de partie"
            
            self.tree.updateStack(actionOrdi)
            
            if(self.numTour==0):
                self.tree.setRandomPlayerHandFromRange()
                self.numTour+=1
                print(str(self.tree.playerHand[0])+str(self.tree.playerHand[1]))

            if(self.fichier.playerPlay()==False):
                return "Piocher une carte"
            
            actionsjoueur=self.tree.getActions() #récupère les différentes actions que le joueur peut faire

            indiceaction = self.demanderActionJoueur() #demande au joueur quelle action il veut faire

            self.tree.updateRange(1,int(indiceaction))

            self.tree.updateStack(actionsjoueur[int(indiceaction)])

            print("<--------------------------------->")
            print(self.fichier.playerPlay()) #Cela recupère les probas pour chaque actions et les affiche
            print("<--------------------------------->\n")

            if(self.fichier.isEndOfGame(actionsjoueur[int(indiceaction)])==True):
                return "Fin de partie"
            
            self.tree.play(actionsjoueur[int(indiceaction)]) #Permet de modifier le chemin selon l'action du joueur
            
            return "Fin du tour"
    
        print("erreur")

    def jouerUnePartie(self):
        while(self.arretPartie!=True): #condition d'arret ligne 50
            self.arretTour=False
            while(self.arretTour!=True and self.arretPartie!=True): #tant qu'on ne doit pas de piocher de carte on continue à jouer dans le même tour
                self.tour()
                print("Arret Tour = "+str(self.arretTour))
                print("Arret Partie = "+str(self.arretPartie))
            if(self.numTour==1 and self.arretPartie!=True):
                self.tree.dealcards("2c") #permet de piocher une carte pour la turn ou la river à modifier pour pas avoir tjrs la même carte
                self.numTour+=1
            elif(self.arretPartie!=True):
                Solveur.solveurRiver()
                GameTree.GameTree(filePath="output_result.json")
                #self.tree.dealcards("2s") #permet de piocher une carte pour la turn ou la river à modifier pour pas avoir tjrs la même carte
        print("Fin de la partie")

if __name__ == "__main__":
            
    partie1=Partie()
    partie1.jouerUnePartie()
