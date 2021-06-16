

class Piece:
    def __init__(self, position, is_white):
        self.position = position
        self.alive = True
        self.is_white = is_white

    def update_position(self, new_position):
        self.position = new_position

    def kill(self):
        self.alive = False

class Pawn(Piece):
    def find_all_possible_moves(self, pieces):
        '''
        pieces do not include self piece 
        '''
        pass

class Rook(Piece):
    def find_all_possible_moves(self, pieces):
        '''
        pieces do not include self piece 
        '''
        pass

class Knight(Piece):
    def find_all_possible_moves(self, pieces):
        '''
        pieces do not include self piece 
        '''
        pass

class Bishop(Piece):
    def find_all_possible_moves(self, pieces):
        '''
        pieces do not include self piece 
        '''
        pass

class Queen(Piece):
    def find_all_possible_moves(self, pieces):
        '''
        pieces do not include self piece 
        '''
        pass

class King(Piece):
    def __init__(self):
        self.check = False
        self.checkmate = False

    def find_all_possible_moves(self, pieces):
        '''
        pieces do not include self piece 
        '''
        pass

    def update_check(self, check):
        self.check = check

    def update_checkmate(self, checkmate):
        self.checkmate = checkmate