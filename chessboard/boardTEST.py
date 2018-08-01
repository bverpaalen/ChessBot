from board import Board

def showFields(board):
    print("board size: "+str(board.size))
    for y in range(0,board.size):
        for x in range(0,board.size):
            if(board.fields[x][y].occupied == False):
                print("Empty",end=" ")
            elif(board.fields[x][y].occupied == True):
                print(board.fields[x][y].piece.__class__.__name__,end=" ")
            else:
                print("ERROR "+str(x)+str(y),end=" ")
        print("")

def showTeam(team):
    for piece in team:
        print(piece.__class__.__name__)

def main():
    board = Board()
    showFields(board)
    print()
    board.startPos()
    showFields(board)
    print("White:")
    showTeam(board.white)
    print("\nBlack: ")
    showTeam(board.black)

main()
