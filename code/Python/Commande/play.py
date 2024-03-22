from PIL import Image
import tkinter
import customtkinter
import os

import Cards as Cards
import GameTree as GameTree

import home as home

class Play(customtkinter.CTkFrame):

    

    def __init__(self, master: any, width: int = 200, height: int = 200):
        super().__init__(master, width, height)
        self.master = master
        self.width = width
        self.height = height

                
        self.home = home.Home(master)
        self.path = self.home.getPath()


        if(self.path == None):
            self.path = "output_strategyTest.json"
        #self.scenario = Scenario()
        self.gameTree = GameTree.GameTree("PokerTrainer/Ressources/" + self.path,"KsKh")
        




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
        
        
        #background  
        self.bg_label = customtkinter.CTkLabel(self, image=self.bg_image,text="")
        self.bg_label.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

        
        
        #create buttons
        self.create_buttons()
        

        #home
        self.home_button = customtkinter.CTkButton(self, text="Home", command=self.home_event, width=150)
        # self.home_button.grid(row=0, column=0, padx=15, pady=(15,15))
        self.home_button.place(relx=0.05,rely=0.03,anchor=tkinter.CENTER)
        #exit
        self.exit_button = customtkinter.CTkButton(self, text="Exit", command=self.exit_event, width=150)
        # self.exit_button.grid(row=0, column=0, padx=15, pady=(15,15))
        self.exit_button.place(relx=0.05,rely=0.97,anchor=tkinter.CENTER)



        #create cards_________________________________________________________________________________________________________________

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
        self.card1 = Cards.Card("c","10",True)
        self.card2 = Cards.Card("c","A",True)
        
        self.card1_label = customtkinter.CTkLabel(self, image=self.card1.image, text="")
        self.card1_label.place(relx=0.48, rely=0.8, anchor=tkinter.CENTER)
        
        self.card2_label = customtkinter.CTkLabel(self, image=self.card2.image, text="")
        self.card2_label.place(relx=0.55, rely=0.8, anchor=tkinter.CENTER)

        #Opponent hand
        self.card1Op = Cards.Card("c","10",False)
        self.card2Op = Cards.Card("c","A",False)
        
        self.card1Op_label = customtkinter.CTkLabel(self, image=self.card1Op.image, text="")
        self.card1Op_label.place(relx=0.48, rely=0.15, anchor=tkinter.CENTER)
        
        self.card2Op_label = customtkinter.CTkLabel(self, image=self.card2Op.image, text="")
        self.card2Op_label.place(relx=0.55, rely=0.15, anchor=tkinter.CENTER)

        #Flop
        self.flop = GameTree.GameTree.flop
        #récupération de chaque carte dans une variable distincte
        #c1 = Cards.Card.splitIn2(self.flop[1])
        #c2 = Cards.Card.splitIn2(self.flop[2])
        #c3 = Cards.Card.splitIn2(self.flop[3])
        #self.card3 = Cards.Card(c1[1],c1[2],False) à compléter
        self.card3 = Cards.Card("c","A",False)
        self.card4 = Cards.Card("c","A",False)
        self.card5 = Cards.Card("c","A",False)

        self.card3_label = customtkinter.CTkLabel(self, image=self.card3.image, text="")
        self.card3_label.place(relx=0.3, rely=0.45, anchor=tkinter.CENTER)

        self.card4_label = customtkinter.CTkLabel(self, image=self.card4.image, text="")
        self.card4_label.place(relx=0.4, rely=0.45, anchor=tkinter.CENTER)

        self.card5_label = customtkinter.CTkLabel(self, image=self.card5.image, text="")
        self.card5_label.place(relx=0.5, rely=0.45, anchor=tkinter.CENTER)

        #Turn
        self.turn = GameTree.GameTree.turn
        self.card6 = Cards.Card("c","A",False)

        self.card6_label = customtkinter.CTkLabel(self, image=self.card6.image, text="")
        self.card6_label.place(relx=0.6, rely=0.45, anchor=tkinter.CENTER)

        #River
        self.river = GameTree.GameTree.river
        self.card7 = Cards.Card("c","A",False)

        self.card7_label = customtkinter.CTkLabel(self, image=self.card7.image, text="")
        self.card7_label.place(relx=0.7, rely=0.45, anchor=tkinter.CENTER)

    def create_buttons(self):
        # if(self.gameTree.isPlayable()==True):
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



    def reset_game(self):
        #self.gameTree.rolloutToInit()
        self.reset_display()

    def reset_display(self):
        self.card3.setFlip(False)
        self.card4.setFlip(False)
        self.card5.setFlip(False)
        self.card6.setFlip(False)
        self.card7.setFlip(False)
        self.update_card_images()

        #self.create_buttons()


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
        print("Player ",action)
        self.gameTree.play(action)
        self.create_buttons()
        print(self.gameTree.getRound())
        if(self.gameTree.getRound() == 1):
            self.card3.setFlip(True)
            self.card4.setFlip(True)
            self.card5.setFlip(True)
        elif(self.gameTree.getRound() == 2):
            self.card6.setFlip(True)
        else:
            self.card7.setFlip(True)
            
        self.update_card_images()
        
        

    
    def update_card_images(self):
        self.card3_label.configure(image=self.card3.image if not self.card3.getFlip() else self.card3.get_image())
        self.card4_label.configure(image=self.card4.image if not self.card4.getFlip() else self.card4.get_image())
        self.card5_label.configure(image=self.card5.image if not self.card5.getFlip() else self.card5.get_image())
        self.card6_label.configure(image=self.card6.image if not self.card6.getFlip() else self.card6.get_image())
        self.card7_label.configure(image=self.card7.image if not self.card7.getFlip() else self.card7.get_image())


    # def button_check_event(self, event):
    #     print("Player Check")

    # def button_fold_event(self, event):
    #     print("Player Fold")


    def button_fold_event(self, event):
        print("Fold")



