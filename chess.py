#Student number: 124500679

import sys

class Point():
    """Point class to represent a point with two coordinates x and y."""

    def __init__(self, x, y):
        """
        Constructor for Point class.
        
        Args:
            x - x coordinate, type int
            y - y coordinate, type int
        """
        
        if type(x) is not int or type(y) is not int:
            raise(TypeError("x and y should be of type int."))
        self._x = x
        self._y = y

class Piece():
    """Piece superclass to represent a basic chess piece."""

    def __init__(self, x, y, colour):
        """
        Constructor for Piece class.
        
        Args:
            x - x coordinate, type int
            y - y coordinate, type int
            colour - colour of chess piece, should be 'black' or 'white'
        """
        
        if colour not in ["black", "white"]:
            raise(TypeError("colour should be 'black' or 'white'."))
        self._pos = Point(x, y)
        self._colour = colour
        self._shape = None

    def __str__(self):
        return self._shape
    
    @property
    def shapeColour(self):
        return self._shape

    @shapeColour.setter
    def shapeColour(self, colour, 
                    blackSymbols = ["♙", "♘", "♗", "♖", "♕", "♔"], 
                    whiteSymbols = ["♟", "♞", "♝", "♜", "♛", "♚"], 
                    pieceTypes = ["pawn", "knight", "bishop", "rook", "queen", "king"]):
        if colour == "black":
            self._shape = blackSymbols[pieceTypes.index(self._type)]
        elif colour == "white":
            self._shape = whiteSymbols[pieceTypes.index(self._type)]
    
    def checkMove(self, x, y):
        """
        Checks if move is valid.
        If it meets the conditions, it sets the new position of the piece.
        Returns boolean.
        """

        #self._pos = Point(x, y)
        return True

class Pawn(Piece):
    """Pawn subclass to represent a pawn piece."""

    def __init__(self, x, y, colour):
        """
        Constructor for Pawn class.
        
        Args:
            x - x coordinate, type int
            y - y coordinate, type int
            colour - colour of chess piece, should be 'black' or 'white'
        """
        
        super().__init__(x, y, colour)
        self._type = "pawn"
        self.shapeColour = colour

    def checkMove(self, x, y):
        if self._colour == "white":
            if self._pos._y == y:
                if self._pos._x == 6:
                    if self._pos._x - x == 2:
                        return True
                if self._pos._x - x == 1:
                    return True
            
        if self._colour == "black":
            if self._pos._y == y: 
                if self._pos._x == 1:
                    if self._pos._x + 2 == x:
                        return True
                if self._pos._x + 1 == x:
                    return True
            
        return False
        
class Knight(Piece):
    """Knight subclass to represent a knight piece."""

    def __init__(self, x, y, colour):
        """
        Constructor for Knight class.
        
        Args:
            x - x coordinate, type int
            y - y coordinate, type int
            colour - colour of chess piece, should be 'black' or 'white'
        """
        
        super().__init__(x, y, colour)
        self._type = "knight"
        self.shapeColour = colour

class Bishop(Piece):
    """Bishop subclass to represent a bishop piece."""

    def __init__(self, x, y, colour):
        """
        Constructor for Bishop class.
        
        Args:
            x - x coordinate, type int
            y - y coordinate, type int
            colour - colour of chess piece, should be 'black' or 'white'
        """
        
        super().__init__(x, y, colour)
        self._type = "bishop"
        self.shapeColour = colour

class Rook(Piece):
    """Rook subclass to represent a rook piece."""

    def __init__(self, x, y, colour):
        """
        Constructor for Rook class.
        
        Args:
            x - x coordinate, type int
            y - y coordinate, type int
            colour - colour of chess piece, should be 'black' or 'white'
        """
        
        super().__init__(x, y, colour)
        self._type = "rook"
        self.shapeColour = colour

class Queen(Piece):
    """Queen subclass to represent a queen piece."""

    def __init__(self, x, y, colour):
        """
        Constructor for Queen class.
        
        Args:
            x - x coordinate, type int
            y - y coordinate, type int
            colour - colour of chess piece, should be 'black' or 'white'
        """
        
        super().__init__(x, y, colour)
        self._type = "queen"
        self.shapeColour = colour

class King(Piece):
    """King subclass to represent a king piece."""

    def __init__(self, x, y, colour):
        """
        Constructor for King class.
        
        Args:
            x - x coordinate, type int
            y - y coordinate, type int
            colour - colour of chess piece, should be 'black' or 'white'
        """
        
        super().__init__(x, y, colour)
        self._type = "king"
        self.shapeColour = colour        

class WhitePlayer():
    """
    WhitePlayer class to represent the
    piece state of the white player.
    """
    
    def __init__(self):
        """Constructor for WhitePlayer class."""

        self._pieces = []
        for col in range(8):
            pawn = Pawn(6, col, "white")
            self._pieces.append(pawn)
        for col in range(1,7,5):
            knight = Knight(7, col, "white")
            self._pieces.append(knight)
        for col in range(0,8,7):
            rook = Rook(7, col, "white")
            self._pieces.append(rook)
        for col in range(2,6,3):
            bishop = Bishop(7, col, "white")
            self._pieces.append(bishop)
        queen = Queen(7, 3, "white")
        self._pieces.append(queen)
        king = King(7, 4, "white")
        self._pieces.append(king)
        

class BlackPlayer():
    """
    BlackPlayer class to represent the
    piece state of the black player.
    """
    def __init__(self):
        """Constructor for WhitePlayer class."""

        self._pieces = []
        for col in range(8):
            pawn = Pawn(1, col, "black")
            self._pieces.append(pawn)
        for col in range(1,7,5):
            knight = Knight(0, col, "black")
            self._pieces.append(knight)
        for col in range(0,8,7):
            rook = Rook(0, col, "black")
            self._pieces.append(rook)
        for col in range(2,6,3):
            bishop = Bishop(0, col, "black")
            self._pieces.append(bishop)
        queen = Queen(0, 3, "black")
        self._pieces.append(queen)
        king = King(0, 4, "black")
        self._pieces.append(king)
        

class Board():
    """
    Board class to represent the
    board state of the game.
    """
    
    def __init__(self):
        """
        Constructor for Board class.
        
        Creates an 8x8 matrix and initialises starting
        piece postions.
        """
        self._board = [["O" for i in range(8)] for j in range(8)]
        self._toMove = "White"

        self._whiteSymbols = ["♙", "♘", "♗", "♖", "♕", "♔"]
        self._blackSymbols = ["♟", "♞", "♝", "♜", "♛", "♚"]
        self._letters = ["A", "B", "C", "D", "E", "F", "G", "H"]
        self._captured = []
            
        self._white = WhitePlayer()
        self._black = BlackPlayer()

        self._turnCount = 1

        for piece in self._black._pieces:
            self._board[piece._pos._x][piece._pos._y] = piece.shapeColour

        for piece in self._white._pieces:
            self._board[piece._pos._x][piece._pos._y] = piece.shapeColour


    def __str__(self):
        output = "__|"
        for i in range(8):
            output = output + "_" + self._letters[i] + "_" 
        for i in range(8):
            row = ""
            for j in range(8):
                row += " " + str(self._board[i][j]) + " "
            output = output + "\n " + str(i+1) + "|" + row
        return output
    
    def play(self):
        """Game loop. Player is able to move a piece or quit."""
        while True:
            print(self)
            if len(self._captured) == 0:
                print("\nNo captured pieces.", end="")
            else:
                print("\nCaptured pieces: ", end="")
                for piece in self._captured:
                    print(piece, end = " ")
            print(f"\n\nTurn {self._turnCount}"
                  f"\n{self._toMove} to move.\nEnter 'quit' to exit.\n"
                    "To move a piece, enter the starting postion and "
                    "target position seperated by a space (e.g. e7 e5).\n")
            inp = input("Enter: ")
            
            if inp.lower() == "quit":
                print("Quitting...")
                sys.exit()
            else:
                pos = inp.split(" ")
                try:
                    originalPos = pos[0]
                    targetPos = pos[1]
                except IndexError:
                    print("\n---Enter the positions in the format '[letter][number] [letter][number]'---")
                    self.play()
                if len(originalPos) == 2 and len(targetPos) == 2:
                    if originalPos[0].isalpha() and targetPos[0].isalpha():
                        if originalPos[1].isnumeric() and targetPos[1].isnumeric():
                            if self._toMove == "White":
                                self.move(originalPos, targetPos, self._white._pieces, self._black._pieces)
                                self.play()
                            elif self._toMove == "Black":
                                self.move(originalPos, targetPos, self._black._pieces, self._white._pieces)
                                self.play()
                print("\n---Enter the positions in the format '[letter][number] [letter][number]'---")
                self.play()

                            

    def move(self, originalPos, targetPos, pieces, opponentPieces):
        """
        Converts postion from [letter][number] form to matrix indices, 
        updates piece position and updates the board.
        
        Args:
            originalPos - original position in the form [letter][number]
            targetPos - target position in the form [letter][number]
            piece - list of current player's pieces
            opponentPieces - list of opponent player's pieces
        """

        originalY = self._letters.index(originalPos[0].upper())
        originalX = int(originalPos[1])-1
        targetY = self._letters.index(targetPos[0].upper())
        targetX = int(targetPos[1])-1
        for piece in pieces:
            if (originalX, originalY) == (piece._pos._x, piece._pos._y):
                if piece.checkMove(targetX, targetY):
                    for opponentPiece in opponentPieces:
                        if (targetX, targetY) == (opponentPiece._pos._x, opponentPiece._pos._y):
                            self.capture(opponentPiece)
                    piece._pos._x = targetX
                    piece._pos._y = targetY
                    self._board[targetX][targetY] = piece.shapeColour
                    self._board[originalX][originalY] = "O"
                    self.switchTurn()
                    return
                else: 
                    print("\nInvalid move")
                    return
        print("\nPiece not found.")
        return
        
    def switchTurn(self):
        """Sets toMove to the other player."""

        if self._toMove == "White":
            self._toMove = "Black"
        elif self._toMove == "Black":
            self._toMove = "White"
            self._turnCount += 1
        return

    def capture(self, piece):
        """
        Removes a piece from a players list of current pieces, and appends it to captured list.
        
        Args:
            piece - piece to be removed
        """
        if piece._colour == "black":
            self._black._pieces.remove(piece)
        else:
            self._white._pieces.remove(piece)
        self._captured.append(piece)
        return
    

if __name__ == "__main__":
    board = Board()
    board.play()