import re
import Cards
import subprocess
import Joueur
import GameTree


gameTree=GameTree.GameTree()

def solveurRiver():
    ecritureEntreeRiver()
    lancerSolveur()

def solveurTurn():
    ecritureEntreeTurn()
    lancerSolveur()

#modifie le fichier texte qui sert d'entrée au solveur (version Linux pour le moment)
def ecritureEntreeRiver():
    modify_line("Solveur/resources/text/commandline_sample_input.txt",r'^set_board.*$',f"{gameTree.flop[0]}{gameTree.flop[1]}{gameTree.flop[2]}{gameTree.river}")
def ecritureEntreeTurn():
    modify_line("Solveur/resources/text/commandline_sample_input.txt", r'^set_board.*$',f"{gameTree.flop[0]}{gameTree.flop[1]}{gameTree.flop[2]}{gameTree.river}{gameTree.turn}")

#lance le solveur (version Linux pour le moment)
def lancerSolveur():
    script = "code/scriptLancement.sh"
    subprocess.run([script])


def modify_line(file_name, regex_pattern, new_content):
    try:
        # Open the file in read mode
        with open(file_name, 'r') as f:
            lines = f.readlines()
        # Find the line containing the regex pattern
        for i, line in enumerate(lines):
            if re.search(regex_pattern, line):
                lines[i] += new_content + '\n'
                break
        # Open the file in write mode and rewrite the modified lines
        with open(file_name, 'w') as f:
            f.writelines(lines)
        print("The line has been successfully modified.")
    except FileNotFoundError:
        print(f"The file '{file_name}' does not exist.")



