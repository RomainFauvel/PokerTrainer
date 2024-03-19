import os
import random
import Cards
import GameTree


class Scenario:
    def __init__(self):
        # recuperation d'un fichier Json aléatoirement
        folder = "./fichiersJson"
        self.nameFile = [f for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f))]
        #initialisation du scenario que l'on stock ensuite dans le GameTree
        # creation du flop a partir du titre du fichier json
        carte1 = CardsFromScenario(self.nameFile[:2])
        carte2 = CardsFromScenario(self.nameFile[2:4])
        carte3 = CardsFromScenario(self.nameFile[4:6])
        self.flop = [carte1, carte2, carte3]
        self.deck=Cards.DeckOfCards()
        self.deck.deleteFlopFromDeck(self.flop)
        self.deck.shuffle()
        self.playerHand=self.deck.dealCards(2)
        self.river=self.deck.dealCards(1)
        self.turn=self.deck.dealCards(1)
        #on crée le GameTree avec tous les elements de la partie
        self.tree = GameTree.GameTree(self.nameFile,self.playerHand,self.flop,self.river,self.turn)

# methode utile pour obtenir les 3 cartes du flop a partir du name du fichier Json
def CardsFromScenario(name):
    correspondingSuit = next(c for c in Cards.Suit if c.value == name[0])
    correspondingHigh = next(h for h in Cards.High if h.value == name[1])
    return Cards.Card(correspondingSuit, correspondingHigh)