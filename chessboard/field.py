class field:
    occupied = False
    piece = None

    def setPiece(self,newPiece):
        self.occupied = True
        self.piece = newPiece

    def removePiece(self):
        self.occupied = False
        self.piece = None
