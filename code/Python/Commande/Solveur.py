import Cards
import subprocess
import Joueur

#modifie le fichier texte qui sert d'entrée au solveur (version Linux pour le moment)
def ecritureEntreeRiver(board,joueur):
    with open("code/Solveur/resources/text/commandline_sample_input.txt", "w") as fichier:
        fichier.write(f"set_pot 50\nset_effective_stack 200\nset_board {board[0]},{board[1]},{board[2]}\nset_range_ip {joueur.toStringIp()}\nset_range_oop {joueur.toStringOop()}\nset_bet_sizes oop,flop,bet,50\nset_bet_sizes oop,flop,raise,60\nset_bet_sizes oop,flop,allin\nset_bet_sizes ip,flop,bet,50\nset_bet_sizes ip,flop,raise,60\nset_bet_sizes ip,flop,allin\nset_bet_sizes oop,turn,bet,50\nset_bet_sizes oop,turn,raise,60\nset_bet_sizes oop,turn,allin\nset_bet_sizes ip,turn,bet,50\nset_bet_sizes ip,turn,raise,60\nset_bet_sizes ip,turn,allin\nset_bet_sizes oop,river,bet,50\nset_bet_sizes oop,river,donk,50\nset_bet_sizes oop,river,raise,60,100\nset_bet_sizes oop,river,allin\nset_bet_sizes ip,river,bet,50\nset_bet_sizes ip,river,raise,60,100\nset_bet_sizes ip,river,allin\nset_allin_threshold 0.67\nbuild_tree\nset_thread_num 8\nset_accuracy 0.5\nset_max_iteration 200\nset_print_interval 10\nset_use_isomorphism 1\nstart_solve\nset_dump_rounds 2\ndump_result output_result.json")

def ecritureEntreeTurn(board,joueur):
    with open("code/Solveur/resources/text/commandline_sample_input.txt", "w") as fichier:
        fichier.write(f"set_pot 50\nset_effective_stack 200\nset_board {board[0]},{board[1]},{board[2]}\nset_range_ip {joueur.toStringIp()}\nset_range_oop {joueur.toStringOop()}\nset_bet_sizes oop,flop,bet,50\nset_bet_sizes oop,flop,raise,60\nset_bet_sizes oop,flop,allin\nset_bet_sizes ip,flop,bet,50\nset_bet_sizes ip,flop,raise,60\nset_bet_sizes ip,flop,allin\nset_bet_sizes oop,turn,bet,50\nset_bet_sizes oop,turn,raise,60\nset_bet_sizes oop,turn,allin\nset_bet_sizes ip,turn,bet,50\nset_bet_sizes ip,turn,raise,60\nset_bet_sizes ip,turn,allin\nset_bet_sizes oop,river,bet,50\nset_bet_sizes oop,river,donk,50\nset_bet_sizes oop,river,raise,60,100\nset_bet_sizes oop,river,allin\nset_bet_sizes ip,river,bet,50\nset_bet_sizes ip,river,raise,60,100\nset_bet_sizes ip,river,allin\nset_allin_threshold 0.67\nbuild_tree\nset_thread_num 8\nset_accuracy 0.5\nset_max_iteration 200\nset_print_interval 10\nset_use_isomorphism 1\nstart_solve\nset_dump_rounds 2\ndump_result output_result.json")


#lance le solveur (version Linux pour le moment)
def lancerSolveur():
    
    script = "code/scriptLancement.sh"
    subprocess.run([script])
