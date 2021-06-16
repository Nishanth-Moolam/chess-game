

class Board:
    '''
    board class
    '''
    def __init__(self):
        self.pieces = {white: [], black: []}
        self.graveyard = {white: [], black: []}
        self.check = {white: False, black: False}
        self.checkmate = {white: False, black: False}

    def add_piece(self, piece):
        '''
        appends to the appropriate list in self pieces
        '''
        pass

    def move_to_graveyard(self, piece):
        '''
        removes from pieces, append to graveyard
        '''
        pass

    def update_board(self):
        '''
        removes old piece, finds new piece position of moved piece, adds the piece
        '''
        pass
    
    def update_check(self):
        '''
        performs the kings pieces' update_check functions, and updates board variable
        '''
        pass

    def update_checkmate(self):
        '''
        performs the kings pieces' update_checkmate functions, and updates board variable
        '''
        pass

    

    