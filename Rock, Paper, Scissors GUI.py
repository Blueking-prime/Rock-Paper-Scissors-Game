from tkinter import *
from random import choice

root = Tk()
root.title('R, P, S')

l1 = Label(root, text = 'Welcome to R, P, S',font = ('Segoe UI Light', 20, 'bold')).grid(row = 0, column = 0, padx = 30, pady = 20)
l2 = Label(
    root, 
    text=
    '''This is basically Rock, Paper, Scissors, in case that wasn't obvious already
Anyway, you play any number of rounds you want against the computer''',
    font = ('Segoe UI Light', 11)
            ).grid(row = 1, column = 0, padx = 30)
lf1 = LabelFrame(root, text = 'HOW TO PLAY',font = ('Segoe UI Light', 16, 'bold italic'))
lf1.grid(row = 2, column = 0, padx = 30, pady = 10)
Label(lf1, text = '-Press \'Play Game!\' to start ', font = ('Segoe UI Light', 11)).grid(row = 0, column = 0, padx = 30, sticky = W)
Label(lf1, text = '-Standard Rock, Paper, Scissors rules', font = ('Segoe UI Light', 11)).grid(row = 1, column = 0, padx = 30, sticky = W)
Label(lf1, text = '-\'R\' for Rock, \'P\' for Paper and \'S\' for Scissors', font = ('Segoe UI Light', 11)).grid(row = 2, column = 0, padx = 30, sticky = W)
Label(lf1, text = '-Use the \'Reset\' button to reset the scoreboard', font = ('Segoe UI Light', 11)).grid(row = 3, column = 0, padx = 30, sticky = W)
Label(lf1, text = 'Basic stuff', font = ('Segoe UI Light', 11)).grid(row = 4, column = 0, padx = 30)
Label(lf1, text = 'Have fun!!', font = ('Segoe UI Light', 11)).grid(row = 5, column = 0, padx = 30)

lspace = Label(root, ).grid(row = 4, column = 0, pady = 10)

#Scoreboard
p = 0
c = 0

def play_game():
    game = Tk()
    game.title('Game!')
    game.geometry('410x295')

    def reset():
        global p
        global c
        c = 0
        p = 0
        Label(game).grid(row = 4, column = 0, columnspan = 5, sticky = W + E)
        Label(game).grid(row = 5, column = 0, columnspan = 5, sticky = W + E)
        lr2 = Label(game, text = 'Player- ' + str(p) + ':' + str(c) + ' -Computer', font = ('Segoe UI Light', 11)).grid(row = 6, column = 0, columnspan = 5, sticky = W + E, padx = (25, 0))

    #Game
    def p_move(p_turn):
        
        #Player's move
        p_value = 0
        if p_turn == 'R':
            p_value += 1
        elif p_turn == 'P':
            p_value += 2
        elif p_turn == 'S':
            p_value += 3

        #Computer move
        c_turn = choice(['R', 'P', 'S'])
        c_value = 0
        if c_turn == 'R':
            c_value += 1
        elif c_turn == 'P':
            c_value += 2
        elif c_turn == 'S':
            c_value += 3
        
        #Rule set
        global p
        global c
        if p_value == c_value:
            lr1 = Label(game, text = 'Draw', font = ('Segoe UI Light', 11)).grid(row = 4, column = 0, columnspan = 5, sticky = W + E, padx = (25, 0))
        elif p_value == (c_value + 1):
            lr1 = Label(game, text = 'You Win', font = ('Segoe UI Light', 11)).grid(row = 4, column = 0, columnspan = 5, sticky = W + E, padx = (25, 0))
            p += 1
        elif p_value == (c_value - 1):
            lr1 = Label(game, text = 'You Lose', font = ('Segoe UI Light', 11)).grid(row = 4, column = 0, columnspan = 5, sticky = W + E, padx = (25, 0))
            c += 1
        elif p_value == 1 and c_value == 3:
            lr1 = Label(game, text = 'You Win', font = ('Segoe UI Light', 11)).grid(row = 4, column = 0, columnspan = 5, sticky = W + E, padx = (25, 0))
            p += 1
        elif p_value == 3 and c_value == 1:
            lr1 = Label(game, text = 'You Lose', font = ('Segoe UI Light', 11)).grid(row = 4, column = 0, columnspan = 5, sticky = W + E, padx = (25, 0))
            c += 1
        
        lc1 = Label(game, text = 'Computer played ' + c_turn, font = ('Segoe UI Light', 11)).grid(row = 5, column = 0, columnspan = 5, sticky = W + E, padx = (25, 0))
        lr2 = Label(game, text = 'Player- ' + str(p) + ':' + str(c) + ' -Computer', font = ('Segoe UI Light', 11)).grid(row = 6, column = 0, columnspan = 5, padx = (25, 0))
        B2 = Button(game, text='Reset', padx = 35, pady = 20, relief = 'solid', borderwidth = 1, font = ('Segoe UI Light', 11), command = reset).grid(row = 7, column = 0, columnspan = 5, padx = (25, 0), pady = 10)
    #Move selection
    lp1 = Label(game, text = 'Make a move: ', font = ('Segoe UI Light', 20)).grid(row = 2, column = 0, columnspan = 5, pady = 10, padx = (25, 0))
    bp1 = Button(game, text='R', padx = 28, pady = 10, relief = 'solid', borderwidth = 1, font = ('Segoe UI Light', 11), command = lambda: p_move('R')).grid(row = 3, column = 0, padx = (25, 0))
    Button(game, padx = 30, pady = 10, relief = 'flat', state = DISABLED).grid(row = 3, column = 1)
    bp2 = Button(game, text='P', padx = 28, pady = 10, relief = 'solid', borderwidth = 1, font = ('Segoe UI Light', 11), command= lambda: p_move('P')).grid(row = 3, column = 2)
    Button(game, padx = 30, pady = 10, relief = 'flat', state = DISABLED).grid(row = 3, column = 3)
    bp3 = Button(game, text='S', padx = 28, pady = 10, relief = 'solid', borderwidth = 1, font = ('Segoe UI Light', 11), command= lambda: p_move('S')).grid(row = 3, column = 4)


B1 = Button(root, text='Play Game!', padx = 20, pady = 20, relief = 'solid', borderwidth = 1, font = ('Segoe UI Light', 11), command = play_game).grid(row = 5, column = 0, pady = (0, 30))

root.mainloop()