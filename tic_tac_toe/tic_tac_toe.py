from tkinter import *
import random
from PIL import Image, ImageTk


def next_turn(row, col):
    global player

    if buttons[row][col]['text'] == "" and winner_check() is False:
        if player == players[0]:
            buttons[row][col]['text'] = player
            if winner_check() is False:
                player = players[1]
                label.config(text=(players[1]+" turn"))

            elif winner_check() is True:
                label.config(text=(players[0]+" wins"))

            elif winner_check() == "Tie":
                label.config(text="Tie!")

        else:

            buttons[row][col]['text'] = player
            if winner_check() is False:
                player = players[0]
                label.config(text=(players[0]+" turn"))

            elif winner_check() is True:
                label.config(text=(players[1]+" wins"))

            elif winner_check() == "Tie":
                label.config(text="Tie!")


def winner_check():
    for row in range(3):
        if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] != "":
            buttons[row][0].config(bg='#12E195')
            buttons[row][1].config(bg='#12E195')
            buttons[row][2].config(bg='#12E195')
            return True

    for column in range(3):
        if buttons[0][column]['text'] == buttons[1][column]['text'] == buttons[2][column]['text'] != "":
            buttons[0][column].config(bg='#12E195')
            buttons[1][column].config(bg='#12E195')
            buttons[2][column].config(bg='#12E195')
            return True
    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
        buttons[0][0].config(bg='#12E195')
        buttons[1][1].config(bg='#12E195')
        buttons[2][2].config(bg='#12E195')
        return True
    elif buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "":
        buttons[0][2].config(bg='#12E195')
        buttons[1][1].config(bg='#12E195')
        buttons[2][0].config(bg='#12E195')
        return True
    elif empty_spaces() is False:
        for i in range(3):
            for j in range(3):
                buttons[i][j].config(bg="#7885FF")
        return "Tie"
    else:
        return False


def empty_spaces():
    spaces = 9
    for row in range(3):
        for column in range(3):
            if buttons[row][column]['text'] != "":
                spaces -= 1

    if spaces == 0:
        return False
    else:
        return True


def new_game():
    global player

    player = random.choice(players)

    label.config(text=player + " turn")

    for row in range(3):
        for column in range(3):
            buttons[row][column].config(text="", bg="#D3D0C9")


window = Tk()
window.title("Tic-Tac-Toe")
window.geometry("500x500")
window.resizable(width=False, height=False)
icon = PhotoImage(file="images\\icon.png")
window.iconphoto(True, icon)
window.config(bg="black")
players = ["X", "O"]
player = random.choice(players)
buttons = [[0, 0, 0],
           [0, 0, 0],
           [0, 0, 0]]

img = Image.open("images\\background.png")
img = img.resize((500, 500))
background = ImageTk.PhotoImage(img)
bg_label = Label(window,image=background)
bg_label.place(x=0, y=0)
label = Label(text=player + " turn", font=("Impact", 40), fg="white", bg="#220070")
label.pack(side="bottom")
photo = Image.open("images\\restart.png")
photo = photo.resize((70, 70))
restart = ImageTk.PhotoImage(photo)
restart_button = Button(window, image=restart, command=new_game)
restart_button.pack(side="top")


frame = Frame(window, bg="#220070", height=100, width=100)
frame.pack()

for i in range(3):
    for j in range(3):
        buttons[i][j] = Button(frame, text='', font=("Impact", 40), fg="#5F0FFF", bg="#D3D0C9", height=1, width=4,
                               command=lambda row=i, col=j: next_turn(row, col))
        buttons[i][j].grid(row=i, column=j)


window.mainloop()
