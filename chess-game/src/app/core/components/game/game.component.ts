import { Component, OnInit } from '@angular/core';
import { CoreService } from '../../core.service';
import { SelectedPlayer } from '../../enums/selected-player';
import { Board } from '../../models/board.interface';

@Component({
  selector: 'app-game',
  templateUrl: './game.component.html',
  styleUrls: ['./game.component.scss']
})
export class GameComponent implements OnInit {
  board: Board;
  selectedPlayer: SelectedPlayer;
  moves = []

  constructor(
    private coreService: CoreService
    ) { }

  ngOnInit(): void {
    console.log('game')
    this.board = this.coreService.getBoard();
    this.selectedPlayer = this.coreService.getSelectedPlayer();
    this.coreService.getMoves().subscribe((res) => {
      this.moves = res ? res : []
    })
  }

  resetBoard() { 
    this.board = this.coreService.resetBoard()
    this.selectedPlayer = this.coreService.resetSelectedPlayer();
    this.coreService.resetMoves()
    this.moves = []
  }

  onUpdateMoves() { 
    this.coreService.getMoves().subscribe((res) => {
      this.moves = res ? res : []
    })
  }
}
