import PaquetDeCartes
import Scenario
import Joueur


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

def test(position):
    p1=Partie(0)
    p1.paquetDeCartes.afficher_cartes(p1.scenario.flop)
    p1.paquetDeCartes.afficher_cartes(p1.river)
    p1.paquetDeCartes.afficher_cartes(p1.turn)
    print("======================================\nmain:")
    p1.paquetDeCartes.afficher_cartes(p1.joueur.main)

test(1)