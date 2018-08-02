from chessboard.board import Board

def showFields(board):
    print("board size: "+str(board.size))
    board.print()

def showTeam(team):
    for piece in team:
        print(piece.__class__.__name__)

def main():
    board = Board(8)
    showFields(board)
    print()
    board.startPos()
    showFields(board)
    print("White:")
    showTeam(board.white)
    print("\nBlack: ")
    showTeam(board.black)

main()
