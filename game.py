from piece import *

class ChessGame:
    '''
    Initialize the game
    '''
    def __init__(self):
        self.col_names = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
        self.board = {}
        for letter in self.col_names:
            self.board[letter] = [None] * 9
        # Populate pawns
        for col in self.col_names:
            # White Pawns
            self.board[col][2] = Pawn((col, 2), True)
            # Black Pawns
            self.board[col][7] = Pawn((col, 7), False)
        
        
        self.graveyard = {'white': [], 'black': []}
        self.check = {'white': False, 'black': False}
        self.checkmate = {'white': False, 'black': False}

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
    
    '''
    
    '''
    def __str__(self):
        p1 = Pawn(('A', 1), is_white=True)
        p2 = Pawn(('B', 2), is_white=False)
        '''
        P .
        . P
        '''
        return p1.print_game() + " .\n. " + p2.print_game()
    
    def __repr__(self):
        return self.__str__()


if __name__ == '__main__':
    game = ChessGame()