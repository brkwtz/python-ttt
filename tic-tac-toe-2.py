from itertools import cycle
from random import randint

class Board(object):
    def __init__(self):
        self.tie = False
        self.win = False
        self.spaces = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    def __str__(self):
        return ("\nHere's the board. Blank spaces are assigned numbers.\n"
        "%s | %s | %s\n"
        "----------\n"
        "%s | %s | %s\n"
        "----------\n"
        "%s | %s | %s\n") % (self.spaces[0], self.spaces[1], self.spaces[2],
        self.spaces[3], self.spaces[4], self.spaces[5], self.spaces[6],
        self.spaces[7], self.spaces[8])

    def _tie_check(self):
        self.tie = True
        for space in self.spaces:
            if self._is_int(space):
                self.tie = False

    def _win_check(self):
        if self.spaces[0] == self.spaces[4] == self.spaces[8]:
            self.win = True
        elif self.spaces[2] == self.spaces[4] == self.spaces[6]:
            self.win = True
        elif self.spaces[3] == self.spaces[4] == self.spaces[5]:
            self.win = True
        elif self.spaces[0] == self.spaces[1] == self.spaces[2]:
            self.win = True
        elif self.spaces[6] == self.spaces[7] == self.spaces[8]:
            self.win = True
        elif self.spaces[0] == self.spaces[3] == self.spaces[6]:
            self.win = True
        elif self.spaces[1] == self.spaces[4] == self.spaces[7]:
            self.win = True
        elif self.spaces[2] == self.spaces[5] == self.spaces[8]:
            self.win = True
        else:
            self.win = False
            self._tie_check()

    def is_valid(self, move):
        try:
            return self._is_int(self.spaces[int(move)-1])
        except ValueError:
            return False

    def _make_move(self, player, move):
        self.spaces[int(move)-1] = player

    def _state(self):
        if self.win:
            return str(self)+"\nCongratulations!\nYou won the game of tic-tac-toe.\nGive yourself a tic on the tac.\n"
        elif self.tie:
            return str(self)+"\nIt's a draw.\nI hate it when that happens!\n"
        else:
            return "\nGreat choice.\nHand the keyboard to the other dude.\n"

    def _is_int(self, x):
        return type(x) is int

    def is_game_over(self):
        return self.win or self.tie

    def complete_move(self, move, player):
        if self.is_valid(move):
            self._make_move(player, move)
            self._win_check()
            return self._state()
        else:
            return "Sorry, that's not a valid move. Choose an available space."


def play_game(current_player, board, players):
    print board

    human = (current_player == "X")

    if human:
        move = raw_input("Where do you want to go? ")
    else:
        move = randint(1, 9)

    while not board.is_valid(move):
        if human:
            move = raw_input("Sorry, that's not a valid move. Choose an available space." )
        else:
            move = randint(1, 9)

    print board.complete_move(move, current_player)
    if board.is_game_over():
        return
    else:
        next_player = players.next()
        play_game(next_player, board, players)


board = Board()
players = cycle(['X','O'])
next_player = players.next()
play_game(next_player, board, players)
