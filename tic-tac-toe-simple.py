spaces = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def is_int(x):
    return type(x) is int


# prints board as it currently looks and prompts move
def print_board():

    print "Here's the board. Blank spaces are assigned numbers."
    print "%r | %r | %r" % (spaces[0], spaces[1], spaces[2])
    print "----------"
    print "%r | %r | %r" % (spaces[3], spaces[4], spaces[5])
    print "----------"
    print "%r | %r | %r" % (spaces[6], spaces[7], spaces[8])


# function used to define a move, ideally the whole game should just be a loop of move(X), move(Y) until the game end
def move(player):
    # IMPORTANT: need to make it so all variables below inherit values from previous function!!!
    print_board()
    print "Where do you want to go?"
    move = int(raw_input(""))

    if is_int(spaces[move-1]):
        spaces[move-1] = player

        result(player)
    else:
        print "Sorry, that's not a valid move. Choose an available space."


# checks if there is a tie, only works in conjunction with win_check()
def tie_check():
    global tie
    tie = True
    for space in spaces:
        if is_int(space):
            tie = False
    # tie = any(type(space) is int for space in spaces)


# checks if there is a win, checks for tie if no win
def win_check():
    global win
    if spaces[0] == spaces[4] == spaces[8]:
        win = True
    elif spaces[2] == spaces[4] == spaces[6]:
        win = True
    elif spaces[3] == spaces[4] == spaces[5]:
        win = True
    elif spaces[0] == spaces[1] == spaces[2]:
        win = True
    elif spaces[6] == spaces[7] == spaces[8]:
        win = True
    elif spaces[0] == spaces[3] == spaces[6]:
        win = True
    elif spaces[1] == spaces[4] == spaces[7]:
        win = True
    elif spaces[2] == spaces[5] == spaces[8]:
        win = True
    else:
        win = False
        tie_check()


# function used to show result at end of each turn
def result(player):
    win_check()
    if win:
        print_board()
        print "\nCongratulations!\nYou won the game of tic-tac-toe.\nGive yourself a tic on the tac.\n"
    elif tie:
        print "\nIt's a draw.\nI hate it when that happens!\n"
    else:
        print "\nGreat choice.\nHand the keyboard to the other dude.\n"


win = tie = False
while (not win) and (not tie):
    move('X')
    if win or tie:
        break
    move('O')
