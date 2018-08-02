from chessboard.board import Board
from myenum.color import Color
import copy

class Game:
    board = None
    players = []
    cur = 0

    def __init__(self,players):
        self.board = Board(8)
        self.players = players

        self.board.startPos()
        
        for player in players:
            player.pieces = self.board.getPiecesSide(player.side)
            print("Welcome player: "+player.name+" playing "+str(player.side.name))
        #self.move()
        self.board.print()
        
        
    def movePiece(self,player,piece,x,y):
        if(isMoveAllowed(player,piece,x,y) == True):
                if(self.board[x][y].occupied == True):
                   self.board.movePiece(piece,x,y) 

    def isMoveAllowed(self,player,piece,x,y):
        if(piece.side == player.side):
            if(piece.__class__.__name__ == "Pawn"):
                take = self.board.fields[x][y].occupied and self.board.fields[x][y].piece.side != piece.side
                allowed = piece.isMoveAllowed(x,y,take)
            else:
                allowed = piece.isMoveAllowed(x,y)

            if(allowed):
                tempBoard = copy.copy(self.board)
                tempBoard.movePiece(piece,x,y)
                if(not tempBoard.isCheck(player.side)):
                    return True
                else:
                    print("Can't be checked after move!")
                    return False
            else:
                print("Move not Allowed!")
                return False
        else:
            print("Wrong Color!")
            return False
        return False

    def move(self):
        player = self.players[self.cur]
        print("Next to move player: "+player.name+" as "+player.side.name)

        piece = player.pieces[0]
        if(player.side == Color.WHITE):
            y = piece.y + 1
        else:
            y = piece.y - 1
        x = 0
        while(not self.isMoveAllowed(player,piece,x,y)):
            print("Wrong")
        self.board.print()
        print(piece.x,piece.y)
