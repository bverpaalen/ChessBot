class field:
    occupied = false
    piece = None

    def setPiece(self,newPiece):
        occupied = True
        self.piece = newPiece

    def removePiece(self):
        occupied = False
        self.piece = None
