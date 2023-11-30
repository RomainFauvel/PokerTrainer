from PIL import Image
import tkinter
import customtkinter
import os

import card as card

class Play(customtkinter.CTkFrame):
    def __init__(self, master: any, width: int = 200, height: int = 200):
        super().__init__(master, width, height)
        self.master = master
        self.width = width
        self.height = height

        self.number_of_buttons = 4
        self.button_size=(height/(2*self.number_of_buttons),height/(2*self.number_of_buttons))
        
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        
        #Import images
        current_path = os.path.dirname(os.path.realpath(__file__))
        self.bg_image = customtkinter.CTkImage(Image.open(current_path + "\\..\\..\\img\\fond_vierge.png"),
                                               size=(self.width, self.height))
        self.button_image = customtkinter.CTkImage(Image.open(current_path + "\\..\\..\\img\\bouton.png"),
                                                   size=self.button_size)
        
        
        #background  
        self.bg_label = customtkinter.CTkLabel(self, image=self.bg_image,text="")
        self.bg_label.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

        
        
        #create buttons
        #bet 'x'
        self.button_bet_x = customtkinter.CTkLabel(self, image=self.button_image, text="Bet\n 'x'",text_color="white")
        self.button_bet_x.bind("<Button-1>", self.button_bet_x_event) 
        # self.button_bet_x.grid(row=0, column=0, padx=15, pady=(15,15))
        self.button_bet_x.place(relx=0.1, rely=1*(1/(self.number_of_buttons+1)), anchor=tkinter.CENTER)
        
        #bet 'y'
        self.button_bet_y = customtkinter.CTkLabel(self, image=self.button_image, text="Bet\n 'y'",text_color="white")
        self.button_bet_y.bind("<Button-1>", self.button_bet_y_event)
        # self.button_bet_y.grid(row=1, column=0, padx=15, pady=(15,15))
        self.button_bet_y.place(relx=0.1, rely=2*(1/(self.number_of_buttons+1)), anchor=tkinter.CENTER)
        
        #check
        self.button_check = customtkinter.CTkLabel(self, image=self.button_image, text="Check",text_color="white")
        self.button_check.bind("<Button-1>", self.button_check_event)
        # self.button_check.grid(row=2, column=0, padx=15, pady=(15,15))
        self.button_check.place(relx=0.1, rely=3*(1/(self.number_of_buttons+1)), anchor=tkinter.CENTER)
        
        #fold
        self.button_fold = customtkinter.CTkLabel(self, image=self.button_image, text="Fold",text_color="white")
        self.button_fold.bind("<Button-1>", self.button_fold_event)
        # self.button_fold.grid(row=3, column=0, padx=15, pady=(15,15))
        self.button_fold.place(relx=0.1, rely=4*(1/(self.number_of_buttons+1)), anchor=tkinter.CENTER)
        



        
        #home
        self.home_button = customtkinter.CTkButton(self, text="Home", command=self.home_event, width=150)
        # self.home_button.grid(row=0, column=0, padx=15, pady=(15,15))
        self.home_button.place(relx=0.05,rely=0.03,anchor=tkinter.CENTER)
        #exit
        self.exit_button = customtkinter.CTkButton(self, text="Exit", command=self.exit_event, width=150)
        # self.exit_button.grid(row=0, column=0, padx=15, pady=(15,15))
        self.exit_button.place(relx=0.05,rely=0.97,anchor=tkinter.CENTER)



        #create cards

        #Player Hand
        self.card1 = card.card("c","A",True)
        self.card2 = card.card("c","A",True)
        
        self.card1_label = customtkinter.CTkLabel(self, image=self.card1.image, text="")
        self.card1_label.place(relx=0.4, rely=0.8, anchor=tkinter.CENTER)
        
        self.card2_label = customtkinter.CTkLabel(self, image=self.card2.image, text="")
        self.card2_label.place(relx=0.6, rely=0.8, anchor=tkinter.CENTER)

        #Flop
        self.card3 = card.card("c","A",True)
        self.card4 = card.card("c","A",True)
        self.card5 = card.card("c","A",True)

        self.card3_label = customtkinter.CTkLabel(self, image=self.card3.image, text="")
        self.card3_label.place(relx=0.3, rely=0.4, anchor=tkinter.CENTER)

        self.card4_label = customtkinter.CTkLabel(self, image=self.card4.image, text="")
        self.card4_label.place(relx=0.4, rely=0.4, anchor=tkinter.CENTER)

        self.card5_label = customtkinter.CTkLabel(self, image=self.card5.image, text="")
        self.card5_label.place(relx=0.5, rely=0.4, anchor=tkinter.CENTER)

        #Turn
        self.card6 = card.card("c","A",True)

        self.card6_label = customtkinter.CTkLabel(self, image=self.card6.image, text="")
        self.card6_label.place(relx=0.7, rely=0.4, anchor=tkinter.CENTER)

        #River
        self.card7 = card.card("c","A",True)

        self.card7_label = customtkinter.CTkLabel(self, image=self.card7.image, text="")
        self.card7_label.place(relx=0.8, rely=0.4, anchor=tkinter.CENTER)


    def home_event(self):
        self.master.show_frame("Home")

    def exit_event(self):
        self.master.destroy()
        
    def resize(self,event):
        width=event.width
        height=event.height
        if((width != self.width or height != self.height) and self.master.frame == self):
            print("Play resize")
            print("New width: ", width)
            print("New height: ", height)
            self.width = width
            self.height = height

            #resize background
            self.bg_image.configure(size=(self.width, self.height))
            self.bg_label.configure(image=self.bg_image)

            #resize buttons
            self.button_size=(height/(2*self.number_of_buttons),height/(2*self.number_of_buttons))
            self.button_image.configure(size=self.button_size)

            self.button_bet_x.configure(image=self.button_image)
            self.button_bet_y.configure(image=self.button_image)
            self.button_check.configure(image=self.button_image)
            self.button_fold.configure(image=self.button_image)



    def button_bet_x_event(self, event):
        print("Bet x")
    
    def button_bet_y_event(self, event):
        print("Bet y")

    def button_check_event(self, event):
        print("Check")

    def button_fold_event(self, event):
        print("Fold")