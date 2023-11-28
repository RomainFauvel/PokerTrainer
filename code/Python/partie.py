import joueur
import Cartes
import lectureFichierJson

class partie:
    def __init__(self,positionJoueur):
        self.position=positionJoueur
        self.joueur=lectureFichierJson.joueur("nomFichierJson","valeurCarteJoueur")
        #je te laisse faire théo tout ce qui touche à la partie je fais juste les parties que j'ai besoin pour récupérer les probas


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


        

