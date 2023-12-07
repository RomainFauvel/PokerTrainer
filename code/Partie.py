import PaquetDeCartes
import Scenario
import Joueur
import LectureFichierJson


class Partie:
    def __init__(self,position):
        #On crée un paquet de cartes et un scénario (On retire le flop du scénario dans le paquet de cartes)
        self.paquetDeCartes=PaquetDeCartes.creationJeu()
        self.scenario=Scenario.Scenario()
        self.paquetDeCartes.retirerFlop(self.scenario.flop)
        #On initialise le joueur a partir de sa position et on pioche sa main
        self.joueur=Joueur.Joueur(position,self.paquetDeCartes.distribuer(2))
        #On pioche la carte river et turn
        self.river=self.paquetDeCartes.distribuer(1)
        self.turn = self.paquetDeCartes.distribuer(1)
        
        self.fichier=LectureFichierJson.LectureFichierJson(f"./fichiersJson/{self.scenario.nomFichierJson}",f"{self.joueur.main[0]}{self.joueur.main[1]}")


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
            return True

        elif(self.position==1):
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
            return True

    def jouerUnePartie(self):
        arret=False
        self.position = input ("Choisissez la position 0 ou 1\n")  #Faudra checker l'input du joueur qd c'est sur terminal
        print(self.position)
        while(arret!=True): #condition d'arret ligne 50
            boolean=True
            while(boolean==True): #tant qu'on ne doit pas de piocher de carte on continue à jouer dans le même tour
                boolean=self.tour()
                print(boolean)
            if (self.fichier.data["node_type"] == "chance_node"):
                arret = True
                print("Fin de partie")
                return 0
            self.fichier.dealcards(f"{self.river}") #permet de piocher une carte pour la turn ou la river à modifier pour pas avoir tjrs la même carte


        

partie1=Partie(0)
partie1.jouerUnePartie()



    
def test(position):
    p1=Partie(0)
    p1.paquetDeCartes.afficher_cartes(p1.scenario.flop)
    p1.paquetDeCartes.afficher_cartes(p1.river)
    p1.paquetDeCartes.afficher_cartes(p1.turn)
    print("======================================\nmain:")
    p1.paquetDeCartes.afficher_cartes(p1.joueur.main)

