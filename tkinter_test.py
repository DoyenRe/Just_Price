import tkinter as tk
from PIL import Image, ImageTk
import random2 as rnd

def less():
    less_list = ['It is less.', 'Less !!', "It's less!", "Lower"]
    n = rnd.randrange(0, len(less_list))
    return(less_list[n])

def more():
    more_list = ['It is more.', 'More !!', "It's more!", "Higher"]
    n = rnd.randrange(0, len(more_list))
    return(more_list[n])

root = tk.Tk()
root.title('Juste Price - The Game')
canvas = tk.Canvas(root, width = 500, height=500)
canvas.grid(columnspan=10, rowspan=100)


#Logo
path = '/Users/rdoyen/PythonProject/Just_Price/image/unnamed.png'
logo = Image.open(path)
logo = logo.resize((100,100))
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image=logo, borderwidth=0, highlightthickness=0, state='normal')
logo_label.image = logo
logo_label.grid(column=3, row=0)


#Welcome Text
welcome_text = tk.Label(root, text='Welcome in the Game Just Price! \n Hope you will get a lot of fun!', fg = 'black', font='Helvetica 25 bold')
welcome_text.grid(column=3, row=3)

#Instruction
instruction_text = tk.Label(root, text='In this game, there are two game modes :  \n \n 1) Tentatives'\
                  ' - You have a limited number of trials to find the Just Price \n 2) TimeOut'\
                  ' - You have a limited time to find the Just Price \n \n Which one do you want to play?', 
fg = 'black', font='Raleway 23')
instruction_text.grid(column=0, row=10)

text_lbl = None
end_game = None
button_game_replay= None
victory_label = None

#Function Buttons
def function_button_1():
    global tentative, text_lbl, end_game, button_game_replay, victory_label
    tk.Label(root, text = 'Mode Tentative', font='Raleway 23 bold').grid(column=5, row=10)
    if text_lbl is not None: 
        text_lbl.destroy()
    if end_game is not None: 
        end_game.destroy()
    if button_game_replay is not None: 
        button_game_replay.destroy()
    if victory_label is not None: 
        victory_label.destroy()
    entry1 = tk.Entry(root)
    canvas.create_window(200, 140, window=entry1)
    canvas.grid(column=5, row=11)
    tentative = 0
   #price = rnd.randrange(0, 100)
    price = 50
    def validate():
        global tentative, text_lbl, end_game, button_game_replay, victory_label
        entry_proposal = entry1.get()
        if tentative == 0:
            if int(entry_proposal) == price:
                end_game = tk.Label(root,text='Congratulation, you won!', fg = 'blue', font='Raleway 23')
                end_game.grid(column=6, row=12)
                button_game_val.destroy()
                #Button Replay
                button_replay_text = tk.StringVar()
                button_game_replay = tk.Button(root, textvariable=button_replay_text, font='Times 18 bold', command=function_button_1)
                button_replay_text.set('Replay')    
                button_game_replay.grid(column=6, row=13)
                #Victory
                path_victory = '/Users/rdoyen/PythonProject/Just_Price/image/victory.png'
                victory = Image.open(path_victory)
                victory = victory.resize((350,350))
                victory = ImageTk.PhotoImage(victory)
                victory_label = tk.Label(image=victory, borderwidth=0, highlightthickness=0, state='normal')
                victory_label.image = victory
                victory_label.grid(column=0, row=18)
            elif int(entry_proposal) > price: 
                text_lbl = tk.Label(root,text=less(), fg = 'red', font='Raleway 23')
                text_lbl.grid(column=6, row=12)
                tentative += 1
            else: 
                text_lbl = tk.Label(root,text=more(), fg = 'green', font='Raleway 23')
                text_lbl.grid(column=6, row=12)
                tentative += 1
        if 0 < tentative <= 10:
            if int(entry_proposal) == price:
                text_lbl.destroy()
                button_game_val.destroy()
                end_game = tk.Label(root,text='Congratulation, you won!', fg = 'blue', font='Raleway 23')
                end_game.grid(column=6, row=12)
                #Button Replay
                button_replay_text = tk.StringVar()
                button_game_replay = tk.Button(root, textvariable=button_replay_text, font='Times 18 bold', command=function_button_1)
                button_replay_text.set('Replay')    
                button_game_replay.grid(column=6, row=13)
                #Victory
                path_victory = '/Users/rdoyen/PythonProject/Just_Price/image/victory.png'
                victory = Image.open(path_victory)
                victory = victory.resize((350,350))
                victory = ImageTk.PhotoImage(victory)
                victory_label = tk.Label(image=victory, borderwidth=0, highlightthickness=0, state='normal')
                victory_label.image = victory
                victory_label.grid(column=0, row=18)
            elif int(entry_proposal) > price: 
                text_lbl.destroy()
                text_lbl = tk.Label(root,text=less(), fg = 'red', font='Raleway 23')
                text_lbl.grid(column=6, row=12)
                tentative += 1
            else: 
                text_lbl.destroy()
                text_lbl = tk.Label(root,text=more(), fg = 'green', font='Raleway 23')
                text_lbl.grid(column=6, row=12)
                tentative += 1
        else: 
            text_lbl.destroy()
            button_game_val.destroy()
            end_game = tk.Label(root,text='Game Over \n No more tentative', fg = 'black', font='Raleway 23')
            end_game.grid(column=6, row=12)
            #Button Replay
            button_replay_text = tk.StringVar()
            button_game_replay = tk.Button(root, textvariable=button_replay_text, font='Times 18 bold', command=function_button_1)
            button_replay_text.set('Replay')    
            button_game_replay.grid(column=6, row=13)
            print(button_game_replay)
            print(end_game)


    #Button Validate
    button_game_val_text = tk.StringVar()
    button_game_val = tk.Button(root, textvariable=button_game_val_text, font='Times 18 bold', command=validate)
    button_game_val_text.set('Validate')    
    button_game_val.grid(column=6, row=11)


#Button game 1
button_game_1_text = tk.StringVar()
button_game_1 = tk.Button(root, textvariable=button_game_1_text, font='Times 18 bold', command=function_button_1)
button_game_1_text.set('Mode Tentative')
button_game_1.grid(column=0, row=15)

root.mainloop()

