from tkinter import*

class MenuGui:
    
    def __init__(self, pathGui, pathButton):
        self.gui = PhotoImage(file = pathGui) #file of the background
        self.buttonGui = PhotoImage(file = pathButton)#file of the button
        self.button = None

        self.isReady = False

    def display(self, can):
        """Display the background and the button on a given canvas"""
        
        height = int(can.cget("height"))
        width = int(can.cget("width"))
        
        can.create_image(width/2 , height/2, image = self.gui)

        #the button call launchGame
        self.button = Button(can, image = self.buttonGui, borderwidth = 1, command = self.launchGame)
        self.button.place(x = width/2 , y =height/2, anchor='center')

    def launchGame(self):
        """turn the flag isReady to true"""
        self.isReady = True
        
#-------Test of the class -----------------------     
fen = Tk()
fen.title("test")
    
can = Canvas(fen,bg= "white" ,height=700, width=1000)
can.pack()

menu = MenuGui("images/Menu_GUI.png", "images/PlayButton.png")
menu.display(can)

fen.mainloop()
