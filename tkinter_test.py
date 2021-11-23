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
canvas = tk.Canvas(root, width = 1500, height=1000)
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

#Function Buttons
def function_button_1():
    global tentative, text_lbl
    tk.Label(root, text = 'Mode Tentative', font='Raleway 23 bold').grid(column=5, row=10)
    if text_lbl is not None: 
        text_lbl.destroy()
    entry1 = tk.Entry(root)
    canvas.create_window(200, 140, window=entry1)
    canvas.grid(column=5, row=11)
    tentative = 0
    price = rnd.randrange(0, 100)
    def validate():
        global tentative, text_lbl
        entry_proposal = entry1.get()
        if tentative == 0:
            if int(entry_proposal) == price:
                print('GG')
                tentative += 1
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
                print('GG')
                tentative += 1
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
            game_over = tk.Label(root,text='Game Over \n No more tentative', fg = 'black', font='Raleway 23')
            game_over.grid(column=6, row=12)



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

