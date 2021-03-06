from tkinter import *

class MenuGui:
    
    def __init__(self, pathGui, pathButton):
        self.gui = PhotoImage(file = pathGui) #file of the background
        self.buttonGui = PhotoImage(file = pathButton)#file of the button

        self.button = None
        
        self.entryPlayer1 = None
        self.entryPlayer2 = None
        
        self.lab1 = None
        self.lab2 = None
        
        self.isReady = False

    def display(self, can):
        """Display the background and the button on a given canvas"""
        
        height = int(can.cget("height"))
        width = int(can.cget("width"))
        
        can.create_image(width/2 , height/2, image = self.gui)
        
        #create the button which call launchGame()
        self.button = Button(can, image = self.buttonGui, borderwidth = 1, command = self.launchGame)
        self.button.place(x = width/2 , y =height/2 + height/4, anchor='center')

        #Label and TextBox
        
        self.lab1 = can.create_text(width/2, height/3 - 40, text = "Pseudo for Player 1", font=("Rockwell Extra Bold", 15))

        self.entryPlayer1 = Entry(can, bg = "white", fg = "red" ,width = 20, font=("Rockwell Extra Bold", 20))
        self.entryPlayer1.place(x = width/2 , y = height/3, anchor='center')

        self.lab2 = can.create_text(width/2, height/2 - 40, text = "Pseudo for Player 2", font=("Rockwell Extra Bold", 15))
        
        self.entryPlayer2 = Entry(can, bg = "white", fg = "blue" ,width = 20, font=("Rockwell Extra Bold", 20))
        self.entryPlayer2.place(x = width/2 ,y = height/2, anchor='center')
        
    def launchGame(self):
        """turn the flag isReady to true if the two player set their name"""
        if self.entryPlayer1.get().strip() != "" or self.entryPlayer1.get().strip() != "":
            self.isReady = True
            print(self.getPseudo())

    def getPseudo(self):
        """return an array of length 2 with the current pseudos for the players"""
        return [self.entryPlayer1.get().strip(), self.entryPlayer2.get().strip()]
        
#-------Test of the class -----------------------     
fen = Tk()
fen.title("test")
    
can = Canvas(fen,bg= "white" ,height=700, width=1000)
can.pack()

#tkinter 8.5 only supports gifs, while 8.6 supports png, I modified it 
#to add better cross platform funtionality - Ben
#menu = MenuGui("images/Menu_GUI.png", "images/PlayButton.png")
menu = MenuGui("images/Menu_GUI.gif", "images/PlayButton.gif")

menu.display(can)

fen.mainloop()
