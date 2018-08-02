from chessboard.field import field
from chessboard.pieces import *
from myenum.color import Color

class Board:
    size = -1
    fields = []
    white = []
    black = []

    def __init__(self,size):
        self.size = size
        self.createFields()

    def print(self):
        print()
        print("WHITE")
        for y in range(0,self.size):
            for x in range(0,self.size):
                if(self.fields[x][y].occupied == False):
                    print("Empty",end=" ")
                elif(self.fields[x][y].occupied == True):
                    print(self.fields[x][y].piece.__class__.__name__,end=" ")
                else:
                    print("ERROR "+str(x)+str(y),end=" ")
            print()
        print("BLACK")

    def createFields(self):
        for i in range(0,self.size):
            self.fields.append([])
            for j in range(0,self.size):
                self.fields[i].append(field())

    def startPos(self):
        size = self.size
        for x in range(0,size):
            self.fields[x][1].setPiece(Pawn(Color.WHITE,x,1))
            self.fields[x][size-2].setPiece(Pawn(Color.BLACK,x,size-2))

            #Rook
            if(x==0):
                self.fields[x][0].setPiece(Rook(Color.WHITE,x,0))
                self.fields[size-1][0].setPiece(Rook(Color.WHITE,size-1,0))

                self.fields[x][size-1].setPiece(Rook(Color.BLACK,x,size-1))
                self.fields[size-1][size-1].setPiece(Rook(Color.BLACK,size-1,size-1))
            #knight
            elif(x==1):
                self.fields[x][0].setPiece(Knight(Color.WHITE,x,0))
                self.fields[size-x-1][0].setPiece(Knight(Color.WHITE,size-x-1,0))

                self.fields[x][size-1].setPiece(Knight(Color.BLACK,x,size-1))
                self.fields[size-x-1][size-1].setPiece(Knight(Color.BLACK,size-x-1,size-1))
            #bishop
            elif(x==2):
                self.fields[x][0].setPiece(Bishop(Color.WHITE,x,0))
                self.fields[size-x-1][0].setPiece(Bishop(Color.WHITE,x,size-1))

                self.fields[x][size-1].setPiece(Bishop(Color.BLACK,x,size-1))
                self.fields[size-x-1][size-1].setPiece(Bishop(Color.BLACK,size-x-1,size-1))
            #king
            elif(x==3):
                self.fields[x][0].setPiece(King(Color.WHITE,x,0))

                self.fields[size-x-1][size-1].setPiece(King(Color.BLACK,size-x-1,size-1))
            #queen
            elif(x==4):
                self.fields[x][0].setPiece(Queen(Color.WHITE,x,0))

                self.fields[size-x-1][size-1].setPiece(Queen(Color.BLACK,size-x-1,size-1))

            #adding pawn to side list
            self.white.append(self.fields[x][1].piece)
            self.white.append(self.fields[x][0].piece)

            #adding piece to side list
            self.black.append(self.fields[x][size-2].piece)
            self.black.append(self.fields[size-x-1][size-1].piece)

    def movePiece(self,piece,x,y):
        self.removePiece(piece)
        self.setPiece(piece,x,y)
        
    def setPiece(self,piece,x,y):
        if(self.fields[x][y].occupied):
            if(self.fields[x][y].piece.color == piece.color):
                raise Exception("Taking same color")
            else:
                self.removePiece(self.fields[x][y].piece)
                self.fields[x][y] == piece
        else:
            self.fields[x][y] == piece

    def removePiece(self,piece):
        self.fields[piece.x][piece.y].removePiece();   

    def isCheck(self,side):
        return False
    
    def reset(self):
        fields = []
        createFields()
        startPos()

    def getPiecesSide(self,color):
        if(color == Color.WHITE):
            return self.white
        elif color == Color.BLACK:
            return self.black
