from collections import Counter
from random import randint as ri
from dialog import DialogReader as dr
"""    
"  1| 3| 5 "
"----------"
" 16|18|20 "
"----------"
" 31|33|35 "
"""
while True:
    # Creating the board
    board = list("  | | "+"\n"+"-------"+"\n"+"  | | "+"\n"+"-------"+"\n"+"  | | ")
    #board = list("  |o|x"+"\n"+"-------"+"\n"+" x|x|o"+"\n"+"-------"+"\n"+" o|x|o") test board
    for i in board:
        print(i, end="")
    print()

    #Assigning variables
    g = Counter(x1= 0, o1= 0, x2= 0, o2= 0, x3= 0, o3= 0, x4= 0, o4= 0)
    sl = [1,3,5,16,18,20,31,33,35]
    su = [1,16,31,3,18,33,5,20,35]
    cu = {1:0,16:0,31:0,3:0,18:0,33:0,5:0,20:0,35:0}
    #cu = {1} test cu
    sd1 = [1,18,35]
    sd2 = [5,18,31]
    win = ""
    c = {}
    s = {}
    score = cu
    f = 3
    h = 3
    m = 0
    typ = 0
    p1 = "x"
    p2 = 0
    turn = ri(0,1)

    #Assigning dictionary
    for i in board:
        c[m] = i
        m += 1
    for _ in range(3):
        for i in sl[(h-3):h]:
            s[i] = int(h/3)
        h += 3
    #print(s)
    h = 3

    # Main loop
    while True:
        #Turn Checker
        while True:
            if turn == 0:
                # Input Rule
                print("Your turn!")
                n = int(dr.dialog("Input a number ", ["numb"]))
            if turn == 1:
                if p1 == "x":
                    p = "o"
                else:
                    p = "x"
                if p2 == 0:
                    # Computer input Rule
                    print("Computer's turn!")
                    while True:
                        k = ri(0, 35)
                        if c[k] == " " and k != 0 and k != 15 and k != 30:
                            n = k
                            break
                        
                else:
                    # Second player's Rule
                    print("Your turn!")
                    p1 = "x"
                    n = int(dr.dialog("Input a number ", ["numb"]))

            # input checker
            if typ == 0 and (turn == 0 or p2 == 1):
                if n > 9:
                    n = 9
                if n <= 0:
                    n = 1
                n = sl[n - 1]
            elif typ == 1 and (turn == 0 or p2 == 1):
                if n > 8:
                    n = 8
                if n <= 0:
                    n = 1
                n = sl[n]
            else:
                n = n

            #Error Checker Section
            if n > 35:
                n = 35
            if board[n] != "|" and board[n] != "\n" and  board[n] != "-" and n != 0 and n != 15 and n != 30:
                if board[n] != "x" and board[n] != "o":
                    if turn == 0:
                        board[n] = p1
                        c[n] = p1
                        break
                    elif turn == 1:
                        board[n] = p
                        c[n] = p
                        break
                else:
                    print("Space occupied!")
            else:
                print("wrong input!")

        # Game Rules
        while True:
            for w in g:
                #reset Rule
                g[w] = 0
            for k in c.keys():
                # Straight Up Rule
                for i in su[(f-3):f]:
                    if k == i:
                        if c[k] == "x":
                            g["x1"] += 1
                        if c[k] == "o":
                            g["o1"] += 1
                # Straight left Rule
                for i in sl[(f-3):f]:
                    if k == i:
                        if c[k] == "x":
                            g["x2"] += 1
                        if c[k] == "o":
                            g["o2"] += 1
                # Diagonals 1Rule
                for i in sd1:
                    if k == i:
                        if c[k] == "x":
                            g["x3"] += 1
                        if c[k] == "o":
                            g["o3"] += 1
                # Diagonals 2Rule
                for i in sd2:
                    if k == i:
                        if c[k] == "x":
                            g["x4"] += 1
                        if c[k] == "o":
                            g["o4"] += 1

            #Win Rule
            for w in g:
                if g[w] == 3:
                    win = str(w)[0]
                    break
            if cu != {}:
                for i in cu:
                    if i == n:
                        cu.pop(i)
                        break
            if cu == {} and win == "":
                win = str("no one")
                break
            
            #Continue Rule
            f += 3
            if f > 9:
                f = 0
                break
        if turn >= 1:
            turn = 0
        else:
            turn += 1
        
        # Drawing board
        for i in board:
            print(i, end="")
        print()

        #winner checker
        if win != "":
            print(win, "won the game")
            break

    # Continue Statement
    contyn = dr.dialog("Do you want to continue Yes[Y] or No[N] ")
    if contyn[0].lower().strip() == "n":
        break