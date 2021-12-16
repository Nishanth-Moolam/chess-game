import { Injectable } from "@angular/core";
import { HttpClient } from '@angular/common/http';
import { Observable, throwError } from 'rxjs';

import { Board, BoardCircle, BoardColor, Stats } from "./models/board.interface";
import { Piece } from 'src/app/core/models/piece.interface';

@Injectable({
    providedIn: 'root'
})
export class CoreService { 

    baseURL: string = "http://127.0.0.1:5000/";

    constructor (private http: HttpClient) {}

    board: Board;
    stats: Stats;

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

    piece(piece: string, color: string): Piece { 
        return { 
            type: piece+'-'+color,
            isWhite: color === 'white' ? true : false,
            isDead: false,
            moves: []
        }
    }

    getBoard() { 
        this.board = JSON.parse(localStorage.getItem('board')) ? JSON.parse(localStorage.getItem('board')) : this.resetBoard()
        return this.board
    }

    updateBoard(board: Board) { 
        this.board = board;
        localStorage.setItem('board', JSON.stringify(this.board))
    }

    findMoves(board: Board): Observable<any> { 
        const body = JSON.stringify(board) 
        return this.http.post<any>(this.baseURL + '/findmoves', body)
    }
    
    resetBoard() { 
        this.board = {
            1: { 
                a: this.piece('rook', 'white'), 
                b: this.piece('knight', 'white'), 
                c: this.piece('bishop', 'white'), 
                d: this.piece('queen', 'white'), 
                e: this.piece('king', 'white'), 
                f: this.piece('bishop', 'white'), 
                g: this.piece('knight', 'white'), 
                h: this.piece('rook', 'white') 
            },
            2: { 
                a: this.piece('pawn', 'white'), 
                b: this.piece('pawn', 'white'), 
                c: this.piece('pawn', 'white'), 
                d: this.piece('pawn', 'white'), 
                e: this.piece('pawn', 'white'), 
                f: this.piece('pawn', 'white'), 
                g: this.piece('pawn', 'white'), 
                h: this.piece('pawn', 'white') 
            },
            3: { a: null, b: null, c: null, d: null, e: null, f: null, g: null, h: null },
            4: { a: null, b: null, c: null, d: null, e: null, f: null, g: null, h: null },
            5: { a: null, b: null, c: null, d: null, e: null, f: null, g: null, h: null },
            6: { a: null, b: null, c: null, d: null, e: null, f: null, g: null, h: null },
            7: { 
                a: this.piece('pawn', 'black'), 
                b: this.piece('pawn', 'black'), 
                c: this.piece('pawn', 'black'), 
                d: this.piece('pawn', 'black'), 
                e: this.piece('pawn', 'black'), 
                f: this.piece('pawn', 'black'), 
                g: this.piece('pawn', 'black'), 
                h: this.piece('pawn', 'black') 
            },
            8: { 
                a: this.piece('rook', 'black'), 
                b: this.piece('knight', 'black'), 
                c: this.piece('bishop', 'black'), 
                d: this.piece('queen', 'black'), 
                e: this.piece('king', 'black'), 
                f: this.piece('bishop', 'black'), 
                g: this.piece('knight', 'black'), 
                h: this.piece('rook', 'black')
            },
        };
        Object.keys(this.board['2']).map((key, val) => {
            if (this.board['2'][key]) { 
                this.board['2'][key].moves = [
                    {
                        isKill: false,
                        newPosition: ['3', key]
                    },
                    {
                        isKill: false,
                        newPosition: ['4', key]
                    }
                ]
            }
            if (this.board['7'][key]) { 
                this.board['7'][key].moves = [
                    {
                        isKill: false,
                        newPosition: ['6', key]
                    },
                    {
                        isKill: false,
                        newPosition: ['5', key]
                    }
                ]
            }
        })
        localStorage.setItem('board', JSON.stringify(this.board))
        return this.board
    }
}