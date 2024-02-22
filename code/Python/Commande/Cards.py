import random
from enum import Enum
from itertools import product



class Suit(Enum):
    SPADES="s"
    HEARTS="h"
    DIAMONDS="d"
    CLUBS="c"

class Height(Enum):
    TWO="2"
    THREE="3"
    FOUR="4"
    FIVE="5"
    SIX="6"
    SEVEN="7"
    EIGHT="8"
    NINE="9"
    TEN="T"
    JACK="J"
    QUEEN="Q"
    KING="K"
    ACE="A"




class Card:
    #attributs de la classe
    def __init__(self, suit, height):
        self.suit = suit
        self.height = height
    
    def randomCard(self):
        self.suit=random.choice(list(Suit))
        self.height=random.choice(list(Height))

    def __str__(self):
        return f"{self.height.value}{self.suit.value}"
    



class DeckOfCards:
    def __init__(self):
        suits = list(Suit)
        heights = list(Height)
        # Crée le jeu de cards sans doublons
        self.cards = [Card(suit, height) for suit in suits for height in heights]
        self.hand = None

    #melange le jeu
    def shuffle(self):
        random.shuffle(self.cards)

    #distribue dans une liste le nombre de cards demandées en les supprimant du jeu de cards
    def dealCards(self, number_of_cards):
        if number_of_cards > len(self.cards):
            print("Il n'y a pas assez de cartes pour distribuer.")
            return None
        hand = self.cards[:number_of_cards]
        self.cards = self.cards[number_of_cards:]
        return hand

    #affiche le jeu de cards
    def displayCards(self, cards):
        for card in cards:
            print(card)

    #renvoie la paire de cards du joueur sous la forme "AsJh"
    def toStringPaireLectureJson(self):
        card1=self.hand[0]
        card2=self.hand[1]
        cardHeight = {height: index for index, height in enumerate(self.height)}
        #Modifier la comparaison qui ne marche pas bien
        if(cardHeight[card1.height] > cardHeight[card2.height]):
            res=f"{card1}{card2}"
        else:
            res=f"{card2}{card1}"
        return res
            


# créer un jeu et le mélange (utile en début de partie)
def creationJeu():
    deck = DeckOfCards()
    deck.shuffle()
    return deck
    


