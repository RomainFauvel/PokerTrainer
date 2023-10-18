import premierApproche
import subprocess


def ecritureEntree():
    with open("Solveur/resources/text/commandline_sample_input.txt", "w") as fichier:
        fichier.write(f"set_pot 50\nset_effective_stack 200\nset_board {flop[0]},{flop[1]},{flop[2]}\nset_range_ip AA,KK,QQ,JJ,TT,99:0.75,88:0.75,77:0.5,66:0.25,55:0.25,AK,AQs,AQo:0.75,AJs,AJo:0.5,ATs:0.75,A6s:0.25,A5s:0.75,A4s:0.75,A3s:0.5,A2s:0.5,KQs,KQo:0.5,KJs,KTs:0.75,K5s:0.25,K4s:0.25,QJs:0.75,QTs:0.75,Q9s:0.5,JTs:0.75,J9s:0.75,J8s:0.75,T9s:0.75,T8s:0.75,T7s:0.75,98s:0.75,97s:0.75,96s:0.5,87s:0.75,86s:0.5,85s:0.5,76s:0.75,75s:0.5,65s:0.75,64s:0.5,54s:0.75,53s:0.5,43s:0.5\nset_range_oop QQ:0.5,JJ:0.75,TT,99,88,77,66,55,44,33,22,AKo:0.25,AQs,AQo:0.75,AJs,AJo:0.75,ATs,ATo:0.75,A9s,A8s,A7s,A6s,A5s,A4s,A3s,A2s,KQ,KJ,KTs,KTo:0.5,K9s,K8s,K7s,K6s,K5s,K4s:0.5,K3s:0.5,K2s:0.5,QJ,QTs,Q9s,Q8s,Q7s,JTs,JTo:0.5,J9s,J8s,T9s,T8s,T7s,98s,97s,96s,87s,86s,76s,75s,65s,64s,54s,53s,43s\nset_bet_sizes oop,flop,bet,50\nset_bet_sizes oop,flop,raise,60\nset_bet_sizes oop,flop,allin\nset_bet_sizes ip,flop,bet,50\nset_bet_sizes ip,flop,raise,60\nset_bet_sizes ip,flop,allin\nset_bet_sizes oop,turn,bet,50\nset_bet_sizes oop,turn,raise,60\nset_bet_sizes oop,turn,allin\nset_bet_sizes ip,turn,bet,50\nset_bet_sizes ip,turn,raise,60\nset_bet_sizes ip,turn,allin\nset_bet_sizes oop,river,bet,50\nset_bet_sizes oop,river,donk,50\nset_bet_sizes oop,river,raise,60,100\nset_bet_sizes oop,river,allin\nset_bet_sizes ip,river,bet,50\nset_bet_sizes ip,river,raise,60,100\nset_bet_sizes ip,river,allin\nset_allin_threshold 0.67\nbuild_tree\nset_thread_num 8\nset_accuracy 0.4\nset_max_iteration 100\nset_print_interval 10\nset_use_isomorphism 1\nstart_solve\nset_dump_rounds 2\ndump_result output_result.json")

def lancerSolveur():
    
    script = "./scriptLancement.sh"
    subprocess.run([script])

jeu =premierApproche.creationJeu()
flop=premierApproche.JeuDeCartes.distribuer(jeu,3)  
ecritureEntree()
lancerSolveur()
