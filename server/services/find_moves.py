from models.piece import *
from models.board import *
import json

def find_moves(board):
    c = Board(board)
    # print (c.board)
    # for i in c.board:
    #     for j in c.board[i]:
    #         # print (type(c.board[i][j]))
    #         # c.board[i][j].find_possible_moves()
    #         # print (c.board[i][j].out())
    return c.board