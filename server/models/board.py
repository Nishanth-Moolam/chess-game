from services.constants import row_index, col_index, empty_board
from models.piece import *

class Board:
    def __init__(self, board, selected_player):
        self.board = empty_board()

        self.map_pieces(board)

    def map_pieces(self, board):
        '''
        will put the pieces in the correct place on the board and find all possible moves
        for each piece
        '''
        for row in row_index:
            for col in col_index:
                if board[row][col]:
                    piece_type = board[row][col]['type'].split('-')[0]
                    is_dead = board[row][col]['isDead']
                    is_white = board[row][col]['isWhite']
                    position = [row, col]
                    if piece_type == 'pawn':
                        self.board[row][col] = Pawn(is_dead=is_dead, is_white=is_white, position=position)
                    elif piece_type == 'rook':
                        self.board[row][col] = Rook(is_dead=is_dead, is_white=is_white, position=position)
                    elif piece_type == 'knight':
                        self.board[row][col] = Knight(is_dead=is_dead, is_white=is_white, position=position)
                    elif piece_type == 'bishop':
                        self.board[row][col] = Bishop(is_dead=is_dead, is_white=is_white, position=position)
                    elif piece_type == 'queen':
                        self.board[row][col] = Queen(is_dead=is_dead, is_white=is_white, position=position)
                    elif piece_type == 'king':
                        self.board[row][col] = King(is_dead=is_dead, is_white=is_white, position=position)

    def get_exact_moves(self):
        '''
        finds exact moves for pieces
        '''
        pass

    def display_board(self):
        output_board = empty_board()
        for row in row_index:
            for col in col_index:
                if self.board[row][col]:
                    output_board[row][col] = self.board[row][col].out()

        return output_board
