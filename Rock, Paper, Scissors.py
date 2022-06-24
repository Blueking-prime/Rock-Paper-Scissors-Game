from random import choice
#Scoreboard
p = 0
c = 0

t = 0
print('''Welcome to R, P, S
It's basically Rock, Paper, Scissors if that was'nt obvious
Anyway, you play any number of rounds you want against the computer
*How to Play*
-Standard Rock, Paper, Scissors rules
-'R' for Rock, 'P' for Paper and 'S' for Scissors
Basic stuff
Have fun!!''')
print ()
n = int(input('How many rounds? '))
while t < n:
    #Computer move
    c_turn = choice(['R', 'P', 'S'])
    c_value = 0
    if c_turn == 'R':
        c_value += 1
    elif c_turn == 'P':
        c_value += 2
    elif c_turn == 'S':
        c_value += 3

    #Player move
    p_turn = input('Make a move: ')
    p_value = 0
    if p_turn == 'R':
        p_value += 1
    elif p_turn == 'P':
        p_value += 2
    elif p_turn == 'S':
        p_value += 3

    print (c_turn)

    #Rule set
    if p_value == c_value:
        print ('Draw')
        print ('Player- ' + str(p) + ':' + str(c) + ' -Computer')
        print ()
    elif p_value == (c_value + 1):
        print ('You Win')
        p += 1
        print ('Player- ' + str(p) + ':' + str(c) + ' -Computer')
        print ()
    elif p_value == (c_value - 1):
        print ('You Lose')
        c += 1
        print ('Player- ' + str(p) + ':' + str(c) + ' -Computer')
        print ()
    elif p_value == 1 and c_value == 3:
        print ('You Win')
        p += 1
        print ('Player- ' + str(p) + ':' + str(c) + ' -Computer')
        print ()
    elif p_value == 3 and c_value == 1:
        print ('You Lose')
        c += 1
        print ('Player- ' + str(p) + ':' + str(c) + ' -Computer')
        print ()

    t += 1
print ()
if p > c:
    print ('Congrats!!!!')
elif p < c:
    print ('Chai, too bad')
else:
    print ('Huh, draw')