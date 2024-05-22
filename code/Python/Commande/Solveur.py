import os
import platform
import subprocess

def executer_script():
    systeme = platform.system()
    if systeme == "Linux":
        chemin_executable = os.path.abspath("./code/Solveur/resources/console_solver")
        chemin_fichier_texte = os.path.abspath("./text/test.txt")
        
        # Vérification de l'existence des fichiers
        if not os.path.isfile(chemin_executable):
            print(f"L'exécutable n'existe pas : {chemin_executable}")
            return
        if not os.path.isfile(chemin_fichier_texte):
            print(f"Le fichier texte n'existe pas : {chemin_fichier_texte}")
            return
        
        commande = f"{chemin_executable} -i {chemin_fichier_texte}"
        try:
            result = subprocess.run(commande, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            print("linux")
            print("Sortie standard :", result.stdout)
            print("Erreurs :", result.stderr)
        except subprocess.CalledProcessError as e:
            print("Erreur lors de l'exécution :", e)
            print("Sortie standard :", e.stdout)
            print("Erreurs :", e.stderr)
    elif systeme == "Windows":
        chemin_executable = os.path.abspath("code/Solveur/TexasSolverWindows/console_solver.exe")
        chemin_fichier_texte = os.path.abspath("code/Solveur/TexasSolverWindows/resources/text/test.txt")
        
        # Vérification de l'existence des fichiers
        if not os.path.isfile(chemin_executable):
            print(f"L'exécutable n'existe pas : {chemin_executable}")
            return
        if not os.path.isfile(chemin_fichier_texte):
            print(f"Le fichier texte n'existe pas : {chemin_fichier_texte}")
            return
        
        commande = [chemin_executable, "--input_file", chemin_fichier_texte]
        try:
            result = subprocess.run(commande, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            print("windows")
            print("Sortie standard :", result.stdout)
            print("Erreurs :", result.stderr)
        except subprocess.CalledProcessError as e:
            print("Erreur lors de l'exécution :", e)
            print("Sortie standard :", e.stdout)
            print("Erreurs :", e.stderr)
    else:
        print("Système d'exploitation non pris en charge.")

executer_script()
