import customtkinter
import tkinter
import os

# Ours imports
import home as home
import play as play
import settings as settings
import utils as utils
import help as help


class App(customtkinter.CTk):
    def __init__(self,height,width):
        super().__init__()

        # configure window
        self.title("Poker Trainer")
        self.attributes('-topmost', True)
        self.geometry(str(width)+"x"+str(height)+"+0+0")
        
        current_path = os.path.dirname(os.path.realpath(__file__))
        self.iconbitmap(os.path.join(current_path+"/img/icone.ico"))
        
        #import frames
        self.frames = {}
        for F in (home.Home, play.Play, settings.Settings, help.Help):
            page_name = F.__name__
            self.frame = F(master=self, width=width, height=height)
            self.frames[page_name] = self.frame
            
            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            self.frame.place(x=0, y=0, relwidth=1, relheight=1)
            
            print(self.frames)
            
        # show home page
        self.show_frame("Home")
        
        #Window resizing event
        self.bind("<Configure>", func=self.frame.resize)
        
    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        self.frame = self.frames[page_name]
        self.frame.tkraise()

        # Il y a un bug ici. Je pense que ca vient de l instanciation des frames
        print("Frames", self.frames)
        print("Frame raised: ", self.frame)
            
        


def main():
    print("------------------Main called------------------")
    height, width = utils.get_display_size()
    root = App(height, width)
    root.mainloop()

main()