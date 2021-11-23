import tkinter as tk
from PIL import Image, ImageTk
import random2 as rnd
import time

def place_image(photo, bg, x, y):
    label = tk.Label(image=photo, bg=bg)
    label.image = photo
    label.place(x=x, y=y)

def place_text(master, txt, x, y, bg, j='center', fg='black', font='Times', wraplength=100000):
    global text
    text = tk.Label(master=master, text=txt, font=font, bg=bg, fg=fg, justify=j,wraplength=wraplength )
    text.place(x=x, y=y)

def place_button(master, text, x, y, bg, command, fg='black' ,font='Times'):
    button_text = tk.StringVar()
    button = tk.Button(master=master, textvariable=button_text, font=font, command=command, highlightbackground=bg, fg=fg, bg=bg, highlightcolor=bg, activebackground=bg)
    button_text.set(text)
    button.place(x=x, y=y)

root = tk.Tk()

#Aspect - Main Window 
root.title('The Price is Right - The Game')
root.geometry("1200x650")
root['background']='#fbda74'

#Aspect - Banner
banner = tk.Frame(root, width=1200, height=100, bg="#e71b24", borderwidth=100).place(x=0, y=0 )
banner2 = tk.Frame(root, width=16, height=100, bg="#fbda74", borderwidth=100).place(x=320, y=0)
banner3 = tk.Frame(root, width=16, height=550, bg="#e71b24",borderwidth=100).place(x=320, y=100)
banner4 = tk.Frame(root, width=16, height=100, bg="#fbda74", borderwidth=100).place(x=864, y=0)
banner5 = tk.Frame(root, width=16, height=550, bg="#e71b24",borderwidth=100).place(x=864, y=100)

image = Image.open("/Users/rdoyen/PythonProject/Just_Price/image/the_price_is_right_logo.png")
photo = ImageTk.PhotoImage(image.resize((85, 85)))
place_image(photo, '#e71b24', 5, 5)
place_image(photo, '#e71b24', 1110, 5)
place_text(master=root, txt='The Price is Right',bg="#e71b24", x=524, y=35, font='Calibri 18', fg='white')

#Left Pan - Instruction
instruction_txt = 'In this game, there are two game modes :  \n \n 1) Tentatives'\
                  ' - You have a limited number of trials to find the Just Price \n 2) TimeOut'\
                  ' - You have a limited time to find the Just Price \n \n Which one do you want to play?'
place_text(master=root, txt=instruction_txt, bg='#fbda74' , x = 5, y= 125, font='Calibri 16', j = 'left',wraplength=300)

image = Image.open("/Users/rdoyen/PythonProject/Just_Price/image/wip.png")
photo = ImageTk.PhotoImage(image.resize((20, 20)))
place_image(photo, '#fbda74', 7, 230)

image = Image.open("/Users/rdoyen/PythonProject/Just_Price/image/wip.png")
photo = ImageTk.PhotoImage(image.resize((30, 30)))
place_image(photo, '#fbda74', 100, 371)

def gm_tentative():
    place_text(root, 'Mode Tentative', 531, 105, '#fbda74', j='center', font='Helvetica 18 bold underline')

def gm_timeout():
    global text
    place_text(root, 'Mode not yet available', 25, 420, '#fbda74', j='left', font='Helvetica 18 bold')
    root.after(2000, text.destroy)


y_button = 340
place_button(master=root, text='Tentative', x=25, y=y_button,  bg="red", font='Helvetica 16 bold', command=gm_tentative)
place_button(master=root, text='TimeOut', x=25, y=y_button+35, bg='red', font='Helvetica 16 bold', command=gm_timeout)


#Display
root.mainloop()

