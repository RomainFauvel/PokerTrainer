import os
import random
import Cards
import GameTree
import random
import play


class Scenario:

    def __init__(self):
        # recuperation d'un fichier Json aléatoirement
        folder = "./fichiersJson"
        self.nameFile = [f for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f))]
        #initialisation du scenario que l'on stock ensuite dans le GameTree
        # creation du flop a partir du titre du fichier json
        i=random.randint(0,len(self.nameFile)-1)
        carte1 = CardsFromScenario(self.nameFile[i][:2])
        carte2 = CardsFromScenario(self.nameFile[i][2:4])
        carte3 = CardsFromScenario(self.nameFile[i][4:6])
        self.flop = [carte1, carte2, carte3]
        self.deck=Cards.DeckOfCards()
        self.deck.deleteFlopFromDeck(self.flop)
        self.deck.shuffle()
        self.playerHand=None #self.deck.dealCards(2) j'ai mis en commentaire car je gère le piochage de la main après dans la gameTree pour être sûr que la paire du joueur soit possible 
        self.river=self.deck.dealCards(1)
        self.turn=self.deck.dealCards(1)
        #on crée le GameTree avec tous les elements de la partie
        print(self.nameFile[i])
        print(str(self.flop))
        print(str(self.turn))
        print(str(self.river))
        self.tree = GameTree.GameTree("fichiersJson/"+self.nameFile[i],self.playerHand,self.flop,self.river,self.turn)
        print("tree in scenario "+str(self.tree))
        self.deck.deleteHandFromDeck(self.tree.playerHand)


# methode utile pour obtenir les 3 cartes du flop a partir du name du fichier Json
def CardsFromScenario(name):
    correspondingSuit = next(c for c in Cards.Suit if c.value == name[0])
    correspondingHigh = next(h for h in Cards.Height if h.value == name[1])
    return Cards.Card(correspondingSuit, correspondingHigh)


if(__name__=="__main__"):
    scenario=Scenario()
    # print(scenario.tree.data)
    # print(scenario.tree.getActions())
    # print(scenario.tree.getStrategies()
    gameTree = GameTree.GameTree()
    print(gameTree.getFlop())
    print(gameTree.getFlop()[1])
