import customtkinter
import tkinter
import os

def get_display_size():
    root = tkinter.Tk()
    root.update_idletasks()
    root.attributes('-fullscreen', True)
    root.state('iconic')
    height = root.winfo_screenheight()
    width = root.winfo_screenwidth()
    root.destroy()
    return height, width


def getIndexMax(tab):  # Fonction pour récupérer l'indice de la valeur max dans un tableau
        res=0
        max=tab[0]
        for i in range(len(tab)):
            if(tab[i]>max):
                res=i
                max=tab[i]
        return res