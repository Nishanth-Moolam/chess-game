from services.constants import row_index, col_index, empty_board
from models.piece import *

class Board:
    def __init__(self, board, selected_player):
        self.board = empty_board()

        # attack positions of white pieces (attacking black team)
        self.white_attack_positions = []
        # attack positions of black pieces (attacking white team)
        self.black_attack_positions = []

        self.selected_player = selected_player

        self.map_pieces(board)
        self.get_exact_moves()

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
                    unmoved = board[row][col]['unmoved'] if ('unmoved' in board[row][col]) else False
                    position = [row, col]
                    if piece_type == 'pawn':
                        self.board[row][col] = Pawn(is_dead=is_dead, is_white=is_white, position=position, unmoved=unmoved)
                    elif piece_type == 'rook':
                        self.board[row][col] = Rook(is_dead=is_dead, is_white=is_white, position=position, unmoved=unmoved)
                    elif piece_type == 'knight':
                        self.board[row][col] = Knight(is_dead=is_dead, is_white=is_white, position=position, unmoved=unmoved)
                    elif piece_type == 'bishop':
                        self.board[row][col] = Bishop(is_dead=is_dead, is_white=is_white, position=position, unmoved=unmoved)
                    elif piece_type == 'queen':
                        self.board[row][col] = Queen(is_dead=is_dead, is_white=is_white, position=position, unmoved=unmoved)
                    elif piece_type == 'king':
                        self.board[row][col] = King(is_dead=is_dead, is_white=is_white, position=position, unmoved=unmoved)

    def get_exact_moves(self):
        '''
        finds exact moves for pieces (takes into account the selected player) and appends them to 
        moves in pieces
        * this will need to be refactored to deal with check
        * remember to add en passant
        * remember to add castle
        '''
        for row in row_index:
            for col in col_index:
                # only adds moves to the current player
                if self.board[row][col] and self.xnor(a = (self.selected_player == 'BLACK'), b = self.board[row][col].is_white):

                    piece = self.board[row][col]
                    row_i, col_i = row_index.index(row), col_index.index(col)
                    board_range = range(0,8) 

                    # This doesn't yet include en passant
                    if piece.type == 'pawn':
                        self.find_pawn_moves(row, col, piece, row_i, col_i, board_range)

                    elif piece.type == 'rook':
                        self.find_rook_moves(row, col, piece, row_i, col_i, board_range)

                    elif piece.type == 'knight':
                        self.find_knight_moves(row, col, piece, row_i, col_i, board_range)
                        
                    elif piece.type == 'bishop':
                        self.find_bishop_moves(row, col, piece, row_i, col_i, board_range)

                    elif piece.type == 'queen':
                        self.find_queen_moves(row, col, piece, row_i, col_i, board_range)

                    # This doesn't yet include castle
                    elif piece.type == 'king':
                        self.find_king_moves(row, col, piece, row_i, col_i, board_range)

    def find_pawn_moves(self, row, col, piece, row_i, col_i, board_range):
        attack_positions = []
        all_possible_moves = piece.find_possible_moves()

        # will identify positions on the board that the pawn can attack (if on board)
        if piece.is_white:
            if (row_i+1 in board_range) and (col_i+1 in board_range):
                attack_positions.append([row_index[row_i+1], col_index[col_i+1]])
            if (row_i+1 in board_range) and (col_i-1 in board_range):
                attack_positions.append([row_index[row_i+1], col_index[col_i-1]])
        else:
            if (row_i-1 in board_range) and (col_i+1 in board_range):
                attack_positions.append([row_index[row_i-1], col_index[col_i+1]])
            if (row_i-1 in board_range) and (col_i-1 in board_range):
                attack_positions.append([row_index[row_i-1], col_index[col_i-1]])
        # adds possible attacking moves
        for position in attack_positions:
            attack_piece = self.board[position[0]][position[1]]
            self.add_attack_position(piece, position)
            if attack_piece and (attack_piece.is_white is not piece.is_white):
                piece.add_move(position = position, is_kill = True)
        # adds the possible moves if there is no piece in the way
        for position in all_possible_moves:
            blocking_piece = self.board[position[0]][position[1]]
            if not blocking_piece:
                piece.add_move(position = position, is_kill = False)

    def find_rook_moves(self, row, col, piece, row_i, col_i, board_range):
        # this doesn't use the find all moves function
        # checks all 4 directions with a separate loop
        for i in board_range:
            if (row_i+i in board_range):
                position = [row_index[row_i+i], col]
                if position != piece.position:
                    attack_piece = self.board[row_index[row_i+i]][col]
                    if attack_piece:
                        if attack_piece.is_white is not piece.is_white:
                            piece.add_move(position = position, is_kill = True)
                            self.add_attack_position(piece, position)
                        break
                    piece.add_move(position = position, is_kill = False)
                    self.add_attack_position(piece, position)
        for i in board_range:    
            if (row_i-i in board_range):
                position = [row_index[row_i-i], col]
                if position != piece.position:
                    attack_piece = self.board[row_index[row_i-i]][col]
                    if attack_piece:
                        if attack_piece.is_white is not piece.is_white:
                            piece.add_move(position = position, is_kill = True)
                            self.add_attack_position(piece, position)
                        break
                    piece.add_move(position = position, is_kill = False)
                    self.add_attack_position(piece, position)
        for i in board_range:
            if (col_i+i in board_range):
                position = [row, col_index[col_i+i]]
                if position != piece.position:
                    attack_piece = self.board[row][col_index[col_i+i]]
                    if attack_piece:
                        if attack_piece.is_white is not piece.is_white:
                            piece.add_move(position = position, is_kill = True)
                            self.add_attack_position(piece, position)
                        break
                    piece.add_move(position = position, is_kill = False)
                    self.add_attack_position(piece, position)
        for i in board_range:
            if (col_i-i in board_range):
                position = [row, col_index[col_i-i]]
                if position != piece.position:
                    attack_piece = self.board[row][col_index[col_i-i]]
                    if attack_piece:
                        if attack_piece.is_white is not piece.is_white:
                            piece.add_move(position = position, is_kill = True)
                            self.add_attack_position(piece, position)
                        break
                    piece.add_move(position = position, is_kill = False)
                    self.add_attack_position(piece, position)

    def find_knight_moves(self, row, col, piece, row_i, col_i, board_range):
        all_possible_moves = piece.find_possible_moves()

        for position in all_possible_moves:
            attack_piece = self.board[position[0]][position[1]]
            if attack_piece and (attack_piece.is_white != piece.is_white):
                piece.add_move(position = position, is_kill = True)
                self.add_attack_position(piece, position)
            elif not attack_piece:
                piece.add_move(position = position, is_kill = False)
                self.add_attack_position(piece, position)

    def find_bishop_moves(self, row, col, piece, row_i, col_i, board_range):
        '''
        does not use find all move function in piece
        '''
        for i in board_range:
            if row_i+i in board_range and col_i+i in board_range:
                position = [row_index[row_i+i], col_index[col_i+i]]
                if position != piece.position:
                    attack_piece = self.board[position[0]][position[1]]
                    if attack_piece:
                        if attack_piece.is_white is not piece.is_white:
                            piece.add_move(position = position, is_kill = True)
                            self.add_attack_position(piece, position)
                        break
                    piece.add_move(position = position, is_kill = False)
                    self.add_attack_position(piece, position)
        for i in board_range:
            if row_i+i in board_range and col_i-i in board_range:
                position = [row_index[row_i+i], col_index[col_i-i]]
                if position != piece.position:
                    attack_piece = self.board[position[0]][position[1]]
                    if attack_piece:
                        if attack_piece.is_white is not piece.is_white:
                            piece.add_move(position = position, is_kill = True)
                            self.add_attack_position(piece, position)
                        break
                    piece.add_move(position = position, is_kill = False)
                    self.add_attack_position(piece, position)
        for i in board_range:
            if row_i-i in board_range and col_i+i in board_range:
                position = [row_index[row_i-i], col_index[col_i+i]]
                if position != piece.position:
                    attack_piece = self.board[position[0]][position[1]]
                    if attack_piece:
                        if attack_piece.is_white is not piece.is_white:
                            piece.add_move(position = position, is_kill = True)
                            self.add_attack_position(piece, position)
                        break
                    piece.add_move(position = position, is_kill = False)
                    self.add_attack_position(piece, position)
        for i in board_range:
            if row_i-i in board_range and col_i-i in board_range:
                position = [row_index[row_i-i], col_index[col_i-i]]
                if position != piece.position:
                    attack_piece = self.board[position[0]][position[1]]
                    if attack_piece:
                        if attack_piece.is_white is not piece.is_white:
                            piece.add_move(position = position, is_kill = True)
                            self.add_attack_position(piece, position)
                        break
                    piece.add_move(position = position, is_kill = False)
                    self.add_attack_position(piece, position)

    def find_queen_moves(self, row, col, piece, row_i, col_i, board_range):
        '''
        does not use find all move function in piece
        '''
        # Vertical & Horizontal
        for i in board_range:
            if (row_i+i in board_range):
                position = [row_index[row_i+i], col]
                if position != piece.position:
                    attack_piece = self.board[row_index[row_i+i]][col]
                    if attack_piece:
                        if attack_piece.is_white is not piece.is_white:
                            piece.add_move(position = position, is_kill = True)
                            self.add_attack_position(piece, position)
                        break
                    piece.add_move(position = position, is_kill = False)
                    self.add_attack_position(piece, position)
        for i in board_range:    
            if (row_i-i in board_range):
                position = [row_index[row_i-i], col]
                if position != piece.position:
                    attack_piece = self.board[row_index[row_i-i]][col]
                    if attack_piece:
                        if attack_piece.is_white is not piece.is_white:
                            piece.add_move(position = position, is_kill = True)
                            self.add_attack_position(piece, position)
                        break
                    piece.add_move(position = position, is_kill = False)
                    self.add_attack_position(piece, position)
        for i in board_range:
            if (col_i+i in board_range):
                position = [row, col_index[col_i+i]]
                if position != piece.position:
                    attack_piece = self.board[row][col_index[col_i+i]]
                    if attack_piece:
                        if attack_piece.is_white is not piece.is_white:
                            piece.add_move(position = position, is_kill = True)
                            self.add_attack_position(piece, position)
                        break
                    piece.add_move(position = position, is_kill = False)
                    self.add_attack_position(piece, position)
        for i in board_range:
            if (col_i-i in board_range):
                position = [row, col_index[col_i-i]]
                if position != piece.position:
                    attack_piece = self.board[row][col_index[col_i-i]]
                    if attack_piece:
                        if attack_piece.is_white is not piece.is_white:
                            piece.add_move(position = position, is_kill = True)
                            self.add_attack_position(piece, position)
                        break
                    piece.add_move(position = position, is_kill = False)
                    self.add_attack_position(piece, position)

        # Diagonal
        for i in board_range:
            if row_i+i in board_range and col_i+i in board_range:
                position = [row_index[row_i+i], col_index[col_i+i]]
                if position != piece.position:
                    attack_piece = self.board[position[0]][position[1]]
                    if attack_piece:
                        if attack_piece.is_white is not piece.is_white:
                            piece.add_move(position = position, is_kill = True)
                            self.add_attack_position(piece, position)
                        break
                    piece.add_move(position = position, is_kill = False)
                    self.add_attack_position(piece, position)
        for i in board_range:
            if row_i+i in board_range and col_i-i in board_range:
                position = [row_index[row_i+i], col_index[col_i-i]]
                if position != piece.position:
                    attack_piece = self.board[position[0]][position[1]]
                    if attack_piece:
                        if attack_piece.is_white is not piece.is_white:
                            piece.add_move(position = position, is_kill = True)
                            self.add_attack_position(piece, position)
                        break
                    piece.add_move(position = position, is_kill = False)
                    self.add_attack_position(piece, position)
        for i in board_range:
            if row_i-i in board_range and col_i+i in board_range:
                position = [row_index[row_i-i], col_index[col_i+i]]
                if position != piece.position:
                    attack_piece = self.board[position[0]][position[1]]
                    if attack_piece:
                        if attack_piece.is_white is not piece.is_white:
                            piece.add_move(position = position, is_kill = True)
                            self.add_attack_position(piece, position)
                        break
                    piece.add_move(position = position, is_kill = False)
                    self.add_attack_position(piece, position)
        for i in board_range:
            if row_i-i in board_range and col_i-i in board_range:
                position = [row_index[row_i-i], col_index[col_i-i]]
                if position != piece.position:
                    attack_piece = self.board[position[0]][position[1]]
                    if attack_piece:
                        if attack_piece.is_white is not piece.is_white:
                            piece.add_move(position = position, is_kill = True)
                            self.add_attack_position(piece, position)
                        break
                    piece.add_move(position = position, is_kill = False)
                    self.add_attack_position(piece, position)

    def find_king_moves(self, row, col, piece, row_i, col_i, board_range):
        all_possible_moves = piece.find_possible_moves()

        for position in all_possible_moves:
            attack_piece = self.board[position[0]][position[1]]
            if attack_piece and (attack_piece.is_white != piece.is_white):
                piece.add_move(position = position, is_kill = True)
                self.add_attack_position(piece, position)
            elif not attack_piece:
                piece.add_move(position = position, is_kill = False)
                self.add_attack_position(piece, position)

        # castle moves
        if piece.unmoved and self.board[row][col_index[0]].unmoved:
            is_empty = True
            for i in [1, 2, 3]:
                if self.board[row][col_index[i]]:
                    is_empty = False
            if is_empty:
                piece.add_move(
                    position = [row, col_index[1]],
                    is_kill = False,
                    castle = {
                        'rookStartPosition': [row, col_index[0]], 
                        'rookEndPosition': [row, col_index[2]], 
                    }
                )
        if piece.unmoved and self.board[row][col_index[7]] and self.board[row][col_index[7]].unmoved:
            is_empty = True
            for i in [5, 6]:
                if self.board[row][col_index[i]]:
                    is_empty = False
            if is_empty:
                piece.add_move(
                    position = [row, col_index[6]],
                    is_kill = False,
                    castle = {
                        'rookStartPosition': [row, col_index[7]], 
                        'rookEndPosition': [row, col_index[5]], 
                    }
                )

    def display_board(self):
        output_board = empty_board()
        for row in row_index:
            for col in col_index:
                if self.board[row][col]:
                    output_board[row][col] = self.board[row][col].out()

        return output_board

    def xnor(self, a, b):
        if a == b:
            return True
        return False

    def add_attack_position(self, piece, position):
        '''
        instead of using a list, it may be better to store this as a board matrix
        '''
        if piece.is_white:
            self.white_attack_positions.append(position)
        else:
            self.black_attack_positions.append(position)
