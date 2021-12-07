import { Injectable } from "@angular/core";

import { Board, BoardCircle, BoardColor } from "./models/board.interface";
import { Piece } from 'src/app/core/models/piece.interface';

@Injectable({
    providedIn: 'root'
})
export class CoreService { 
    constructor () {}

    board: Board = {
        1: { a: this.rookWhite(), b: this.knightWhite(), c: this.bishopWhite(), d: this.queenWhite(), e: this.kingWhite(), f: this.bishopWhite(), g: this.knightWhite(), h: this.rookWhite() },
        2: { a: this.pawnWhite(), b: this.pawnWhite(), c: this.pawnWhite(), d: this.pawnWhite(), e: this.pawnWhite(), f: this.pawnWhite(), g: this.pawnWhite(), h: this.pawnWhite() },
        3: { a: null, b: null, c: null, d: null, e: null, f: null, g: null, h: null },
        4: { a: null, b: null, c: null, d: null, e: null, f: null, g: null, h: null },
        5: { a: null, b: null, c: null, d: null, e: null, f: null, g: null, h: null },
        6: { a: null, b: null, c: null, d: null, e: null, f: null, g: null, h: null },
        7: { a: this.pawnBlack(), b: this.pawnBlack(), c: this.pawnBlack(), d: this.pawnBlack(), e: this.pawnBlack(), f: this.pawnBlack(), g: this.pawnBlack(), h: this.pawnBlack() },
        8: { a: this.rookBlack(), b: this.knightBlack(), c: this.bishopBlack(), d: this.queenBlack(), e: this.kingBlack(), f: this.bishopBlack(), g: this.knightBlack(), h: this.rookBlack() },
    };

    boardColor: BoardColor = { 
        1: { a: 'black', b: 'white', c: 'black', d: 'white', e: 'black', f: 'white', g: 'black', h: 'white' },
        2: { a: 'white', b: 'black', c: 'white', d: 'black', e: 'white', f: 'black', g: 'white', h: 'black' },
        3: { a: 'black', b: 'white', c: 'black', d: 'white', e: 'black', f: 'white', g: 'black', h: 'white' },
        4: { a: 'white', b: 'black', c: 'white', d: 'black', e: 'white', f: 'black', g: 'white', h: 'black' },
        5: { a: 'black', b: 'white', c: 'black', d: 'white', e: 'black', f: 'white', g: 'black', h: 'white' },
        6: { a: 'white', b: 'black', c: 'white', d: 'black', e: 'white', f: 'black', g: 'white', h: 'black' },
        7: { a: 'black', b: 'white', c: 'black', d: 'white', e: 'black', f: 'white', g: 'black', h: 'white' },
        8: { a: 'white', b: 'black', c: 'white', d: 'black', e: 'white', f: 'black', g: 'white', h: 'black' },
    }

    boardEmptyCircle(): BoardCircle {
        return { 
                1: { a: false, b: false, c: false, d: false, e: false, f: false, g: false, h: false },
                2: { a: false, b: false, c: false, d: false, e: false, f: false, g: false, h: false },
                3: { a: false, b: false, c: false, d: false, e: false, f: false, g: false, h: false },
                4: { a: false, b: false, c: false, d: false, e: false, f: false, g: false, h: false },
                5: { a: false, b: false, c: false, d: false, e: false, f: false, g: false, h: false },
                6: { a: false, b: false, c: false, d: false, e: false, f: false, g: false, h: false },
                7: { a: false, b: false, c: false, d: false, e: false, f: false, g: false, h: false },
                8: { a: false, b: false, c: false, d: false, e: false, f: false, g: false, h: false },
            }
    } 

    //moves: Moves = {};

    pawnWhite(): Piece { 
        return {
            type: 'pawn-white',
            isWhite: true,
            isDead: false,
            moves: []
        }
    }

    rookWhite(): Piece { 
        return {
            type: 'rook-white',
            isWhite: true,
            isDead: false,
            moves: []
        }
    }

    knightWhite(): Piece { 
        return {
            type: 'knight-white',
            isWhite: true,
            isDead: false,
            moves: []
        }
    }

    bishopWhite(): Piece { 
        return {
            type: 'bishop-white',
            isWhite: true,
            isDead: false,
            moves: []
        }
    }

    queenWhite(): Piece { 
        return {
            type: 'queen-white',
            isWhite: true,
            isDead: false,
            moves: []
        }
    }

    kingWhite(): Piece { 
        return {
            type: 'king-white',
            isWhite: true,
            isDead: false,
            moves: []
        }
    }

    pawnBlack(): Piece { 
        return {
            type: 'pawn-black',
            isWhite: true,
            isDead: false,
            moves: []
        }
    }

    rookBlack(): Piece { 
        return {
            type: 'rook-black',
            isWhite: true,
            isDead: false,
            moves: []
        }
    }

    knightBlack(): Piece { 
        return {
            type: 'knight-black',
            isWhite: true,
            isDead: false,
            moves: []
        }
    }

    bishopBlack(): Piece { 
        return {
            type: 'bishop-black',
            isWhite: true,
            isDead: false,
            moves: []
        }
    }

    queenBlack(): Piece { 
        return {
            type: 'queen-black',
            isWhite: true,
            isDead: false,
            moves: []
        }
    }

    kingBlack(): Piece { 
        return {
            type: 'king-black',
            isWhite: true,
            isDead: false,
            moves: []
        }
    }

    updateBoard(board: Board) { 
        //this.board = board;
    }

    findMoves(board: Board) { 
        Object.keys(board['2']).map((key, val) => {
            board['2'][key].moves = [
                {
                    isKill: false,
                    newPosition: ['3', key]
                },
                {
                    isKill: false,
                    newPosition: ['4', key]
                }
            ]
            board['7'][key].moves = [
                {
                    isKill: false,
                    newPosition: ['6', key]
                },
                {
                    isKill: false,
                    newPosition: ['5', key]
                }
            ]
        })
        //this.moves = {}
    }
    
    resetBoard() { 
        //this.board = {}
    }
}