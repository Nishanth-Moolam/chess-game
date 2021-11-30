import { Injectable } from "@angular/core";

import { Board } from "./models/board.interface";
import { Moves } from "./models/moves.interface";

@Injectable({
    providedIn: 'root'
})
export class CoreService { 
    constructor () {}

    board = {};
    moves = {};

    updateBoard(board: Board) { 
        this.board = board;
    }

    findMoves(board: Board) { 
        this.moves = {}
    }
    
    resetBoard() { 
        this.board = {}
    }
}