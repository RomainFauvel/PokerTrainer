import ijson

with open("C:\\Users\\buche\\OneDrive\\Documents\\INSA_Rennes\\3A_INFO\\EtudePratique", 'r') as fichier:
        # Créer un lecteur ijson
    lecteur = ijson.items(fichier, 'output_strategy.json')

        # Iterer sur les objets du fichier JSON
    for objet in lecteur:
            # Faire quelque chose avec chaque objet
        print(objet)