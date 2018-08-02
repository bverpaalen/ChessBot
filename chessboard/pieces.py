from myenum.color import Color

class Piece:
    side = None;
    x = -1
    y = -1

    def __init__(self,side,startx,starty):
        self.side = side
        self.x = startx
        self.y = starty

    def domove(self,newx,newy):
        self.x = newx
        self.y = newy
        return True

class Pawn(Piece):
    def isMoveAllowed(self,newx,newy,take):
        difx = newx - self.x
        dify = newy - self.y

        #print(newy,self.y)
        #print(difx,dify)
                
        if(difx == 0 and dify == 1 and take == False):
            return True
        elif((difx == 1 or difx == -1) and dify == 1 and take == True):
            return True
        return False

class Bishop(Piece):
    def isMoveAllowed(self,newx,newy):
        difx = newx - self.x
        dify = newy - self.y

        if(difx == dify and difx != 0):
            return True
        return False
            

class Knight(Piece):
    def isMoveAllowed(self,newx,newy):
        difx = newx - self.x
        dify = newy - self.y

        if((difx == 1 and dify == 2) or (difx == 2 and dify == 1)):
            return True
        return False

class Rook(Piece):
    def isMoveAllowed(self,newx,newy):
        difx = newx - self.x
        dify = newy - self.y

        if(difx == 0 or dify == 0):
            return True
        return False

class Queen(Piece):
    def isMoveAllowed(self,newx,newy):
        difx = newx - self.x
        dify = newy - self.y

        if((difx == 0 or dify == 0) or (difx == dify and difx != 0)):
            return True
        return False

class King(Piece):
    hasMoved = False
    
    def isCheck(self,x,y):
        return False
    
    def isMoveAllowed(self,newx,newy):
        difx = newx - self.x
        dify = newy - self.y

        if(((difx == 0 or dify == 0) or (difx == dify and difx != 0)) and (difx == 1 or difx == 0) and (dify == 0 or dify == 1) and not self.isCheck(newx,newy)):
            return True
        return False

    def domove(self,newx,newy):
        hasMoved = True
        self.x = newx
        self.y = newy
        return True

    

