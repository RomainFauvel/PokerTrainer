import PaquetDeCartes
import Scenario
import Joueur


class Partie:
    def __init__(self,position):
        self.paquetDeCartes=PaquetDeCartes.creationJeu()
        self.scenario=Scenario.Scenario()
        self.paquetDeCartes.retirerFlop(self.scenario.flop)

        self.joueur=Joueur.Joueur(position,self.paquetDeCartes.distribuer(2))

        self.river=self.paquetDeCartes.distribuer(1)
        self.turn = self.paquetDeCartes.distribuer(1)


p1=Partie(0)
p1.paquetDeCartes.afficher_cartes(p1.scenario.flop)

p1.paquetDeCartes.afficher_cartes(p1.river)

p1.paquetDeCartes.afficher_cartes(p1.turn)
print("======================================\nmain:")
p1.paquetDeCartes.afficher_cartes(p1.joueur.main)
