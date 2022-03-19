from services.constants import row_index, col_index

class Piece:
    def piece_type(self, is_white, piece_type):
        if is_white:
            return piece_type+'-white'
        return piece_type+'-black'

    def add_move(self, position):
        self.moves.append(
            {
            "isKill": False,
            "newPosition": position
            }
        )

    def out(self):
        return {
            "type":self.piece_type(self.is_white, self.type), 
            "isWhite": self.is_white,
            "isDead": self.is_dead,
            "moves": self.moves
            }

class Pawn(Piece):
    def __init__(self, is_dead, is_white, position):
        """
        is_dead: boolean
        is_white: boolean
        """
        self.is_dead = is_dead
        self.is_white = is_white
        self.type = 'pawn'
        self.position = position
        self.moves = []

        self.find_possible_moves()

    def find_possible_moves(self):
        '''
        this method will return all moves possible assuming no other
        pieces exist on the board
        '''
        row = row_index.index(self.position[0])
        col = col_index.index(self.position[1])
        if self.is_white:
            self.add_move([row_index[row+1], col_index[col]])
            # first move may move up 2 (row = 1 means second row)
            if row == 1:
                self.add_move([row_index[row+2], col_index[col]])
        elif not self.is_white:
            self.add_move([row_index[row-1], col_index[col]])
            # first move may move up 2 (row = 1 means second row)
            if row == 6:
                self.add_move([row_index[row-2], col_index[col]])

class Rook(Piece):
    def __init__(self, is_dead, is_white, position):
        self.is_dead = is_dead
        self.is_white = is_white
        self.type = 'rook'
        self.position = position
        self.moves = []

    def find_possible_moves(self):
        pass

class Knight(Piece):
    def __init__(self, is_dead, is_white, position):
        self.is_dead = is_dead
        self.is_white = is_white
        self.type = 'knight'
        self.position = position
        self.moves = []

    def find_possible_moves(self):
        pass

class Bishop(Piece):
    def __init__(self, is_dead, is_white, position):
        self.is_dead = is_dead
        self.is_white = is_white
        self.type = 'bishop'
        self.position = position
        self.moves = []

    def find_possible_moves(self):
        pass

class Queen(Piece):
    def __init__(self, is_dead, is_white, position):
        self.is_dead = is_dead
        self.is_white = is_white
        self.type = 'queen'
        self.position = position
        self.moves = []

    def find_possible_moves(self):
        pass

class King(Piece):
    def __init__(self, is_dead, is_white, position):
        self.is_dead = is_dead
        self.is_white = is_white
        self.type = 'king'
        self.position = position
        self.moves = []

    def find_possible_moves(self):
        pass
