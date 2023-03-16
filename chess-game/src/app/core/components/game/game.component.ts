import { Breakpoints } from '@angular/cdk/layout';
import { Component, OnInit } from '@angular/core';
import { CoreService } from '../../core.service';
import { Media } from '../../enums/media';
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
  mediaType: string;
  media = Media;

  constructor(
    private coreService: CoreService
    ) { }

  ngOnInit(): void {
    this.board = this.coreService.getBoard();
    this.selectedPlayer = this.coreService.getSelectedPlayer();
    this.coreService.getMoves().subscribe((res) => {
      this.moves = res ? res : []
    })
    this.coreService.observeBreakpoints().subscribe((state) => {
      this.mediaType = state.breakpoints[Breakpoints.HandsetLandscape] || 
        state.breakpoints[Breakpoints.HandsetPortrait] ||  
        state.breakpoints[Breakpoints.TabletLandscape] || 
        state.breakpoints[Breakpoints.TabletPortrait] ? 
        Media.MOBILE : Media.WEB
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
