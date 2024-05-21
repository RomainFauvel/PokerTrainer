import re
import Cards
import subprocess
import Joueur
import GameTree
import os
import platform


gameTree=GameTree.GameTree()

def solveurRiver():
    ecritureEntreeRiver()
    print("le script est lancé")
    run_script()
    print("fin du script")

# def solveurTurn():
#     ecritureEntreeTurn()
#     run_script()

#modifie le fichier texte qui sert d'entrée au solveur
def ecritureEntreeRiver():
    with open("code/Solveur/TexasSolverWindows/resources/text/commandline_sample_input.txt", "w") as fichier:
        fichier.write(
            f"set_pot {str(gameTree.pot)}\nset_effective_stack {str(gameTree.stack)}\nset_board {gameTree.flop[0]},{gameTree.flop[1]},{gameTree.flop[2]},{gameTree.turn[0]},{gameTree.river[0]}\nset_range_oop {gameTree.formattedRange(0)}\nset_range_ip {gameTree.formattedRange(1)}\nset_bet_sizes oop,flop,bet,50\nset_bet_sizes oop,flop,raise,60\nset_bet_sizes oop,flop,allin\nset_bet_sizes ip,flop,bet,50\nset_bet_sizes ip,flop,raise,60\nset_bet_sizes ip,flop,allin\nset_bet_sizes oop,turn,bet,50\nset_bet_sizes oop,turn,raise,60\nset_bet_sizes oop,turn,donk,50\nset_bet_sizes oop,turn,allin\nset_bet_sizes ip,turn,bet,50\nset_bet_sizes ip,turn,raise,60\nset_bet_sizes ip,turn,allin\nset_bet_sizes oop,river,bet,50\nset_bet_sizes oop,river,raise,60,100\nset_bet_sizes oop,river,allin\nset_bet_sizes ip,river,bet,50\nset_bet_sizes ip,river,raise,60,100\nset_bet_sizes oop,river,donk,50\nset_bet_sizes ip,river,allin\nset_allin_threshold 0.67\nset_raise_limit 3\nbuild_tree\nset_thread_num 8\nset_accuracy 0.5\nset_max_iteration 200\nset_print_interval 10\nset_use_isomorphism 1\nstart_solve\nset_dump_rounds 1\ndump_result output_result.json")
            #AA,KK,QQ,JJ,TT,99:0.75,88:0.75,77:0.5,66:0.25,55:0.25,AK,AQs,AQo:0.75,AJs,AJo:0.5,ATs:0.75,A6s:0.25,A5s:0.75,A4s:0.75,A3s:0.5,A2s:0.5,KQs,KQo:0.5,KJs,KTs:0.75,K5s:0.25,K4s:0.25,QJs:0.75,QTs:0.75,Q9s:0.5,JTs:0.75,J9s:0.75,J8s:0.75,T9s:0.75,T8s:0.75,T7s:0.75,98s:0.75,97s:0.75,96s:0.5,87s:0.75,86s:0.5,85s:0.5,76s:0.75,75s:0.5,65s:0.75,64s:0.5,54s:0.75,53s:0.5,43s:0.5
            #QQ:0.5,JJ:0.75,TT,99,88,77,66,55,44,33,22,AKo:0.25,AQs,AQo:0.75,AJs,AJo:0.75,ATs,ATo:0.75,A9s,A8s,A7s,A6s,A5s,A4s,A3s,A2s,KQ,KJ,KTs,KTo:0.5,K9s,K8s,K7s,K6s,K5s,K4s:0.5,K3s:0.5,K2s:0.5,QJ,QTs,Q9s,Q8s,Q7s,JTs,JTo:0.5,J9s,J8s,T9s,T8s,T7s,98s,97s,96s,87s,86s,76s,75s,65s,64s,54s,53s,43s
# def ecritureEntreeTurn():
#     with open("code/Solveur/resources/text/commandline_sample_input.txt", "w") as fichier:
#         fichier.write(
#             f"set_pot 50\nset_effective_stack 200\nset_board {gameTree.flop[0]},{gameTree.flop[1]},{gameTree.flop[2]},{gameTree.turn[0]}\nset_range_ip :AA,KK,QQ,JJ,TT,99:0.75,88:0.75,77:0.5,66:0.25,55:0.25,AK,AQs,AQo:0.75,AJs,AJo:0.5,ATs:0.75,A6s:0.25,A5s:0.75,A4s:0.75,A3s:0.5,A2s:0.5,KQs,KQo:0.5,KJs,KTs:0.75,K5s:0.25,K4s:0.25,QJs:0.75,QTs:0.75,Q9s:0.5,JTs:0.75,J9s:0.75,J8s:0.75,T9s:0.75,T8s:0.75,T7s:0.75,98s:0.75,97s:0.75,96s:0.5,87s:0.75,86s:0.5,85s:0.5,76s:0.75,75s:0.5,65s:0.75,64s:0.5,54s:0.75,53s:0.5,43s:0.5\nset_range_oop QQ:0.5,JJ:0.75,TT,99,88,77,66,55,44,33,22,AKo:0.25,AQs,AQo:0.75,AJs,AJo:0.75,ATs,ATo:0.75,A9s,A8s,A7s,A6s,A5s,A4s,A3s,A2s,KQ,KJ,KTs,KTo:0.5,K9s,K8s,K7s,K6s,K5s,K4s:0.5,K3s:0.5,K2s:0.5,QJ,QTs,Q9s,Q8s,Q7s,JTs,JTo:0.5,J9s,J8s,T9s,T8s,T7s,98s,97s,96s,87s,86s,76s,75s,65s,64s,54s,53s,43s\nset_bet_sizes oop,flop,bet,50\nset_bet_sizes oop,flop,raise,60\nset_bet_sizes oop,flop,allin\nset_bet_sizes ip,flop,bet,50\nset_bet_sizes ip,flop,raise,60\nset_bet_sizes ip,flop,allin\nset_bet_sizes oop,turn,bet,50\nset_bet_sizes oop,turn,raise,60\nset_bet_sizes oop,turn,allin\nset_bet_sizes ip,turn,bet,50\nset_bet_sizes ip,turn,raise,60\nset_bet_sizes ip,turn,allin\nset_bet_sizes oop,river,bet,50\nset_bet_sizes oop,river,donk,50\nset_bet_sizes oop,river,raise,60,100\nset_bet_sizes oop,river,allin\nset_bet_sizes ip,river,bet,50\nset_bet_sizes ip,river,raise,60,100\nset_bet_sizes ip,river,allin\nset_allin_threshold 0.67\nbuild_tree\nset_thread_num 8\nset_accuracy 0.4\nset_max_iteration 100\nset_print_interval 10\nset_use_isomorphism 1\nstart_solve\nset_dump_rounds 1\ndump_result output_result.json")

def solveurRiverTest():
    ecritureTest()
    run_script()

def ecritureTest():
    with open("code/Solveur/TexasSolverWindows/resources/text/commandline_sample_input.txt", "w") as fichier:
        fichier.write(
            f"set_pot 50\nset_effective_stack 200\nset_board As,3s,Tc,8h,Ts\nset_range_oop 22:0.024,33:0.0,43s:0.126,44:0.187,53s:0.15,54s:0.256,55:0.358,64s:0.078,65s:0.107,66:0.66,75s:0.057,76s:0.123,76o:0.0,77:0.69,86s:0.08,87s:0.02,87o:0.0,88:0.547,97s:0.083,98s:0.04,98o:0.0,99:0.768,A2s:0.987,A2o:0.952,A3s:0.63,A3o:0.411,A4s:0.982,A4o:0.984,A5s:0.951,A5o:0.961,A6s:0.835,A6o:0.865,A7s:0.788,A7o:0.759,A8s:0.621,A8o:0.616,A9s:0.689,A9o:0.587,AJs:0.309,AJo:0.185,AKs:0.0,AKo:0.004,AQs:0.061,AQo:0.011,ATo:0.356,AA:0.993,ATs:0.405,J6s:0.111,J7s:0.165,J8s:0.163,J9s:0.159,JTo:0.915,JJ:0.9,JTs:0.924,K2s:0.071,K3s:0.317,K4s:0.151,K5s:0.201,K6s:0.168,K7s:0.15,K7o:0.0,K8s:0.179,K8o:0.0,K9s:0.15,K9o:0.0,KJs:0.789,KJo:0.617,KQs:0.946,KQo:0.926,KTo:0.994,KK:0.996,KTs:0.995,Q5s:0.141,Q6s:0.109,Q7s:0.064,Q8s:0.117,Q9s:0.149,Q9o:0.0,QJs:0.657,QJo:0.376,QTo:0.934,QQ:0.98,QTs:0.922,T7s:0.997,T8s:0.755,T9o:0.885,T9s:0.938,TT:0.801\nset_range_ip 22:0.029,33:0.0,43s:0.414,44:0.039,53s:0.358,54s:0.054,55:0.121,64s:0.005,65s:0.003,66:0.001,75s:0.008,76s:0.019,76o:0.101,77:0.0,86s:0.274,87s:0.13,87o:0.216,88:0.0,97s:0.05,98s:0.166,98o:0.146,99:0.0,A2s:0.033,A2o:0.135,A3s:0.0,A3o:0.0,A4s:0.032,A4o:0.085,A5s:0.098,A5o:0.13,A6s:0.104,A6o:0.134,A7s:0.178,A7o:0.212,A8s:0.053,A8o:0.036,A9s:0.0,A9o:0.004,AJs:0.0,AJo:0.0,AKs:0.0,AKo:0.0,AQs:0.0,AQo:0.0,ATo:0.0,AA:0.173,ATs:0.0,J6s:0.427,J7s:0.5,J8s:0.257,J9s:0.623,JTo:0.112,JJ:0.044,JTs:0.03,K2s:0.526,K3s:0.32,K4s:0.66,K5s:0.547,K6s:0.15,K7s:0.15,K7o:0.229,K8s:0.012,K8o:0.079,K9s:0.001,K9o:0.003,KJs:0.137,KJo:0.394,KQs:0.012,KQo:0.153,KTo:0.065,KK:0.0,KTs:0.007,Q5s:0.675,Q6s:0.379,Q7s:0.272,Q8s:0.1,Q9s:0.333,Q9o:0.465,QJs:0.248,QJo:0.559,QTo:0.101,QQ:0.074,QTs:0.051,T7s:0.002,T8s:0.0,T9o:0.092,T9s:0.022,TT:0.0\nset_bet_sizes oop,flop,bet,50\nset_bet_sizes oop,flop,raise,60\nset_bet_sizes oop,flop,allin\nset_bet_sizes ip,flop,bet,50\nset_bet_sizes ip,flop,raise,60\nset_bet_sizes ip,flop,allin\nset_bet_sizes oop,turn,bet,50\nset_bet_sizes oop,turn,raise,60\nset_bet_sizes oop,turn,donk,50\nset_bet_sizes oop,turn,allin\nset_bet_sizes ip,turn,bet,50\nset_bet_sizes ip,turn,raise,60\nset_bet_sizes ip,turn,allin\nset_bet_sizes oop,river,bet,50\nset_bet_sizes oop,river,raise,60,100\nset_bet_sizes oop,river,allin\nset_bet_sizes ip,river,bet,50\nset_bet_sizes ip,river,raise,60,100\nset_bet_sizes oop,river,donk,50\nset_bet_sizes ip,river,allin\nset_allin_threshold 0.67\nset_raise_limit 3\nbuild_tree\nset_thread_num 8\nset_accuracy 0.5\nset_max_iteration 200\nset_print_interval 10\nset_use_isomorphism 1\nstart_solve\nset_dump_rounds 1\ndump_result output_result.json")
      
def run_script():
    system = platform.system()
    if system == "Linux":
        os.system("./code/Solveur/resources/console_solver -i text/commandline_sample_input.txt")
        print("linux")
    elif system == "Windows":
        chemin_executable = "code/Solveur/TexasSolverWindows/console_solver.exe"
        chemin_fichier_texte = "code/Solveur/TexasSolverWindows/resources/text/commandline_sample_input.txt"
        subprocess.run([chemin_executable,"--input_file",chemin_fichier_texte])
        print("windows")
    else:
        print("Système d'exploitation non pris en charge.")


#lance le solveur (version Linux pour le moment)
#def lancerSolveur():
#    script = "code/Solveur/scriptLancement.sh"
#    subprocess.run([script])



solveurRiverTest()


