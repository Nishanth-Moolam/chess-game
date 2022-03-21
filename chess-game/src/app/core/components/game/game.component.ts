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

  constructor(
    private coreService: CoreService
    ) { }

  ngOnInit(): void {
    this.board = this.coreService.getBoard();
    this.selectedPlayer = this.coreService.getSelectedPlayer();
  }

  resetBoard() { 
    this.board = this.coreService.resetBoard()
    this.selectedPlayer = this.coreService.resetSelectedPlayer();
  }
}
