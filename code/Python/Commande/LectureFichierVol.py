import ijson

with open("C:\\Users\\buche\\Documents\\INSA_Rennes\\3A_INFO\\EtudePratique\\output_strategy.json", 'r') as fichier:
        # Créer un lecteur ijson
    lecteur=ijson.items(fichier,'')

    strategy=next(lecteur,None)
    actions=strategy.get("childrens")
    print(actions)