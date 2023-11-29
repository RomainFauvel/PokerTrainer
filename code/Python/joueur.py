import Cartes



class Joueur:
    def __init__(self, pos):
        #position=0 => ip , position=1 => oop
        self.position=pos
        self.main=None

    #permet de piocher 2 cartes dans le paquet
    def pioche(self,jeu):
        self.main=jeu.distribuer(2)

    
    def toStringIp(self):
        ip="AA,KK,QQ,JJ,TT,99:0.75,88:0.75,77:0.5,66:0.25,55:0.25,AK,AQs,AQo:0.75,AJs,AJo:0.5,ATs:0.75,A6s:0.25,A5s:0.75,A4s:0.75,A3s:0.5,A2s:0.5,KQs,KQo:0.5,KJs,KTs:0.75,K5s:0.25,K4s:0.25,QJs:0.75,QTs:0.75,Q9s:0.5,JTs:0.75,J9s:0.75,J8s:0.75,T9s:0.75,T8s:0.75,T7s:0.75,98s:0.75,97s:0.75,96s:0.5,87s:0.75,86s:0.5,85s:0.5,76s:0.75,75s:0.5,65s:0.75,64s:0.5,54s:0.75,53s:0.5,43s:0.5"
        if(self.position==1):
            return ip
        else:
            return self.toStringPaire()
        
    def toStringOop(self):
        oop="QQ:0.5,JJ:0.75,TT,99,88,77,66,55,44,33,22,AKo:0.25,AQs,AQo:0.75,AJs,AJo:0.75,ATs,ATo:0.75,A9s,A8s,A7s,A6s,A5s,A4s,A3s,A2s,KQ,KJ,KTs,KTo:0.5,K9s,K8s,K7s,K6s,K5s,K4s:0.5,K3s:0.5,K2s:0.5,QJ,QTs,Q9s,Q8s,Q7s,JTs,JTo:0.5,J9s,J8s,T9s,T8s,T7s,98s,97s,96s,87s,86s,76s,75s,65s,64s,54s,53s,43s"
        if(self.position==0):
            return oop
        else:
            return self.toStringPaire()

    # revoie un String correspondant à ceux utilisés par le solveur en prenant une liste de 2 cartes en entrée (une main)
    #tri les cartes et formate le string pour l'appel du solveur 
    def toStringPaire(self):
        carte1=self.main[0]
        carte2=self.main[1]
        hauteur_correspondance = {hauteur: index for index, hauteur in enumerate(Cartes.Hauteur)}
        res=f"{carte1.hauteur.value}{carte2.hauteur.value}"
        if(carte1.hauteur.value!=carte2.hauteur.value):
            #Modifier la comparaison qui ne marche pas bien
            if(hauteur_correspondance[carte1.hauteur] > hauteur_correspondance[carte2.hauteur]):
                res=f"{carte1.hauteur.value}{carte2.hauteur.value}"
            else:
                res=f"{carte2.hauteur.value}{carte1.hauteur.value}"
            if(carte1.couleur==carte2.couleur):
                return f"{res}s"
            else:
                return f"{res}o"
        else:
            res=f"{carte1.hauteur.value}{carte2.hauteur.value}"
            return res
       