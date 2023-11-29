
import Joueur
import Cartes
import lectureFichierJson
import Solveur

class Partie:

    def __init__(self,position):
        self.paquetDeCartes=Cartes.creationJeu()
        self.joueur=Joueur.Joueur(position)
        self.board=self.paquetDeCartes.distribuer(5)
        self.joueur.pioche(self.paquetDeCartes)


    #modifie le fichier d'entrée du solveur et lance automatiquement le solveur
    def appelerSolveur(self):
        Solveur.ecritureEntree(self.board,self.joueur)
        Solveur.lancerSolveur()

    


    def tourFlop(self):
        # self.joueur.faireJouerOrdi() si c'est à l'ordi de jouer mais pas faite pour l'instant cette fonction

        # doit demander à l'interface ce que joue le joueur
        # il faut rester dans le flop tant que qqun mise plus que l'autre d'avant
        # après avoir récupéré l'action du joueur, 
        # je modifie le chemin actuel dans l'arbre pour pouvoir récupérer proba ordi puis du prochain tour 
        self.joueur.setData(actionARealiser="")  # renvoie vrai si la modif a bien été effectuée
        return self.joueur.recupProba() # renvoie les proba pour le flop

        
    #meme principe que le tourFLOP
    def tourTurnCard(self,turnCard):
        self.joueur.data=self.joueur.data["dealcards"][turnCard] # remplacer turnCard ! au début du tour on modifie le chemin pour se placer au prochain tour
        # self.joueur.faireJouerOrdi() si c'est à l'ordi de jouer mais pas faite pour l'instant cette fonction
        self.joueur.setData(actionARealiser="")
        return self.joueur.recupProba()
    
    def tourRiver(self,river):
        self.joueur.data=self.joueur.data["dealcards"][river]
        # self.joueur.faireJouerOrdi() si c'est à l'ordi de jouer mais pas faite pour l'instant cette fonction
        self.joueur.setData(actionARealiser="")
        return self.joueur.recupProba()

        # faudra faire différents cas quand un joueur peut encore jouer ou pas selon s'il a fait tapis au tour d'avant extc


        

partie1=Partie(1)

partie1.appelerSolveur()

    