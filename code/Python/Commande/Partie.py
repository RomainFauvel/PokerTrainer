
import Joueur
import Cartes
import LectureFichierJson
import Solveur

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
            print(self.faireJouerJoueur())
            self.fichier.faireJouerOrdi()
        else:
            self.fichier.faireJouerOrdi()
            self.faireJouerJoueur()
        

        
    #meme principe que le tourFLOP
    def tourTurnCard(self,turnCard):
        self.fichier.data=self.fichier.data["dealcards"][turnCard] # remplacer turnCard ! au début du tour on modifie le chemin pour se placer au prochain tour
        # self.joueur.faireJouerOrdi() si c'est à l'ordi de jouer mais pas faite pour l'instant cette fonction
        self.fichier.setData(actionARealiser="")
        return self.fichier.recupProba()
    
    def tourRiver(self,river):
        self.fichier.data=self.fichier.data["dealcards"][river]
        # self.joueur.faireJouerOrdi() si c'est à l'ordi de jouer mais pas faite pour l'instant cette fonction
        self.fichier.setData(actionARealiser="")
        return self.fichier.recupProba()

        # faudra faire différents cas quand un joueur peut encore jouer ou pas selon s'il a fait tapis au tour d'avant extc


        

partie1=Partie(0,"\\Users\\buche\\OneDrive\\Documents\\GitHub\\PokerTrainer\\code\\Solveur\\resources\\output_result.json","KdJd")
print(partie1.tour())
