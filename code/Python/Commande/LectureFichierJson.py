
import json

class LectureFichierJson:

    data=None  #contient sous forme de dico les données du fichier json qui va être modifié selon les actions du joueur et de l'ordi
    valeurCarte="" #contient la paire de cartes du joueur sous la forme "AsJh"

    def __init__(self,nomFichier,valeurCarte):
        with open(nomFichier,'r') as json_file:
            self.data=json.load(json_file)
        self.valeurCarte=valeurCarte

    def recupProba(self): # renvoie les proba pour le flop pour joueur IP
        return self.data["strategy"]["strategy"][self.valeurCarte]

    def setData(self,actionARealiser): # modifie le chemin pour prendre en compte l'action réalisée par le joueur
        self.data=self.data["childrens"][actionARealiser]
        return True

    def faireJouerOrdi(self):
        if (self.data.get("strategy", 0, ) != 0):
            actions = self.data["strategy"]["actions"]  # Pour récupérer le contenu des actions
            coupajouer = self.data["strategy"][
                "strategy"]  # Pour récupérer le contenu de toutes les paires possibles de l'ordi
            tab = []  # tableau de la somme des probas de chaque action
            for i in range(len(actions)):
                for carte in coupajouer:
                    tab[i] += carte[i]  # On fait la somme de toutes les probas de l'action i pour chaque paire de carte
            actionordi = self.recupmax(tab)  # On récupère l'indice de l'action à jouer
            self.setData(actions[
                             actionordi])  # on modifie le chemin en passant par children et l'action que doit effectuer l'ordi
        else:
            cartepiochee =""# cartepiochee = appeler fonction pour piocher une carte
            self.dealcards(cartepiochee)

    def recupmax(self,tab):                             # Fonction pour récupérer l'indice de la valeur max dans un tableau
        res=0
        for i in range(len(tab)-1):
            if(tab[i]<tab[i+1]):
                res=i+1
        return res
   
    def recupActions(self):
        return self.data["strategy"]["actions"]     # retourne un tableau contenant les actions possibles du joueur (pour savoir à quoi correspondent les probas)
    def dealcards(self,cartepiochee):
        self.data=self.data["dealcards"][cartepiochee]


