#! ./python3/bin/python3
test = False

from game import Game
from player import Player
from myenum.color import Color

if(test):
    from chessboard.pieceTEST import *
    from chessboard.boardTEST import *

def main():    
    a = Player("a",Color.WHITE)
    b = Player("b",Color.BLACK)
    players = [a,b]
    game = Game(players)
main()
