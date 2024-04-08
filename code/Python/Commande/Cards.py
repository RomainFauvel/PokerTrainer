import random
from enum import Enum
from itertools import product
import os
import customtkinter as tk
import customtkinter
from PIL import Image



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
    def __init__(self, suit, height,flip=False):
        self.suit = suit
        self.height = height
        self.flip = flip #Carte face cachée si false et retournée si true
        #self.show = show #Afficher ou cache la carte (True->affiche,False->cache)      <-------------- Tentative de faire un attribut pour afficher et caché la carte mais c'est assez galère donc on verra si on en a vraiment besoin
        self.image = self.get_image()
        #self.setShow(self.show)
    
    def randomCard(self):
        self.suit=random.choice(list(Suit))
        self.height=random.choice(list(Height))

    def __str__(self):
        return f"{self.height.value}{self.suit.value}"
    
    def get_image(self):

        #Chemin vers le bon dossier, ici, on revient en arrière vers le dossier PokerTrainer (la racine)
        current_path = os.path.dirname(os.path.realpath(__file__))
        parent_path = os.path.abspath(os.path.join(current_path,"..","..",".."))

        if (self.flip):
            if(self.suit == "c"):
                return customtkinter.CTkImage(Image.open(parent_path + "/Ressources/Flat Playing Cards Set/Clubs/" + self.height + ".png"), size=(100, 150))
            elif(self.suit == "d"):
                return customtkinter.CTkImage(Image.open(parent_path + "/Ressources/Flat Playing Cards Set/Diamonds/" + self.height + ".png"), size=(100, 150))
            elif(self.suit == "s"):
                return customtkinter.CTkImage(Image.open(parent_path + "/Ressources/Flat Playing Cards Set/Spades/" + self.height + ".png"), size=(100, 150))
            elif(self.suit == "h"):
                return customtkinter.CTkImage(Image.open(parent_path + "/Ressources/Flat Playing Cards Set/Hearts/" + self.height + ".png"), size=(100, 150))
            else:
                return "ERREUR"

        else:
            #Dans le cas où flip est false, on laisse la carte face cachée
            return customtkinter.CTkImage(Image.open(parent_path + "/Ressources/img/back_card.png"), size=(100, 150))    #carte face cachée
        
    #Setter de flip
    def setFlip(self,bool):
        self.flip = bool
        self.get_image()
    def getFlip(self):
        return self.flip
    
    def getSuit(self):
        return self.suit
    
    def getHeight(self):
        return self.height

    #méthode qui permet de passer de cette écriture: cA     à une écriture séparée: c A     et met les éléments dans une liste
    #permet de réutiliser cette écriture pour la création des cartes (utilsé dans le play.py)
    def splitIn2(textCard):
        card = []
        card.append(textCard.getSuit().value)
        card.append(textCard.getHeight().value)
        print(card)
        return card
    



class DeckOfCards:
    def __init__(self):
        suits = list(Suit)
        heights = list(Height)
        # Crée le jeu de cards sans doublons
        self.cards = [Card(suit, height) for suit in suits for height in heights]

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

    def deleteFlopFromDeck(self,flop):
        print(flop[0])
        # print(self.cards)
        for f in flop:
            for c in self.cards:
                if f.getHeight() == c.getHeight() and f.getSuit() == c.getSuit():
                    self.cards.remove(c)
                    print("removed",c)
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
    


