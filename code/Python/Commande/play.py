from PIL import Image
import tkinter
import customtkinter
import os

import card as card
import GameTree as GameTree

import home as home

class Play(customtkinter.CTkFrame):
    current_path = os.path.dirname(os.path.realpath(__file__))
    parent_path = os.path.abspath(os.path.join(current_path, "..", "..", ".."))
    fichierStrategy = parent_path + "/Ressources/output_strategyTest.json"

<<<<<<< HEAD
    
=======
    gameTree = GameTree.GameTree(fichierStrategy,"KsKh")#il faudra enlever les param
>>>>>>> 838138c584910b215fab12e3ba7778e71472eef3

    def __init__(self, master: any, width: int = 200, height: int = 200):
        super().__init__(master, width, height)
        self.master = master
        self.width = width
        self.height = height

        # Créez une instance de la classe Home
        self.home_instance = home.Home(master)

        # Maintenant, vous pouvez appeler la méthode getPath () sur cette instance
        self.path = self.home_instance.getPath()

        if(self.path == None):
            self.path = "output_strategyTest.json"
        print(self.path)

        
        self.gameTree = GameTree.GameTree("PokerTrainer/Ressources/" + self.path,"KsKh")#il faudra enlever les param
        




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
        self.cardDeck1 = card.card(None,None,False)
        self.cardDeck2 = card.card(None,None,False)
        self.cardDeck3 = card.card(None,None,False)
        self.cardDeck4 = card.card(None,None,False)

        self.cardDeck1_label = customtkinter.CTkLabel(self, image=self.cardDeck1.image, text="")
        self.cardDeck1_label.place(relx=0.90, rely=0.45, anchor=tkinter.CENTER)

        self.cardDeck2_label = customtkinter.CTkLabel(self, image=self.cardDeck2.image, text="")
        self.cardDeck2_label.place(relx=0.901, rely=0.451, anchor=tkinter.CENTER)

        self.cardDeck3_label = customtkinter.CTkLabel(self, image=self.cardDeck3.image, text="")
        self.cardDeck3_label.place(relx=0.902, rely=0.452, anchor=tkinter.CENTER)

        self.cardDeck4_label = customtkinter.CTkLabel(self, image=self.cardDeck4.image, text="")
        self.cardDeck4_label.place(relx=0.903, rely=0.453, anchor=tkinter.CENTER)

        #Player Hand
        self.card1 = card.card("c","10",True)
        self.card2 = card.card("c","A",True)
        
        self.card1_label = customtkinter.CTkLabel(self, image=self.card1.image, text="")
        self.card1_label.place(relx=0.48, rely=0.8, anchor=tkinter.CENTER)
        
        self.card2_label = customtkinter.CTkLabel(self, image=self.card2.image, text="")
        self.card2_label.place(relx=0.55, rely=0.8, anchor=tkinter.CENTER)

        #Opponent hand
        self.card1Op = card.card("c","10",False)
        self.card2Op = card.card("c","A",False)
        
        self.card1Op_label = customtkinter.CTkLabel(self, image=self.card1Op.image, text="")
        self.card1Op_label.place(relx=0.48, rely=0.15, anchor=tkinter.CENTER)
        
        self.card2Op_label = customtkinter.CTkLabel(self, image=self.card2Op.image, text="")
        self.card2Op_label.place(relx=0.55, rely=0.15, anchor=tkinter.CENTER)

        #Flop
        self.card3 = card.card("c","A",False)
        self.card4 = card.card("c","A",False)
        self.card5 = card.card("c","A",False)

        self.card3_label = customtkinter.CTkLabel(self, image=self.card3.image, text="")
        self.card3_label.place(relx=0.3, rely=0.45, anchor=tkinter.CENTER)

        self.card4_label = customtkinter.CTkLabel(self, image=self.card4.image, text="")
        self.card4_label.place(relx=0.4, rely=0.45, anchor=tkinter.CENTER)

        self.card5_label = customtkinter.CTkLabel(self, image=self.card5.image, text="")
        self.card5_label.place(relx=0.5, rely=0.45, anchor=tkinter.CENTER)

        #Turn
        self.card6 = card.card("c","A",False)

        self.card6_label = customtkinter.CTkLabel(self, image=self.card6.image, text="")
        self.card6_label.place(relx=0.6, rely=0.45, anchor=tkinter.CENTER)

        #River
        self.card7 = card.card("c","A",False)

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



    def home_event(self):
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

    # def button_check_event(self, event):
    #     print("Player Check")

    # def button_fold_event(self, event):
    #     print("Player Fold")

    # def button_bet_25_000000_event(self, event):
    #     print("Player Bet 25")

    # def button_bet_200_000000_event(self, event):
    #     print("Player Bet 200")

