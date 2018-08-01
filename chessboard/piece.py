from enum import Enum

class Color(Enum):
    WHITE = 1
    BLACK = 2

class Piece:
    side = None;
    boardx = -1
    boardy = -1

    def __init__(self,side,startx,starty):
        self.side = side
        self.boardx = startx
        self.boardy = starty

    def domove(self,newx,newy):
        self.boardx = newx
        self.boardy = newy
        return True

class Pawn(Piece):
    def isMoveAllowed(self,newx,newy,take):
        difx = newx - self.boardx
        dify = newy - self.boardy

        #print(newy,self.boardy)
        #print(difx,dify)
                
        if(difx == 0 and dify == 1 and take == False):
            super().domove(newx,newy)
            return True
        elif((difx == 1 or difx == -1) and dify == 1 and take == True):
            super().domove(newx,newy)
            return True
        return False

class Bishop(Piece):
    def isMoveAllowed(self,newx,newy):
        difx = newx - self.boardx
        dify = newy - self.boardy

        if(difx == dify and difx != 0):
            super().domove(newx,newy)
            return True
        return False
            

class Knight(Piece):
    def isMoveAllowed(self,newx,newy):
        difx = newx - self.boardx
        dify = newy - self.boardy

        if((difx == 1 and dify == 2) or (difx == 2 and dify == 1)):
            super().domove(newx,newy)
            return True
        return False

class Rook(Piece):
    def isMoveAllowed(self,newx,newy):
        difx = newx - self.boardx
        dify = newy - self.boardy

        if(difx == 0 or dify == 0):
            super().domove(newx,newy)
            return True
        return False

class Queen(Piece):
    def isMoveAllowed(self,newx,newy):
        difx = newx - self.boardx
        dify = newy - self.boardy

        if((difx == 0 or dify == 0) or (difx == dify and difx != 0)):
            super().domove(newx,newy)
            return True
        return False

class King(Piece):
    
    def isCheck(self,x,y):
        return False
    
    def isMoveAllowed(self,newx,newy):
        difx = newx - self.boardx
        dify = newy - self.boardy

        if(((difx == 0 or dify == 0) or (difx == dify and difx != 0)) and (difx == 1 or difx == 0) and (dify == 0 or dify == 1) and not self.isCheck(newx,newy)):
            super().domove(newx,newy)
            return True
        return False

    

