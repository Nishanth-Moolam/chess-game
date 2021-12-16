import { Component, OnInit, Input } from '@angular/core';

import { Board, BoardCircle, BoardColor } from 'src/app/core/models/board.interface';
import { CoreService } from 'src/app/core/core.service';

@Component({
  selector: 'app-board',
  templateUrl: './board.component.html',
  styleUrls: ['./board.component.scss']
})
export class BoardComponent implements OnInit {
  @Input() board: Board;

  showCircle = false;
  startingPosition: string[];
  boardColor: BoardColor;
  boardCircle: BoardCircle;
  loading: boolean = false;
  errorMessage;

  constructor(
    private coreService: CoreService
  ) { }

  ngOnInit(): void {
    this.boardColor = this.coreService.boardColor
    this.boardCircle = this.coreService.boardEmptyCircle()
    this.getData();
  }

  getData() { 
    this.loading = true;
    this.errorMessage = "";
    this.coreService.findMoves(this.board)
      .subscribe((res) => {
        this.board = res
      }, (error) => { 
        console.log(error)
        this.errorMessage = error;
        this.loading = false;
      }, () => { 
        this.loading = false; 
      })
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
        this.movePiece(row, col)
      }
    }
  }

  movePiece(row: string, col: string) { 
    let movingPiece = this.board[this.startingPosition[0]][this.startingPosition[1]]
    let destPiece = this.board[row][col]
    let move = movingPiece.moves.filter((move) => { 
      return move.newPosition[0] === row && move.newPosition[1] === col
    })

    // TODO: add exception for special moves like castles
    this.board[this.startingPosition[0]][this.startingPosition[1]] = null
    this.board[row][col] = movingPiece
    this.boardCircle = this.coreService.boardEmptyCircle()
    this.startingPosition = []
    this.showCircle = false
    this.coreService.updateBoard(this.board)
    this.getData()
  }

  urlConcat(pieceType: string): string { 
    return 'assets/'+pieceType+'.png'
  }

}
