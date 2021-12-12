import { Component, OnInit } from '@angular/core';
import { CoreService } from '../../core.service';
import { Board } from '../../models/board.interface';

@Component({
  selector: 'app-game',
  templateUrl: './game.component.html',
  styleUrls: ['./game.component.scss']
})
export class GameComponent implements OnInit {
  board: Board;

  constructor(
    private coreService: CoreService
    ) { }

  ngOnInit(): void {
    this.board = this.coreService.getBoard();
  }

  resetBoard() { 
    this.board = this.coreService.resetBoard()
  }
}
