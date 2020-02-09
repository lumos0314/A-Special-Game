import tkinter as tk
import tkinter.messagebox,pickle,random
from PIL import Image, ImageTk


class A_Special_Game:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('A Special Game')
        self.root.geometry('450x300')
        self.root.resizable(0,0)
        self.number_draw = 0
        self.number_win = 0
        self.number_total = 0
        self.number_lose = 0
        self.Computer = 0
        self.ans = 0

        self.canvas = tk.Canvas(self.root, height=200, width=500)
        self.image_file = tk.PhotoImage(file='welcome.png')
        self.image = self.canvas.create_image(0,0, anchor='nw', image=self.image_file)
        self.canvas.place(x=0,y=0)

        self.label = tk.Label(self.root, text='Player Name')
        self.label.place(x=40,y=180)
        self.player=tk.StringVar()
        self.entry_player=tk.Entry(self.root,textvariable=self.player).place(x=135,y=180)
        self.button_login=tk.Button(self.root,text='Login',width=10,command=self.enter_player_name).place(x=135,y=210)
        self.button_quit=tk.Button(self.root,text='Quit',width=10,command=self.confirm_to_quit).place(x=233,y=210)
   
    def Game_Window(self):
        self.window = tk.Tk()
        self.window.title('Start New Game')
        self.window.geometry('392x390') 
        self.window.resizable(0,0)
        
        self.path = 'boxing.png'
        self.img = Image.open(self.path)
        self.photo = ImageTk.PhotoImage(self.img)
        self.label_boxing = tk.Label(self.window,image=self.photo)
        self.label_boxing.place(x=0,y=0,ancho='nw')
       
        self.Label_player = tk.Label(self.window,text = 'VS',
                        bg = 'gray',
                        fg = 'white',
                        font = ('Arial',14),
                        width = 18
                        )
        self.Label_player.place(x=120,y=135,ancho='nw')

        self.Label_player = tk.Label(self.window,text = self.player.get(),
                        bg = 'black',
                        fg = 'white',
                        font = ('Arial',14),
                        width = 15
                        )
        self.Label_player.place(x=3,y=135,ancho='nw')

        self.label_Computer = tk.Label(self.window,text = 'Computer',
                        bg = 'black',
                        fg = 'white',
                        font = ('Arial',14), 
                        width = 15 
                        )
        self.label_Computer.place(x=262,y=135,ancho='nw')

        self.label_down = tk.Label(self.window,text = 'Choose a role to start new game!\r Press the button above',
                    bg = 'yellow',
                    fg = 'black',
                    font = ('Arial',15),
                    width=42,height=4
                    )
        self.label_down.place(x=3,y=310,ancho='nw')

        self.label_result = tk.Label(self.window,text = 'Win: '+str(self.number_win)+ ' + '
                            'Lose: '+ str(self.number_lose)+ ' + ' + 'Draw: '+str(self.number_draw)+ ' = '
                            'Total: '+ str(self.number_total),
                            bg = 'blue',
                            fg = 'white',
                            font = ('Arial',14),
                            width = 47,
                            height = 1)
        self.label_result.place(x=3,y=285,ancho='nw')
   

    
        self.button_Scissors = tk.Button(self.window,text = 'Scissors',
                            command = self.showScissors,
                            bg = 'white',
                            fg = 'black',
                            font = ('Arial',14),
                            width = 15
                            )
        self.button_Scissors.place(x=134,y=163,ancho='nw')

        self.button_Paper = tk.Button(self.window,text = 'Paper',
                        command = self.showPaper,
                        bg = 'white',
                        fg = 'black',
                        font = ('Arial',14),
                        width = 15
                        )
        self.button_Paper.place(x=134,y=185,ancho='nw')

        self.button_Rock = tk.Button(self.window,text = 'Rock',
                            command = self.showRock,
                            bg = 'white',
                            fg = 'black',
                            font = ('Arial',14),
                            width = 15
                            )
        self.button_Rock.place(x=134,y=207,ancho='nw')

        self.button_Lizard = tk.Button(self.window,text = 'Lizard',
                            command = self.showLizard,
                            bg = 'white',
                            fg = 'black',
                            font = ('Arial',14),
                            width = 15
                            )
        self.button_Lizard.place(x=134,y=229,ancho='nw')

        self.button_Spock = tk.Button(self.window,text = 'Spock',
                            command = self.showSpock,
                            bg = 'white',
                            fg = 'black',
                            font = ('Arial',14),
                            width = 15
                            )
        self.button_Spock.place(x=134,y=251,ancho='nw')


        self.image = Image.open('link.png')
        self.image.thumbnail((120,100), Image.ANTIALIAS)
        self.image_player = ImageTk.PhotoImage(self.image)
        self.label_image = tk.Label(self.window,image=self.image_player)
        self.label_image.place(x= 8,y=160,ancho='nw')
     
        image = Image.open('computer.png')
        image.thumbnail((120,100), Image.ANTIALIAS)
        self.image_computer = ImageTk.PhotoImage(image)
        self.label_image = tk.Label(self.window,image=self.image_computer)
        self.label_image.place(x=262,y=160,ancho='nw')
        
    def judge_conditions(self,playername):
        Computer = random.randint(0, 4)
        print (Computer)
        if Computer == 0:
            self.computer_image = Image.open('scissors.png')
            self.computer_image.thumbnail((120,100), Image.ANTIALIAS)
            self.image_scissors_computer = ImageTk.PhotoImage(self.computer_image)
            self.canvas = tk.Canvas(self.window, width=120, height=100, bg='white')
            self.canvas.create_image(0, 0, image=self.image_scissors_computer, anchor="nw")
            self.canvas.place(x=262,y=160)
        elif Computer == 1:
            self.computer_image = Image.open('paper.png')
            self.computer_image.thumbnail((120,100), Image.ANTIALIAS)
            self.image_paper_computer = ImageTk.PhotoImage(self.computer_image)
            self.canvas = tk.Canvas(self.window, width=120, height=100, bg='white')
            self.canvas.create_image(0, 0, image=self.image_paper_computer, anchor="nw")
            self.canvas.place(x=262,y=160)
        elif Computer == 2:
            self.computer_image = Image.open('rock.png')
            self.computer_image.thumbnail((120,100), Image.ANTIALIAS)
            self.image_rock_computer = ImageTk.PhotoImage(self.computer_image)
            self.canvas = tk.Canvas(self.window, width=120, height=100, bg='white')
            self.canvas.create_image(0, 0, image=self.image_rock_computer, anchor="nw")
            self.canvas.place(x=262,y=160)
        elif Computer == 3:
            self.computer_image = Image.open('lizard.png')
            self.computer_image.thumbnail((120,100), Image.ANTIALIAS)
            self.image_lizard_computer = ImageTk.PhotoImage(self.computer_image)
            self.canvas = tk.Canvas(self.window, width=120, height=100, bg='white')
            self.canvas.create_image(0, 0, image=self.image_lizard_computer, anchor="nw")
            self.canvas.place(x=262,y=160)
        else:
            self.computer_image = Image.open('spock.png')
            self.computer_image.thumbnail((120,100), Image.ANTIALIAS)
            self.image_spock_computer = ImageTk.PhotoImage(self.computer_image)
            self.canvas = tk.Canvas(self.window, width=120, height=100, bg='white')
            self.canvas.create_image(0, 0, image=self.image_spock_computer, anchor="nw")
            self.canvas.place(x=262,y=160)
            
        if (playername == 0 and Computer == 1):
            self.number_win+=1
            self.label_down.configure(text=self.player.get()+" wins because 'Scissors cuts Paper''")
        elif (playername == 0 and Computer == 3):
            self.number_win+=1
            self.label_down.configure(text=self.player.get()+" wins because 'Scissors decapitates Lizard'")
        elif (playername == 1 and Computer == 2):
            self.number_win+=1
            self.label_down.configure(text=self.player.get()+" wins because 'Paper covers Rock'")
        elif (playername == 1 and Computer == 4):
            self.number_win+=1
            self.label_down.configure(text=self.player.get()+" wins because 'Paper disproves Spock'")
        elif (playername == 2 and Computer == 3):
            self.number_win+=1
            self.label_down.configure(text=self.player.get()+" wins because 'Rock crushes Lizard'")
        elif (playername == 2 and Computer == 0):
            self.number_win+=1
            self.label_down.configure(text=self.player.get()+" wins because 'Rock crushes Scissors'")
        elif (playername == 3 and Computer == 4):
            self.number_win+=1
            self.label_down.configure(text=self.player.get()+" wins because 'Lizard poisons Spock'")
        elif (playername == 3 and Computer == 1):
            self.number_win+=1
            self.label_down.configure(text=self.player.get()+" wins because 'Lizard eats Papar'")
        elif (playername == 4 and Computer == 0):
            self.number_win+=1
            self.label_down.configure(text=self.player.get()+" wins because 'Spock smashes Scissors'")
        elif (playername == 4 and Computer == 2):
            self.number_win+=1
            self.label_down.configure(text=self.player.get()+" wins because 'Spock vaporizes Rock'")
        elif (playername == 0 and Computer == 0):
            self.label_down.configure(text = "Tie because of both 'Scissors'")
            self.number_draw+=1
        elif (playername == 1 and Computer == 1):
            self.label_down.configure(text = "Tie because of both 'Scissors'")
            self.number_draw+=1
        elif (playername == 2 and Computer == 2):
            self.label_down.configure(text = "Tie because of both 'Scissors'")
            self.number_draw+=1
        elif (playername == 3 and Computer == 3):
            self.label_down.configure(text = "Tie because of both 'Scissors'")
            self.number_draw+=1
        elif (playername == 4 and Computer == 4):
            self.label_down.configure(text = "Tie because of both 'Scissors'")
            self.number_draw+=1
        else:
            self.number_lose+=1
            self.label_down.configure(text=self.player.get()+" lost!")
        
        if self.number_total == 6:
            if self.number_win > self.number_lose:
                self.ans = tk.messagebox.askquestion(title='Tournament', message=self.player.get()+' wins!\nDo you want to continue?')

            elif self.number_win == self.number_lose:
                self.ans = tk.messagebox.askquestion(title='Tournament', message='Tie!\nDo you want to continue?')

            else:
                self.ans = tk.messagebox.askquestion(title='Tournament', message='Computer wins!\nDo you want to Continue?')
            
            if self.ans == 'yes':
                self.number_total = 0
                self.number_win = 0
                self.number_lose = 0
                self.number_draw = 0            
            else:
                self.window.destroy()
        
        self.label_result.configure(text = 'Win: '+str(self.number_win)+ ' + ''Lose: '+ str(self.number_lose)+ ' + ' + 
                                           'Draw: '+str(self.number_draw)+ ' = '
                                          'Total: '+ str(self.number_total),
                            bg = 'blue',
                            fg = 'white',
                            font = ('Arial',14),
                            width = 47,
                            height = 1)


    def showScissors(self):
        self.number_total+=1
        self.player_image = Image.open('scissors.png')
        self.player_image.thumbnail((120,100), Image.ANTIALIAS)
        self.image_scissors_player = ImageTk.PhotoImage(self.player_image)
        self.canvas = tk.Canvas(self.window, width=120, height=100, bg='white')
        self.canvas.create_image(0, 0, image=self.image_scissors_player, anchor="nw")
        self.canvas.place(x=8,y=160) 
        self.playername = 0
        self.judge_conditions(self.playername)
    def showPaper(self):
        self.number_total+=1
        self.player_image = Image.open('paper.png')
        self.player_image.thumbnail((120,100), Image.ANTIALIAS)
        self.image_paper_player = ImageTk.PhotoImage(self.player_image)
        self.canvas = tk.Canvas(self.window, width=120, height=100, bg='white')
        self.canvas.create_image(0, 0, image=self.image_paper_player, anchor="nw")
        self.canvas.place(x=8,y=160) 
        self.playername = 1
        self.judge_conditions(self.playername)
    def showRock(self):
        self.number_total+=1
        self.player_image = Image.open('rock.png')
        self.player_image.thumbnail((120,100), Image.ANTIALIAS)
        self.image_rock_player = ImageTk.PhotoImage(self.player_image)
        self.canvas = tk.Canvas(self.window, width=120, height=100, bg='white')
        self.canvas.create_image(0, 0, image=self.image_rock_player, anchor="nw")
        self.canvas.place(x=8,y=160) 
        self.playername = 2
        self.judge_conditions(self.playername)
    def showLizard(self):
        self.number_total+=1
        self.player_image = Image.open('lizard.png')
        self.player_image.thumbnail((120,100), Image.ANTIALIAS)
        self.image_lizard_player = ImageTk.PhotoImage(self.player_image)
        self.canvas = tk.Canvas(self.window, width=120, height=100, bg='white')
        self.canvas.create_image(0, 0, image=self.image_lizard_player, anchor="nw")
        self.canvas.place(x=8,y=160) 
        self.playername = 3
        self.judge_conditions(self.playername)
    def showSpock(self):
        self.number_total += 1
        self.player_image = Image.open('spock.png')
        self.player_image.thumbnail((120,100), Image.ANTIALIAS)
        self.image_spock_player = ImageTk.PhotoImage(self.player_image)
        self.canvas = tk.Canvas(self.window, width=120, height=100, bg='white')
        self.canvas.create_image(0, 0, image=self.image_spock_player, anchor="nw")
        self.canvas.place(x=8,y=160) 
        self.playername = 4
        self.judge_conditions(self.playername)
    
    def enter_player_name(self):
        player = self.player.get()
        if not player:
            tk.messagebox.showerror('Error', 'Enter player name')
        else:
            tk.messagebox.showinfo(title='Hello',message='Welcome '+ self.player.get() + '!')
            self.root.destroy()
            self.Game_Window()
    def confirm_to_quit(self):
        if tk.messagebox.askokcancel('Just a reminder', 'Do you reaaaaally want to quit?'):
           self.root.destroy()

window = A_Special_Game()
window.root.mainloop()