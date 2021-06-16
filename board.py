

class Board:
    def __init__(self):
        self.pieces = {white: [], black: []}
        self.graveyard = {white: [], black: []}
        self.check = {white: False, black: False}
        self.checkmate = {white: False, black: False}

    def add_piece(self, piece):
        pass

    def move_to_graveyard(self, piece):
        pass

    def update_board(self):
        '''
        removes old piece, finds new piece position of moved piece, adds the piece
        '''
        pass
    
    def update_check(self):
        pass

    def update_checkmate(self):
        pass

    

    