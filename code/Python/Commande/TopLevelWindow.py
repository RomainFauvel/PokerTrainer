import customtkinter
import os
from PIL import Image

class EndOfTheGame(customtkinter.CTkToplevel):

    def __init__(self):
        super().__init__()
        self.title("Acknowledment")
        self.geometry("400x200+400+400")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.attributes("-topmost", 1)  # Always on top

        self._create_widgets()

    def _create_widgets(self):
        #text
        self.acknowledment_text = customtkinter.CTkLabel(self,text="This is the end of the game. \nThank you for playing!",
                                                            width=50, height=20)
            
        self.acknowledment_text.cget("font").configure(size=18)

        self.acknowledment_text.grid(row=0, column=0,padx=(20,20),pady=(20), sticky="nsew")

        #button
        self.ok_button = customtkinter.CTkButton(self,text='OK',command=self._ok)
        self.ok_button.grid(row=1, column=0,padx=(20,20),pady=(20,20), sticky="nsew")

    def _ok(self):
        self.destroy()


class WaitNextRound(customtkinter.CTkToplevel):

    def __init__(self):
        super().__init__()
        self.title("Acknowledment")
        self.geometry("400x200+400+650")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.attributes("-topmost", 1)  # Always on top

        self._create_widgets()

    def _create_widgets(self):
        #text
        self.acknowledment_text = customtkinter.CTkLabel(self,text="Ready for the next play ? \nClick OK to continue!",
                                                            width=50, height=20)
            
        self.acknowledment_text.cget("font").configure(size=18)

        self.acknowledment_text.grid(row=0, column=0,padx=(20,20),pady=(20), sticky="nsew")

        #button
        self.ok_button = customtkinter.CTkButton(self,text='OK',command=self._ok)
        self.ok_button.grid(row=1, column=0,padx=(20,20),pady=(20,20), sticky="nsew")

    def _ok(self):
        self.destroy()