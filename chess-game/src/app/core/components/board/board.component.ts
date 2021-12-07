import { Component, OnInit } from '@angular/core';

import { Board, BoardCircle, BoardColor } from 'src/app/core/models/board.interface';
import { CoreService } from 'src/app/core/core.service';

@Component({
  selector: 'app-board',
  templateUrl: './board.component.html',
  styleUrls: ['./board.component.scss']
})
export class BoardComponent implements OnInit {
  showCircle = false;
  startingPosition: string[];
  board: Board;
  boardColor: BoardColor;
  boardCircle: BoardCircle;

  constructor(
    private coreService: CoreService
  ) { }

  ngOnInit(): void {
    this.board = this.coreService.board
    this.boardColor = this.coreService.boardColor
    this.boardCircle = this.coreService.boardEmptyCircle()
    this.coreService.findMoves(this.board)
  }

  findMovesOrMovePiece(row: string, col: string) {
    if (!this.showCircle) { 
      this.boardCircle = this.coreService.boardEmptyCircle()
      let moves = this.board[row][col]?.moves
      if (moves) { 
        moves?.map((move) => { 
          let position = move.newPosition
          this.boardCircle[position[0]][position[1]] = true
        })
        this.startingPosition = [row, col]
        this.showCircle = true
      }
    } else { 
      if (!this.boardCircle[row][col]) { 
        this.boardCircle = this.coreService.boardEmptyCircle()
        this.startingPosition = []
        this.showCircle = false
      } else { 
        // TODO: add a piece swapping function
        let movingPiece = this.board[this.startingPosition[0]][this.startingPosition[1]]
        this.board[this.startingPosition[0]][this.startingPosition[1]] = null
        this.board[row][col] = movingPiece
        this.boardCircle = this.coreService.boardEmptyCircle()
        this.startingPosition = []
        this.showCircle = false
        // TODO: add an update board function in services
      }
    }
  }

  urlConcat(pieceType: string): string { 
    return 'assets/'+pieceType+'.png'
  }

}
