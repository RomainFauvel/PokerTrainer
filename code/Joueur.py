
#Un joueur a une position (Ip ou Oop avec 0 ou 1)
#et une main composée de 2 cartes
class Joueur:
    def __init__(self,position,main):
        self.position=position
        self.main=main