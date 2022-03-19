from services.constants import row_index, col_index

class Piece:
    def piece_type(self, is_white, piece_type):
        '''
        returns the peice type with its colour for the frontend
        '''
        if is_white:
            return piece_type+'-white'
        return piece_type+'-black'

    def add_move(self, position):
        '''
        appends a move that assumes false isKill. This must be overriden (or changed)
        '''
        self.moves.append(
            {
            "isKill": False,
            "newPosition": position
            }
        )

    def out(self):
        '''
        output formatting
        '''
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

        this looks messy. redo this
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

        self.find_possible_moves()

    def find_possible_moves(self):
        '''
        this method will return all moves possible assuming no other
        pieces exist on the board
        '''
        row, col = self.position
        for i in col_index:
            self.add_move([row, i])
        for j in row_index:
            self.add_move([j, col])

class Knight(Piece):
    def __init__(self, is_dead, is_white, position):
        self.is_dead = is_dead
        self.is_white = is_white
        self.type = 'knight'
        self.position = position
        self.moves = []

        self.find_possible_moves()

    def find_possible_moves(self):
        '''
        this method will return all moves possible assuming no other
        pieces exist on the board

        this is hard coded in for now. Might make it cleaner later
        '''
        row, col = self.position
        row_i, col_i = row_index.index(row), col_index.index(col)
        board_range = range(0,8)
        if row_i+2 in board_range and col_i+1 in board_range:
            new_row, new_col = row_index[row_i+2], col_index[col_i+1]
            self.add_move([new_row, new_col])
        if row_i+1 in board_range and col_i+2 in board_range:
            new_row, new_col = row_index[row_i+1], col_index[col_i+2]
            self.add_move([new_row, new_col])

        if row_i-2 in board_range and col_i+1 in board_range:
            new_row, new_col = row_index[row_i-2], col_index[col_i+1]
            self.add_move([new_row, new_col])
        if row_i-1 in board_range and col_i+2 in board_range:
            new_row, new_col = row_index[row_i-1], col_index[col_i+2]
            self.add_move([new_row, new_col])

        if row_i+2 in board_range and col_i-1 in board_range:
            new_row, new_col = row_index[row_i+2], col_index[col_i-1]
            self.add_move([new_row, new_col])
        if row_i+1 in board_range and col_i-2 in board_range:
            new_row, new_col = row_index[row_i+1], col_index[col_i-2]
            self.add_move([new_row, new_col])

        if row_i-2 in board_range and col_i-1 in board_range:
            new_row, new_col = row_index[row_i-2], col_index[col_i-1]
            self.add_move([new_row, new_col])
        if row_i-1 in board_range and col_i-2 in board_range:
            new_row, new_col = row_index[row_i-1], col_index[col_i-2]
            self.add_move([new_row, new_col])
            

class Bishop(Piece):
    def __init__(self, is_dead, is_white, position):
        self.is_dead = is_dead
        self.is_white = is_white
        self.type = 'bishop'
        self.position = position
        self.moves = []

        self.find_possible_moves()

    def find_possible_moves(self):
        '''
        this method will return all moves possible assuming no other
        pieces exist on the board
        '''
        row, col = self.position
        row_i, col_i = row_index.index(row), col_index.index(col)
        board_range = range(0,8)
        for i in board_range:
            if row_i+i in board_range and col_i+i in board_range:
                new_row, new_col = row_index[row_i+i], col_index[col_i+i]
                self.add_move([new_row, new_col])
            if row_i-i in board_range and col_i+i in board_range:
                new_row, new_col = row_index[row_i-i], col_index[col_i+i]
                self.add_move([new_row, new_col])
            if row_i+i in board_range and col_i-i in board_range:
                new_row, new_col = row_index[row_i+i], col_index[col_i-i]
                self.add_move([new_row, new_col])
            if row_i-i in board_range and col_i-i in board_range:
                new_row, new_col = row_index[row_i-i], col_index[col_i-i]
                self.add_move([new_row, new_col])

class Queen(Piece):
    def __init__(self, is_dead, is_white, position):
        self.is_dead = is_dead
        self.is_white = is_white
        self.type = 'queen'
        self.position = position
        self.moves = []

        self.find_possible_moves()

    def find_possible_moves(self):
        '''
        this method will return all moves possible assuming no other
        pieces exist on the board
        '''
        row, col = self.position
        row_i, col_i = row_index.index(row), col_index.index(col)
        board_range = range(0,8)

        for i in col_index:
            self.add_move([row, i])
        for j in row_index:
            self.add_move([j, col])

        for i in board_range:
            if row_i+i in board_range and col_i+i in board_range:
                new_row, new_col = row_index[row_i+i], col_index[col_i+i]
                self.add_move([new_row, new_col])
            if row_i-i in board_range and col_i+i in board_range:
                new_row, new_col = row_index[row_i-i], col_index[col_i+i]
                self.add_move([new_row, new_col])
            if row_i+i in board_range and col_i-i in board_range:
                new_row, new_col = row_index[row_i+i], col_index[col_i-i]
                self.add_move([new_row, new_col])
            if row_i-i in board_range and col_i-i in board_range:
                new_row, new_col = row_index[row_i-i], col_index[col_i-i]
                self.add_move([new_row, new_col])


class King(Piece):
    def __init__(self, is_dead, is_white, position):
        self.is_dead = is_dead
        self.is_white = is_white
        self.type = 'king'
        self.position = position
        self.moves = []

        self.find_possible_moves()

    def find_possible_moves(self):
        '''
        this method will return all moves possible assuming no other
        pieces exist on the board
        '''
        row, col = self.position
        row_i, col_i = row_index.index(row), col_index.index(col)
        board_range = range(0,8)

        if row_i+1 in board_range and col_i+1 in board_range:
            self.add_move([row_index[row_i+1], col_index[col_i+1]])
        if row_i+1 in board_range and col_i in board_range:
            self.add_move([row_index[row_i+1], col_index[col_i]])
        if row_i+1 in board_range and col_i-1 in board_range:
            self.add_move([row_index[row_i+1], col_index[col_i-1]])

        if row_i in board_range and col_i+1 in board_range:
            self.add_move([row_index[row_i], col_index[col_i+1]])
        if row_i in board_range and col_i-1 in board_range:
            self.add_move([row_index[row_i], col_index[col_i-1]])

        if row_i-1 in board_range and col_i+1 in board_range:
            self.add_move([row_index[row_i-1], col_index[col_i+1]])
        if row_i-1 in board_range and col_i in board_range:
            self.add_move([row_index[row_i-1], col_index[col_i]])
        if row_i-1 in board_range and col_i-1 in board_range:
            self.add_move([row_index[row_i-1], col_index[col_i-1]])

