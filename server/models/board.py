from services.constants import row_index, col_index
from models.piece import *

class Board:
    def __init__(self, board):
        self.board = {
            '1': { 'a': None, 'b': None, 'c': None, 'd': None, 'e': None, 'f': None, 'g': None, 'h': None },
            '2': { 'a': None, 'b': None, 'c': None, 'd': None, 'e': None, 'f': None, 'g': None, 'h': None },
            '3': { 'a': None, 'b': None, 'c': None, 'd': None, 'e': None, 'f': None, 'g': None, 'h': None },
            '4': { 'a': None, 'b': None, 'c': None, 'd': None, 'e': None, 'f': None, 'g': None, 'h': None },
            '5': { 'a': None, 'b': None, 'c': None, 'd': None, 'e': None, 'f': None, 'g': None, 'h': None },
            '6': { 'a': None, 'b': None, 'c': None, 'd': None, 'e': None, 'f': None, 'g': None, 'h': None },
            '7': { 'a': None, 'b': None, 'c': None, 'd': None, 'e': None, 'f': None, 'g': None, 'h': None },
            '8': { 'a': None, 'b': None, 'c': None, 'd': None, 'e': None, 'f': None, 'g': None, 'h': None }
        }
        for row in row_index:
            for col in col_index:
                if board[row][col]:
                    piece_type = board[row][col]['type'].split('-')[0]
                    is_dead = board[row][col]['isDead']
                    is_white = board[row][col]['isWhite']
                    position = [row, col]
                    if piece_type == 'pawn':
                        self.board[row][col] = Pawn(is_dead=is_dead, is_white=is_white, position=position).out()
                    elif piece_type == 'rook':
                        self.board[row][col] = Rook(is_dead=is_dead, is_white=is_white, position=position).out()
                    elif piece_type == 'knight':
                        self.board[row][col] = Knight(is_dead=is_dead, is_white=is_white, position=position).out()
                    elif piece_type == 'bishop':
                        self.board[row][col] = Bishop(is_dead=is_dead, is_white=is_white, position=position).out()
                    elif piece_type == 'queen':
                        self.board[row][col] = Queen(is_dead=is_dead, is_white=is_white, position=position).out()
                    elif piece_type == 'king':
                        self.board[row][col] = King(is_dead=is_dead, is_white=is_white, position=position).out()