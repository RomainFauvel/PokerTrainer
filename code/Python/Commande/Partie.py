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

    def demanderActionJoueur(self): #prend en paramètre les différentes actions que le joueur peut faire
        
        actionsjoueur = self.tree.getActions()
        for i in range(len(actionsjoueur)):
            print("Pour faire "+actionsjoueur[i]+" tapez "+str(i))
        
        return input("\nEntrez l'action choisie :\n")  # Récupérer l'action faite par le joueur (lire sur le clavier)
        
        
    def tour(self):
        if(self.position==0):
            if(self.fichier.playerPlay()==False): #Permet de tester si on doit ou pas tourner une carte
                return "Piocher une carte"
            
            actionsjoueur=self.tree.getActions() #récupère les différentes actions que le joueur peut faire

            indiceaction = self.demanderActionJoueur() #demande au joueur quelle action il veut faire

            print("<--------------------------------->")
            print(self.fichier.playerPlay()) #Cela recupère les probas pour chaque actions et les affiche
            print("<--------------------------------->\n")

            if(actionsjoueur[int(indiceaction)]=="FOLD"): #car fin de partie quand fold
                return "Fin de partie"
            
            self.tree.play(actionsjoueur[int(indiceaction)]) #Permet de modifier le chemin selon l'action du joueur

            actionOrdi=self.fichier.computerPlay()
            print(actionOrdi)

            if(actionOrdi==False):
                return "Piocher une carte"
            if(actionOrdi=="Fin de partie"):
                return "Fin de partie"

            return "Fin du tour"

        elif(self.position==1):

            actionOrdi=self.fichier.computerPlay()
            
            if(actionOrdi==False): 
                return "Piocher une carte"
            if(actionOrdi=="Fin de partie"):
                return "Fin de partie"
        
            
            if(self.fichier.playerPlay()==False):
                return "Piocher une carte"
            
            actionsjoueur=self.tree.getAction() #récupère les différentes actions que le joueur peut faire

            indiceaction = self.demanderActionJoueur() #demande au joueur quelle action il veut faire

            print("<--------------------------------->")
            print(self.fichier.playerPlay()) #Cela recupère les probas pour chaque actions et les affiche
            print("<--------------------------------->\n")

            if(actionsjoueur[int(indiceaction)]=="FOLD"):
                return "Fin de partie"
            
            self.tree.play(actionsjoueur[int(indiceaction)]) #Permet de modifier le chemin selon l'action du joueur
            
            return "Fin du tour"
    
        print("erreur")

    def jouerUnePartie(self):
        arret=False
        nbCarte=1
        while(arret!=True): #condition d'arret ligne 50
            Etat="Fin du tour"
            while(Etat=="Fin du tour"): #tant qu'on ne doit pas de piocher de carte on continue à jouer dans le même tour
                Etat=self.tour()
                print(Etat)
                if(Etat=="Fin de partie"):
                    print("<--------------------------------->")
                    print("Fin de partie")
                    print("<--------------------------------->\n")
                    return 0       
            if(nbCarte==1):
                self.tree.dealcards("2c") #permet de piocher une carte pour la turn ou la river à modifier pour pas avoir tjrs la même carte
                nbCarte+=1
                print("\nLa turn card est : \n")
                print("┌───────┐")
                print("│ 2     │")
                print("│       │")
                print("│   ♦   │")
                print("│       │")
                print("│     2 │")
                print("└───────┘\n")
            else:
                Solveur.solveurRiver()
                GameTree.GameTree(filePath="code/Solveur/resources/outputs/outputs_strategy.json")
                #self.tree.dealcards("2s") #permet de piocher une carte pour la turn ou la river à modifier pour pas avoir tjrs la même carte
                
                print("\nLa river card est : \n")
                print("┌───────┐")
                print("│ 2     │")
                print("│       │")
                print("│   ♠   │")
                print("│       │")
                print("│     2 │")
                print("└───────┘\n")




if __name__ == "__main__":
            
    partie1=Partie()
    print("\nVotre main est : \n")

    print("┌───────┐ ┌───────┐")
    print("│ K     │ │ K     │")
    print("│       │ │       │")
    print("│   ♠   │ │   ♥   │")
    print("│       │ │       │")
    print("│     K │ │     K │")
    print("└───────┘ └───────┘\n")

    print("\nLes cartes du board sont : \n")

    print("┌───────┐ ┌───────┐ ┌───────┐")
    print("│ Q     │ │ J     │ │ 2     │")
    print("│       │ │       │ │       │")
    print("│   ♠   │ │   ♥   │ │   ♥   │")
    print("│       │ │       │ │       │")
    print("│     Q │ │     J │ │     2 │")
    print("└───────┘ └───────┘ └───────┘\n")
    partie1.jouerUnePartie()
