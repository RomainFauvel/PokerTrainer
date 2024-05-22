from PIL import Image
import tkinter
import customtkinter
import os

import Cards as Cards
import GameTree as GameTree
import Scenario as Scenario
import GameEngine as GameEngine
import Solveur as Solveur
import TopLevelWindow as TopLevelWindow

import home as home

import time


class Play(customtkinter.CTkFrame):

    

    def __init__(self, master: any, width: int = 200, height: int = 200):
        super().__init__(master, width, height)
        self.master = master
        self.width = width
        self.height = height

                
        self.home = home.Home(master)
        self.path = self.home.getPath()

        self.scenario = Scenario.Scenario()
        self.gameTree = GameTree.GameTree()
        self.gameEngine = GameEngine.GameEngine()

        self.playerHand = self.gameTree.getPlayerHand()
        self.flop = self.gameTree.getFlop()
        self.turn = self.gameTree.getTurn()
        self.river = self.gameTree.getRiver()

        self.cards = None
        self.cards_labels = None
    


        if(self.path == None):
            self.path = "output_strategyTest.json"


        self.worstAct = None
        self.bestAct = None

        self.round = 0
        self.round2Cond = False
        self.round3Cond = False


        self.number_of_buttons = 4
        self.button_size=(height/(2*self.number_of_buttons),height/(2*self.number_of_buttons))
        self.buttons=[]
        
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        
        #Import images
        current_path = os.path.dirname(os.path.realpath(__file__))
        #print(current_path)
        parent_path = os.path.abspath(os.path.join(current_path,"..","..",".."))
        #print(parent_path)
        self.bg_image = customtkinter.CTkImage(Image.open(parent_path + "/Ressources/img/fond_vierge.png"),
                                               size=(self.width, self.height))
        self.button_image = customtkinter.CTkImage(Image.open(parent_path + "/Ressources/img/bouton.png"),
                                                   size=self.button_size)
        self.button_green_image = customtkinter.CTkImage(Image.open(parent_path + "/Ressources/img/boutonVert.png"),
                                                   size=self.button_size)
        self.button_red_image = customtkinter.CTkImage(Image.open(parent_path + "/Ressources/img/boutonRouge.png"),
                                                   size=self.button_size)
        
        
        #background  
        self.bg_label = customtkinter.CTkLabel(self, image=self.bg_image,text="")
        self.bg_label.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

        #create buttons

        #home
        self.home_button = customtkinter.CTkButton(self, text="Home", command=self.home_event, width=150)
        # self.home_button.grid(row=0, column=0, padx=15, pady=(15,15))
        self.home_button.place(relx=0.05,rely=0.03,anchor=tkinter.CENTER)
        #exit
        self.exit_button = customtkinter.CTkButton(self, text="Exit", command=self.exit_event, width=150)
        # self.exit_button.grid(row=0, column=0, padx=15, pady=(15,15))
        self.exit_button.place(relx=0.05,rely=0.97,anchor=tkinter.CENTER)

        #Computer Action Label
        self.computer_action_label = customtkinter.CTkLabel(self, text="Computer Action", text_color="black",bg_color="white")
        self.computer_action_label.place(relx=0.515, rely=0.25, anchor=tkinter.CENTER)  


        #create cards_________________________________________________________________________________________________________________

    def create_cards(self):

        #Supprime les cartes déjà affichées
        if(self.cards != None):
            for card in self.cards:
                card=None
        if(self.cards_labels != None):
            for card_label in self.cards_labels:
                card_label.destroy()

        #Deck affichage (pour l'esthétique tout à droite, empilement de carte)
        self.cardDeck1 = Cards.Card(None,None,False)
        self.cardDeck2 = Cards.Card(None,None,False)
        self.cardDeck3 = Cards.Card(None,None,False)
        self.cardDeck4 = Cards.Card(None,None,False)

        self.cardDeck1_label = customtkinter.CTkLabel(self, image=self.cardDeck1.image, text="")
        self.cardDeck1_label.place(relx=0.90, rely=0.45, anchor=tkinter.CENTER)

        self.cardDeck2_label = customtkinter.CTkLabel(self, image=self.cardDeck2.image, text="")
        self.cardDeck2_label.place(relx=0.901, rely=0.451, anchor=tkinter.CENTER)

        self.cardDeck3_label = customtkinter.CTkLabel(self, image=self.cardDeck3.image, text="")
        self.cardDeck3_label.place(relx=0.902, rely=0.452, anchor=tkinter.CENTER)

        self.cardDeck4_label = customtkinter.CTkLabel(self, image=self.cardDeck4.image, text="")
        self.cardDeck4_label.place(relx=0.903, rely=0.453, anchor=tkinter.CENTER)

        #Player Hand
        self.card1 = self.playerHand[0]
        self.card2 = self.playerHand[1]
        
        self.card1_label = customtkinter.CTkLabel(self, image=self.card1.image, text="")
        self.card1_label.place(relx=0.48, rely=0.8, anchor=tkinter.CENTER)
        
        self.card2_label = customtkinter.CTkLabel(self, image=self.card2.image, text="")
        self.card2_label.place(relx=0.55, rely=0.8, anchor=tkinter.CENTER)

        #Opponent hand
        self.card1Op = Cards.Card(None,None,False)
        self.card2Op = Cards.Card(None,None,False)
        
        self.card1Op_label = customtkinter.CTkLabel(self, image=self.card1Op.image, text="")
        self.card1Op_label.place(relx=0.48, rely=0.15, anchor=tkinter.CENTER)
        
        self.card2Op_label = customtkinter.CTkLabel(self, image=self.card2Op.image, text="")
        self.card2Op_label.place(relx=0.55, rely=0.15, anchor=tkinter.CENTER)

        #Flop
        #récupération de chaque carte dans une variable distincte
        self.card3 = self.flop[0]
        self.card4 = self.flop[1]
        self.card5 = self.flop[2]
        self.card3.setFlip(True)
        self.card4.setFlip(True)
        self.card5.setFlip(True)

        self.card3_label = customtkinter.CTkLabel(self, image=self.card3.get_image(), text="")
        self.card3_label.place(relx=0.3, rely=0.45, anchor=tkinter.CENTER)

        self.card4_label = customtkinter.CTkLabel(self, image=self.card4.get_image(), text="")
        self.card4_label.place(relx=0.4, rely=0.45, anchor=tkinter.CENTER)

        self.card5_label = customtkinter.CTkLabel(self, image=self.card5.get_image(), text="")
        self.card5_label.place(relx=0.5, rely=0.45, anchor=tkinter.CENTER)

        #Turn
        self.card6 = self.turn[0]

        self.card6_label = customtkinter.CTkLabel(self, image=self.card6.image, text="")
        self.card6_label.place(relx=0.6, rely=0.45, anchor=tkinter.CENTER)

        #River
        self.card7 = self.river[0]

        self.card7_label = customtkinter.CTkLabel(self, image=self.card7.image, text="")
        self.card7_label.place(relx=0.7, rely=0.45, anchor=tkinter.CENTER)

        #Stock tout les cartes dans cards
        self.cards = [self.cardDeck1, self.cardDeck2, self.cardDeck3, self.cardDeck4, self.card1, self.card2, self.card1Op, self.card2Op, self.card3, self.card4, self.card5, self.card6, self.card7]

        #Stock tout les labels dans cards
        self.cards_labels = [self.cardDeck1_label, self.cardDeck2_label, self.cardDeck3_label, self.cardDeck4_label, self.card1_label, self.card2_label, self.card1Op_label, self.card2Op_label, self.card3_label, self.card4_label, self.card5_label, self.card6_label, self.card7_label]

    def create_buttons(self):
        if(self.gameTree.isPlayable()==True):
            for button in self.buttons:
                button.destroy()
            self.buttons = []

            actions=self.gameTree.getActions()
            self.number_of_buttons = 0
            for i in range(len(actions)):
                self.number_of_buttons+=1
                button = customtkinter.CTkLabel(self, image=self.button_image, text=actions[i],text_color="white")
                # fct_str = "button_"+actions[i].lower().replace(" ","_").replace(",","_")+"_event" #nom de la fonction a appeler
                # fct=getattr(self, fct_str) #transforme la chaine de caractere en pointeur vers la fonction
                # button.bind("<Button-1>",fct )
                button.bind("<Button-1>", lambda event, action=button._text: self.on_button_click(action))
                button.place(relx=0.1, rely=(self.number_of_buttons)/(len(actions)+1), anchor=tkinter.CENTER)
                self.buttons.append(button)

    def home_event(self):
        self.reset_game()
        self.master.show_frame("Home")

    def exit_event(self):
        self.master.destroy()
        
    def resize(self,event):
        width=event.width
        height=event.height
        if((width != self.width or height != self.height) and self.master.frame == self):
            # print("Play resize")
            # print("New width: ", width)
            # print("New height: ", height)
            self.width = width
            self.height = height

            #resize background
            self.bg_image.configure(size=(self.width, self.height))
            self.bg_label.configure(image=self.bg_image)

            #resize buttons
            # self.button_size=(height/(2*self.number_of_buttons),height/(2*self.number_of_buttons))
            # self.button_image.configure(size=self.button_size)

            # self.button_bet_x.configure(image=self.button_image)
            # self.button_bet_y.configure(image=self.button_image)
            # self.button_check.configure(image=self.button_image)
            # self.button_fold.configure(image=self.button_image)



    def on_button_click(self,action):
        self.worstAct = self.gameTree.getPlayerWorstAction()
        print("pire action",self.worstAct)
        self.bestAct = self.gameTree.getPlayerBestAction()
        print("meilleure action",self.bestAct)

        probabilities=self.gameTree.getPlayerPossiblities()
        for button in self.buttons:
            if(button._text == self.worstAct):
                button.configure(self,text_color="red", image=self.button_red_image)
            elif(button._text == self.bestAct):
                button.configure(self,text_color="green", image=self.button_green_image)
            else:
                button.configure(self,text_color="blue")
            button.configure(self,text=button._text+"\n\n"+str(round(probabilities[button._text],2)))

        self.update_idletasks()
        

        print("Player ",action)
        self.gameEngine.playerPlay(action)
        self.round = self.gameEngine.getNumRound()
        print("Round ",self.round)
            

        computerAction = self.gameEngine.getComputerLastAction()
        self.computer_action_label.configure(text=computerAction)

        
        if(self.gameEngine.getEndOfTheGame()==True):
            self.endOfTheGame()

        if(self.round == 2 and self.round2Cond==False):#Turn

            self.gameTree.dealcards(str(self.gameTree.getTurn()[0]))
            self.card6.setFlip(True)
            self.gameEngine.endOfTheRound=False
            self.round2Cond=True

        elif(self.round == 3 and self.round3Cond==False):#River
            self.card7.setFlip(True)
            self.round3Cond=True

        self.create_buttons()
        self.update_card_images()
        time.sleep(2)

    
    def endOfTheGame(self):
        self.master.attributes('-topmost', False)
        self.popUp = TopLevelWindow.EndOfTheGame()
        self.popUp.focus()
        self.popUp.wait_window()
        self.master.attributes('-topmost', True)
        self.reset_game()

    def reset_display(self):
        self.update_card_images()
        self.card6.setFlip(False)
        self.card7.setFlip(False)
        computerAction = self.gameEngine.getComputerLastAction()
        self.computer_action_label.configure(text=computerAction)
        

        #self.create_buttons()

    def reset_game(self):
        self.gameEngine = GameEngine.GameEngine()
        self.scenario= Scenario.Scenario()
        self.gameTree= GameTree.GameTree()

        self.playerHand = self.gameTree.getPlayerHand()
        self.flop = self.gameTree.getFlop()
        self.turn = self.gameTree.getTurn()
        self.river = self.gameTree.getRiver()
        self.gameTree.setPotAndStackToInitialPotAndStack()
        self.round=0
        self.worstAct = None
        self.bestAct = None
        self.round2Cond = False
        self.round3Cond = False
        self.gameTree.setActionBeforeToNone()

        print(str(self.gameEngine.getEndOfTheGame()))
        print(str(self.gameEngine.getEndOfTheRound()))
        print(str(self.gameEngine.getComputerLastAction()))

        self.create_cards()
        self.create_buttons()
        self.update_idletasks()
        self.reset_display()
    
    def update_card_images(self):
        self.card3_label.configure(image=self.card3.get_image())
        self.card4_label.configure(image=self.card4.get_image())
        self.card5_label.configure(image=self.card5.get_image())
        self.card6_label.configure(image=self.card6.get_image())
        self.card7_label.configure(image=self.card7.get_image())



