from chessboard.pieces import *

def reset(resetPiece):
    resetPiece.domove(0,0)

def testPawn():
    print("Testing Pawn")
    pawn = Pawn(Color.WHITE,0,0)
    print(pawn.isMoveAllowed(0,1,False))
    reset(pawn)
    print(not pawn.isMoveAllowed(1,1,False))
    reset(pawn)
    print(pawn.isMoveAllowed(1,1,True))
    reset(pawn)
    print(not pawn.isMoveAllowed(0,1,True))
    reset(pawn)
    print("")

def testBishop():
    print("Testing Bishop")
    bishop = Bishop(Color.WHITE,0,0)
    print(bishop.isMoveAllowed(1,1))
    reset(bishop)
    print(not bishop.isMoveAllowed(0,1))
    print("")

def testKnight():
    print("Testing Knight")
    knight = Knight(Color.WHITE,0,0)
    print(knight.isMoveAllowed(1,2))
    reset(knight)
    print(not knight.isMoveAllowed(0,2))
    print("")

def testRook():
    print("Testing Rook")
    rook = Rook(Color.WHITE,0,0)
    print(rook.isMoveAllowed(0,1))
    reset(rook)
    print(not rook.isMoveAllowed(1,1))
    print("")

def testQueen():
    print("Testing Queen")
    queen = Queen(Color.WHITE,0,0)
    print(queen.isMoveAllowed(0,1))
    reset(queen)
    print(queen.isMoveAllowed(1,1))
    reset(queen)
    print(not queen.isMoveAllowed(1,2))
    print("")

def testKing():
    print("Testing King")
    king = King(Color.WHITE,0,0)
    print(king.isMoveAllowed(0,1))
    reset(king)
    print(king.isMoveAllowed(1,1))
    reset(king)
    print(not king.isMoveAllowed(1,2))
    reset(king)
    print(not king.isMoveAllowed(0,2))
    print("")

def main():
    print("Testing pieces")
    print("")
    testPawn()
    testBishop()
    testKnight()
    testRook()
    testQueen()
    testKing()
    print("Piece testing complete")
    
main()
