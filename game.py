from chessboard.board import Board

class Game:
    board = None
    players = []

    def __init__(self,players):
        self.board = Board(8)
        self.players = players

    def movePiece(self,player,piece,x,y):
        if(isMoveAllowed(player,piece,x,y) == True):
                if(self.board[x][y].occupied == True):
                   self.board.movePiece(piece,x,y) 

    def isMoveAllowed(self,player,piece,x,y):
        if(piece.Color == player.Color):
            if(piece.isMoveAllowed(x,y)):
                tempBoard = board
                tempBoard.movePiece(piece,x,y)
                if(not tempBoard.isCheck(player.color)):
                    return True
                else:
                    raise Exception("Can't be checked after move!")
            else:
                raise Exception("Move not Allowed!")
        else:
            raise Exception("Wrong Color!")
        return False
