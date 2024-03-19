import Cards


class Joueur:
    def __init__(self, pos):
        #position=0 => ip , position=1 => oop
        self.position=pos
        self.hand=None

    #permet de piocher 2 cards dans le paquet
    def pick2Cards(self,deck):
        self.hand=deck.dealCards(2)

    
    def toStringIp(self):
        ip="AA,KK,QQ,JJ,TT,99:0.75,88:0.75,77:0.5,66:0.25,55:0.25,AK,AQs,AQo:0.75,AJs,AJo:0.5,ATs:0.75,A6s:0.25,A5s:0.75,A4s:0.75,A3s:0.5,A2s:0.5,KQs,KQo:0.5,KJs,KTs:0.75,K5s:0.25,K4s:0.25,QJs:0.75,QTs:0.75,Q9s:0.5,JTs:0.75,J9s:0.75,J8s:0.75,T9s:0.75,T8s:0.75,T7s:0.75,98s:0.75,97s:0.75,96s:0.5,87s:0.75,86s:0.5,85s:0.5,76s:0.75,75s:0.5,65s:0.75,64s:0.5,54s:0.75,53s:0.5,43s:0.5"
        if(self.position==1):
            return ip
        else:
            return self.toStringPaireSolveur()
        
    def toStringOop(self):
        oop="QQ:0.5,JJ:0.75,TT,99,88,77,66,55,44,33,22,AKo:0.25,AQs,AQo:0.75,AJs,AJo:0.75,ATs,ATo:0.75,A9s,A8s,A7s,A6s,A5s,A4s,A3s,A2s,KQ,KJ,KTs,KTo:0.5,K9s,K8s,K7s,K6s,K5s,K4s:0.5,K3s:0.5,K2s:0.5,QJ,QTs,Q9s,Q8s,Q7s,JTs,JTo:0.5,J9s,J8s,T9s,T8s,T7s,98s,97s,96s,87s,86s,76s,75s,65s,64s,54s,53s,43s"
        if(self.position==0):
            return oop
        else:
            return self.toStringPaireSolveur()

    #renvoie un String correspondant à ceux utilisés par le solveur en prenant une liste de 2 cards en entrée (une hand)
    #tri les cards et formate le string pour l'appel du solveur 
    def toStringPaireSolveur(self):
        card1=self.hand[0]
        card2=self.hand[1]
        cardHeight = {height: index for index, height in enumerate(Cards.height)}
        res=f"{card1.height.value}{card2.height.value}"
        if(card1.height.value!=card2.height.value):
            #Modifier la comparaison qui ne marche pas bien
            if(cardHeight[card1.height] > cardHeight[card2.height]):
                res=f"{card1.height.value}{card2.height.value}"
            else:
                res=f"{card2.height.value}{card1.height.value}"
            if(card1.couleur==card2.couleur):
                return f"{res}s"
            else:
                return f"{res}o"
        else:
            res=f"{card1.height.value}{card2.height.value}"
            return res
       
    
       